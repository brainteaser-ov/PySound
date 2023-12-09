from abc import ABC, abstractmethod
from typing import Any, List

import numpy as np


class Parameters(ABC):
    def __init__(self, syllables_list: List[float]):
        self.syllables_list = syllables_list

    @abstractmethod
    def calculate_coeff(self):
        pass

    @abstractmethod
    def calculate_main(self):
        pass

    @abstractmethod
    def calculate_mean(self):
        pass

    @abstractmethod
    def calculate_corr(self):
        pass


class Calculation(Parameters, ABC):
    def __init__(self, syllables_list: List[float]):
        super().__init__(syllables_list)

    def calculate_mean(self):
        return sum(self.syllables_list) / len(self.syllables_list) * self.calculate_coeff()

    def calculate_corr(self):
        row = []
        for i in range(len(self.syllables_list) - 1):
            if self.syllables_list[i] > self.syllables_list[i + 1]:
                row.append(self.syllables_list[i] / self.syllables_list[i + 1])
            else:
                row.append(self.syllables_list[i + 1] / self.syllables_list[i])
        corr = [round(num * self.calculate_coeff(), 2) for num in row]
        return corr


class BaseWorker:

    @staticmethod
    def provide_description(value: Any) -> str:
        if 0 <= value <= 16:
            return f"ЭН: {value}"
        elif 17 <= value <= 33:
            return f"Н: {value}"
        elif 34 <= value <= 50:
            return f"СН: {value}"
        elif 51 <= value <= 67:
            return f"СВ: {value}"
        elif 68 <= value <= 84:
            return f"В: {value}"
        elif 85 <= value:
            return f"ЭВ: {value}"

    @staticmethod
    def provide_range_description(value: Any) -> str:
        if 0 <= value <= 16:
            return f"Малый: {value}"
        elif 17 <= value <= 33:
            return f"Узкий: {value}"
        elif 34 <= value <= 50:
            return f"Суженный: {value}"
        elif 51 <= value <= 67:
            return f"Средний: {value}"
        elif 68 <= value <= 84:
            return f"Расширенный: {value}"
        elif 85 <= value:
            return f"Широкий: {value}"

        #return "Неверное значение"

    @staticmethod
    def get_dictionary():
        tone_dict = {
            1.059: 1,
            1.122: 2,
            1.188: 3,
            1.258: 4,
            1.331: 5,
            1.411: 6,
            1.494: 7,
            1.582: 8,
            1.675: 9,
            1.744: 10,
            1.879: 11,
            2: 12,
            2.118: 13,
            2.234: 14,
            2.357: 15,
            2.596: 16,
            2.749: 17,
            2.911: 18,
            3.266: 20,
            3.439: 21,
            3.642: 22,
            3.857: 23,
            4: 24,
            4.236: 25,
            4.586: 26,
            4.857: 27,
            5.144: 28,
            5.447: 29,
            5.748: 30,
            6.1: 31,
            6.446: 32,
            6.826: 33,
            7.229: 34,
            7.965: 35,
            9: 36
        }
        return tone_dict

    @staticmethod
    def unpack_list(result: Any):
        row = []
        for i in range(len(result)):
            if 0 <= result[i] <= 1.3:
                row.append(['Минимальная степень контраста', result[i]])
            if 1.4 <= result[i] <= 1.5:
                row.append(["Слабая степень контраста", result[i]])
            if 1.6 <= result[i] <= 1.9:
                row.append(["Средняя степень контраста", result[i]])
            if 2 <= result[i] <= 3:
                row.append(["Яркая степень контраста", result[i]])
            if result[i] >= 3.1:
                row.append(["Максимальная степень контраста", result[i]])
        return row


    @staticmethod
    def provide_register(value: Any) -> int:
        if 0 <= value <= 16:
            #print(f"НУн: {value};")
            return 1
        elif 17 <= value <= 33:
            #print(f"НУв: {value};")
            return 2
        elif 34 <= value <= 50:
            #print(f"СУн: {value};")
            return 3
        elif 51 <= value <= 67:
            #print(f"СУв: {value};")
            return 4
        elif 68 <= value <= 84:
            #print(f"ВУн: {value};")
            return 5
        elif 85 <= value <= 100:
            #print(f"Вув: {value};")
            return 6
        else:
            return "Неверное значение"

    @staticmethod
    def find_register(result: Any) -> str:
        if result[0] == 6 and result[1] == 5:
            return f"ВУ: {(result[0], result[1])}"
        if result[0] == 6 and result[1] == 4:
            return f"ВШвв: {(result[0], result[1])}"
        if result[0] == 6 and result[1] == 3:
            return f"ВШ: {(result[0], result[1])}"
        if result[0] == 6 and result[1] == 2:
            return f"Пвв: {(result[0], result[1])}"
        if result[0] == 6 and result[1] == 1:
            return f"П: {(result[0], result[1])}"
        if result[0] == 5 and result[1] == 4:
            return f"ВШнв: {(result[0], result[1])}"
        if result[0] == 5 and result[1] == 3:
            return f"ВШнн: {(result[0], result[1])}"
        if result[0] == 5 and result[1] == 2:
            return f"Пнв: {(result[0], result[1])}"
        if result[0] == 5 and result[1] == 1:
            return f"Пнн: {(result[0], result[1])}"
        if result[0] == 4 and result[1] == 3:
            return f"СУ: {(result[0], result[1])}"
        if result[0] == 4 and result[1] == 2:
            return f"СШвв: {(result[0], result[1])}"
        if result[0] == 4 and result[1] == 1:
            return f"СШ: {(result[0], result[1])}"
        if result[0] == 3 and result[1] == 2:
            return f"СШнв: {(result[0], result[1])}"
        if result[0] == 3 and result[1] == 1:
            return f"СШнн: {(result[0], result[1])}"
        if result[0] == 2 and result[1] == 1:
            return f"НУ: {(result[0], result[1])}"

        return "Неверное значение"

    @staticmethod
    def calculate(number1, number2) -> int:
        tone_dict = BaseWorker.get_dictionary()
        key = min(tone_dict.keys(), key=lambda x: abs(x - (number1 / number2)))
        value = tone_dict[key]
        return value

    @staticmethod
    def correlation(result):
        row = []
        for i in range(len(result)-1):
            row.append(round((result[i] / result[i + 1]), 3))
        if len(result) > 2:
            row.append(round((result[0] / result[2]), 3))

        return row


    @staticmethod
    def round_list(result):
        rounded_result = []
        for value in result:
            rounded_value = round(value, 1)
            rounded_result.append(rounded_value)
        return rounded_result

    @staticmethod
    def statistics(lst, coefficient):
        # Умножаем каждое число в списке на коэффициент
        multiplied_lst = [num * coefficient for num in lst]

        # Вычисляем дисперсию и среднеквадратичное отклонение
        variance = np.var(multiplied_lst)
        std_deviation = np.std(multiplied_lst)

        return variance,  std_deviation

    @staticmethod
    def plots(lst, coefficient):
        plot_lst = [num * coefficient for num in lst]

    @staticmethod
    def find_closest_key(dictionary, variable):
        closest_key = None
        min_difference = float('inf')

        for key in dictionary.keys():
            difference = abs(variable - key)
            if difference < min_difference:
                min_difference = difference
                closest_key = key

        return dictionary[closest_key]



