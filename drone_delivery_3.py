import math

print("🚑 EMERGENCY SUPPLY DRONE SIMULATOR 🚑")
print("------------------------------------------------")

# Base location
base_x, base_y = 0, 0

# Drone settings
battery = 100
base_speed = 70  # km/h

total_distance = 0
total_time = 0

# Number of deliveries
deliveries = int(input("Enter number of delivery locations: "))

weather = input("Enter weather (clear/rain/windy): ").lower()

# Adjust speed based on weather
if weather == "rain":
    speed = base_speed * 0.7
elif weather == "windy":
    speed = base_speed * 0.8
else:
    speed = base_speed

for i in range(deliveries):
    print(f"\n--- Delivery {i+1} ---")
    
    x = float(input("Enter destination X coordinate: "))
    y = float(input("Enter destination Y coordinate: "))
    
    priority = input("Enter priority (high/medium/low): ").lower()
    
    # Distance from base
    distance = math.sqrt((x - base_x)**2 + (y - base_y)**2)
    
    # Priority affects speed slightly
    if priority == "high":
        adjusted_speed = speed * 1.2
    elif priority == "medium":
        adjusted_speed = speed
    else:
        adjusted_speed = speed * 0.9
    
    time = distance / adjusted_speed
    
    # Battery consumption (2% per km now)
    battery_used = distance * 2
    battery -= battery_used
    
    total_distance += distance
    total_time += time
    
    print(f"Distance: {distance:.2f} km")
    print(f"Time: {time:.2f} hours")
    print(f"Battery remaining: {battery:.2f}%")
    
    if battery <= 20:
        print("⚠ Battery Low! Mission Aborted.")
        break

print("\n📊 MISSION SUMMARY")
print("--------------------------------")
print(f"Total Distance Covered: {total_distance:.2f} km")
print(f"Total Time Taken: {total_time:.2f} hours")
print(f"Final Battery Remaining: {battery:.2f}%")

if battery > 20:
    print("✅ All Deliveries Completed Successfully!")
input("Press Enter to exit...")