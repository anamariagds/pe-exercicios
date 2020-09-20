from random import *
def porta():
    score = 0
    tentativas = 0

    while score < 3:
        tentativas +=1

        print("\nTentativa",tentativas,":Escolha uma porta (1,2 ou 3):")
        
        portaEscolhida = input()
        portaEscolhida = int(portaEscolhida)

        portaCerta = randint(1,3)

        print("A porta escolhida foi a", portaEscolhida)
        print("A porta certa é a", portaCerta)

        if portaEscolhida == portaCerta:
            score +=1
            print("Parabéns!")
        else:
            print("Que peninha!")

        print(f'Sua pontuação é: {score}')
        
    print("\n** Você conseguiu! Terminou o jogo em", tentativas, "tentativas **")
    
def main():
    print(''' 
Porta da Fortuna!
========

Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!
   _____    _____   _____
  |     |  |     | |     |
  | [1] |  | [2] | | [3] |
  |    o|  |    o| |    o|
  |_____|  |_____| |_____|
   
''')
    porta()


if __name__=='__main__':
    main()