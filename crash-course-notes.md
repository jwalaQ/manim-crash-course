# Manim Crash Course – Concepts & Patterns

This document summarizes the **concepts, mental models, and code patterns** discussed so far while learning Manim (Community Edition).

---

## 1. Mental Model

Manim works around three core ideas:

* **Scene** → one video
* **Mobject** → anything visible (text, shapes, arrows, groups)
* **Animation** → how mobjects appear, move, or change

```text
Scene
 ├── Mobjects (Text, Rectangle, Arrow, VGroup)
 ├── Animations (Write, FadeIn, Transform)
 └── Timing (wait, run_time)
```

---

## 2. Coordinate System & Units

Manim uses a **continuous mathematical coordinate system** (not pixels).

```python
RIGHT = [1, 0, 0]
LEFT  = [-1, 0, 0]
UP    = [0, 1, 0]
DOWN  = [0, -1, 0]
```

* Screen width ≈ **14 units**
* Screen height ≈ **8 units**
* Origin `(0, 0, 0)` is the center

### Best Practices

* Use raw coordinates for **geometry**
* Use layout helpers for **UI/layout**

---

## 3. Common Mobjects

### Text

```python
Text("Hello")
MathTex(r"E = mc^2")
```

### Shapes

```python
Circle()
Square()
Rectangle(width=3, height=1)
Line(start, end)
Arrow(start, end)
```

---

## 4. Positioning & Layout

### Absolute / Relative Positioning

```python
obj.move_to(ORIGIN)
obj.shift(RIGHT * 2)
```

### Layout Helpers (preferred)

```python
obj.to_edge(UP)
obj.next_to(other, RIGHT, buff=0.5)
```

### Group Layout

```python
group = VGroup(a, b, c)
group.arrange(RIGHT, buff=1)
group.center()
```

### What `arrange(RIGHT)` does

* Lays objects out left → right
* Respects actual object sizes
* Keeps vertical centers aligned

---

## 5. `buff`

`buff` = spacing **gap between objects** (in Manim units).

```python
text.next_to(box, UP, buff=0.3)
VGroup(a, b).arrange(RIGHT, buff=1)
```

Default is usually `0.25`.

---

## 6. Animations

### Entry / Exit

```python
Write(text)
FadeIn(obj)
FadeOut(obj)
Create(shape)
```

### Transformations

```python
Transform(a, b)
ReplacementTransform(a, b)
```

### Emphasis

```python
Indicate(obj)
Circumscribe(obj)
```

### Animate Syntax

```python
obj.animate.shift(RIGHT)
obj.animate.scale(1.5)
```

> **Nothing animates unless used inside `self.play()`**

---

## 7. Transform vs ReplacementTransform

### `Transform(a, b)`

* `a` morphs into the *shape* of `b`
* `a` remains the same object
* `b` is only a target

### `ReplacementTransform(a, b)`

* `a` morphs into `b`
* `a` is removed
* `b` becomes the real object

**Rule of thumb**:

* Physical object changing form → `Transform`
* Concept / label changing → `ReplacementTransform`

---

## 8. Static vs Animated Operations

```python
square.move_to(LEFT)          # static placement
self.play(square.animate.move_to(RIGHT))  # animated movement
```

Same operation, different context.

---

## 9. Grouping & Composition

### Reusable Component Pattern

```python
class LabeledBox(VGroup):
    def __init__(self, text, width=3, height=1, color=BLUE):
        super().__init__()
        box = Rectangle(width=width, height=height, color=color)
        label = Text(text).move_to(box.get_center())
        self.add(box, label)
        self.box = box
        self.label = label
```

This allows treating a **box + label as one object**.

---

## 10. Arrows & Connections

```python
Arrow(a.get_right(), b.get_left(), buff=0)
```

Use edge anchors (`get_left`, `get_right`) instead of centers.

---

## 11. Scenes & Rendering

```bash
manim intro.py Intro FullDemo AnotherScene
```

* Each Scene → **separate video**
* Scene name = class name
* Manim does **not** auto-concatenate scenes

---

## 12. Rendering Workflow Tips

* Use `-pql` during development
* Split long videos into multiple scenes
* Comment out heavy scenes when iterating

---

## Key Takeaways

* Layout helpers > raw numbers
* `.animate` is the animation switch
* Group semantic objects early
* `arrange()` repositions everything
* Think in **components**, not scenes
