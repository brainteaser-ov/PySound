import parselmouth
import os
import pandas as pd


class MainData:
    def __init__(self, audio_files):
        self.audio_files = audio_files

    @staticmethod
    def get_whole_pitch_info(audio_file):
        pitch_info = []
        sound = parselmouth.Sound(audio_file)
        # Получение параметров высоты тона звукового файла
        pitch = sound.to_pitch()
        pitch_values = pitch.selected_array['frequency']
        min_pitch_whole = int(min(pitch_values))
        max_pitch_whole = int(max(pitch_values))
        start_pitch_whole = int(pitch_values[0])
        end_pitch_whole = int(pitch_values[-1])
        mean_pitch_whole = int(sum(pitch_values) / len(pitch_values))
        # Добавление информации о высоте тона в список pitch_info
        pitch_info.append({
            "file": audio_file,
            "min_pitch_whole": min_pitch_whole,
            "max_pitch_whole": max_pitch_whole,
            "start_pitch_whole": start_pitch_whole,
            "end_pitch_whole": end_pitch_whole,
            "mean_pitch_whole": mean_pitch_whole
        })
        return pitch_info

    # def analyze_pitch(self):
    #     sound = parselmouth.Sound(self.audio_files)  # read the sound
    #     pitch = sound.to_pitch()
    #     pitch_values = {}
    #     pitch_array = pitch.selected_array['frequency']
    #     pitch_values['min_value'] = int(min(filter(lambda x: x != 0, pitch_array)))
    #     pitch_values['max_value'] = int(max(pitch_array))
    #     pitch_values['start_value'] = int(next((x for x in pitch_array if x != 0), None))
    #     pitch_values['end_value'] = int(next((x for x in reversed(pitch_array) if x != 0), None))
    #     return pitch_values

    # def analyze_intensity(self):
    #     sound = parselmouth.Sound(self.audio_files)  # read the sound
    #     intensity = sound.to_intensity()
    #
    #     intensity_values = {}
    #     intensity_array = intensity.values[0]  # Extract the intensity values from the intensity object
    #     intensity_values['min_value'] = int(min(filter(lambda x: x > 0, intensity_array)))
    #     intensity_values['max_value'] = int(max(intensity_array))
    #     intensity_values['start_value'] = int(next((x for x in intensity_array if x > 0), None))
    #     intensity_values['end_value'] = int(intensity_array[-1])
    #     intensity_values['mean_intensity'] = (int(min(filter(lambda x: x > 0, intensity_array))) + int(max(intensity_array))) / 2
    #
    #     return intensity_values
    def analyze_pitch(self):
        pitch_values_list = []

        for file in self.audio_files:
            sound = parselmouth.Sound(file)  # read the sound
            pitch = sound.to_pitch()

            pitch_values = {}
            pitch_array = pitch.selected_array['frequency']
            pitch_values['min_value'] = int(min(filter(lambda x: x != 0, pitch_array)))
            pitch_values['max_value'] = int(max(pitch_array))
            pitch_values['start_value'] = int(next((x for x in pitch_array if x != 0), None))
            pitch_values['end_value'] = int(next((x for x in reversed(pitch_array) if x != 0), None))

            pitch_values_list.append(pitch_values)

        return pitch_values_list

    def analyze_intensity(self):
        intensity_values_list = []

        for file in self.audio_files:
            sound = parselmouth.Sound(file)  # read the sound
            intensity = sound.to_intensity()

            intensity_values = {}
            intensity_array = intensity.values[0]  # Extract the intensity values from the intensity object
            intensity_values['min_value_int'] = int(min(filter(lambda x: x > 0, intensity_array)))
            intensity_values['max_value_int'] = int(max(intensity_array))
            intensity_values['start_value_int'] = int(next((x for x in intensity_array if x > 0), None))
            intensity_values['end_value_int'] = int(intensity_array[-1])
            intensity_values['mean_intensity'] = (int(min(filter(lambda x: x > 0, intensity_array))) + int(
                max(intensity_array))) / 2

            intensity_values_list.append(intensity_values)

        return intensity_values_list

    def get_intensity_info(self):
        intensity_info = []
        for file in self.audio_files:
            # Загрузка звукового файла
            sound = parselmouth.Sound(file)
            # Получение параметров интенсивности звукового файла
            intensity = sound.to_intensity()

            intensity_values = intensity.values[0]
            min_intensity = int(min(intensity_values))
            max_intensity = int(max(intensity_values))
            mean_intensity = int(sum(intensity_values) / len(intensity_values))
            # Добавление информации об интенсивности в список intensity_info
            intensity_info.append({
                "file": os.path.splitext(file)[0],
                "min_intensity": min_intensity,
                "max_intensity": max_intensity,
                "mean_intensity": mean_intensity
            })
        return intensity_info

    def get_duration_info(self):
        duration_info = []
        for file in self.audio_files:
            # Load the sound file
            sound = parselmouth.Sound(file)
            # Get duration of the sound file
            duration = round(sound.get_total_duration(), 3)

            # Add duration information to the duration_info list
            duration_info.append({
                "file": os.path.splitext(file)[0],
                "duration": duration
            })
        return duration_info

    def save_intensity_to_df(self):
        intensity_df = pd.DataFrame()
        intensity_values = self.analyze_intensity()
        for i, value in enumerate(intensity_values):
            path = self.audio_files[i]
            filename = os.path.basename(path)  # Получаем имя файла из полного пути
            filename_parts = filename.split('_')  # Разделяем имя файла по символу "_"
            name = filename_parts[0] + "_" + filename_parts[-1].split('.')[0]  # Собираем новое имя файла из частей
            intensity_df = intensity_df._append(
                {'File': name, 'Min Intensity': value['min_value_int'],
                 'Max Intensity': value['max_value_int'],
                 'Start Intensity': value['start_value_int'], 'End Intensity': value['end_value_int'],
                 'Mean Intensity': value['mean_intensity']}, ignore_index=True)
        return intensity_df

    def save_pitch_to_df(self):
        pitch_df = pd.DataFrame()
        pitch_values = self.analyze_pitch()

        for i, value in enumerate(pitch_values):
            path = self.audio_files[i]
            filename = os.path.basename(path)  # Получаем имя файла из полного пути
            filename_parts = filename.split('_')  # Разделяем имя файла по символу "_"
            name = filename_parts[0] + "_" + filename_parts[-1].split('.')[0]  # Собираем новое имя файла из частей
            pitch_df = pitch_df._append(
                {'File': name, 'Min pitch': value['min_value'],
                 'Max pitch': value['max_value'],
                 'Start pitch': value['start_value'], 'End pitch': value['end_value'],
                 }, ignore_index=True)
        return pitch_df

    @staticmethod
    def save_data_to_files(df, csv_filename, doc_filename):
        df.to_csv(csv_filename, index=False)
        doc_content = df.to_string(index=False)
        with open(doc_filename, 'w') as file:
            file.write(doc_content)


