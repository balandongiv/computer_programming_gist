

I'm working on a Python project and need help with importing classes across files. Here's the situation:

I have a file called `main.py` inside a `session8` folder, and it already includes the following import line:

```python
from helper.robot_helper import initialize_canvas, bot_clicked
```

The structure of my project is:

```
project_folder/
│
├── helper/
│   └── robot_helper.py
│
└── session8/
    ├── main.py
    ├── active_component.py
    └── passive_component.py
```

Now, I want to use the class `Bot` from `active_component.py`, and the classes `Dirt`, `Counter`, `WiFiHub`, and `Charger` from `passive_component.py`.

**My questions are:**
1. Where in `main.py` should I add the import statements for these classes?
2. What should the correct import statements look like, given that all these files are in the same `session8` folder?

Please explain it in a way that a beginner Python programmer can understand. Thanks!