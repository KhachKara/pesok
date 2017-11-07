def write_to_dict(some_list):
    dict = {}
    for i in some_list:
        if i not in dict:dict[i] = 1
        else:dict[i] += 1
    return dict