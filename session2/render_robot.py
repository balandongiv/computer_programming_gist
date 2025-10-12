canvas.create_polygon(robot2_points, fill=body_color, tags='robot')
canvas.create_oval(center_x2 - 8, center_y2 - 8, center_x2 + 8, center_y2 + 8, fill=light_color, tags='robot')


# Create robot components on the canvas for robot 2
canvas.create_oval(wheel1_x2 - constant_val, wheel1_y2 - constant_val, wheel1_x2 + constant_val, wheel1_y2 + constant_val, fill=wheel_color_left, tags='robot')
canvas.create_oval(wheel2_x2 - constant_val, wheel2_y2 - constant_val, wheel2_x2 + constant_val, wheel2_y2 + constant_val, fill=wheel_color_right, tags='robot')
canvas.create_oval(sensor1_x2 - constant_val, sensor1_y2 - constant_val, sensor1_x2 + constant_val, sensor1_y2 + constant_val, fill=sensor_color, tags='robot')
canvas.create_oval(sensor2_x2 - constant_val, sensor2_y2 - constant_val, sensor2_x2 + constant_val, sensor2_y2 + constant_val, fill=sensor_color, tags='robot')