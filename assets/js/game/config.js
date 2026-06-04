/* ============================================================
   config.js — single source of truth for all tunables.
   Keeping balance/feel constants in one place lets us tweak
   game-feel without touching system logic (Open/Closed).
   ============================================================ */
export const CONFIG = Object.freeze({
  /* simulation */
  step: 1 / 120,            // fixed update step (s) — deterministic logic
  gravity: 1650,            // px/s² (css px), size-independent arcs

  /* lives & scoring */
  lives: 3,
  comboWindow: 0.45,        // s — slices within this chain into a combo
  pointsPerNode: 10,

  /* spawning (difficulty ramps with elapsed time) */
  spawn: {
    baseInterval: 1.05,     // s between waves at start
    minInterval: 0.42,      // hard cap
    ramp: 0.010,            // interval -= ramp * elapsedSeconds
    burstMax: 3,            // up to N nodes per wave (grows over time)
  },

  /* a node's launch arc */
  node: {
    rMin: 26, rMax: 40,
    apexMin: 0.55, apexMax: 0.86, // fraction of play-height the arc peaks at
    spinMin: -2.4, spinMax: 2.4,  // rad/s
  },

  /* corrupted "bug" nodes — slicing them costs a life */
  bomb: {
    baseChance: 0.07,
    maxChance: 0.20,
    ramp: 0.0009,           // chance += ramp * elapsedSeconds
  },

  /* juice */
  particle: { count: 18, life: 0.75, speed: 480, drag: 0.92 },
  shard: { life: 0.9, speed: 300 },
  blade: { maxPoints: 20, life: 0.13 }, // trail length / fade

  /* palette — pulled from the site's design tokens */
  palette: {
    nodes: ['#2fe6e0', '#4d7dff', '#9a6bff', '#ff6ad5'],
    bomb: '#ff5468',
    blade: ['#2fe6e0', '#9a6bff'],
  },
});
