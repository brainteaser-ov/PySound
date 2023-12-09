import parselmouth
import pandas as pd


class FormantData:
    def __init__(self, audio_files, time, vowels):
        self.audio_files = audio_files
        self.time = time
        self.vowels = vowels


    @staticmethod
    def extract_formant(audio_file, time_markers):
        # загрузка аудиофайла
        snd = parselmouth.Sound(audio_file)
        # извлечение формант
        formant = snd.to_formant_burg()
        # создание списка для хранения значений формант в заданные временные метки
        formant_values = []
        # получение значений формант в каждую временную метку
        for time in time_markers:
            # получение ширины полосы и значения форманта в заданный момент времени
            value1 = formant.get_value_at_time(1, time)
            value2 = formant.get_value_at_time(2, time)
            # добавление значений в список
            formant_values.append((time, value1, value2))
        return formant_values

    def list_formant(self):
        formant_values = {}
        for i in range(len(self.audio_files)):
            file = self.audio_files[i]
            times = self.time[i]
            vowel = self.vowels[i]
            snd = parselmouth.Sound(file)
            formant = snd.to_formant_burg()
            for j, label in enumerate(times):
                value1 = round(formant.get_value_at_time(1, label), 3)
                value2 = round(formant.get_value_at_time(2, label), 3)
                formant_values.setdefault(vowel[j], []).append(
                    {'Time': label, 'F1': value1, 'F2': value2})
        return formant_values


    def save_formant_to_df(self):
        formant_df = pd.DataFrame()
        formant_values = formant_data.list_formant()
        for vowel, values in formant_values.items():
            for value in values:
                formant_df = formant_df._append(
                    {'Vowel': vowel, 'F1': value['F1'], 'F2': value['F2']},
                    ignore_index=True)
        return formant_df

    @staticmethod
    def save_formant_to_files(df, csv_filename, doc_filename):
        df.to_csv(csv_filename, index=False)
        doc_content = df.to_string(index=False)
        with open(doc_filename, 'w') as file:
            file.write(doc_content)


audio_f = ["/Users/226/Desktop/cut/Rec-105.wav",
           "/Users/226/Рабочий стол/grant1/радость/Rec 42.wav"]
times = [[0.959, 3.17, 3.511],
    [0.39, 0.53, 0.62]]
vowel = [['o', 'a', 'i'],
         ['o:R42', 'i:R42', 'i:R42']]


formant_data = FormantData(audio_f, times, vowel)

df = formant_data.save_formant_to_df()
FormantData.save_formant_to_files(df, 'formants.csv', 'formants.doc')