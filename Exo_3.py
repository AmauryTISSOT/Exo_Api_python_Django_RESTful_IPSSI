# On vient créer un dictionnaire contenant la correspondance chiffre romain / chiffre arabes
roman_number_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romain_number_to_arab_number(roman_number: str):
    response = 0
    roman_number_length = len(roman_number)

    # On parcours les chiffres romains
    for i in range(roman_number_length):
        # Si le chiffre romain est plus petit que son suivant on le soustrait, sinon on l'additionne
        if (
            i < roman_number_length - 1
            and roman_number_dict[roman_number[i]]
            < roman_number_dict[roman_number[i + 1]]
        ):
            response -= roman_number_dict[roman_number[i]]
        else:
            response += roman_number_dict[roman_number[i]]

    return response


print(romain_number_to_arab_number("III"))
print(romain_number_to_arab_number("LVIII"))
print(romain_number_to_arab_number("MCMXCIV"))
