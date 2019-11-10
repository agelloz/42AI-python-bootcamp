from collections import OrderedDict

def custom_sort(word):
    return word.swapcase()

def generator(text, sep=" ", option=None):
    res = text.split(sep)
    if option == "shuffle":
        for i in range(99):
            odd = []
            even = []
            third = []
            j = 0
            while j < len(res):
                if j % 2 == 0:
                    even.append(res[j])
                elif j % 3 == 0:
                    third.append(res[j])
                else:
                    odd.append(res[j])
                j += 1
            res = third + even + odd
    if option == "unique":
       res = list(OrderedDict.fromkeys(res)) 
    if option == "ordered":
       res = sorted(res, key=custom_sort) 
    for word in res:
        yield word
