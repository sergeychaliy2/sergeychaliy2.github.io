/* ============================================================
   Vec2.js — tiny 2D math helpers (pure, allocation-light).
   ============================================================ */
export const Vec2 = {
  len(x, y) { return Math.hypot(x, y); },
  dist(ax, ay, bx, by) { return Math.hypot(ax - bx, ay - by); },

  /** Squared distance from point P to segment A→B. Avoids sqrt in the
   *  hot slice-test path; callers compare against r². */
  distToSegmentSq(px, py, ax, ay, bx, by) {
    const dx = bx - ax, dy = by - ay;
    const lenSq = dx * dx + dy * dy;
    let t = lenSq > 0 ? ((px - ax) * dx + (py - ay) * dy) / lenSq : 0;
    t = t < 0 ? 0 : t > 1 ? 1 : t;
    const cx = ax + t * dx, cy = ay + t * dy;
    const ex = px - cx, ey = py - cy;
    return ex * ex + ey * ey;
  },
};
