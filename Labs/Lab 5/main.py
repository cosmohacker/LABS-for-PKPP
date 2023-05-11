import matplotlib.pyplot as plt
import numpy as np


def show_variant_number(first_letter_of_name):
    return str("My Variant Number is: " + str(ord(first_letter_of_name) % 10 + 1))


def draw_first_line():
    # – 10.2 x1 + 9.3 x2 = 73
    # x2 = 7.849
    # x1 = -7.157
    x1 = np.linspace(-10, 10, 100)
    x2 = (73 - 10.2 * x1) / 9.3
    return x1, x2, '-10.2 x1 + 9.3 x2 = 73', 'dotted', 'red'


def draw_second_line():
    # 5.3 x1 + 15.8 x2 = 173
    # x2 = 10.95
    # x1 = 32.64
    x1 = np.linspace(-10, 10, 100)
    x2 = (173 - 5.3 * x1) / 15.8

    return x1, x2, '5.3 x1 + 15.8 x2 = 173', 'dashed', 'green'


def draw_third_line():
    # 17.2 x1 + 10.3 x2 = 159
    # x2 = 15.44
    # x1 = 9.24
    x1 = np.linspace(-10, 10, 100)
    x2 = (159 - 17.2 * x1) / 10.3

    return x1, x2, '17.2 x1 + 10.3 x2 = 159', 'dashdot', 'blue'


def draw_all_lines():
    lines = [draw_first_line(), draw_second_line(), draw_third_line()]

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 6))

    for i, (x1, x2, label, linestyle, color) in enumerate(lines):
        ax = axes[i]
        ax.plot(x1, x2, linestyle=linestyle, color=color, label=label)
        ax.set_title(label)
        ax.legend()
        ax.grid(linestyle=':', color='gray')
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')

    fig.suptitle('All Lines')
    plt.show()


def merge_all_lines():
    x1 = np.linspace(-20, 20, 100)

    x2_1 = (73 - 10.2 * x1) / 9.3
    x2_2 = (173 - 5.3 * x1) / 15.8
    x2_3 = (159 - 17.2 * x1) / 10.3

    # fig = figure, ax = axis
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(x1, x2_1, linestyle='dotted', color='red', label='-10.2 x1 + 9.3 x2 = 73')
    ax.plot(x1, x2_2, linestyle='dashed', color='green', label='5.3 x1 + 15.8 x2 = 173')
    ax.plot(x1, x2_3, linestyle='dashdot', color='blue', label='17.2 x1 + 10.3 x2 = 159')

    ax.annotate('-10.2 x1 + 9.3 x2 = 73', xy=(-15, 14), rotation=-27, fontsize=10, color='red')
    ax.annotate('5.3 x1 + 15.8 x2 = 173', xy=(5, 6), rotation=-8, fontsize=10, color='green')
    ax.annotate('17.2 x1 + 10.3 x2 = 159', xy=(-13, 22), rotation=-37, fontsize=10, color='blue')

    ax.set_title('All Lines In One Figure')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.grid(linestyle=':', color='gray')
    ax.legend()

    A1 = np.array([[-10.2, 9.3], [5.3, 15.8]])
    B1 = np.array([73, 173])
    intersection1 = np.linalg.solve(A1, B1)

    intersection2 = np.array([12.6, -6])

    A3 = np.array([[5.3, 15.8], [-17.2, 10.3]])
    B3 = np.array([173, 159])
    intersection3 = np.linalg.solve(A3, B3)

    ax.plot(intersection1[0], intersection1[1], marker='o', color='black')
    ax.plot(intersection2[0], intersection2[1], marker='o', color='black')
    ax.plot(intersection3[0], intersection3[1], marker='o', color='black')

    plt.show()


print(show_variant_number("Y"))

draw_all_lines()
merge_all_lines()
