print("*************************************")
print("aqui e pra vc tentar acertar o numero")
print("*************************************")

numero = 10
numero = 1
chute = int (input("digita o numero que vc acredita que seja: "))

print(f"voce digitou: {chute}")

taCerto = chute == numero
taMaior = chute > numero

if (taCerto):
    print("vc acertou!!!")
else:
    if(taMaior):
        print("vc errou! esta numeros a cima.")
    else:
        print("ta errdo! ta com numeros a penos ai.")