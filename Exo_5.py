def divisible_by_seven_and_five(number_list: list):
    result = []
    for i in number_list:
        if i % 7 == 0 and i % 5 == 0:
            result.append(i)
    return result


input = list(range(1500, 2701))
print(divisible_by_seven_and_five(input))
