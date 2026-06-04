/* ============================================================
   EventBus.js — minimal pub/sub.
   Systems stay decoupled: they publish facts ("node:sliced")
   instead of calling each other directly. The presentation
   layer (HUD/overlays) subscribes without the domain knowing
   the DOM exists.
   ============================================================ */
export class EventBus {
  constructor() {
    /** @type {Map<string, Set<Function>>} */
    this._listeners = new Map();
  }

  /** Subscribe. Returns an unsubscribe function. */
  on(type, handler) {
    let set = this._listeners.get(type);
    if (!set) this._listeners.set(type, (set = new Set()));
    set.add(handler);
    return () => set.delete(handler);
  }

  emit(type, payload) {
    const set = this._listeners.get(type);
    if (!set) return;
    // Snapshot so handlers may (un)subscribe during dispatch.
    for (const handler of [...set]) handler(payload);
  }

  clear() { this._listeners.clear(); }
}
