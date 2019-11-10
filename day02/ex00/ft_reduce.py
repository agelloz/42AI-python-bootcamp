
def ft_reduce(function_to_apply, list_of_inputs):
    res = list_of_inputs[0]
    for i in range(len(list_of_inputs) - 1):
        res = function_to_apply(res, list_of_inputs[i + 1])
        yield res
