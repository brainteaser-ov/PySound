import matplotlib.pyplot as plt

# Данные для графика arm
arm = {'Vowels': ['i', 'a', 'y'],
        'F1': [-0.324, 0.043, 1.167],
        'F2': [0.39, -0.692, 0.516]}

# Данные для графика rus
rus = {'Vowels': ['i', 'a', 'y'],
        'F1': [-0.27, 0.098, 0.788],
        'F2': [0.799, -0.896, -0.51]}

# Построение графиков для arm
plt.figure(1)
plt.plot(rus['F1'], arm['F1'], 'bo-', label='arm')
plt.plot(rus['F2'], arm['F2'], 'bo-', label='rus')
plt.xlabel('F1')
plt.ylabel('F1')
plt.title('Linear plot for arm/rus F1/F2')
plt.legend()

# Построение графиков на одной плоскости
plt.figure(9)
plt.plot(arm['F1'], arm['F2'], 'bo-', label='arm')
plt.plot(rus['F1'], rus['F2'], 'go-', label='rus')
plt.xlabel('F1')
plt.ylabel('F2')
plt.title('Linear plot for arm and rus')
plt.legend()


plt.figure(12)
plt.scatter(arm['F1'], arm['F2'], c='r', marker='o', label='arm')
plt.scatter(rus['F1'], rus['F2'], c='b', marker='o', label='rus')
plt.xlabel('F1')
plt.ylabel('F2')
plt.title('Scatter plot for arm and rus')
plt.legend()

# Отображение всех графиков
plt.show()
