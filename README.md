This program is an Emergency Supply Drone Simulator written in Python. It simulates a drone delivering supplies to multiple locations while considering weather conditions, delivery priority, battery usage, and total mission statistics.

First, the math module is imported to calculate distances using the square root function. The drone base location is set at coordinates (0,0). The drone starts with a battery level of 100% and a base speed of 70 km/h. Two variables, total_distance and total_time, are initialized to track the overall mission performance.

The user is asked to enter the number of delivery locations. Then, the user provides the current weather condition (clear, rain, or windy). Based on the weather, the drone’s speed is adjusted. Rain reduces the speed to 70% of the base speed, windy weather reduces it to 80%, and clear weather keeps it unchanged. This simulates real-world environmental impact on drones.

The program then runs a loop for each delivery location. For every delivery, the user enters destination coordinates (x, y) and selects a priority level (high, medium, or low). The distance from the base to the destination is calculated using the distance formula:

√((x - base_x)² + (y - base_y)²)

The delivery priority slightly modifies the drone’s speed. High priority increases speed by 20%, medium keeps it normal, and low priority reduces it by 10%. The time required for delivery is calculated using:

Time = Distance ÷ Speed

Battery consumption is calculated at 2% per kilometer, and the used battery is subtracted from the total battery. The program keeps updating the total distance and total time for all deliveries.

After each delivery, the program checks if the battery falls below or equal to 20%. If it does, the mission is aborted for safety reasons. Otherwise, it continues to the next delivery.

Finally, the program prints a mission summary showing total distance covered, total time taken, and final battery remaining. If the battery is still above 20%, it confirms that all deliveries were successfully completed.
