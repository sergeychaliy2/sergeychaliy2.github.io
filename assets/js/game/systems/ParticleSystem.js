/* ============================================================
   ParticleSystem — an emitter. It reacts to slice events and
   seeds the burst of sparks + the two split halves (shards).
   Integration/decay is handled by PhysicsSystem; this class
   only authors the effect.
   ============================================================ */
import { CONFIG } from '../config.js';

const rand = (a, b) => a + Math.random() * (b - a);

export class ParticleSystem {
  constructor(world, bus) {
    this.world = world;
    bus.on('node:sliced', (e) => this._burst(e, false));
    bus.on('bomb:sliced', (e) => this._burst(e, true));
  }

  _burst(e, isBomb) {
    const w = this.world;
    const count = CONFIG.particle.count + (isBomb ? 14 : 0);

    for (let i = 0; i < count; i++) {
      const a = rand(0, Math.PI * 2);
      const sp = rand(0.25, 1) * CONFIG.particle.speed;
      const p = w.spawnParticle();
      p.x = e.x; p.y = e.y;
      p.vx = Math.cos(a) * sp;
      p.vy = Math.sin(a) * sp - rand(0, 120);
      p.r = rand(1.5, isBomb ? 4.5 : 3.5);
      p.max = rand(0.4, 1) * CONFIG.particle.life;
      p.life = 0;
      p.color = Math.random() < 0.3 ? '#ffffff' : e.color;
    }

    // two halves split perpendicular to the cut
    for (const side of [-1, 1]) {
      const pa = e.angle + side * Math.PI / 2;
      const s = w.spawnShard();
      s.x = e.x; s.y = e.y;
      s.vx = Math.cos(pa) * CONFIG.shard.speed * 0.55;
      s.vy = Math.sin(pa) * CONFIG.shard.speed * 0.55 - 120;
      s.r = e.r * 0.92;
      s.rot = e.angle;
      s.spin = side * rand(2, 5);
      s.max = CONFIG.shard.life;
      s.life = 0;
      s.color = e.color;
      s.side = side;
      s.cut = e.angle;
    }
  }
}
