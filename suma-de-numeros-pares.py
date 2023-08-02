# Escribe un programa que sume todos 
# los números pares del 1 al 1000 e imprima el resultado.

def es_par(number): 
    return number % 2 == 0

def main():
    total = 0
    for i in range(1, 1001):
        if(es_par(i)):
            total = total + i
    print(total)
    

if __name__ == "__main__":
    main()