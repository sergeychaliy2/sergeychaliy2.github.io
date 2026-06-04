/* ============================================================
   RenderSystem — all drawing. Reads world + input, never
   mutates game state. Neon "neuron" nodes, split halves,
   additive spark particles and a tapering blade trail.
   ============================================================ */
import { CONFIG } from '../config.js';

export class RenderSystem {
  constructor(world, input, ctx, bus) {
    this.world = world; this.input = input; this.ctx = ctx;
    this._flash = 0;
    bus.on('fx:flash', () => { this._flash = 1; });
  }

  render() {
    const ctx = this.ctx, w = this.world;
    ctx.clearRect(0, 0, w.w, w.h);
    ctx.save();

    // screen shake
    if (w.shake > 0) {
      const m = w.shake * 14;
      ctx.translate((Math.random() - 0.5) * m, (Math.random() - 0.5) * m);
    }

    this._drawLinks();
    for (const s of w.shards) this._drawShard(s);
    for (const n of w.nodes) (n.type === 'bomb' ? this._drawBomb(n) : this._drawNode(n));
    this._drawParticles();
    this._drawBlade();

    ctx.restore();

    // bomb flash overlay
    if (this._flash > 0) {
      ctx.save();
      ctx.globalAlpha = this._flash * 0.5;
      ctx.fillStyle = '#ff5468';
      ctx.fillRect(0, 0, w.w, w.h);
      ctx.restore();
      this._flash = Math.max(0, this._flash - 0.06);
    }
  }

