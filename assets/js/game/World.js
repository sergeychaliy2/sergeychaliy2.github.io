/* ============================================================
   World.js — the mutable game state shared by all systems.
   Holds entity pools, active lists, viewport size and the
   run's score/lives/combo. Systems read & mutate this; they
   never hold their own copies of it.
   ============================================================ */
import { ObjectPool } from './core/ObjectPool.js';
import { createNode, resetNode, createParticle, resetParticle, createShard, resetShard } from './entities.js';

export class World {
  constructor() {
    this.nodePool = new ObjectPool(createNode, resetNode, 24);
    this.particlePool = new ObjectPool(createParticle, resetParticle, 160);
    this.shardPool = new ObjectPool(createShard, resetShard, 24);

    /** @type {object[]} */ this.nodes = [];
    /** @type {object[]} */ this.particles = [];
    /** @type {object[]} */ this.shards = [];

    this.w = 0; this.h = 0;     // play area, css px
    this.dpr = 1;

    this.reset();
  }

  reset() {
    this.nodes.forEach((n) => this.nodePool.release(n));
    this.particles.forEach((p) => this.particlePool.release(p));
    this.shards.forEach((s) => this.shardPool.release(s));
    this.nodes.length = this.particles.length = this.shards.length = 0;

    this.score = 0;
    this.lives = 0;
    this.elapsed = 0;       // seconds since run start
    this.combo = 0;         // current chain size
    this.comboTimer = 0;    // seconds left to keep the chain
    this.best = 0;
    this.shake = 0;         // screen-shake energy
  }

  spawnNode() {
    const n = this.nodePool.acquire();
    this.nodes.push(n);
    return n;
  }
  killNode(n) {
    const i = this.nodes.indexOf(n);
    if (i >= 0) this.nodes.splice(i, 1);
    this.nodePool.release(n);
  }

  spawnParticle() {
    const p = this.particlePool.acquire();
    this.particles.push(p);
    return p;
  }
  spawnShard() {
    const s = this.shardPool.acquire();
    this.shards.push(s);
    return s;
  }
}
