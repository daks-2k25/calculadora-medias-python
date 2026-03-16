import time
import os
import platform

#Inicio do laço de repetição
while True: 
   
    os.system('cls' if platform.system() == 'Windows' else 'clear')

    print("=== SISTEMA DE MÉDIAS ===")
    
    nome = input("Escreva o nome do aluno (ou 'sair'): ")
    if nome.lower() == 'sair':
        break 

    turma = input("Qual a turma do aluno: ")

#Captura das notas para fazer a soma

    try:
        nota1 = float(input("Escreva a 1ª nota: "))
        nota2 = float(input("Escreva a 2ª nota: "))
        nota3 = float(input("Escreva a 3ª nota: "))
    except ValueError:
        print("\nErro: Escreva apenas números (Exemplo: 7.0)")
        time.sleep(2)
        continue 

#Volta para o início do loop em vez de fechar o programa

    print("\nAguarde enquanto calculamos...")
    time.sleep(1)

    media_final = (nota1 + nota2 + nota3) / 3
    media_minima = 6.0

#Mostrar a soma das notas e o resultado letivo

    print(f"\nA média final é: {round(media_final, 2)}")

    if media_final >= media_minima:
        print(f"O aluno {nome} está APROVADO!")
    elif media_final >= 4.0:
        faltante = round(media_minima - media_final, 2)
        print(f"O aluno {nome} da turma {turma} está em RECUPERAÇÃO.")
        print(f"Faltam {faltante} pontos para atingir a média {media_minima}.")
    else:
        print(f"O aluno {nome} está REPROVADO.")

    print("\n" + "-"*30)
    input("Pressione ENTER para calcular outro aluno...")