audio_f = ["/Users/226/Рабочий стол/grant1/радость/Rec 41_split/syllable_0.wav",
           "/Users/226/Рабочий стол/grant1/радость/Rec 41_split/syllable_1.wav",
           "/Users/226/Рабочий стол/grant1/радость/Rec 41_split/syllable_2.wav",
           "/Users/226/Рабочий стол/grant1/радость/Rec 41_split/syllable_3.wav",
           "/Users/226/Рабочий стол/grant1/радость/Rec 41_split/syllable_4.wav",
           "/Users/226/Рабочий стол/grant1/радость/Rec 41_split/syllable_5.wav",
           "/Users/226/Рабочий стол/grant1/радость/Rec 41_split/syllable_6.wav",
           "/Users/226/Рабочий стол/grant1/радость/Rec 41_split/syllable_7.wav",
           '/Users/226/Рабочий стол/grant1/радость/Rec 42_split/syllable_0.wav',
           '/Users/226/Рабочий стол/grant1/радость/Rec 42_split/syllable_1.wav',
           '/Users/226/Рабочий стол/grant1/радость/Rec 42_split/syllable_2.wav',
           '/Users/226/Рабочий стол/grant1/радость/Rec 42_split/syllable_3.wav',
           '/Users/226/Рабочий стол/grant1/радость/Rec 42_split/syllable_4.wav',
           '/Users/226/Рабочий стол/grant1/радость/Rec 42_split/syllable_5.wav',
           '/Users/226/Рабочий стол/grant1/радость/Rec 42_split/syllable_6.wav',
           '/Users/226/Рабочий стол/grant1/радость/Rec 42_split/syllable_7.wav'
           ]

syllable_info = MainData(audio_f)

syllable_info.save_data_to_files(syllable_info.save_pitch_to_df(), 'pitch.csv', 'pitch.doc')
syllable_info.save_data_to_files(syllable_info.save_intensity_to_df(), 'intensity.csv', 'intensity.doc')

# path = self.audio_files
# filename = os.path.basename(path)  # Получаем имя файла из полного пути
# filename_parts = filename.split('_')  # Разделяем имя файла по символу "_"
# name = filename_parts[0] + "_" + filename_parts[-1].split('.')[0]  # Собираем новое имя файла из частей
# print(name)
