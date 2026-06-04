/* ============================================================
   Loop.js — fixed-timestep game loop with an accumulator.
   Logic advances in deterministic `step` slices regardless of
   display refresh rate; rendering interpolates with `alpha`.
   (Glenn Fiedler's "Fix Your Timestep".)
   ============================================================ */
export class Loop {
  /**
   * @param {object} o
   * @param {(dt:number)=>void} o.update   fixed-step simulation
   * @param {(alpha:number)=>void} o.render  draw, alpha∈[0,1)
   * @param {number} o.step                  seconds per update
   */
  constructor({ update, render, step }) {
    this._update = update;
    this._render = render;
    this._step = step;
    this._acc = 0;
    this._last = 0;
    this._raf = 0;
    this._running = false;
    this._frame = this._frame.bind(this);
  }

  start() {
    if (this._running) return;
    this._running = true;
    this._last = 0;
    this._raf = requestAnimationFrame(this._frame);
  }

  stop() {
    this._running = false;
    cancelAnimationFrame(this._raf);
  }

  _frame(now) {
    if (!this._running) return;
    if (!this._last) this._last = now;
    // Clamp huge gaps (tab was backgrounded) so we never spiral.
    let dt = (now - this._last) / 1000;
    this._last = now;
    if (dt > 0.25) dt = 0.25;

    this._acc += dt;
    while (this._acc >= this._step) {
      this._update(this._step);
      this._acc -= this._step;
    }
    this._render(this._acc / this._step);
    this._raf = requestAnimationFrame(this._frame);
  }
}
