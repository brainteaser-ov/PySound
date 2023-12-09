import matplotlib.pyplot as plt


def scatter_plot(x_values, y_values):
    plt.scatter(x_values, y_values, color='blue', label='русские радость')
    plt.scatter(y_values, x_values, color='red', label='армяне радость')
    # plt.xlabel('русские радость')
    # plt.ylabel('армяне радость')
    plt.legend()
    plt.show()



# Пример использования функции
x = [431, 386, 450, 567, 489, 392]
y = [589, 598, 566, 597, 553, 568]


