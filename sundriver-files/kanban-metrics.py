"""
This is an example for creating simple plots for the KANBAN method, as used during the lecture.
Students are not supposed to understand this at the beginning of the course.
There will be detailed lessons about how to create graphs later on.

Lecture "Modelling and Simulation" 
Master course "Technology of Circular Economy"

Uwe Reimer, Emden, October 2025
"""

import matplotlib.pyplot as plt

pngfile = "Team-A.png"
# ToDo
ydat = [6,5,3,1,1,1,0]
# Done
y2dat = [0,0,0,2,3,4,6]


xdat = []
x = 0
for a in ydat:
    xdat.append(x)
    x = x + 1

cm = 1.0/2.54  # centimeters in inches
plt.subplots(figsize=(10*cm, (10*3/4)*cm))

l1 = plt.plot(xdat, ydat, label="ToDo")
l2 = plt.plot(xdat, y2dat, label="Done")


plt.legend(loc='upper left', shadow=True)
plt.xlabel("time step")
plt.ylabel("Work packages (Cards)")
plt.tight_layout()
plt.savefig(pngfile)

