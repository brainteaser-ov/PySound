import pandas as pd
from frequency import Frequency
from docx import Document
from utils.utils_transform import split_column_to_str_int, interval_split, level_split, range_split, correlation_split


coeff_list = []
frequency_list = []
range_list = []
int_rising_list = []
int_falling_list = []
level_list = []
corr_list = []

frequency_dict = {'R41': [80, 450, 289, 247, 247, 332, 359, 306, 306],
 'R42': [70, 550, 350, 254, 254, 512, 416, 287, 335],
 }

frequency_list = []
for key, value in frequency_dict.items():
    frequency = Frequency(*value)
    frequency_list.append((key, frequency))
for obj in frequency_list:
    # print(obj[0], obj[1].calculate_coeff())
    coeff_list.append(obj[1].calculate_coeff())
for i in frequency_list:
    # print(i[0], 'Тональный диапазон/Регистр - ', i[1].calculate_range())
    range_list.append(i[1].calculate_range())
for a in frequency_list:
    # print(a[0], 'Объем интервала повышения тона -', a[1].calculate_int_rising())
    int_rising_list.append(a[1].calculate_int_rising())
for b in frequency_list:
    # print(b[0], 'Объем интервала понижения тона -', b[1].calculate_int_falling())
    int_falling_list.append(b[1].calculate_int_falling())
for c in frequency_list:
    # print(c[0], 'Уровни начала фразы/первого ударного слога/конца фразы -', c[1].calculate_level())
    level_list.append(b[1].calculate_level())
for d in frequency_list:
    # print(d[0], 'Соотношение уровней начала/первого ударного слога; '
    #       'первого ударного слога/конца фразы; уровня начала/конца фразы: -', d[1].calculate_corr())
    corr_list.append(d[1].calculate_corr())

d = pd.DataFrame({
    "id": [key for key in frequency_dict.keys()],
    "correlation": [corr_list[i] for i in range(len(corr_list))],
    "range": [range_list[i] for i in range(len(range_list))],
    "int_rising": [int_rising_list[i] for i in range(len(int_rising_list))],
    "int_falling": [int_falling_list[i] for i in range(len(int_falling_list))],
    "level": [level_list[i] for i in range(len(level_list))],
})

f = (level_split(d, 'level'))
n = (range_split(f, 'range'))
final = (correlation_split(n, 'correlation'))
final = (split_column_to_str_int(final, 'НФ/ПУ_pitch'))
final = (split_column_to_str_int(final, 'ПУ/КФ_pitch'))
final = (split_column_to_str_int(final, 'НФ/КФ_pitch'))
final = (interval_split(final, 'int_rising'))
final = (interval_split(final, 'int_falling'))
print(final.info())



final.to_csv('final.csv', index=False)
doc = Document()
with open('final.csv', 'r') as f:
    data = pd.read_csv(f)
table = doc.add_table(rows=data.shape[0]+1, cols=data.shape[1])
for i in range(data.shape[0]+1):
    for j in range(data.shape[1]):
        if i == 0:
            table.cell(i, j).text = data.columns[j]
        else:
            table.cell(i, j).text = str(data.values[i-1, j])

doc.save('final.docx')