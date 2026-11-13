from cadastro import Func, Empresa
def main():
    f1 = Func('122','Lucas',27,'Gerente',5200)
    f2 = Func('123','Fernando',27,'Tech Lead',7200)
    emp = Empresa()
    emp.cadastrar_func(f1)
    emp.cadastrar_func(f2)
    resultado = emp.buscar_func('123')
    print(resultado)
    print(emp.calcular_folha())
   
    


if __name__ == "__main__":
    main()