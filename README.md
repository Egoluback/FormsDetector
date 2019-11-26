# FormsDetector
A class that spots forms with specific color and prints the number of it.
Also it can fill forms into color you want.

# Getting started

Just import class into your program and start it with params:

```python
from Detector import Detector

detector = Detector(FILL_COLOR, IMAGE_PATH, [{"value": RED_COLOR_VALUE, "mode": MODE_RED}, {"value": GREEN_COLOR_VALUE, "mode": MODE_GREEN}, {"value": BLUE_COLOR_VALUE, "mode": MODE_BLUE}], SHOULD_FILL_FORMS)

detector.Main()
```
