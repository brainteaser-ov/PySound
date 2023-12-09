from docx import Document
import pandas as pd

# Открываем файл doc
doc = Document('/Users/226/Desktop/анализ текста/Женщина.docx')

# Создаем пустой список для хранения данных из таблицы
data = []

# Итерируемся по всем таблицам в документе
for table in doc.tables:
    # Итерируемся по всем строкам в таблице
    for row in table.rows:
        # Создаем список для хранения данных из текущей строки
        row_data = []
        # Итерируемся по всем ячейкам в строке
        for cell in row.cells:
            # Добавляем текст ячейки в список данных строки
            row_data.append(cell.text)
        # Добавляем список данных строки в общий список данных таблицы
        data.append(row_data)

# Создаем датафрейм из списка данных
df = pd.DataFrame(data[1:], columns=data[0])

# Выводим датафрейм
print(df)

data = df[df['KAB'].isin(['F1', 'F2'])]

#
print(data)