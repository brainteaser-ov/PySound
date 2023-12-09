
import matplotlib.pyplot as plt
import pandas as pd

# Create the dataframe
# data = {'Speaker': ['sk1', 'sk1', 'sk1', 'arm_w', 'arm_w', 'arm_w'],
#         'Vowel': ['u', 'i', 'a', 'i', 'a', 'y'],
#         'F1': [0.92, -1.244, 0.325, -0.324, 0.043, 1.167],
#         'F2': [-1.291, 0.634, 0.657, 0.39, -0.692, 0.516]}
#
# df = pd.DataFrame(data)
#
# def plot_points(data, x_columns, y_columns):
#     # Create subplots
#     fig, axs = plt.subplots(len(y_columns), len(x_columns), figsize=(4*len(x_columns), 4*len(y_columns)))
#
#     # Plot for each pair of columns
#     for i, y_column in enumerate(y_columns):
#         for j, x_column in enumerate(x_columns):
#             axs[i, j].scatter(data[x_column], data[y_column])
#             axs[i, j].set_xlabel(x_column)
#             axs[i, j].set_ylabel(y_column)
#
#     # Display the plot
#     plt.show()
#
# # Example usage of the function
# plot_points(df, ['F1', 'F2'], ['Speaker', 'Vowel'])


# Create the dataframe
# data = {'Speaker': ['каб', 'каб', 'каб', 'рус', 'рус', 'рус'],
#         'Vowel': ['i', 'a', 'o', 'i', 'a', 'o'],
#         'F1': [446, 648, 513, 240, 700, 400],
#         'F2': [1720, 1389, 1007, 2250, 1250, 750]}
#
# df = pd.DataFrame(data)
#
# def plot_points(data, x_column, y_column):
#     # Create a scatter plot
#     plt.scatter(data[x_column], data[y_column], color='blue', edgecolors='white')
#     plt.xlabel(x_column)
#     plt.ylabel(y_column)
#     plt.title(f"{x_column} vs {y_column}")
#
#     # Add labels for each point
#     for i in range(len(data)):
#         plt.annotate(data['Vowel'][i], (data[x_column][i], data[y_column][i]), color='red')
#
#     # Display the plot
#     plt.show()

# Example usage of the function
# plot_points(df, 'F1', 'F2')
import pandas as pd
import matplotlib.pyplot as plt

data = {'Speaker': ['арм', 'арм', 'арм', 'рус', 'рус', 'рус', 'юрф', 'юрф', 'юрф'],
        'Vowel': ['i', 'a', 'o', 'i', 'a', 'o', 'i', 'a', 'o'],
        'F1': [334, 700, 850, 240, 700, 400, 318, 646, 603],
        'F2': [2105, 1850, 1110, 2250, 1250, 750, 1999, 1400, 890]}

df = pd.DataFrame(data)

# def plot_points(data, x_column, y_column):
#     # Create a scatter plot
#     for i in range(len(data)):
#         if data['Speaker'][i] == 'каб':
#             plt.scatter(data[x_column][i], data[y_column][i], color='blue', edgecolors='white', label='каб')
#         else:
#             plt.scatter(data[x_column][i], data[y_column][i], color='red', edgecolors='white', label='рус')
#     plt.xlabel(x_column)
#     plt.ylabel(y_column)
#     plt.title(f"{x_column} vs {y_column}")
#     plt.legend()
#
#     # Display the plot
#     plt.show()
#
# plot_points(df, 'F1', 'F2')
# def plot_points(data, x_column, y_column):
#     # Create a scatter plot
#     for i in range(len(data)):
#         if data['Speaker'][i] == 'арм':
#             plt.scatter(data[x_column][i], data[y_column][i], color='blue', edgecolors='white', label='арм')
#         elif data['Speaker'][i] == 'рус':
#             plt.scatter(data[x_column][i], data[y_column][i], color='red', edgecolors='white', label='рус')
#
#         else:
#             plt.scatter(data[x_column][i], data[y_column][i], color='green', edgecolors='white', label='юрф')
#         plt.text(data[x_column][i], data[y_column][i], data['Vowel'][i])  # Add vowel labels
#
#
#
#
#
#     plt.xlabel(x_column)
#     plt.ylabel(y_column)
#     plt.title(f"{x_column} vs {y_column}")
#     plt.legend()
#
#     # Display the plot
#     plt.show()
#
# plot_points(df, 'F1', 'F2')
def plot_points(data, x_column, y_column):
    # Create a scatter plot
    for i in range(len(data)):
        if data['Speaker'][i] == 'арм':
            plt.scatter(data[y_column][i], data[x_column][i], color='blue', edgecolors='white', label='арм')
        elif data['Speaker'][i] == 'рус':
            plt.scatter(data[y_column][i], data[x_column][i], color='red', edgecolors='white', label='рус')

        else:
            plt.scatter(data[y_column][i], data[x_column][i], color='green', edgecolors='white', label='юрф')
        plt.text(data[y_column][i], data[x_column][i], data['Vowel'][i])  # Add vowel labels

    plt.xlabel(y_column)
    plt.ylabel(x_column)
    plt.title(f"{x_column} vs {y_column}")
    plt.legend()

    # Display the plot
    plt.show()

plot_points(df, 'F2', 'F1')