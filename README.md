# manim-crash-course

Small collection of Manim example scenes used for learning and demonstrations.

## Overview

I asked ChatGPT for: 
> Crash course on manim. Common commands, common classes, stringing components together, customization - colours, animations, transitions.

The summarized crash-course is available in [crash-course-notes.md](crash-course-notes.md)

### Requirements

- Python 3.10 or newer
- manim (Community edition)

Install with:

```bash
pip install manim
```

### Quick Start

Run the `SimpleDataFlow` scene locally (renders a low-quality preview):

```bash
manim -pql src/scenes/SimpleDataFlow.py SimpleDataFlow
```

For gif

```bash
manim -pql --format=gif src/scenes/SimpleDataFlow.py SimpleDataFlow
```

Replace `-pql` with `-pqh` or `-p` for higher-quality renders.

Assignment output (gif): 

![](https://github.com/jwalaQ/manim-crash-course/blob/mainline/media/videos/SimpleDataFlow/480p15/SimpleDataFlow_ManimCE_v0.19.1.gif)


## License

Add a license as appropriate for your project.
