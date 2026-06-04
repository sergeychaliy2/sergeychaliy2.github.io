/* ============================================================
   ScoringSystem — owns score, combo chain, lives and screen
   shake. It is the only place that reacts to slice/miss facts,
   keeping that policy in one auditable spot. Re-emits compact
   HUD events for the presentation layer.
   ============================================================ */
import { CONFIG } from '../config.js';

export class ScoringSystem {
  constructor(world, bus) {
    this.world = world; this.bus = bus; this._over = false;
    bus.on('node:sliced', (e) => this._onSlice(e));
    bus.on('bomb:sliced', (e) => this._onBomb(e));
    bus.on('node:missed', () => this._onMiss());
  }

  reset() { this._over = false; }

  _onSlice(e) {
    const w = this.world;
    w.combo += 1;
    w.comboTimer = CONFIG.comboWindow;
    const gained = CONFIG.pointsPerNode * w.combo;   // chain multiplies
    w.score += gained;
    this.bus.emit('hud:score', w.score);
    if (w.combo >= 2) this.bus.emit('fx:combo', { combo: w.combo, x: e.x, y: e.y });
  }

  _onBomb(e) {
    const w = this.world;
    w.shake = Math.min(1, w.shake + 0.9);
    w.combo = 0; w.comboTimer = 0;
    this.bus.emit('fx:flash');
    this._loseLife();
  }

  _onMiss() {
    const w = this.world;
    w.combo = 0; w.comboTimer = 0;
    w.shake = Math.min(1, w.shake + 0.25);
    this._loseLife();
  }

  _loseLife() {
    if (this._over) return;
    this.world.lives -= 1;
    this.bus.emit('hud:lives', this.world.lives);
    if (this.world.lives <= 0) {
      this._over = true;
      this.bus.emit('game:over', this.world.score);
    }
  }

  update(dt) {
    const w = this.world;
    if (w.comboTimer > 0) {
      w.comboTimer -= dt;
      if (w.comboTimer <= 0) w.combo = 0;
    }
    if (w.shake > 0) w.shake = Math.max(0, w.shake - dt * 1.6);
  }
}
