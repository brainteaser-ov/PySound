from utils.utils import BaseWorker


class Frequency:
    """Class to perform calculations with the tone frequency:
            min_value: minimum speaker tone value
            max_value: maximum speaker tone value
            stressed_value: frequency of the main tone of the first stressed syllable
            main_tone frequency: main tone of the beginning of the phrase/first syllable
            min_int_rise: start of the rise interval
            max_int_rise: end of the rise interval
            min_int_fall: start of tone down interval
            max_int_fall: end of the pitch down interval
            end_value: frequency of the end-of-phrase/last-syllable main tone
    """
    def __init__(
            self, min_value: int,
            max_value: int,
            stressed_value: int,
            main_tone: int,
            min_int_rise: int,
            max_int_rise: int,
            min_int_fall: int,
            max_int_fall: int,
            end_value: int
    ):
        self.min_value = min_value
        self.stressed_value = stressed_value
        self.max_value = max_value
        self.main_tone = main_tone  # первый ударный
        self.min_int_rise = min_int_rise
        self.max_int_rise = max_int_rise
        self.min_int_fall = min_int_fall
        self.max_int_fall = max_int_fall
        self.end_value = end_value

    def calculate_coeff(self) -> float:
        return round((100 / BaseWorker.calculate(self.max_value, self.min_value)), 2)

    def calculate_frequency(self):
        level_first = BaseWorker.calculate(self.main_tone, self.min_value)
        level_stressed = BaseWorker.calculate(self.stressed_value, self.min_value)
        level_end = BaseWorker.calculate(self.end_value, self.min_value)
        return [level_first, level_stressed, level_end]

    def calculate_range(self):
        level_left = BaseWorker.calculate(self.end_value, self.min_value)
        level_right = BaseWorker.calculate(self.max_value, self.min_value)
        register = [BaseWorker.provide_register(
            int(level_right * self.calculate_coeff())),
            BaseWorker.provide_register(int(level_left * self.calculate_coeff()))]
        # return f"Тональный диапазон - " \
        #        f"{BaseWorker.provide_range_description(level_right - level_left)} " \
        #        f" Регистр - {BaseWorker.find_register(register)}"
        return [BaseWorker.provide_range_description(level_right - level_left),
                BaseWorker.find_register(register)]

    def calculate_level(self):
        # print(f"ПТ начала фразы, первого ударного слога и конца фразы - {self.calculate_frequency()};")
        # print(f"Коэффициент говорящего - {self.calculate_coeff()};")
        start = self.calculate_frequency()
        end = self.calculate_coeff()
        # return f"Уровни начала фразы/первого ударного слога/конца фразы" \
        #        f" {list(map(BaseWorker.provide_description, [int(f * end) for f in start]))}"
        return list(map(BaseWorker.provide_description, [int(f * end) for f in start]))

    def calculate_int_rising(self) -> str:
        int_rises: float = abs(((self.max_int_rise - self.min_int_rise) / self.max_int_rise) * 100)
        # return f"Объем интервала повышения тона - {BaseWorker.provide_range_description(int(int_rises))}"
        return BaseWorker.provide_range_description(int(int_rises))

    def calculate_int_falling(self) -> str:
        int_falls: float = abs(((self.max_int_fall - self.min_int_fall) / self.min_int_fall) * 100)
        # return f"Объем интервала понижения тона - {BaseWorker.provide_range_description(int(int_falls))}"
        return BaseWorker.provide_range_description(int(int_falls))

    def calculate_corr(self):
        response = self.calculate_frequency()
        # return f"Соотношение уровней начала/первого ударного слога;" \
        #        f" первого ударного слога/конца фразы; уровня начала/конца фразы: -" \
        #        f" {BaseWorker.unpack_list(BaseWorker.round_list(BaseWorker.correlation(response)))}"
        return BaseWorker.unpack_list(BaseWorker.round_list(BaseWorker.correlation(response)))

    @staticmethod
    def calculate_speed(start_level: int, end_level: int, time: int):
        Z = 1000
        speed = start_level / end_level
        tone_dict = BaseWorker.get_dictionary()
        key = BaseWorker.find_closest_key(tone_dict, speed)
        total = int((key * Z) / time)
        return f"Скорость интервала повышения/понижения: {total};"
