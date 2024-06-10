#6-https://www.codewars.com/kata/5809c661f15835266900010a/train/python
'''def double_every_other(lst):
    if not isinstance(lst, list):
        raise TypeError("The provided input is not a list")

    result = []
    for i, lst in enumerate(lst):
        if i % 2 == 1:
            result.append(lst * 2)
        else:
            result.append(lst)

    return result'''



#7-https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
'''def filter_list(l):
    return [item for item in l if isinstance(item, int)]
'''



#8-https://www.codewars.com/kata/586ec0b8d098206cce001141/train/python
'''def inverse_slice(items, a, b):
    return items[:a] + items[b:]'''


#9-https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef/train/python
'''def find_children(santas_list, children):
    santas_set = set(santas_list)
    children_set = set(children)
    present_children = santas_set.intersection(children_set)
    return sorted(present_children)'''