import os
import parselmouth


def cut_audio_by_time_markers(audio_file, time_markers):
    sound = parselmouth.Sound(audio_file)
    output_folder = os.path.splitext(audio_file)[0] + "_split"
    os.makedirs(output_folder, exist_ok=True)

    for i, marker in enumerate(time_markers):
        start_time = marker[0]
        end_time = marker[1]
        sliced_sound = sound.extract_part(from_time=start_time, to_time=end_time)
        output_file = os.path.join(output_folder, f"syllable_{i}.wav")
        sliced_sound.save(output_file, "WAV")

    return os.listdir(output_folder)


audio_file = '/Users/226/Рабочий стол/grant1/радость/Rec 42.wav'
time_markers = [[0.280, 0.48], [0.486, 0.572], [0.579, 0.686], [0.688, 0.858], [0.864, 1.143], [1.157, 1.36], [1.388, 1.599], [1.608, 2.150]]

cut_audio_by_time_markers(audio_file, time_markers)


