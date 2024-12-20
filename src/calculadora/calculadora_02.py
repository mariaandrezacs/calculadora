def calculadora():

    print(
        "************************************ Calculadora em Python ************************************"
    )

    print(
        "\nSelecione o número da operação desejada: \n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão"
    )

    opcao = input("Digite sua opção (1/2/3/4): ")

    if opcao == "1":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"A soma de {num1} + {num2} = {resultado}")
    elif opcao == "2":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"A subtração de {num1} - {num2} = {resultado}")
    elif opcao == "3":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"A multiplicação de {num1} * {num2} = {resultado}")
    elif opcao == "4":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 / num2
        print(f"A divisão de {num1} / {num2} = {resultado}")


calculadora()


# construido sem ajuda.
