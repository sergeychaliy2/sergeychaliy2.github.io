/* ============================================================
   StateMachine.js — explicit finite states (menu / playing /
   paused / over). Each state owns its enter/exit/update so the
   game loop never grows a tangle of boolean flags.
   ============================================================ */
export class StateMachine {
  /** @param {Record<string,{enter?:Function,exit?:Function,update?:Function}>} states */
  constructor(states) {
    this._states = states;
    this._current = null;
    this._name = null;
  }

  get name() { return this._name; }
  is(name) { return this._name === name; }

  change(name, payload) {
    if (this._name === name) return;
    this._current?.exit?.();
    this._name = name;
    this._current = this._states[name];
    this._current?.enter?.(payload);
  }

  update(dt) { this._current?.update?.(dt); }
}
