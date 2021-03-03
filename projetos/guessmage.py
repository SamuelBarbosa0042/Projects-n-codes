import random

def jogar():
    print("Bem vindo ao jogo de advinhação")
    secreto = (random.randrange(1,101))
    tentativas = 0
    pontos = 1000
    print("Qual o nivel de dificuldade ?\n(1) fácil\n(2) médio\n(3) difícil\n")
    dificuldade = int(input("Escolha a dificuldade : "))
    if ( dificuldade == 1 ) :
        tentativas = 20
    elif( dificuldade == 2 ) :
        tentativas = 10
    else:
        tentativas=5
    print( "tentativas" , tentativas )

    for round in range ( 1 , tentativas+1 , 1 ):
        print( "Este é a {}º rodada de {} tentativas".format(str(round), str(tentativas) ) )
        print("Digite um numero entre 1 e 100")
        chute = int(input("Digite o seu chute :"))
        print( "Você digitou :" , chute )
        acertou = chute == secreto
        maior = chute > secreto
        menor = chute < secreto
        if (chute < 1 or chute > 100):
            print("deve digitar um numero entre 1 e 100")
            continue

        if (acertou):
            print("Acerto miseravi, e fez {} pontos\n".format(pontos))
            break
        else:
            if (maior):
                print("errou, chutou acima do numero\n")
            elif (menor):
                print("errou, chutou abaixo\n")
        pontos_perdidos = abs(secreto-chute)
        pontos = pontos - pontos_perdidos
        if (round==tentativas):
            print("O numero secreto era {0}, você fez {1} pontos".format(secreto,pontos))

    print("Acabou o joguinho!")
if (__name__=="__main__"):
    jogar()
