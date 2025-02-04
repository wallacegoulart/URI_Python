#3170 BOlinhas de Natal


bolinhas = int(input())
galhos = int(input())

falta = galhos//2
qtd_bolinhas = (falta - bolinhas)

if qtd_bolinhas == 0:
    print("Amelia tem todas bolinhas!")

else:
    print("Faltam {} bolinha(s)".format(qtd_bolinhas) )
