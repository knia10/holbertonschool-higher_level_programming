#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary:
        change_dic = {key: value}
        a_dictionary.update(change_dic)
        return(a_dictionary)
    else:
        return None
