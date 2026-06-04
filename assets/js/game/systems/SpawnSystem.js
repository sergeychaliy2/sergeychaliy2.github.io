/* ============================================================
   SpawnSystem — launches waves of nodes on physically-derived
   arcs. Velocity is solved from a target apex height as a
   fraction of the play area, so arcs feel identical on any
   screen size. Difficulty ramps with elapsed time.
   ============================================================ */
import { CONFIG } from '../config.js';

const rand = (a, b) => a + Math.random() * (b - a);

export class SpawnSystem {
  constructor(world) {
    this.world = world;
    this._timer = 0;
  }

  reset() { this._timer = 0.6; }

  update(dt) {
    const w = this.world;
    if (w.h < 50 || w.w < 50) return;   // wait until the field has a real size
    this._timer -= dt;
    if (this._timer > 0) return;

    const cfg = CONFIG.spawn;
    const interval = Math.max(cfg.minInterval, cfg.baseInterval - cfg.ramp * w.elapsed);
    this._timer = interval;

    const count = 1 + Math.min(cfg.burstMax - 1, Math.floor(w.elapsed / 22));
    for (let i = 0; i < count; i++) this._launch();
  }

  _launch() {
    const w = this.world;
    const c = CONFIG.node;
    const g = CONFIG.gravity;

    const r = rand(c.rMin, c.rMax);
    const apexH = rand(c.apexMin, c.apexMax) * w.h;
    const vy = -Math.sqrt(2 * g * apexH);
    const tApex = -vy / g;

    const x0 = rand(w.w * 0.12, w.w * 0.88);
    const apexX = rand(w.w * 0.2, w.w * 0.8);

    const bombChance = Math.min(CONFIG.bomb.maxChance, CONFIG.bomb.baseChance + CONFIG.bomb.ramp * w.elapsed);
    const isBomb = Math.random() < bombChance;
    const palette = CONFIG.palette.nodes;

    const n = w.spawnNode();
    n.type = isBomb ? 'bomb' : 'node';
    n.x = x0; n.y = w.h + r;
    n.vx = (apexX - x0) / tApex;
    n.vy = vy;
    n.r = r;
    n.rot = 0;
    n.spin = rand(c.spinMin, c.spinMax);
    n.seed = Math.random() * Math.PI * 2;
    n.color = isBomb ? CONFIG.palette.bomb : palette[(Math.random() * palette.length) | 0];
    n.sliced = false;
  }
}
