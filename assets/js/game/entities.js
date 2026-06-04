/* ============================================================
   entities.js — plain data objects + their pool reset fns.
   Entities are data; behaviour lives in systems (ECS-lite).
   ============================================================ */

/* ---- Node: the sliceable neuron (or a "bug" bomb) ---- */
export function createNode() {
  return {
    active: false, type: 'node', // 'node' | 'bomb'
    x: 0, y: 0, vx: 0, vy: 0,
    r: 30, rot: 0, spin: 0, seed: 0,
    color: '#4d7dff', sliced: false,
  };
}
export function resetNode(n) {
  n.sliced = false; n.vx = n.vy = n.rot = 0;
}

/* ---- Particle: short-lived spark from a slice ---- */
export function createParticle() {
  return { active: false, x: 0, y: 0, vx: 0, vy: 0, r: 2, life: 0, max: 1, color: '#fff' };
}
export function resetParticle(p) { p.life = 0; }

/* ---- Shard: the two glowing halves a node splits into ---- */
export function createShard() {
  return { active: false, x: 0, y: 0, vx: 0, vy: 0, r: 16, rot: 0, spin: 0, life: 0, max: 1, color: '#fff', side: 1 };
}
export function resetShard(s) { s.life = 0; }
