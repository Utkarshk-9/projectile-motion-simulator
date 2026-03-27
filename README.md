# projectile-motion-simulator

Overview

The Projectile Motion Simulator is a Python-based program that models the trajectory of an object launched at a given velocity and angle. It uses fundamental physics equations to calculate how far and how high the object travels over time.

This project demonstrates how continuous motion can be approximated using discrete time steps, forming the basis of real-world simulations used in engineering and physics.

Features
- User input for velocity and launch angle
- Angle conversion from degrees to radians
- Calculation of horizontal ("vx") and vertical ("vy") velocity components
- Time-based simulation using a loop
- Step-by-step calculation of position (x, y)
- Automatic termination when the projectile hits the ground

Concepts Used
- Projectile motion
- Trigonometry ("sin", "cos")
- Kinematic equations
- Time stepping ("dt")
- Loop-based simulation

 Working Principle
The program takes initial conditions and resolves velocity into components. It then simulates motion over small time intervals ("dt") using a loop.

At each step:

- Horizontal position: "x = vx × t"
- Vertical position: "y = vy × t − ½gt²"

The simulation continues until the vertical position becomes negative, indicating the projectile has reached the ground.

---

▶️ How to Run

python projectile.py

---

 Project Structure

projectile-motion/
│── projectile.py
│── README.md

 Requirements
- Python 3.x
- Built-in "math" module

🎯 Learning Outcomes

- Understanding projectile motion through code
- Applying trigonometry in real problems
- Simulating continuous systems using discrete steps
- Building a foundation for advanced physics simulations
  
