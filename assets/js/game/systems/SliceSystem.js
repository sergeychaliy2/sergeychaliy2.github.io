/* ============================================================
   SliceSystem — tests this frame's swipe segments against every
   live node (segment↔circle). Hits publish node:sliced /
   bomb:sliced with the cut angle; scoring & particles react.
   ============================================================ */
import { Vec2 } from '../core/Vec2.js';

export class SliceSystem {
  constructor(world, bus, input) {
    this.world = world; this.bus = bus; this.input = input;
  }

  update() {
    const segments = this.input.consumeSegments();
    if (!segments.length) return;
    const nodes = this.world.nodes;

    for (const seg of segments) {
      const angle = Math.atan2(seg.y2 - seg.y1, seg.x2 - seg.x1);
      for (let i = nodes.length - 1; i >= 0; i--) {
        const n = nodes[i];
        if (n.sliced) continue;
        const rr = n.r * n.r;
        if (Vec2.distToSegmentSq(n.x, n.y, seg.x1, seg.y1, seg.x2, seg.y2) <= rr) {
          n.sliced = true;
          this.world.nodes.splice(i, 1);
          this.bus.emit(n.type === 'bomb' ? 'bomb:sliced' : 'node:sliced',
            { x: n.x, y: n.y, color: n.color, r: n.r, angle });
          this.world.nodePool.release(n);
        }
      }
    }
  }
}
