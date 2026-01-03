
# Manim Crash Course – Notes (Part 2)

> This document continues from the original [Manim notes file]().
> It focuses on **dynamic scenes, updaters, coordinate systems, and camera control**.

---

## 1. Dynamic Objects: ValueTracker

### What it is

`ValueTracker` stores a single floating-point value that can be animated over time.

```python
x = ValueTracker(0)
self.play(x.animate.set_value(3))
```

### Why it exists

* Separates *state* from *visuals*
* Enables smooth, continuous animation logic

> Rule: **Never animate numbers directly — animate trackers**

---

## 2. always_redraw vs Updaters

### always_redraw

Recreates an object *every frame*.

```python
label = always_redraw(
    lambda: Text(f"x = {x.get_value():.1f}")
)
```

**Use when**:

* Object structure changes (text, arrows, shapes)
* Object depends on multiple moving targets

---

### add_updater

Modifies the *same object* every frame.

```python
dot.add_updater(
    lambda m: m.move_to(RIGHT * x.get_value())
)
```

**Use when**:

* Position / color / opacity changes
* You want performance + continuity

---

### Key difference

| always_redraw         | updater             |
| --------------------- | ------------------- |
| New object each frame | Same object mutated |
| Easy                  | Efficient           |
| Slightly heavier      | Lightweight         |

---

## 3. Clearing Updaters (Very Important)

Updaters **persist forever** unless removed.

```python
dot.clear_updaters()
```

Failure to clear updaters leads to:

* Unexpected motion
* Conflicting animations
* Hard-to-debug scenes

---

## 4. Coordinate Systems

### Axes

```python
axes = Axes(
    x_range=[-6, 6, 1],
    y_range=[-4, 4, 1]
)
```

### c2p — coordinate to point

```python
axes.c2p(x, y)
```

**What it does**:

* Converts *math coordinates* → *scene coordinates*
* Handles scaling automatically

> Always use `c2p` when working with Axes

---

## 5. NumberPlane vs Axes

| Axes          | NumberPlane          |
| ------------- | -------------------- |
| Minimal       | Grid included        |
| Cleaner       | Visually noisy       |
| Final visuals | Debugging & learning |

---

## 6. Camera Control

### Scene types

| Scene             | Camera        |
| ----------------- | ------------- |
| Scene             | Static        |
| MovingCameraScene | Movable frame |

---

### Camera frame

```python
frame = self.camera.frame
```

* `frame` is a normal Mobject
* Can be animated like any other object

---

### Camera following a moving object

If the target moves via updater, the camera **must also use an updater**.

```python
frame.add_updater(lambda f: f.move_to(dot))
```

> animate → static target
> updater → dynamic tracking

---

## 7. Why Camera.animate.move_to(dot) Sometimes Fails

Animations sample targets **once at the start**.

If `dot` moves during the animation:

* Camera moves to initial position
* Dot continues moving elsewhere

**Fix**: use updaters.

---

## 8. arrange(), next_to(), buff

### arrange

```python
VGroup(a, b, c).arrange(RIGHT, buff=1)
```

* Positions objects sequentially
* Uses each object's bounding box

---

### buff

`buff` = gap between objects (scene units, not pixels)

* Default ≈ 0.25
* Uses Manim's internal coordinate system

---

## 9. Scene Units (Important Concept)

* Manim uses **logical scene units**, not pixels
* Default frame width ≈ 14 units

So:

* RIGHT = (1, 0, 0)
* UP = (0, 1, 0)

> Design visually, not numerically

---

## 10. Debugging & Development Tips

* Use `NumberPlane()` while building
* Use `-pql` (preview low quality)
* Render final with `-pqh` or `-pqk`
* Clear updaters aggressively

---

## Other Notes

### 1. `self.add(...)`

* Immediately places mobjects on screen
* No animation
* Think: **initial scene composition**

---

### 2. `c2p(x, y)`

* Converts **data coordinates → scene coordinates**
* Automatically accounts for:

  * Axis ranges
  * Axis scaling
  * Screen size

You work in *math space*, Manim handles *pixel space*.

---

### 3. `always_redraw` vs `add_updater`

**Use `always_redraw` when:**

* Object is cheap to recreate (text, arrows)
* Shape depends on multiple things

**Use `add_updater` when:**

* Object persists
* Only position / small property changes
* Performance matters

---

### 4. Camera Mental Model

* `animate.move_to(obj)` → samples once
* `add_updater(lambda f: f.move_to(obj))` → tracks live

If *A moves continuously* and *B follows A* → **B needs an updater**.

---

### 5. Grids / NumberPlane

* Useful for:

  * Debugging
  * Teaching coordinates
* Avoid for final polished explainers:

  * Too visually noisy
  * Distracts from the idea

---

## Mental Models to Keep

* Scene = timeline
* Mobject = stateful visual object
* animate = interpolation
* updater = continuous rule
* camera = just another object

---

## What You Should Be Able To Do Now

* Read Manim docs meaningfully
* Translate math → animation structure
* Decide between updaters and redraws
* Control camera motion intentionally

You're officially past "tutorial hell" for Manim 🎉
