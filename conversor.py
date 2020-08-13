pregunta = input('desea convertir sus monedas S/N ')

while (pregunta.upper() == 'S'):

    print(' **** CONVERSOR DE MONEDAS ******* \n')
    print('MONEDAS \n USD = dolar estadounidense \n COP= peso colombiano \n EUR = euro \n JPY = yen japones \n GBP= libra esterlina \n')

    moneda = str(input("Digite la moneda "))

    valor = int(input("Digite el valor "))
    monedaConvertir = str(input("Digite la moneda a la cual va convertir su dinero "))

    def convert(a,b,c):
    
  
        if (c.upper() == "COP"):
            if (a.upper() == "USD"):
                result = b * 3756
            elif (a.upper() == "EUR"):
                result = b * 4426
            elif (a.upper() == "JPY"):
                result = b * 35.15
            elif (a.upper() == "GBP"):
                result = b * 5000
            else:
                print('digite una moneda existente')

        if (c.upper() == "USD"):
            if (a.upper() == "COP"):
                result = b * 0.00027
            elif (a.upper() == "EUR"):
                result = b * 1.18
            elif (a.upper() == "JPY"):
                result = b * 0.0094
            elif (a.upper() == "GBP"):
                result = b * 1.30
            else:
                print('digite una moneda existente')

        if (c.upper() == "EUR"):
            if (a.upper() == "COP"):
                result = b * 0.00023
            elif (a.upper() == "USD"):
                result = b * 0.85
            elif (a.upper() == "JPY"):
                result = b * 0.0079
            elif (a.upper() == "GBP"):
                result = b * 1.11
            else:
                print('digite una moneda existente')

        if (c.upper() == "JPY"):
            if (a.upper() == "COP"):
                result = b * 0.028
            elif (a.upper() == "USD"):
                result = b * 106.86
            elif (a.upper() == "EUR"):
                result = b * 126.03
            elif (a.upper() == "GBP"):
                result = b * 139.36
            else:
                print('digite una moneda existente')

        if (c.upper() == "GBP"):
            if (a.upper() == "COP"):
                result = b * 0.00020
            elif (a.upper() == "USD"):
                result = b * 0.77
            elif (a.upper() == "EUR"):
                result = b * 0.90
            elif (a.upper() == "JPY"):
                result = b * 0.0072
            else:
                print('digite una moneda existente')
        print('muchas gracias su respuesta es: ')
        print(f'Tienes {int(b)} {a} que equivalen a {float(result)}')

    
    convert(moneda, valor, monedaConvertir)
    
    pregunta = input('desea convertir mas monedas S/N ')

