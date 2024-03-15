import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis for the animation
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-2, 2)

# Initialize a line plot and text
line, = ax.plot([], [], lw=2)
text = ax.text(0.5, 1.5, 'Hello Joseph', fontsize=15, va='bottom', ha='center', color='red')

# Initialization function for the animation
def init():
    line.set_data([], [])
    return line, text

# Animation function that will be called sequentially
def animate(i):
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x + 0.1*i)
    line.set_data(x, y)
    return line, text

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

plt.show()