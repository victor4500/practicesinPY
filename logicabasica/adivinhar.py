print("*************************************")
print("aqui e pra vc tentar acertar o numero")
print("*************************************")

numero = 10

tdtentativas = 3

rodada = 1

while (rodada <= tdtentativas ):
    chute = int (input("digita o numero que vc acredita que seja: "))
    print(f"tá na rodada {rodada} de {tdtentativas} tentativas.")
    print(f"voce digitou: {chute}")

    if(chute < 1 or chute > 10):
        print("o numero deve ser entre 1 e 10 ")
        rodada = rodada + 1
        continue

    taCerto = chute == numero
    taMaior = chute > numero

    if (taCerto):
        print("vc acertou!!!")
        break
    else:
        if(taMaior):
            print("vc errou! esta numeros a cima.")
        else:
            print("ta errdo! ta com numeros a penos ai.")

    rodada = rodada + 1