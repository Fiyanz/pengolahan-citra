# fungsi untuk mencari frekuensi array 1 dimensi
def get_frequency(arr):
    frequency = {}
    frequency_list = []
    for i in arr:
        i = int(i)
        frequency[i] = frequency.get(i, 0) + 1

    # mengubah dictionary ke list
    for key, value in frequency.items():
        frequency_list.append([key, value])
    return frequency_list

# fungsi untuk mencari frekuensi array 2 dimension
def get_frequency2d(arr):
    frequency = {}
    frequency_list = []
    for i in arr:
        for j in i:
            j = int(j)
            frequency[j] = frequency.get(j, 0) + 1

    # mengubah dictionary ke list
    for key, value in frequency.items():
        frequency_list.append([key, value])
    return frequency_list


