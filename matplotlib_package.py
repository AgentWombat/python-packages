import matplotlib.pyplot as plt

# matplotlib is a simple way to quickly graph data

x = [1,2,3,4,5]
y = [1,2,4,8,16]

# This will graph the data, connecting neighboring datapoints with lines
plt.plot(x, y) # This sends the data to the library
plt.show() # This displays the graph

# This graphs the data without connecting neighboring datapoints.
plt.scatter(x, y)
plt.show()


# This is how we can label the axes.
plt.plot(x, y)
plt.xlabel("The number of upcoming exams")
plt.ylabel("Amount of caffeine consumed by the average student")
plt.show()


# We can graph multiple bits of data and using different methods in one display.

x1 = [3, 5, 7]
y1 = [8, 6, 8]

x2 = [2, 5, 8]
y2 = [5, 3, 5]

plt.scatter(x1, y1)
plt.plot(x2, y2)

plt.show()