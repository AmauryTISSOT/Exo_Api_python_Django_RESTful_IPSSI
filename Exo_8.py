def fizz_buzz(numbers):
    result = []
    for i in range(1, numbers + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


# Example usage
fizzbuzz_list = fizz_buzz(50)
for item in fizzbuzz_list:
    print(item)
