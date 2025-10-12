# Iterate over robot configurations and create robots
for config in data['robot_configurations']:  # Assuming data['robot_configurations'] is a list of configurations
    color_key = 'robot1' if config['label'] == 'Robot One' else 'robot2'  # Determine color key based on robot label
    robot = Bot(canvas,
                label=config['label'],  # Use the label from the configuration
                color=data['colors'][color_key],  # Get color from data['colors'] using the determined color key
                robot_configuration=config)  # Pass the current configuration
    robot.draw_robot()  # Draw each robot
