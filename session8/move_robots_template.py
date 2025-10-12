def move_robots(canvas, bots, passive_components, dirt_counter, moves, max_moves, move_delay,window):
    """
    Continuously updates the state and position of a swarm of robot agents on a canvas,
    simulating autonomous movement and dirt collection until a maximum number of moves is reached.

    This function is typically called in a loop using `canvas.after()` to simulate
    real-time autonomous robot behavior. It utilizes sensor inputs and transfer functions
    to drive the robots toward charging hubs and perform dirt collection. Each robot's
    battery level, position, and heading are updated accordingly.

    Parameters:
        canvas (tk.Canvas): The tkinter canvas where robots and other components are drawn and updated.
        bots (list): A list of robot objects, each containing state attributes (x, y, theta, battery, etc.).
        passive_components (list): A list of passive elements in the environment, such as charging hubs and dirt patches.
        dirt_counter (DirtCounter): An object responsible for tracking the number of dirt patches collected.
        moves (int, optional): The current number of move iterations completed. Defaults to 0.
        max_moves (int, optional): The maximum number of allowed moves before the simulation ends. Defaults to 200000.
        move_delay (int, optional): Time in milliseconds between each move iteration, controls animation speed. Defaults to 20.

    Behavior:
        - Each robot senses nearby charging hubs using its left and right sensors.
        - Based on the sensed data, it calculates the next movement via its transfer function.
        - The robot moves in the environment and updates its internal state.
        - If the robot encounters dirt, it collects it and updates the dirt counter.
        - Once the maximum number of moves is reached, the simulation ends with a summary printout.

    Example Usage:
        move_robots(canvas, bots, passive_components, dirt_counter)

    Notes:
        - This function uses recursion via `canvas.after()` to create an event-driven loop
          without blocking the GUI thread.
        - `sys.exit()` is used to terminate the simulation; this can be replaced with
          `window.destroy()` if a clean GUI shutdown is desired.
    """
    if window.should_stop:
        return

    moves += 1
    print(f'Move count: {moves}')

    for bot in bots:
        agent = RobotAgent(bot)
        charger_intensity_left, charger_intensity_right = agent.sense_charger(passive_components)
        agent.transfer_function(charger_intensity_left, charger_intensity_right)
        agent.move(canvas, passive_components, dt=1.0)

        # Update bot state from agent (more efficient way)
        bot.x = agent.x
        bot.y = agent.y
        bot.theta = agent.theta
        bot.battery = agent.battery
        bot.sensor_positions = agent.sensor_positions

        # Dirt collection
        passive_components = agent.collect_dirt(canvas, passive_components, dirt_counter)

    if moves > max_moves:
        print(f"Total dirt collected after {max_moves} moves: {dirt_counter.dirt_collected}")
        # sys.exit()  # Or window.destroy() to close the window
        window.should_stop = True
        window.root.after(10,  window.root.destroy)  # Schedule window to close after this call finishes

    canvas.after(move_delay, move_robots, canvas, bots, passive_components, dirt_counter, moves, max_moves, move_delay,window)
