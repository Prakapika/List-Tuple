def sort_list(Output):
    return Output[-1]

Output =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(Output, key = sort_list))