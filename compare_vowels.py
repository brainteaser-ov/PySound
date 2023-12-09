from math import sqrt

import numpy as np
import pandas as pd
from numpy.linalg import norm


class Compare:
    def __init__(self, F1a, F1i, F1y, F2a, F2i, F2y, S1a, S1i, S1y, S2a, S2i, S2y):
        self.F1a = F1a
        self.F1i = F1i
        self.F1y = F1y
        self.F2a= F2a
        self.F2i = F2i
        self.F2y = F2y
        self.S1a = S1a
        self.S1i = S1i
        self.S1y = S1y
        self.S2a = S2a
        self.S2i = S2i
        self.S2y = S2y
        self.S = np.array([S1a, S1i, S1y, S2a, S2i, S2y])
        self.F = np.array([F1a, F1i, F1y, F2a, F2i, F2y])
        self.F1 = np.array([F1a, F1i, F1y])
        self.F2 = np.array([F2a, F2i, F2y])
        self.S1 = np.array([S1a, S1i, S1y])
        self.S2 = np.array([S2a, S2i, S2y])

        self.F3 = np.array([F1a, F2a])
        self.F4 = np.array([F1i, F2i])
        self.F5 = np.array([F1y, F2y])

        self.S3 = np.array([S1a, S2a])
        self.S4 = np.array([S1i, S2i])
        self.S5 = np.array([S1y, S2y])

    def disperse(self):
        row = np.round((self.F - self.S) ** 2, 3)
        return row.tolist()

    def std(self):
        disp = self.disperse()
        row = np.round(np.sqrt(disp), 3)
        return row.tolist()


    def evc(self):
        row = [round(norm(self.F3 - self.F4), 3), round(norm(self.F4 - self.F5), 3),
               round(norm(self.F3 - self.F5), 3), ]
        row1 = [round(norm(self.S3 - self.S4), 3), round(norm(self.S4 - self.S5), 3),
                round(norm(self.S3 - self.S5), 3), ]
        row2 = [round(norm(self.S3 - self.F3), 3), round(norm(self.S4 - self.F4), 3),
                round(norm(self.S5 - self.F5), 3), ]

        return f"между гласными русский вариант: {row1}, " \
               f"между гласными акцентный вариант: {row}, " \
               f"между гласными русский/акцентный варианты: {row2}"


compare = Compare(0.043, -0.324, 1.167, -0.692, 0.39, 0.516, 0.098, -0.27, 0.788, -0.896, 0.799, -0.51)
dispersions = compare.disperse()
stds = compare.std()
evcs = compare.evc()

print("Дисперсия:", dispersions)
print("Стандартное отклонение:", stds)
print("Евклидово расстояние:", evcs)

