import collections

def flatten(outlst, l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            flatten(outlst, el)
        else:
            outlst.append(el)

def flattenLst(l):
    outlst = []
    flatten(outlst, l)   
    return outlst

lst = [[[1, 2, 3], [4, 5]], 6]

print(flattenLst(lst))
