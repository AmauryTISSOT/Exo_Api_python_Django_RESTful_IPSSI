def number_of_even_odd(numbers: int):
    nb_even = 0
    nb_odd = 0

    for n in numbers:
        if n % 2 == 0:
            nb_even += 1
        else:
            nb_odd += 1

    return nb_even, nb_odd


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = number_of_even_odd(numbers_list)
print(f"Nombre de nombres pairs: {even}")
print(f"Nombre de nombres impairs: {odd}")
