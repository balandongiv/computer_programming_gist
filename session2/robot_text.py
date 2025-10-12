# Add text next to the robots
text_x1 = center_x1 + 40  # Adjust the X-coordinate to position the text for robot 1
text_y1 = center_y1

text_x2 = center_x2 + 40  # Adjust the X-coordinate to position the text for robot 2
text_y2 = center_y2
canvas.create_text(text_x1, text_y1, text="Your Matric Number", anchor=tk.W)
canvas.create_text(text_x2, text_y2, text="Your Full Name", anchor=tk.W)