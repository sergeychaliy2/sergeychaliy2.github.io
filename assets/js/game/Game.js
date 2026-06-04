/* ============================================================
   Game.js — composition root. Builds the world, wires systems
   via constructor injection, owns the fixed-step loop and the
   menu→playing→paused→over state machine. The DOM layer talks
   to it only through `bus` events and a small public API.
   ============================================================ */
import { CONFIG } from './config.js';
import { EventBus } from './core/EventBus.js';
import { StateMachine } from './core/StateMachine.js';
import { Loop } from './core/Loop.js';
import { Input } from './core/Input.js';
import { World } from './World.js';
import { SpawnSystem } from './systems/SpawnSystem.js';
import { PhysicsSystem } from './systems/PhysicsSystem.js';
import { SliceSystem } from './systems/SliceSystem.js';
import { ScoringSystem } from './systems/ScoringSystem.js';
import { ParticleSystem } from './systems/ParticleSystem.js';
import { RenderSystem } from './systems/RenderSystem.js';

export class Game {
  /** @param {HTMLCanvasElement} canvas */
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.bus = new EventBus();
    this.clock = () => performance.now() / 1000;

    this.world = new World();
    this.input = new Input(canvas, this.clock);
    this.input.setEnabled(false);

    // systems (dependencies injected — no globals, no singletons)
    this.spawn = new SpawnSystem(this.world);
    this.physics = new PhysicsSystem(this.world, this.bus);
    this.slice = new SliceSystem(this.world, this.bus, this.input);
    this.scoring = new ScoringSystem(this.world, this.bus);
    this.particles = new ParticleSystem(this.world, this.bus);
    this.renderer = new RenderSystem(this.world, this.input, this.ctx, this.bus);

    this.sm = new StateMachine({
      menu: { enter: () => this._enterMenu() },
      playing: { enter: () => this._enterPlaying(), update: (dt) => this._updatePlaying(dt) },
      paused: {},
      over: { enter: () => this._enterOver() },
    });

    this.loop = new Loop({
      update: (dt) => this.sm.update(dt),
      render: () => this._render(),
      step: CONFIG.step,
    });

    this.bus.on('game:over', () => this.sm.change('over'));

    this._ro = new ResizeObserver(() => this._resize());
    this._ro.observe(canvas);
    this._resize();
  }

  /* ---------- public API ---------- */
  mount() { this.sm.change('menu'); this.loop.start(); }

  startRun() { this._fresh = true; this.sm.change('playing'); }

  pause() {
    if (!this.sm.is('playing')) return;
    this.sm.change('paused');
    this.input.setEnabled(false);
    this.bus.emit('game:paused');
  }

  /** Resume keeps the field intact (the `_fresh` flag stays false). */
  resume() {
    if (!this.sm.is('paused')) return;
    this._fresh = false;
    this.sm.change('playing');
    this.bus.emit('game:resumed');
  }

  togglePause() { this.sm.is('paused') ? this.resume() : this.pause(); }

  get state() { return this.sm.name; }

  destroy() {
    this.loop.stop();
    this.input.destroy();
    this._ro.disconnect();
    this.bus.clear();
  }

  /* ---------- state handlers ---------- */
  _enterMenu() {
    this.world.reset();
    this.input.setEnabled(false);
  }

  _enterPlaying() {
    // Full reset only when arriving fresh — resuming keeps the field.
    if (this._fresh) {
      this.world.reset();
      this.world.lives = CONFIG.lives;
      this.spawn.reset();
      this.scoring.reset();
      this.bus.emit('hud:score', 0);
      this.bus.emit('hud:lives', this.world.lives);
    }
    this.input.setEnabled(true);
  }

  _updatePlaying(dt) {
    this.world.elapsed += dt;
    this.slice.update();
    this.spawn.update(dt);
    this.physics.update(dt);
    this.scoring.update(dt);
  }

  _enterOver() {
    this.input.setEnabled(false);
  }

  _render() {
    this.input.pruneTrail(CONFIG.blade.life);
    this.renderer.render();
  }

  /* ---------- viewport ---------- */
  _resize() {
    const rect = this.canvas.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    this.world.w = rect.width;
    this.world.h = rect.height;
    this.world.dpr = dpr;
    this.canvas.width = Math.round(rect.width * dpr);
    this.canvas.height = Math.round(rect.height * dpr);
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
}
