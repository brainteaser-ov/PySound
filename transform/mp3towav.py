import os
from pydub import AudioSegment


def convert_mp3_to_wav(folder_name):
    for filename in os.listdir(folder_name):
        if filename.endswith(".mp3"):
            mp3_file = os.path.join(folder_name, filename)
            wav_file = os.path.join(folder_name, os.path.splitext(filename)[0] + ".wav")
            sound = AudioSegment.from_mp3(mp3_file)
            sound.export(wav_file, format="wav")
            print(f"Converted {filename} to {os.path.basename(wav_file)}")


# Пример вызова функции
name = "/Users/226/Desktop/записи/2 армяне радость"
convert_mp3_to_wav(name)
