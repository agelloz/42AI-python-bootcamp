
def ft_map(function_to_apply, list_of_inputs):
    for elem in list_of_inputs:
        yield function_to_apply(elem)
