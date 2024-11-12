from matplotlib.patches import Wedge, Arc
import matplotlib.pyplot as plt

plt.xlim(0, 6)
plt.ylim(0, 5)
ax = plt.gca()

figure_w = Wedge((3, 1), 2, 45, 135)
ax.add_patch(figure_w)

figure_a = Arc((3, 1), 6, 6, angle=0, theta1=45, theta2=135, linewidth=3)
ax.add_patch(figure_a)

plt.show()
