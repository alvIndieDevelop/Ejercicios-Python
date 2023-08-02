# Escribe una función que tome 
# un número como argumento y determine
# si es un número primo o no.

import sys
import math

def es_primo(number):
    if number <= 1:
        return False    
    sqrt_number = math.sqrt(number) + 1
    for i in range(2, int(sqrt_number)):
        if number % i == 0:
            return False
    return True
    

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.isdigit():
            print("el numero introducido es: ", arg)
            if es_primo(int(arg)):
                print("El numero es Primo")
            else: 
                print("El numero no es primo")
        else:
            print("el argumento no es un numero.")
    else:
        print("deme un argumento y tiene que ser numero.")


if __name__ == "__main__":
    main()