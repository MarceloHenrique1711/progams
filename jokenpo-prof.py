import random
Jogador = 0
Maquina = 0
def tesoura():    
    print("   _    _")
    print("  (_)  / )")
    print("    | (_/")
    print("   _+/")
    print("  //|\\")
    print(" // ||")
    print("(/  |/")

def pedra():
    print("   ____")
    print(" _/  _ \\")
    print("/ _ - _ \\")
    print("\\_______/")

def papel():
    print("    _____")
    print("   O_____O")
    print("  /     /")
    print(" /____ /")
    print("O_____O")

def mostraJogada(player, maquina):
    print("\n\nVocê: ")
    if player == 1:
        pedra()
    elif player == 2:
        papel()
    else:
        tesoura()
    print("\nMáquina: ")
    if maquina == 1:
        pedra()
    elif maquina == 2:
        papel()
    else:
        tesoura()

def mostraPlacar(placar):
    print(f"Vitórias: {placar[0]}\nDerrotas: {placar[1]}\nEmpates: {placar[2]}")

def jokenpo(player, maquina, placar):
    
    if player == 1:
        if maquina == 1:
            placar[2] = placar[2]+1
            print(f"Placar atual\n Jogador {placar[0]} X Máquina {placar[1]}")
            print(f"\n Total de empates {placar[2]}") 
        
        if maquina == 2:
            placar[1] = placar[1]+1
            print(f"Placar atual\n Jogador {placar[0]} X Máquina {placar[1]}")
            print(f"\n Total de empates {placar[2]}") 

        if maquina == 3:
            placar[0] = placar[0]+1
            print(f"Placar atual\n Jogador {placar[0]} X Máquina {placar[1]}")
            print(f"\n Total de empates {placar[2]}") 
    
    if player == 2:
        if maquina == 1:
            placar[0] = placar[0]+1
            print(f"Placar atual\n Jogador {placar[0]} X Máquina {placar[1]}")
            print(f"\n Total de empates {placar[2]}") 
        
        if maquina == 2:
            placar[2] = placar[2]+1
            print(f"Placar atual\n Jogador {placar[0]} X Máquina {placar[1]}")
            print(f"\n Total de empates {placar[2]}") 

        if maquina == 3:
            placar[1] = placar[1]+1
            print(f"Placar atual\n Jogador {placar[0]} X Máquina {placar[1]}")
            print(f"\n Total de empates {placar[2]}") 

    if player == 3:
        if maquina == 1:
            placar[1] = placar[1]+1
            print(f"Placar atual\n Jogador {placar[0]} X Máquina {placar[1]}")
            print(f"\n Total de empates {placar[2]}") 
        
        if maquina == 2:
            placar[0] = placar[0]+1
            print(f"Placar atual\n Jogador {placar[0]} X Máquina {placar[1]}")
            print(f"\n Total de empates {placar[2]}") 

        if maquina == 3:
            placar[2] = placar[2]+1
            print(f"Placar atual\n Jogador {placar[0]} X Máquina {placar[1]}")
            print(f"\n Total de empates {placar[2]}") 

    
#A lista placar é: Vitórias, Derrotas, Empates
placar = [0,0,0]
gameOn = "s"
while gameOn.lower() == "s":
    bot = random.randint(1,3)
    playerJogada = int(input("O qual você quer jogar?\n (1) Pedra\n (2) Papel\n (3) Tesoura\nDigite a resposta:"))
    mostraJogada(playerJogada, bot)
    jokenpo(playerJogada, bot, placar)
    repetir = input("Quer jogar de novo? (s/n)").lower().startswith("s")
    if repetir == "n":
        gameOn = "nem"
        print("Fim de jogo")