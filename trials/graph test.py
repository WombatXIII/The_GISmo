import matplotlib.pyplot as plt


def graph():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [1, 10, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1000000000]
    plt.plot(x, y)
    plt.xlabel('Eastings')
    plt.ylabel('Northings')
    plt.title('Line')
    plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
    plt.show()


graph()
