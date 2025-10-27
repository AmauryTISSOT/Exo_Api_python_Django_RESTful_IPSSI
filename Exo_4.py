def add_one(number_list: list):
    list_to_string = "".join(map(str, number_list))
    string_to_int = int(list_to_string)
    string_to_int += 1
    int_to_string = str(string_to_int)
    string_to_list = [int(s) for s in int_to_string]
    return string_to_list


print(add_one([1, 2, 3]))
print(add_one([4, 3, 2, 1]))
print(add_one([9]))
