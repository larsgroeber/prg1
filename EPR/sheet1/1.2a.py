def convert_celcius_to_celvin(celsius: float) -> float:
    # source: https://en.wikipedia.org/wiki/Kelvin
    return celsius + 273.15


celsius = input("Enter degrees in Celsius: ")
celvin = convert_celcius_to_celvin(float(celsius))
print("{}° Celsius are {} Celvin".format(celsius, celvin))