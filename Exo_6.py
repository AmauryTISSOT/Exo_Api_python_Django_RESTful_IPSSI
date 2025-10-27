def convert_temp(temp: str):
    value = float(temp[:-1])
    unite = temp[-1].upper()

    if unite == "F":
        celsius = (value - 32) * 5 / 9
        return f"Température en Celsius = {round(celsius)}"
    elif unite == "C":
        fahrenheit = (value * 9 / 5) + 32
        return f"Température en Fahrenheit = {round(fahrenheit)}"
    else:
        return "Erreur - mauvaise unité"


# Exemple d'utilisation
print(convert_temp("45F"))
print(convert_temp("102C"))
