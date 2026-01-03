from manim import *
from components.LabeledBox import LabeledBox

class SimpleDataFlow(Scene):

    def construct(self):
        title = Text("Simple Data Flow").to_edge(UP)
        
        input_box = LabeledBox("Input", color=BLUE)
        processing_box = LabeledBox("Processing", width=4, color=ORANGE)
        output_box = LabeledBox("Output", color=GREEN)

        boxes = VGroup(input_box, processing_box, output_box).arrange(RIGHT, buff=1)

        arrows = [
            Arrow(input_box.get_right(), processing_box.get_left(), buff=0),
            Arrow(processing_box.get_right(), output_box.get_left(), buff=0)
        ]
        
        self.play(Write(title))
        self.play(FadeIn(boxes))
        self.play(Create(arrows[0]), Create(arrows[1]))
        self.play(Indicate(processing_box.box).set_run_time(1))

        self.play(ReplacementTransform(input_box.label, output_box.label).set_run_time(2))

        self.wait()
