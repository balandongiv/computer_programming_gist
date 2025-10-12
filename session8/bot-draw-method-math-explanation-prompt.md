Analyze the mathematical calculations within the `draw` method of the provided Python `Bot` class. Focus on the calculations used to determine the positions of:

*   The four corners of the bot's body (within the `points` list).
*   The two sensor positions (within the `sensor_positions` list).
*   The two wheel positions (`wheel1_x`, `wheel1_y`, `wheel2_x`, `wheel2_y`).

For *each* of these calculations, provide a detailed explanation covering the following:

1.  What is the purpose of this calculation? What visual element is it positioning on the canvas?
2.  Explain the mathematical expression step-by-step, including:
    *   The role of `np.sin(angle)` and `np.cos(angle)` in positioning points relative to the bot's orientation (`self.theta`).
    *   The significance of any distances or constants (e.g., 20, 30).
    *   Why terms are added or subtracted, considering the canvas coordinate system (y-axis increases downwards).
    *   How the bot's `self.theta` angle affects the final coordinates.
3.  Explain how the use of `math.sin` and `math.cos` differs from `np.sin` and `np.cos`, and when each is appropriate.

Assume a reader familiar with basic Python and trigonometry but needing clarification on the specific application within this code.

[Paste the Python code from active\_component.py here]