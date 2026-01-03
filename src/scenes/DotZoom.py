from manim import *

class DotZoom(MovingCameraScene):
    def construct(self):
        x = ValueTracker()
        axes = Axes(
                x_range=[-6, 6, 1],
                y_range=[-4, 4, 1], 
                x_length=12, 
                y_length=6
               )
        
        dot = Dot()
        dot.add_updater(
            lambda m: m.move_to(axes.c2p(x.get_value(),0))
        )

        dotLabel = always_redraw(
            lambda : Text(f"({x.get_value():.1f}, 0)", font_size=12).next_to(dot, UP)
        )

        frame = self.camera.frame
        frame.add_updater(
            lambda f : f.move_to(dot) 
        )

        self.add(axes, dot, dotLabel)
        self.play(FadeIn(axes), FadeIn(dot), run_time=1)
        self.play(
            x.animate.set_value(3), 
            frame.animate.scale(0.5), 
            run_time=3
        )

        frame.clear_updaters()
        self.wait()