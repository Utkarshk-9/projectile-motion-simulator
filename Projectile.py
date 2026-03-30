#This model simulates the distance travelled by the object and how up it has gone within due time
import math 
velocity = float(input("Enter Velocity in m/s: ")) #Enter the velocity in standardized unit
angle = float(input("Enter the Angle: ")) #Enter the angle in Degrees
theta = math.radians(angle) #Degrees is converted into Radians
vx = velocity * math.cos(theta) 
vy = velocity * math.sin(theta)
print(f"{vx:.2f} m/s")
print(f"{vy:.2f} m/s")
g = 9.81  
t = 0
dt = 0.1 #Time Steps (Seconds)
while True:
    x = vx * t #Calculates Horziontal Distance
    y = vy * t - 0.5 * g * t ** 2 #Calculates Vertical Distance
    print(f"t={t:.2f}s  x={x:.2f}m  y={y:.2f}m")
    if y < 0: 
        break #Break the loop when object hits the ground
    t += dt ## Moves time forward in small steps to approximate continuous motion
Hmax = (vy ** 2) / (2 * g)
Tf = (2 * vy) / g
Range = (vx *t)
print(f"Maximum Height- {Hmax:.2f}m ")
print(f"Time Of Flight- {Tf:.2f}s ")
print(f"Total Horizontal Distance- {Range:.2f}m ")
