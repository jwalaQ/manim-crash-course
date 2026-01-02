# Assignment: Mini Explainer Scene (Manim)

## Goal

Create a **single Manim Scene** that visually explains:

> **“A value flows from Input → Processing → Output”**

This assignment reinforces **layout, grouping, animations, and transformations**.

---

## Requirements Checklist

### 1. Title

* Use `Text`
* Positioned at the top using `to_edge(UP)`
* Appears using `Write`

---

### 2. Three Boxes

Represent:

* Input
* Processing
* Output

Requirements:

* Use `Rectangle`
* Boxes arranged horizontally using `VGroup(...).arrange(RIGHT, buff=?)`
* Boxes should be **vertically centered**

---

### 3. Labels

* Each box has a text label inside it
* Labels must move with their boxes

---

### 4. Arrows

* Use `Arrow`
* Arrows must connect **edges** of boxes
* Use `get_left()` / `get_right()`

---

### 5. Animation Order

Animate in this exact sequence:

1. Title appears
2. Input box appears
3. Processing box appears
4. Output box appears
5. Arrows appear
6. Processing box is highlighted
7. Input label transforms into Output label

Use at least:

* `Write`
* `FadeIn` or `Create`
* `Indicate` or `Circumscribe`
* `ReplacementTransform`

---

### 6. Timing

* Use at least one `wait()`
* Use at least one explicit `run_time`
* Animation should not feel rushed

---

### 7. Ending

Fade everything out:

```python
self.play(FadeOut(*self.mobjects))
```

---

## Constraints

* ❌ No `ValueTracker`
* ❌ No `always_redraw`
* ❌ No camera movement
* ❌ No external assets

Only concepts covered so far.

---

## Optional Skeleton

```python
from manim import *

class DataFlow(Scene):
    def construct(self):
        title = Text("Simple Data Flow").to_edge(UP)

        input_box = Rectangle(width=3, height=1)
        process_box = Rectangle(width=4, height=1)
        output_box = Rectangle(width=3, height=1)

        boxes = VGroup(input_box, process_box, output_box)
        boxes.arrange(RIGHT, buff=1)
        boxes.center()

        # Labels
        # Arrows
        # Animations
```

---

## What to Submit

1. The full `Scene` code
2. Short reflection:

   * What felt intuitive?
   * What felt awkward?

---

## Evaluation Criteria

* Clear visual flow without narration
* Correct use of layout helpers
* Proper grouping of box + label
* Correct choice of `ReplacementTransform`
* Readable and reusable code

---

This assignment is a **checkpoint**, not a trick. If it feels doable (but slightly uncomfortable), you’re exactly where you should be.
