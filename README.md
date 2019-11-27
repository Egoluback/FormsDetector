# FormsDetector
A class that spots forms with specific color and prints the number of it.
Also it can fill forms into color you want.

# Getting started

Just import class into your program and start it with params:

```python
from Detector import Detector

IMAGE_PATH = "images/image.png"

COLOR_PARAMS = [{"value": RED_COLOR_VALUE, "mode": MODE_RED}, {"value": GREEN_COLOR_VALUE, "mode": MODE_GREEN}, {"value": BLUE_COLOR_VALUE, "mode": MODE_BLUE}]

FILL_COLOR = [0, 0, 0]

SHOULD_FILL_FORMS = True

detector = Detector(FILL_COLOR, IMAGE_PATH, COLOR_PARAMS, SHOULD_FILL_FORMS)

detector.Main()
```

```
COLOR_PARAMS = [{"value": RED_COLOR_VALUE, "mode": MODE_RED}, {"value": GREEN_COLOR_VALUE, "mode": MODE_GREEN}, {"value": BLUE_COLOR_VALUE, "mode": MODE_BLUE}]
```

COLOR_PARAMS is a array that contains information about your color.
It has 3 dicts, that have 2 fields: value and mode.
Value is a number corresponding to a color value.
Mode is a mode of analyzing your value; it may be:
> "moreEquals";

> "equals"; 

> "less".

# Example
#### Simple example of detector initialization with yellow color as params

```python

IMAGE_PATH = "images/image.png"
fillColor = [0, 0, 0]

detector = Detector(fillColor, IMAGE_PATH, [{"value": 70, "mode": "moreEquals"}, {"value": 70, "mode": "moreEquals"}, {"value": 150, "mode": "less"}], True)

detector.Main()
```

