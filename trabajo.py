nombre= input('ingrese nombre del trabajador: ')
salario= int(input('ingrese salario a ganar: '))
Nhorasextras= int(input('ingrese el numero de horas extras trabajadas: '))
Nhorasdominicales= int(input('ingrese numero de horas dominicales trabajadas: '))
porchoraextra= int(1.35)
porchoradominical= int(1.75)

valordia= int( salario/30)
valorhora= int(salario/240)
valorhoraextra= int(porchoraextra * valorhora)
valorhoradominical= int(porchoradominical * valorhora)

valortotalhoraextra= int (valorhoraextra * Nhorasextras)
valortotalhorasdominicales= int(valorhoradominical * Nhorasdominicales)

totalsalario= int (salario +valortotalhoraextra + valortotalhorasdominicales) 

if totalsalario < 1000000:
    print(f'{nombre} necesita aumento')
elif totalsalario < 2000000:
    retencion=int(0.01)
    totalsalario = totalsalario - (totalsalario * 0.01) 
    print(f'{nombre}, su salario es de {totalsalario} y la retencion es de {retencion}%')
elif totalsalario <=3000000:
    retencion = int(0.03)
    totalsalario = totalsalario- (totalsalario * 0.03) 
    print(f'{nombre}, su salario es de {totalsalario} y la retencion es de {retencion}%')
else:
    retencion= int(0.04)
    totalsalario= totalsalario - (totalsalario * 0.04) 
    print(f'{nombre}, su salario es de {totalsalario} y la retencion es de {retencion}%')

print (f' Sr. {nombre}: \n su salario es de: {int(salario)} \n el valor del dia es: {int(valordia)} \n valor de las hora es de: {int(valorhora)} \n numero de horas extra: {int(Nhorasextras)} \n valor de la hora extra es de: {int(valorhoraextra)} \n el total de horas extras: {int(valortotalhoraextra)} \n total de horas dominicales trabajadas: {int(Nhorasdominicales)} \n valor hora dominical: {int(valorhoradominical)} \n valor total de las horas dominicales: {int(valortotalhorasdominicales)} \n el total a pagar es: {int(totalsalario)}')