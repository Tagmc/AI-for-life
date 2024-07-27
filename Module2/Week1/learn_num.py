import numpy as np
# Tạo mảng 1 chiều 0 -> 9
arr = np.arange(0, 9, 1)
# Cách tạo một mảng boolean 3x3 với tất cả giá trị là True
arr1 = np.full((3, 3), fill_value=True, dtype=bool)
print(arr1)
arr2 = np.arange(0, 10)
print(arr[arr % 2 == 1])
arr = np.arange(10)
# reshape(rows, col) col = -1 co nghia la muon numpy tu dieu chinh kich thuoc cua mang cho phu hop
arr_2d = arr.reshape(2, -1)
print(arr_2d)
# concatenate: nối 2 mảng lại với nhau
arr3 = np.arange(10).reshape(2, -1)
arr4 = np.repeat(1, 10).reshape(2, -1)
# axis 0 noi theo nhieu mang, axis 1 noi theo cot
c = np.concatenate([arr3, arr4], axis=0)
print(c)
# np.tile(arr, 3) lap lai ca  mang 3 lan theo chieu ngang
# np.repeat(arr, 3) lap lai tung phan tu cua mang moi phan tu 3 lan
a = np.array([2, 6, 1, 9, 10, 3, 27])
# tim chi so voi dieu kien
index = np.where((a>=5) & (a<=10))
print(a[index])
def maxx(x, y):
  if x >= y:
    return x
  else:
    return y
c = np.array([5, 7, 9, 8, 6, 4, 5])
d = np.array([6, 3, 4, 8, 9, 7, 1])
# vectorize xu ly cac mang dau vao tra ra 1 vector voi dieu kien ham max
pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(c, d))
