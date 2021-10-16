cpf: int
senha: int
escolhas: int
cpf = 48281902282
senha = 150980
saldo: float
depositar: float
saldo = 1200.00
cpf = int(input("Digite seu CPF: "))
if cpf == 48281902282:
  senha = int(input("Digite sua senha: "))
while cpf != 48281902282:
  print("CPF incorreto, tente novamente!")
  cpf = int(input("Digite seu CPF: "))
  if cpf == 48281902282:
   senha = int(input('Digite sua senha: '))
if senha == 150980:
  print("Escolha (1)Depositar ", "(2):Sacar ", "(3):Saldo")
  escolhas = int(input("Escolher: "))
else:
  print("Senha incorreta, tente novamente")
if escolhas == 1:
  depositar = float(input("Depositar: "))
  print('Seu saldo é de:', depositar + saldo)
  while escolhas != 8:
    escolhas = int(input('Pressione 8 para continuar: '))
  if escolhas == 8:
     print("Escolha (1)Depositar ", "(2):Sacar ", "(3):Saldo")
     escolhas = int(input("Escolher: "))
 #if escolhas == 2:
  escolhas = int(input("Sacar: "))
if escolhas == 3:
  print('Seu saldo é de:', saldo)
