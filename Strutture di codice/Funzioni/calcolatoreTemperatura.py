import time
from tqdm import tqdm

def celsius_to_fahrenheit(gradi):
    convert_To_Fharenheit = (gradi * 9/5) + 32
    return convert_To_Fharenheit

def fahrenheit_to_celsius(gradi):
    convert_to_celsius = (gradi - 32) * 5/9
    return convert_to_celsius

def celsius_to_kelvin(gradi):
    convert_to_kelvin = gradi + 273.15
    return convert_to_kelvin


while True:
    print("=== covertitore temperatura ===")
    print("1 celsius --> fahrenheit")
    print("2 fahrenheit --> Celsius")
    print("3 Celsius --> Kelvin")
    print("0 esci")
    
    
    scelta = int(input("> "))
    
    if scelta == 1:
        gradi = float(input("gradi: "))
        print(celsius_to_fahrenheit(gradi))
    elif scelta == 2:
        gradi = float(input("gradi: "))
        print(fahrenheit_to_celsius(gradi))
    elif scelta == 3:
        gradi = float(input("gradi: "))
        print(celsius_to_kelvin(gradi))
    elif scelta == 0:
        for i in tqdm(range(10), desc="uscita in corso"):
            time.sleep(0.30)
        break
