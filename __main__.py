
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

        opcao = input("\nEscolha uma opção: ")

        try:
            if opcao == "1":
                id = input("ID: ")
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                cargo = input("Cargo: ")
                salario = float(input("Salário: "))

                funcionario = Func(id, nome, idade, cargo, salario)
                empresa.cadastrar_func(funcionario)

                print("Funcionário cadastrado!")

            elif opcao == "2":
                id = input("Digite o ID do funcionário: ")
                funcionario = empresa.buscar_func(id)

                if funcionario is None:
                    print("Funcionário não encontrado!")
                else:
                    empresa.remover_func(funcionario)
                    print("Funcionário removido!")

            elif opcao == "3":
                id = input("Digite o ID: ")
                funcionario = empresa.buscar_func(id)

                if funcionario is None:
                    print("Funcionário não encontrado!")
                else:
                    print(funcionario)

            elif opcao == "4":
                empresa.listar_func()

            elif opcao == "5":
                total = empresa.calcular_folha()
                print(f"Folha salarial: R$ {total:,.2f}")

            elif opcao == "6":
                id = input("Digite o ID: ")
                aumento = float(input("Valor do aumento: "))

                empresa.aumentar_salario(id, aumento)
                print("Salário atualizado!")

            elif opcao == "7":
                print(f"Maior salário: R$ {empresa.maior_salario():,.2f}")

            elif opcao == "0":
                print("Encerrando o sistema...")
                break

            else:
                print("Opção inválida!")

        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
