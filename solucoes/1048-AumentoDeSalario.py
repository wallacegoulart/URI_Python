#1048 Aumento de Salario

salario = float(input())

if salario >= 0 and salario <= 400 :
    percentual = 0.15

elif salario > 400 and salario <= 800 :
    percentual = 0.12

elif salario > 800 and salario <= 1200 :
    percentual = 0.10

elif salario > 1200 and salario <= 2000 :
    percentual = 0.07

else:
    percentual = 0.04


novo_salario = salario + (salario * percentual)
reajuste = salario * percentual

print("Novo salario: {:.2f}".format(novo_salario) )
print("Reajuste ganho: {:.2f}".format(reajuste) )
print("Em percentual: {:.0f} %".format(percentual *100))