  /* faint synapse lines between nearby nodes — the neural motif */
  _drawLinks() {
    const ctx = this.ctx, nodes = this.world.nodes;
    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    ctx.lineWidth = 1;
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i], b = nodes[j];
        const d = Math.hypot(a.x - b.x, a.y - b.y);
        if (d < 240) {
          ctx.strokeStyle = `rgba(120,170,255,${(1 - d / 240) * 0.16})`;
          ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
        }
      }
    }
    ctx.restore();
  }

  _drawNode(n) {
    const ctx = this.ctx;
    const t = this.world.elapsed;
    const pulse = 1 + Math.sin(t * 3 + n.seed) * 0.06;
    const r = n.r * pulse;

    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    // outer glow
    const glow = ctx.createRadialGradient(n.x, n.y, r * 0.3, n.x, n.y, r * 2.3);
    glow.addColorStop(0, hexA(n.color, 0.5));
    glow.addColorStop(1, hexA(n.color, 0));
    ctx.fillStyle = glow;
    ctx.beginPath(); ctx.arc(n.x, n.y, r * 2.3, 0, TAU); ctx.fill();
    ctx.restore();

    ctx.save();
    // core
    const core = ctx.createRadialGradient(n.x - r * 0.3, n.y - r * 0.3, r * 0.1, n.x, n.y, r);
    core.addColorStop(0, '#ffffff');
    core.addColorStop(0.35, n.color);
    core.addColorStop(1, hexA(n.color, 0.25));
    ctx.fillStyle = core;
    ctx.beginPath(); ctx.arc(n.x, n.y, r, 0, TAU); ctx.fill();

    // ring
    ctx.strokeStyle = hexA('#ffffff', 0.65);
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.arc(n.x, n.y, r * 0.82, 0, TAU); ctx.stroke();

    // orbiting electrons
    ctx.fillStyle = '#ffffff';
    for (let k = 0; k < 3; k++) {
      const a = n.rot * 2 + n.seed + (k * TAU) / 3;
      const ex = n.x + Math.cos(a) * r * 1.35;
      const ey = n.y + Math.sin(a) * r * 1.35;
      ctx.globalAlpha = 0.85;
      ctx.beginPath(); ctx.arc(ex, ey, 2.4, 0, TAU); ctx.fill();
    }
    ctx.restore();
  }

  _drawBomb(n) {
    const ctx = this.ctx;
    const t = this.world.elapsed;
    const r = n.r * (1 + Math.sin(t * 7 + n.seed) * 0.10);

    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    const glow = ctx.createRadialGradient(n.x, n.y, r * 0.2, n.x, n.y, r * 2.6);
    glow.addColorStop(0, hexA('#ff5468', 0.7));
    glow.addColorStop(1, hexA('#ff5468', 0));
    ctx.fillStyle = glow;
    ctx.beginPath(); ctx.arc(n.x, n.y, r * 2.6, 0, TAU); ctx.fill();
    ctx.restore();

    ctx.save();
    ctx.translate(n.x, n.y);
    // dark core
    const core = ctx.createRadialGradient(-r * 0.3, -r * 0.3, r * 0.1, 0, 0, r);
    core.addColorStop(0, '#ff8a98');
    core.addColorStop(0.5, '#ff5468');
    core.addColorStop(1, '#5a0e18');
    ctx.fillStyle = core;
    ctx.beginPath(); ctx.arc(0, 0, r, 0, TAU); ctx.fill();

    // rotating warning ring
    ctx.rotate(n.rot * 2.5);
    ctx.strokeStyle = '#ffd2d8';
    ctx.lineWidth = 2.2;
    ctx.setLineDash([6, 7]);
    ctx.beginPath(); ctx.arc(0, 0, r * 1.05, 0, TAU); ctx.stroke();
    ctx.setLineDash([]);

    // X mark
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 3;
    ctx.lineCap = 'round';
    const m = r * 0.42;
    ctx.beginPath();
    ctx.moveTo(-m, -m); ctx.lineTo(m, m);
    ctx.moveTo(m, -m); ctx.lineTo(-m, m);
    ctx.stroke();
    ctx.restore();
  }

  _drawShard(s) {
    const ctx = this.ctx;
    const a = 1 - s.life / s.max;
    ctx.save();
    ctx.globalAlpha = a;
    ctx.translate(s.x, s.y);
    ctx.rotate(s.cut);
    // clip to one half-plane so it reads as a sliced piece
    ctx.beginPath();
    ctx.rect(-s.r * 1.2, s.side > 0 ? 0 : -s.r * 1.2, s.r * 2.4, s.r * 1.2);
    ctx.clip();
    ctx.rotate(s.rot - s.cut);
    ctx.globalCompositeOperation = 'lighter';
    const g = ctx.createRadialGradient(0, 0, s.r * 0.1, 0, 0, s.r);
    g.addColorStop(0, '#ffffff');
    g.addColorStop(0.4, s.color);
    g.addColorStop(1, hexA(s.color, 0));
    ctx.fillStyle = g;
    ctx.beginPath(); ctx.arc(0, 0, s.r, 0, TAU); ctx.fill();
    ctx.restore();
  }

  _drawParticles() {
    const ctx = this.ctx;
    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    for (const p of this.world.particles) {
      const a = 1 - p.life / p.max;
      ctx.globalAlpha = a;
      ctx.fillStyle = p.color;
      ctx.beginPath(); ctx.arc(p.x, p.y, p.r * a + 0.5, 0, TAU); ctx.fill();
    }
    ctx.restore();
  }

  _drawBlade() {
    const tr = this.input.trail;
    if (tr.length < 2) return;
    const ctx = this.ctx;
    const [c0, c1] = CONFIG.palette.blade;
    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    for (let i = 1; i < tr.length; i++) {
      const f = i / (tr.length - 1);          // 0 old → 1 newest
      ctx.strokeStyle = lerpColor(c0, c1, f);
      ctx.globalAlpha = f * 0.9;
      ctx.lineWidth = 1 + f * 13;
      ctx.beginPath();
      ctx.moveTo(tr[i - 1].x, tr[i - 1].y);
      ctx.lineTo(tr[i].x, tr[i].y);
      ctx.stroke();
    }
    // bright core line
    ctx.globalAlpha = 0.9;
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(tr[0].x, tr[0].y);
    for (let i = 1; i < tr.length; i++) ctx.lineTo(tr[i].x, tr[i].y);
    ctx.stroke();
    ctx.restore();
  }
}

const TAU = Math.PI * 2;

/* ---- tiny colour helpers (hex → rgba / lerp) ---- */
function hexRGB(hex) {
  const h = hex.replace('#', '');
  return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
}
function hexA(hex, a) {
  const [r, g, b] = hexRGB(hex);
  return `rgba(${r},${g},${b},${a})`;
}
function lerpColor(c1, c2, t) {
  const a = hexRGB(c1), b = hexRGB(c2);
  return `rgb(${(a[0] + (b[0] - a[0]) * t) | 0},${(a[1] + (b[1] - a[1]) * t) | 0},${(a[2] + (b[2] - a[2]) * t) | 0})`;
}
