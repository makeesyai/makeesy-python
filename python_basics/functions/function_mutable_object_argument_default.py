# Never use mutable object as default function argument
# (default values of the arguments are evaluated ***only once*** when the control reaches the function)

def add_item_to_dict(key, value, target_dict=None):
    if target_dict is None:  # if target_dict is not passed as an argument create an empty dict
        target_dict = {}
    print(locals())
    target_dict[key] = value
    return target_dict


def add_item_to_list(item, target_list=None):
    if target_list is None:  # if target_list is not passed as an argument create an empty list
        target_list = []
    print(locals())
    target_list.append(item)
    return target_list


added_lst1 = add_item_to_list(123)
print(added_lst1)
added_lst2 = add_item_to_list(456)
print(added_lst2)

added_dict1 = add_item_to_dict(1, "Hello")
print(added_dict1)
added_dict2 = add_item_to_dict(2, "Python")
print(added_dict2)
