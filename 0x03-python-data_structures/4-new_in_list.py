def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    cpylist = my_list.copy()
    cpylist[idx] = element
    return cpylisty
