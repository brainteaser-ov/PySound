from pprint import pprint

import pandas as pd
import xlsxwriter

data = {
    'vowel': ['a', 'i'],
    'F1': [661.529, 467.569],
    'F2': [1374.239, 1993.081],
    'pitch': [353.29, 430.36],
    'min_pitch': [295.11, 381.23],
    'max_pitch': [385.58, 470.13],
    'int': [82.84, 82.58],
    'min_int': [81.72, 78.25],
    'max_int': [83.59, 84.55],
    'stressed': [False, False],
}



df = pd.DataFrame(data)
df.loc[len(df.index)] = ['y', '517.628','1441.161','253.97', '231.07', '260.96', '83.43', '75.76', '85.07', 'False']
df2 = pd.DataFrame ({
    'vowel': ['i', 'i'],
    'F1': [439.692, 728.442],
    'F2': [2082.735, 2712.785],
    'pitch': [231.83, 249.77],
    'min_pitch': [225.37, 234.07],
    'max_pitch': [239.51, 255.23],
    'int': [72.47, 75.97],
    'min_int': [70.23, 73.93],
    'max_int': [73.59, 77.29],
    'stressed': [False, True],
})
df = df.append(df2, ignore_index = True)


#df.to_csv('sounds_kab.csv', index=False)
#запись в csv

print(df)

#df_dict = df.to_dict()
#pprint(df_dict)
#приведение к словарю python



#выбрать нужные столбцы
#row = df.loc[df['vowel'] == 'i', ['vowel', 'F1']]
## same df.query("vowel == 'i'")[['vowel', 'F1']]
# lists = df.loc[df['vowel'] == 'a', ['vowel', 'F1']]
## same df.query("vowel == 'a'")[['vowel', 'F1']]
# row = df.loc[df['vowel'] == 'y', ['vowel', 'F1']]
## same df.query("vowel == 'y'")[['vowel', 'F1']]
#rows.to_csv('i_kab.csv', index=False)




#to excel
# filtered_df = df.query("vowel == 'i'")[['vowel', 'F1']]
#
# # Создание нового файла Excel
# workbook = xlsxwriter.Workbook('output.xlsx')
#
# # Добавление нового листа в файл
# worksheet = workbook.add_worksheet()
#
# # Запись заголовков столбцов
# headers = list(filtered_df.columns)
# for col_num, header in enumerate(headers):
#     worksheet.write(0, col_num, header)
#
# # Запись данных
# for row_num, row_data in enumerate(filtered_df.values):
#     for col_num, cell_data in enumerate(row_data):
#         worksheet.write(row_num + 1, col_num, cell_data)
#
# # Закрытие файла
# workbook.close()



