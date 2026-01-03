from manim import *

class LabeledBox(VGroup):
    def __init__(self, text, width=3, height=1, color=BLUE):
        super().__init__()

        box = Rectangle(width=width, height=height, color=color)
        label = Text(text=text).move_to(box.get_center())

        self.add(box, label)
        self.box = box
        self.label = label