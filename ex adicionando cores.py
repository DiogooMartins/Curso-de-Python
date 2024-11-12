from time import sleep

print("\033[1;30;41m Teste \033[m", "\33[4;33;46m Teste \033[m")
print("\033[0;35;43m Teste \033[m", "\033[0;30;42m Teste \033[m")
print("\033[m Teste \033[m", "\033[7;30;m Teste \033[m")

sleep(1)

nome = str(input("\nQual o seu nome? "))
print("Que bom ter você aqui! {}{}{} , Seja bem vindo!".format('\033[4;36m', nome, '\033[m'))