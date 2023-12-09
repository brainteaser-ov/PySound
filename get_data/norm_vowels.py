
from sklearn.preprocessing import (MinMaxScaler, StandardScaler)
from scipy.stats import zscore
from utils.utils_transform import xsl_to_dataframe, save_df_as_csv

file_path = '/Users/226/Рабочий стол/grant1/out.xls'
df = xsl_to_dataframe(file_path)

columns = df[['F1', 'F2']]

transformed_columns = columns.apply(zscore)

# Замена выбранных колонок в исходном датафрейме на преобразованные значения
df[["F1", "F2"]] = transformed_columns
csv_file_path = '/Users/226/Рабочий стол/grant1/out.csv'
save_df_as_csv(df, csv_file_path)

