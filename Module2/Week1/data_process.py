import pandas as pd
import numpy as np
df = pd.read_csv('advertising.csv')
data = df.to_numpy()


def classify(value, average):
    if value > average:
        return 'Good'
    elif value < average:
        return 'Bad'
    else:
        return 'Average'

arr = np.array(data)
col_sales = arr[:, 3]
average_column_sales = np.mean(col_sales)
col_newspaper = arr[:, 2]
average_newspaper = np.mean(col_newspaper)
print(np.max(col_sales))
print(np.argmax(col_sales))
print(np.sum(col_sales >= 20))

# Lọc các hàng có giá trị trong cột 4 >= 15
filtered_rows_sales = arr[col_sales >= 15]
filtered_rows_newspaper = arr[col_newspaper > average_newspaper]
average_column_radio = np.mean(filtered_rows_sales[:, 1])
print(average_column_radio)
print(np.sum(filtered_rows_newspaper[:, 3]))

scores = np.array([classify(sale, average_column_sales) for sale in arr[:, 3]])
print(f'{scores[7:10]}')

diff = np.abs(col_sales - average_column_sales)
index = np.argmin(diff)
nearest_average = col_sales[index]
new_scores = np.array([classify(sale, nearest_average) for sale in col_sales])
print(f'{new_scores[7:10]}')
