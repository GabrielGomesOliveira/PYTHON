nome = (input('Por favor, me diga seu nome! '))
print ("Bem vindo(a) {} a nossa atividade".format(nome)) 

while True:
    try:
        peso = float(input("{}, Qual é o seu peso? (kg) ".format(nome))) 
        altura = float (input("{}, Qual é a sua altura? (m) ".format(nome)))

        imc = peso / (altura ** 2)
        print ("{}, seu IMC é de {:.1f}".format(nome, imc))

        if imc < 18.5:
            print("Isso significa que está abaixo do peso")

        elif imc >= 18.5 and imc < 24.9:
            print ('Isso significa que está com o peso normal')
    
        elif imc >= 25 and imc < 29.9:
            print ('Isso significa que está com sobrepeso')
    
        else:
            print ('Isso significa que está obeso')
    
        continuar = input ('Deseja realizar novamente? (sim ou não): ')
        if continuar.lower() != 'sim':
            break

    except ValueError:
        print("valor inválido, por favor digite um NÚMERO válido")
