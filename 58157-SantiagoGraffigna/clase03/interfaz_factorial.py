def main()
    palabra = input('Ingrese un numero')   
    result = interfaz_factorial(palabra)
    print(result)



def interfaz_factorial(palabra):
    
    try:
        n = int(palabra)
        return factorial(n)
    except:
        return 'Error'