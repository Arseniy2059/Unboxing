def print_params(a =1, b="строка", c=True):
    print(a, b, c)

values_list_2[54.32, "строка"]
print_params(*values_list_2, 42)

print_params(b = 25)
print_params(c = [1, 2, 3])
