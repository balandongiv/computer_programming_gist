
"I need you to describe in detail how to create a program that visually simulates a small, interactive world inside a window on a computer screen. This world will be a simplified environment where a robot cleans up dirt, interacts with cats, and recharges its battery.

Let's break down the elements and their behaviors within this simulated world:

1.  **The Room and Visual Display:**
    *   Imagine a clean, square room. This room needs to be visually represented as the main area of our program. Think of it as a blank canvas where everything will happen. The room should have boundaries, so things stay within it. Let's say it’s a 1000x1000 unit area.
    *   This room should be displayed in a window on the screen. The window should be resizable, but the content inside should maintain its proportions.

2.  **The Cleaning Robot - Detailed Behavior and Appearance:**
    *   Visualize the robot as a clearly defined shape, perhaps like a rounded rectangle or a simple, stylized robot shape, so it's easily distinguishable from other elements.  Make it blue.
    *   **Movement:** The robot should move autonomously and continuously, exploring the room. Its movement should appear as a combination of moving forward and occasionally turning. Imagine it moving in short bursts of straight lines, interspersed with slight turns to change direction, giving a wandering, exploratory feel.  It shouldn't just move in straight lines forever; it needs to explore the whole room over time.
    *   **Battery and Energy:** The robot runs on a battery. Start the battery at a 'full' level (let's say 1000 units). As the robot moves and operates, this battery level should steadily decrease, simulating energy consumption.
    *   **Battery Display:**  Constantly display the robot's current battery level very close to the robot itself, perhaps as a number right on top of it or just beside it, so it's always visible and associated with the robot.
    *   **Seeking Charger:** When the robot's battery gets low (perhaps below 600 units), it needs to change its behavior. It should start actively trying to move towards the 'charger' (which we'll describe later).  When it's seeking a charger, maybe its movement becomes less random and more directed, as if it's trying to find something specific. As it gets closer to the charger, it could even slow down its movement, as if carefully approaching.
    *   **Dirt Collection:** The robot's primary task is to collect dirt. Imagine the robot has a 'collection area' at its front or bottom. When this area physically overlaps with a piece of 'dirt', the dirt is considered collected. Upon collection, the dirt should instantly disappear from the screen.
    *   **Dirt Counter:**  Implement a counter that starts at zero and increases every time the robot collects a piece of dirt. Display this counter prominently at the top of the room display, labeled "Dirt Collected: [number]".

3.  **Dirt - Appearance and Distribution:**
    *   Represent 'dirt' as very small, simple shapes, like tiny grey circles or dots. They should be visually subtle but still noticeable against the background of the room.
    *   Scatter a significant number of these dirt particles randomly throughout the room at the start of the simulation. They should be placed in various locations, not just clustered together.

4.  **Cats - Interactive Obstacles:**
    *   Introduce several 'cats' into the room. Represent each cat visually with a distinct image of a cat. The images should be appropriately sized so they look like small animals within the room.
    *   **Cat Movement:** Cats should also move independently and continuously within the room. Their movement should also be somewhat random and wandering, but perhaps a bit more agile or quicker than the robot’s. They should seem to roam around the room on their own.
    *   **Robot-Cat Interaction (Collision Avoidance):** If the robot gets too close to a cat, consider it a 'near collision'.  The cat should react instantly by 'jumping' or 'darting' away to a new, randomly chosen location within the room. This jump should be a noticeable, quick movement to a new spot that's a reasonable distance away from the robot.

5.  **The Charging Station - Function and Appearance:**
    *   Include a single 'charging station' in the room. Visually represent it as a clear, easily recognizable object, perhaps a bright gold or yellow circle or a stylized charger icon. Place it somewhere within the room, maybe not in the very center, but in a fixed location.
    *   **Charging Process:** When the robot is physically close to the charging station (within a certain proximity), its battery level should start to increase. Simulate a charging rate – for example, the battery level increases by a certain amount every short time interval while it's near the charger.  Once the battery is full (back to 1000), the robot should stop charging and resume its normal wandering and dirt-collecting behavior.

6.  **User Interaction - Direct Robot Control:**
    *   Enable users to interact with the simulation by clicking anywhere within the room display. When the user clicks, the robot should immediately start moving towards the exact location that was clicked. It should move smoothly towards this point, not just instantly jump there. Once it reaches the clicked point, it should resume its autonomous wandering behavior.

7.  **Simulation Flow and Dynamics:**
    *   The entire simulation should be continuously running and dynamic. Once started, the robot, cats, and dirt are all present and active. The robot should be constantly moving, checking for dirt and chargers, and reacting to cats. Cats should be wandering and reacting to the robot. The dirt counter should update in real-time.  It should feel like a little world operating on its own, with user interaction possible at any time.

Please provide the complete set of instructions and code needed to create this visual simulation. Focus on making the simulation as visually clear and functionally accurate to this detailed description as possible."

