'''
Autor: Eric Matheus N Campelo
Data de criação: 04/11/2024
Descrição: Calculadora simples, ela faz operações com soma, subtração, multiplicação e divisão. É necessário apenas dar um "RUN" para dar ínicio a ela.

'''

soma = lambda x,y: x + y

subtracao = lambda x,y: x + y

multiplicacao = lambda x,y: x + y

divisao = lambda x,y: x + y


def calculadora():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")


    while True:
        opcao = input("Digite a opção (1/2/3/4): ")
        lista_opcoes = ['1', '2', '3', '4']

        if opcao in lista_opcoes:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == '1':
                    print(f"Resultado: {num1} + {num2} = {soma(num1, num2)}")
                elif opcao == '2':
                    print(f"Resultado: {num1} - {num2} = {subtracao(num1, num2)}")
                elif opcao == '3':
                    print(f"Resultado: {num1} * {num2} = {multiplicacao(num1, num2)}")
                elif opcao == '4':
                    print(f"Resultado: {num1} / {num2} = {divisao(num1, num2)}")
            except ValueError:
                print("Erro: Por favor, insira um número válido.")

        elif opcao == '':
            print("Por favor, digite alguma opção!")
            continue

        elif isinstance(opcao, str):
            print('Digite apenas números!')
            continue
        
        else:
            print('Opção inválida!')
            continue

        continuar = input("Deseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            print("Encerrando a calculadora.")
            break

calculadora()
