import matplotlib.pyplot as plt
import pandas as pd

WMK = [79, 80, 81, 78, 70, 73, 72, 69, 70]
MWK = [74, 79, 82, 78, 79, 79, 77, 78, 74]
WMR = [79, 78, 81, 80, 79, 77, 77, 74, 66]
MWR = [74, 78, 78, 74, 71, 77, 73, 71, 74]


def plots(lst, coefficient):
    plot_lst = [num * coefficient for num in lst]
    return plot_lst


WMK_plot = plots(WMK, 1.333)
MWK_plot = plots(MWK, 1.429)
WMR_plot = plots(WMR, 1.471)
MWR_plot = plots(MWR, 1.515)
print(WMK_plot)
print(MWK_plot)
print(WMR_plot)
print(MWR_plot)

WMK_plot = pd.Series(WMK_plot)
MWK_plot = pd.Series(MWK_plot)
WMR_plot = pd.Series(WMR_plot)
MWR_plot = pd.Series(MWR_plot)

plt.plot(WMK_plot, label='WMK')
plt.plot(MWK_plot, label='MWK')
plt.plot(WMR_plot, label='WMR')
plt.plot(MWR_plot, label='MWR')

#plt.legend()
plt.show()

