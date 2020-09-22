import random as rd
import matplotlib.pyplot as plt

pts_in_square = int(input('How many points in square ?'))
check_if_in_square = 0 
apx, pts = [], []
x_in, y_in = [], []
x_out, y_out = [], []
for i in range(pts_in_square):

    x = rd.uniform(-1.0, 1.0) #draws a number within range -1.0 - 1.0
    y = rd.uniform(-1.0, 1.0)
    
    if x**2 + y**2 <= 1: #statement that checks if point is in circle
        check_if_in_square +=1
        x_in.append(x)
        y_in.append(y)
    else:
        x_out.append(x)
        y_out.append(y)
    apx.append(4*(check_if_in_square/pts_in_square))# adding a values to see how quantity of points effects on approximation
    pts.append(i)

print(check_if_in_square)

fig, ax = plt.subplots(1, 3)
ax[0].scatter(x_in, y_in, color='g', marker='s')
ax[0].scatter(x_out, y_out, color='r', marker='s')
ax[1].plot(pts, apx)
ax[2].hist(apx)

plt.show()