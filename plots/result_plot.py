import matplotlib.pyplot as plt
import numpy as np

# Данные для столбчатой диаграммы "arm"
labels_arm = ['Площадь', 'Евкл. расст.', 'Станд. откл.', 'Дисп.']
values_arm = [0.829752, 1.65, 0.825, 0.681]

# Данные для столбчатой диаграммы "rus"
labels_rus = ['Площадь', 'Евкл. расст.', 'Станд. откл.', 'Дисп.']
values_rus = [0.655799, 0.791, 0.395, 0.156]

# Создание столбчатой диаграммы
fig, ax = plt.subplots()
bar_width = 0.35

# Положение столбцов на оси x
x = np.arange(len(labels_arm))

# Построение столбцов для "arm"
rects1 = ax.bar(x - bar_width/2, values_arm, bar_width, color='blue', label='arm')

# Построение столбцов для "rus"
rects2 = ax.bar(x + bar_width/2, values_rus, bar_width, color='green', label='rus')

# Добавление легенды
ax.legend()

# Настройка осей и заголовка
ax.set_ylabel('Значение')
ax.set_title('Сравнение данных')

# Установка меток на оси x
ax.set_xticks(x)
ax.set_xticklabels(labels_arm)

# Отображение графика
plt.show()


