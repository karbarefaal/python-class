def compare_lists(list_a, list_b):
    res_list = set()
    for i in list_a:
        for j in list_b:
            if i == j:
                res_list.add(i)
    return list(res_list)

l1 = [1,2,3,4,5,6,7,8]
l2 = [1,2,4,6,8,9,0]

l_res = compare_lists(l1,l2)
print(f"our common list is {l_res}")


