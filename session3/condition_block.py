# Add a variable to control the condition
condition = True  # You can change this condition as needed

# Create robots using a loop
for config in robot_configurations:
    # Access the corresponding color configuration using the robot's id
    robot_colors = colors[config['id']]

    # Check the condition and change the body color accordingly
    body_color = robot_colors["body_color"] if condition else "black"

    print(f"Robot {config['id']} is having the color {body_color} given that the condition is {condition}.")