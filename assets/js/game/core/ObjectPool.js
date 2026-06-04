/* ============================================================
   ObjectPool.js — recycles objects to keep GC quiet.
   Nodes and particles churn dozens of times a second; pooling
   them removes per-frame allocation spikes (GC optimisation).
   ============================================================ */
export class ObjectPool {
  /**
   * @param {() => object} factory  creates a blank instance
   * @param {(o:object) => void} reset  returns an instance to a neutral state
   * @param {number} prealloc  how many to warm up front
   */
  constructor(factory, reset, prealloc = 0) {
    this._factory = factory;
    this._reset = reset;
    this._free = [];
    for (let i = 0; i < prealloc; i++) this._free.push(factory());
  }

  acquire() {
    const obj = this._free.pop() || this._factory();
    obj.active = true;
    return obj;
  }

  release(obj) {
    obj.active = false;
    this._reset(obj);
    this._free.push(obj);
  }

  get size() { return this._free.length; }
}
