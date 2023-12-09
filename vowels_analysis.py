

import numpy as np
import pandas as pd


class Sound:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def vocal_triangle(self):
        F1_values = self.dataframe['F1']
        F2_values = self.dataframe['F2']

        S = 0.5 * ((F2_values[0] * F1_values[1] + F2_values[1] * F1_values[2] + F2_values[2] * F1_values[0]) - (
                    F1_values[0] * F2_values[1] + F1_values[1] * F2_values[2] + F1_values[2] * F2_values[0]))
        return S

    def calculate_evc(self):
        F1_values = self.dataframe['F1']
        F2_values = self.dataframe['F2']

        distances = []

        for i in range(len(F1_values)):
            for j in range(i + 1, len(F1_values)):
                distance = np.sqrt((F1_values[j] - F1_values[i]) ** 2 + (F2_values[j] - F2_values[i]) ** 2)
                distances.append(round(distance, 3))

        return distances

    def calculate_std(self):
        F1_values = self.dataframe['F1']
        F2_values = self.dataframe['F2']

        std_deviations = []

        for i in range(len(F1_values)):
            for j in range(i + 1, len(F1_values)):
                std_deviation = np.sqrt(np.var([F1_values[i], F1_values[j]]) + np.var([F2_values[i], F2_values[j]]))
                std_deviations.append(round(std_deviation, 3))

        return std_deviations

    def calculate_disp(self):
        F1_values = self.dataframe['F1']
        F2_values = self.dataframe['F2']

        dispersions = []

        for i in range(len(F1_values)):
            for j in range(i + 1, len(F1_values)):
                dispersion = np.var([F1_values[i], F1_values[j]]) + np.var([F2_values[i], F2_values[j]])
                dispersions.append(round(dispersion, 3))

        return dispersions


# Создание датафрейма
data = {'Vowels': ['i', 'a', 'y'],
        'F1': [-1.244, 0.325, 0.926],
        'F2': [0.634, 0.657, -0.383]}
rus = {'Vowels': ['i', 'a', 'y'],
        'F1': [-0.27, 0.098, 0.788],
        'F2': [0.799, -0.896, -0.51]}

df = pd.DataFrame(data)
#df = pd.read_csv('/datasets/market_money.csv')

# Создание экземпляра класса Sound
sound = Sound(df)

# Вызов методов для выполнения расчетов
vocal_triangle_value = sound.vocal_triangle()
evc_values = sound.calculate_evc()
std_values = sound.calculate_std()
disp_values = sound.calculate_disp()

# Вывод результатов
print("Площадь вокального треугольника:", vocal_triangle_value)
print("Евклидово расстояние:", evc_values)
print("Стандартное отклонение:", std_values)
print("Дисперсия:", disp_values)

# Speaker, Vowel F1, F2
# arm_w, i, -0.324, 0.39,
# arm_w, a, 0.043, -0.692,
# arm_w, y, 1.167, 0.516,
#
#
#
#
# r_w,   i,  -0.27, 0.799,
# r_w,   a, 3, 0.098, -0.896,
# r_w,   y, 1, 0.788, -0.51,
