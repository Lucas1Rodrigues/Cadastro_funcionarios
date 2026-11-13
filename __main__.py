from cadastro import Func, Empresa
def main():
    empresa = Empresa()

    while True:
        print("\n========== SISTEMA DE FUNCIONÁRIOS ==========")
        print("1 - Cadastrar funcionário")
        print("2 - Remover funcionário")
        print("3 - Buscar funcionário")
        print("4 - Listar funcionários")
        print("5 - Calcular folha salarial")
        print("6 - Aumentar salário")
        print("7 - Mostrar maior salário")
        print("0 - Sair")

        opcao = input("\nEscolha uma opcao: ")

        try:
            if opcao == '1':
                id = input("ID: ")
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                cargo = input("Cargo: ")
                salario = float(input("Salário: "))

                funcionario = Func(id,nome,idade,cargo,salario)
                empresa.cadastrar_func(funcionario)

                print("Funcionario Cadastrado! ")

            elif opcao == "2":
                id = input("Digite o Id do funcionario: ")
                funcionario = empresa.remover_func(id)

            elif opcao == "3":
                id = input("Digite o id do funcionario: ")
                funcionario = empresa.buscar_func()
                print(funcionario)

            elif opcao == "4":
                empresa.listar_func()

            elif opcao == "5":
                print(f"A folha total de funcionarios é R$ {empresa.calcular_folha()}")

            elif opcao == "6":
                id = input("Digite o id do funcionario: ")
                valor = input("Digite o valor do aumento (APENAS O VALOR DO AUMENTO)")
                empresa.aumentar_salario(id,valor)
            
            elif opcao == "7":
                print(f"O maior salario da empresa é R${empresa.maior_salario()}"

            elif opcao = "0"
                print("Encerrando o sistema...")
                break
            else:
                print("Opcao inválida!")

            except ValueError as e:
                print(f"erro: {e}")



                
   
    


if __name__ == "__main__":
    main()