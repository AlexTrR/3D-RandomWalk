from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

class Walker:
    def __init__(self,n):
        self.x = [0]
        self.y = [0]
        self.z = [0]
        self.A = 0
        for i in range(n):
            self.A = random.choice([-1, 0, 1])
            self.x.append(self.x[len(self.x)-1] + self.A)
            self.A = random.choice([-1, 0, 1])
            self.y.append(self.y[len(self.y)-1] + self.A)
            self.A = random.choice([-1, 0, 1])
            self.z.append(self.z[len(self.z)-1] + self.A)
        print(self.x,self.y,self.z)
pasos = int(input("Cuantos pasos se darán? "))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
zombie1 = Walker(pasos)
zombie2 = Walker(pasos)
zombie3 = Walker(pasos)
ax.plot3D(zombie1.x,zombie1.y,zombie1.z,zombie2.x,zombie2.y,zombie2.z,zombie3.x,zombie3.y,zombie3.z)
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
plt.show()