from manim import *

class DotTracker(Scene):
    def construct(self):
        x = ValueTracker(0)

        def dot_pos():
            return RIGHT*x.get_value()
        
        dot = always_redraw(
            lambda: Dot().move_to(dot_pos())
        )

        arrow = always_redraw(
            lambda: Arrow(
                ORIGIN, dot_pos(), buff = 0.1
            )
        )

        self.add(dot, arrow)
        self.play(x.animate.set_value(3))
        self.wait()
