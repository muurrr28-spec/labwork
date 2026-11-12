# Первоначальный (дефектный) вариант
def check_array(arr):
    res = []
    for i in arr:
        if i.islower(): 
            res.append(i)
    if res == sorted(res):
        return True
    return False

arrays = [['a', 'b', 'c'], ['z', 'y', 'x'], ['a', 'C', 'b'], ['a', 'b', 'c', 'd'], ['x', 'y', 'z']]
for i in range(len(arrays)):
    if check_array(arrays[i]):
        print(f"Массив {i+1}: Да")
    else:
        print("Нет")
