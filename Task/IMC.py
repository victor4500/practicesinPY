print ("---sua calculado de IMC---")

print()

altura = float (input("   Digite sua altura: "))

peso = float (input("   digite seu peso: "))

altura2 = (altura * altura) 

imcfinal = (peso / altura2)

print (f"seu IMC é {imcfinal:.2f}")

if imcfinal <= 24.9:
    print("vc esta na medida do seu peso, fique tranquilo.")
elif imcfinal <= 29.9:
    print("vc ta com sobrepeso, seria bom dar uma olhada em receirtas ou até mesmo fazer enxercicios.")
elif imcfinal > 30:
    print("ta gordão, tem que fazer alguma coisa agora antes que seja tarde dmias")

print("obrigado por me utilizar :) ")