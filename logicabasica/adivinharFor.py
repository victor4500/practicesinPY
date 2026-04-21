print("000000000000000000")
print("usando loop for in")
print("000000000000000000")

numero = 15
tdtentativas = 3

for rodada in range(1, tdtentativas + 1):

     chute = int (input("digite o numero que vc acha que é: "))
     print(f"ta na rodada {rodada} de {tdtentativas} tentativas")
     print(f"vc digitou: {chute}")

     if(chute < 1 or chute > 20):
          print("o numero esta entre 1 e 20!")
          continue
     taCerto = chute == numero
     taMaior = chute > numero
     taMenor = chute < numero

     if(taCerto):
          print(f"voce acertou, o numero é {chute}")
          break
     else:
          if(taMaior):
               print("vc errou, tem numeros a mais")
          elif(taMenor):
               print("ta com numeros a menos")
print("fim")