# Assignment 3 — Coordinates, Updaters, Camera

## Goal

Combine:

* Axes + `c2p`
* `ValueTracker`
* Updaters vs `always_redraw`
* Moving camera that *follows* an object

You should be comfortable reading Manim docs after this.

---

## Assignment 3 Tasks

### Task 1 — Moving Dot on Axes

* Create an `Axes`
* Use a `ValueTracker x`
* Place a dot at `(x, 0)` using `axes.c2p`
* Animate `x` from 0 → 4

**Constraints**

* Dot must move via an updater
* No hardcoded pixel coordinates

---

### Task 2 — Live Label

* Add a label above the dot
* Label should display `(x, 0)` rounded to 1 decimal
* Label must update continuously

(Hint: `always_redraw`)

---

### Task 3 — Arrow From Origin

* Draw an arrow from `(0, 0)` to `(x, 0)`
* Arrow length must change live as `x` changes

---

### Task 4 — Camera Follow + Zoom

* Use `MovingCameraScene`
* Camera should:

  * Follow the dot while it moves
  * Zoom in smoothly during motion

**Important:** Camera must track the dot *continuously*, not just once.

---

## Reference Solution (Clean & Idiomatic)

```python
from manim import *

class Assignment3(MovingCameraScene):
    def construct(self):
        x = ValueTracker(0)

        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4
        )

        dot = Dot(color=YELLOW)
        dot.add_updater(lambda m: m.move_to(axes.c2p(x.get_value(), 0)))

        label = always_redraw(
            lambda: Text(
                f"({x.get_value():.1f}, 0)", font_size=24
            ).next_to(dot, UP)
        )

        arrow = always_redraw(
            lambda: Arrow(
                axes.c2p(0, 0),
                axes.c2p(x.get_value(), 0),
                buff=0.1
            )
        )

        frame = self.camera.frame
        frame.add_updater(lambda f: f.move_to(dot))

        self.add(axes, dot, label, arrow)
        self.play(
            x.animate.set_value(4),
            frame.animate.scale(0.6),
            run_time=3
        )

        frame.clear_updaters()
        dot.clear_updaters()
        self.wait()
```
