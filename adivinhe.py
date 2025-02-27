import random  # Importa o módulo random para gerar números aleatórios

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    print(f"(Dica: o número secreto é {numero_secreto})")  # Mostra o número secreto (para testes)

    tentativas = 0  # Inicializa o contador de tentativas
    
    print("Bem-vindo ao jogo Adivinhe o Número!")  # Mensagem de boas-vindas
    print("Tente adivinhar o número que estou pensando entre 1 e 100.")
    
    while True:  # Loop infinito até o jogador adivinhar
        try:
            palpite = int(input("Digite seu palpite: "))  # Lê um número inteiro do usuário
            tentativas += 1  # Incrementa o número de tentativas
            
            if palpite < 1 or palpite > 100:  # Verifica se o palpite está dentro do intervalo válido
                print("Por favor, digite um número entre 1 e 100.")
                continue  # Volta ao início do loop para pedir um novo palpite
            
            if palpite < numero_secreto:  # Se o palpite for menor que o número secreto
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:  # Se o palpite for maior que o número secreto
                print("Muito alto! Tente novamente.")
            else:  # Se o palpite for igual ao número secreto
                print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
                break  # Sai do loop e encerra o jogo
        except ValueError:  # Captura erros caso o usuário digite algo que não seja um número inteiro
            print("Entrada inválida! Por favor, digite um número inteiro.")

if __name__ == "__main__":  # Garante que o jogo só será executado se o arquivo for executado diretamente
    adivinhe_o_numero()
