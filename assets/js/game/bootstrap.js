/* ============================================================
   bootstrap.js — presentation layer for play.html.
   Owns the DOM HUD/overlays and translates Game bus-events into
   pixels. The Game core knows nothing about any of this.
   ============================================================ */
import { CONFIG } from './config.js';
import { Game } from './Game.js';

const BEST_KEY = 'neural-slice-best';
const $ = (id) => document.getElementById(id);

function init() {
  const canvas = $('game-canvas');
  if (!canvas) return;

  const els = {
    score: $('hud-score'),
    lives: $('hud-lives'),
    best: $('hud-best'),
    fx: $('fx-layer'),
    finalScore: $('ov-final-score'),
    finalBest: $('ov-final-best'),
    newBest: $('ov-newbest'),
    ovStart: $('ov-start'),
    ovPause: $('ov-pause'),
    ovOver: $('ov-over'),
    pauseBtn: $('pause-btn'),
  };

  let best = Number(localStorage.getItem(BEST_KEY) || 0);
  const game = new Game(canvas);
  const bus = game.bus;

  renderBest();
  renderLives(CONFIG.lives);

  /* ---- HUD bindings ---- */
  bus.on('hud:score', (s) => { els.score.textContent = format(s); });
  bus.on('hud:lives', (n) => renderLives(n));
  bus.on('fx:combo', (e) => spawnCombo(e));

  bus.on('game:over', (finalScore) => {
    const isBest = finalScore > best;
    if (isBest) { best = finalScore; localStorage.setItem(BEST_KEY, String(best)); renderBest(); }
    els.finalScore.textContent = format(finalScore);
    els.finalBest.textContent = format(best);
    els.newBest.style.display = isBest && finalScore > 0 ? '' : 'none';
    show(els.ovOver);
  });

  bus.on('game:paused', () => show(els.ovPause));
  bus.on('game:resumed', () => hide(els.ovPause));

  /* ---- controls ---- */
  const startRun = () => { hide(els.ovStart); hide(els.ovOver); els.pauseBtn.style.display = ''; game.startRun(); };

  bindClick('btn-start', startRun);
  bindClick('btn-restart', startRun);
  bindClick('btn-resume', () => game.resume());
  els.pauseBtn.addEventListener('click', () => game.togglePause());

  document.addEventListener('keydown', (e) => {
    if (e.code === 'Space' || e.key === 'p' || e.key === 'P') {
      if (game.state === 'playing' || game.state === 'paused') { e.preventDefault(); game.togglePause(); }
    }
    if (e.key === 'Enter') {
      if (game.state === 'menu') startRun();
      else if (game.state === 'over') startRun();
    }
  });

  // auto-pause when the tab is hidden mid-run
  document.addEventListener('visibilitychange', () => {
    if (document.hidden && game.state === 'playing') game.pause();
  });

  game.mount();

  // dev convenience: open play.html#autostart to jump straight into a run
  if (location.hash.indexOf('autostart') !== -1) startRun();

  /* ---- helpers ---- */
  function renderLives(n) {
    const max = CONFIG.lives;
    let html = '';
    for (let i = 0; i < max; i++) html += heart(i < n);
    els.lives.innerHTML = html;
  }
  function renderBest() { if (els.best) els.best.textContent = format(best); }

  function spawnCombo(e) {
    const rect = canvas.getBoundingClientRect();
    const layer = els.fx;
    const lr = layer.getBoundingClientRect();
    const pop = document.createElement('div');
    pop.className = 'combo-pop';
    pop.textContent = `COMBO ×${e.combo}`;
    pop.style.left = (rect.left - lr.left + e.x) + 'px';
    pop.style.top = (rect.top - lr.top + e.y) + 'px';
    layer.appendChild(pop);
    setTimeout(() => pop.remove(), 750);
  }
}

function heart(filled) {
  return `<svg class="life ${filled ? 'on' : 'off'}" viewBox="0 0 24 24"><path d="M12 21s-7.5-4.6-10-9.3C.4 8.4 1.8 4.8 5.2 4.8c2 0 3.3 1.1 4.1 2.3l.6 1 .6-1c.8-1.2 2.1-2.3 4.1-2.3 3.4 0 4.8 3.6 3.2 6.9C19.5 16.4 12 21 12 21z"/></svg>`;
}
function format(n) { return n.toLocaleString('en-US'); }
function bindClick(id, fn) { const el = document.getElementById(id); if (el) el.addEventListener('click', fn); }
function show(el) { el && el.classList.add('show'); }
function hide(el) { el && el.classList.remove('show'); }

if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
else init();
