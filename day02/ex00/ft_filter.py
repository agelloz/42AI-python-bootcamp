
def ft_filter(function_to_apply, list_of_inputs):
    for elem in list_of_inputs:
        res = function_to_apply(elem)
        if res is True:
            yield elem
