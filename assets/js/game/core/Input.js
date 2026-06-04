/* ============================================================
   Input.js — unifies mouse / touch / pen into one "blade".
   Exposes a fading trail (for rendering) and a queue of swipe
   segments since last frame (for hit-testing) so fast swipes
   are never missed between frames.
   ============================================================ */
export class Input {
  /** @param {HTMLCanvasElement} canvas */
  constructor(canvas, clock) {
    this.canvas = canvas;
    this._clock = clock;            // () => seconds
    this.down = false;
    this.x = 0; this.y = 0;
    /** @type {{x:number,y:number,t:number}[]} */
    this.trail = [];
    /** @type {{x1:number,y1:number,x2:number,y2:number}[]} */
    this._segments = [];
    this._enabled = true;

    this._onDown = this._onDown.bind(this);
    this._onMove = this._onMove.bind(this);
    this._onUp = this._onUp.bind(this);

    canvas.addEventListener('pointerdown', this._onDown);
    canvas.addEventListener('pointermove', this._onMove);
    window.addEventListener('pointerup', this._onUp);
    window.addEventListener('pointercancel', this._onUp);
  }

  setEnabled(v) { this._enabled = v; if (!v) { this.down = false; this.trail.length = 0; } }

  _pos(e) {
    const r = this.canvas.getBoundingClientRect();
    return { x: e.clientX - r.left, y: e.clientY - r.top };
  }

  _onDown(e) {
    if (!this._enabled) return;
    this.down = true;
    const p = this._pos(e);
    this.x = p.x; this.y = p.y;
    this.trail.length = 0;
    this.trail.push({ x: p.x, y: p.y, t: this._clock() });
    try { this.canvas.setPointerCapture(e.pointerId); } catch {}
  }

  _onMove(e) {
    if (!this._enabled || !this.down) return;
    e.preventDefault();
    const p = this._pos(e);
    this._segments.push({ x1: this.x, y1: this.y, x2: p.x, y2: p.y });
    this.x = p.x; this.y = p.y;
    this.trail.push({ x: p.x, y: p.y, t: this._clock() });
  }

  _onUp() {
    this.down = false;
  }

  /** Hand the accumulated swipe segments to the slice system, then clear. */
  consumeSegments() {
    if (!this._segments.length) return EMPTY;
    const out = this._segments;
    this._segments = [];
    return out;
  }

  /** Drop trail points older than `life` seconds so the blade tapers off. */
  pruneTrail(life) {
    const cutoff = this._clock() - life;
    const tr = this.trail;
    let i = 0;
    while (i < tr.length && tr[i].t < cutoff) i++;
    if (i > 0) tr.splice(0, i);
  }

  destroy() {
    this.canvas.removeEventListener('pointerdown', this._onDown);
    this.canvas.removeEventListener('pointermove', this._onMove);
    window.removeEventListener('pointerup', this._onUp);
    window.removeEventListener('pointercancel', this._onUp);
  }
}
const EMPTY = [];
