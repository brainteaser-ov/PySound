from typing import List, Tuple

from utils.utils import BaseWorker, Calculation


class Rate(Calculation):
    def __init__(self, syllables_list: List[float], min_duration: int,
                 max_duration: int,
                 nuclear_duration: int,
                 stressed_duration: int, ):
        super().__init__(syllables_list)
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.nuclear_duration = nuclear_duration
        self.stressed_duration = stressed_duration

    def calculate_coeff(self) -> float:
        return 100 / (self.max_duration - self.min_duration)

    def calculate_main(self) -> Tuple[str, str]:
        return BaseWorker.provide_description(self.calculate_coeff() * self.nuclear_duration), \
            BaseWorker.provide_description(self.calculate_coeff() * self.stressed_duration)

    def calculate_mean_and_corr(self):
        return BaseWorker.provide_description(self.calculate_mean()), \
            BaseWorker.unpack_list(self.calculate_corr())


class Loudness(Calculation):
    def __init__(self, syllables_list: List[float], min_intensity: int,
                 max_intensity: int,
                 nuclear_intensity: int,
                 stressed_intensity: int, ):
        super().__init__(syllables_list)
        self.min_intensity = min_intensity
        self.max_intensity = max_intensity
        self.nuclear_intensity = nuclear_intensity
        self.stressed_intensity = stressed_intensity

    def calculate_coeff(self) -> float:
        return round((100 / (self.max_intensity - self.min_intensity)), 3)

    def calculate_main(self) -> Tuple[str, str]:
        return BaseWorker.provide_description(int(self.calculate_coeff() * self.nuclear_intensity)), \
            BaseWorker.provide_description(int(self.calculate_coeff() * self.stressed_intensity))

    def calculate_mean_and_corr(self):
        return BaseWorker.provide_description(int(self.calculate_mean())), \
            BaseWorker.unpack_list(self.calculate_corr())

    def calculate_statistics(self):
        return BaseWorker.statistics(self.syllables_list, self.calculate_coeff())


loudness = Loudness([78, 67, 73, 76, 72, 79, 58, 68], 20, 95, 79, 78)


coeff = loudness.calculate_coeff()
print("Коэффициент интенсивности:", coeff)

main_intensity = loudness.calculate_main()
print("Интенсивность ядерного/ударного слогов", main_intensity)

mean_intensity: str = loudness.calculate_mean_and_corr()
print("Среднеслоговая интенсивность / Соотношение слогов по порядку следования:", mean_intensity)

statistics = loudness.calculate_statistics()
print("Дисперсия/среднеквадратичное отклонение:", statistics)

# rate = Rate([15.5, 12.3, 18.7, 14.2, 17.9], 10, 50, 20, 30)
#
# coeff = rate.calculate_coeff()
# print("Коэффициент длительности:", coeff)
#
# main_rate = rate.calculate_main()
# print("Длительность ядерного/ударного слогов", main_rate)
#
# mean_rate: str = rate.calculate_mean_and_corr()
# print("Среднеслоговая длительность / Соотношение слогов по порядку следования:", mean_rate)

#Женщина (36-60) – мужчина (36-60)Kab [79, 80, 81, 78, 70,73, 72, 69,70]


#Мужчина (36-60) – женщина (36-60) Kab ([74, 79, 82, 78, 79, 79, 77, 78, 74], 15, 85, 82, 82)
#Женщина (36-60) – мужчина (36-60)Rus ([79, 78, 81, 80, 79, 77, 77, 74, 66], 15, 83, 77, 82)
#Мужчина (36-60) – женщина (36-60) Rus
# syllables_list [74, 78, 78, 74, 71, 77, 73, 71, 74]
# min_intensity 10
# max_intensity 81
# nuclear_intensity 77
# stressed_intensity 82

