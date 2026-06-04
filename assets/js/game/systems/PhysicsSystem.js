/* ============================================================
   PhysicsSystem — integrates gravity for nodes, shards and
   particles. A node that falls back below the floor un-sliced
   is a "miss" → it publishes node:missed and is culled.
   ============================================================ */
import { CONFIG } from '../config.js';

export class PhysicsSystem {
  constructor(world, bus) { this.world = world; this.bus = bus; }

  update(dt) {
    const w = this.world;
    const g = CONFIG.gravity;
    const floor = w.h + 80;       // a touch below the visible floor

    /* nodes */
    for (let i = w.nodes.length - 1; i >= 0; i--) {
      const n = w.nodes[i];
      n.vy += g * dt;
      n.x += n.vx * dt;
      n.y += n.vy * dt;
      n.rot += n.spin * dt;
      if (n.y - n.r > floor) {
        w.nodes.splice(i, 1);
        w.nodePool.release(n);
        if (n.type === 'node') this.bus.emit('node:missed', n);
      }
    }

    /* shards (the split halves) */
    for (let i = w.shards.length - 1; i >= 0; i--) {
      const s = w.shards[i];
      s.life += dt;
      s.vy += g * dt;
      s.x += s.vx * dt;
      s.y += s.vy * dt;
      s.rot += s.spin * dt;
      if (s.life >= s.max) { w.shards.splice(i, 1); w.shardPool.release(s); }
    }

    /* particles */
    const drag = CONFIG.particle.drag;
    for (let i = w.particles.length - 1; i >= 0; i--) {
      const p = w.particles[i];
      p.life += dt;
      p.vy += g * 0.45 * dt;
      p.vx *= drag; p.vy *= drag;
      p.x += p.vx * dt;
      p.y += p.vy * dt;
      if (p.life >= p.max) { w.particles.splice(i, 1); w.particlePool.release(p); }
    }
  }
}
