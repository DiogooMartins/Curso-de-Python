sexo = str(input("Informe seu sexo [M/F]: ")).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input("Invalido. Informe novamente: ")).strip().upper()[0]
print("Registrado, seu sexo é {}!".format(sexo))