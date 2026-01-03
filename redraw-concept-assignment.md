# Manim Assignment 2 – Dynamic Tracking with ValueTracker & always_redraw

## Goal

Build an animation where multiple visual elements **react dynamically** to a changing value, without manually animating each object.

This assignment is meant to:

* Reinforce `ValueTracker`
* Build intuition for `always_redraw`
* Separate *state* from *visual representation*

---

## Scene Description

Create a scene that shows:

1. A **number line** (or x-axis)
2. A **dot** that moves along the x-axis
3. A **label** that always stays above the dot and displays its current x-value
4. An **arrow** from the origin pointing to the dot

All elements must update automatically as the value changes.

---

## Required Constraints

* Use **one** `ValueTracker`
* Use `always_redraw` for:

  * The dot
  * The label
  * The arrow
* Do **not** use `.animate` on the dot, label, or arrow directly
* Animate **only the tracker**

---

## Suggested Animation Flow

* Start with the dot at `x = 0`
* Animate the tracker smoothly to `x = 4`
* Pause briefly
* Animate back to `x = -2`

---

## Hints (Optional)

* Remember: `ValueTracker` stores a **number**, not a point
* Convert scalar → point using vectors like `RIGHT * value`
* Use helper functions if multiple objects depend on the same position

---

## Bonus (Optional)

If you want an extra challenge:

* Change the dot color based on whether `x` is positive or negative
* Add a vertical line that always passes through the dot

---

## Success Criteria

You’re done when:

* All objects stay perfectly synchronized
* Removing `always_redraw` breaks the behavior
* You never manually reposition objects during the animation

---

When finished, paste your code back here and we’ll review it before moving on 🚀
