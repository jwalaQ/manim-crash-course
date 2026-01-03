from manim import *

class SimpleDataFlow(Scene):

    def construct(self):
        title = Text("Simple Data Flow").to_edge(UP)
        inputBox = Rectangle(width=3, height = 1, color=BLUE).to_edge(LEFT*2)
        processingBox = Rectangle(width=4, height = 1, color=ORANGE).move_to(ORIGIN)
        outputBox = Rectangle(width=3, height = 1, color=GREEN).to_edge(RIGHT*2)
        
        boxes = VGroup(inputBox, processingBox, outputBox).arrange(RIGHT, buff=1)
        
        boxLabels = [
            Text("Input").move_to(inputBox.get_center()), 
            Text("Processing").move_to(processingBox.get_center()), 
            Text("Output").move_to(outputBox.get_center())
        ]

        arrows = [
            Arrow(inputBox.get_right(), processingBox.get_left(), buff=0),
            Arrow(processingBox.get_right(), outputBox.get_left(), buff=0)
        ]
        
        self.play(Write(title).set_run_time(2))
        for box, label in zip(boxes, boxLabels):
            self.play(FadeIn(box), Write(label))
            self.wait(0.5)

        self.play(FadeIn(arrows[0]), FadeIn(arrows[1]))

        self.play(Indicate(processingBox).set_run_time(1))

        self.play(ReplacementTransform(boxLabels[0], boxLabels[2]).set_run_time(2))

        self.wait()
