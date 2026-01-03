from manim import *

class DotTracker(Scene):
    def construct(self):
        x = ValueTracker(0)

        def dot_pos():
            return RIGHT*x.get_value()
        
        dot = Dot()

        dot.add_updater(
            lambda m: m.move_to(dot_pos())
        )

        label = always_redraw(
            lambda: Text(f"x = {x.get_value():.1f}", font="Arial").next_to(dot, UP)
        )

        arrow = always_redraw(
            lambda: Arrow(
                ORIGIN, dot_pos(), buff = 0.1
            )
        )

        self.add(dot, arrow, label)
        self.play(x.animate.set_value(3))
        dot.clear_updaters()
        self.wait()
