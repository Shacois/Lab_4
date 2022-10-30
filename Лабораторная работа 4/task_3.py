def delete(list_, index=-1):
    left_list_ = list_[:index]
    right_list_ = []
    if index != -1:
        right_list_ = list_[index + 1:]
    list_ = left_list_ + right_list_
    return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
