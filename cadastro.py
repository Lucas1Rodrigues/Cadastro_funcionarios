class Func:
    def __init__(self, id: str, nome: str, idade: int, cargo: str, salario=1612):
        self.__id = id
        self.nome = nome
        self.idade = idade
        self.__cargo = cargo
        self.__salario = salario

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if isinstance(id, str) and len(id) > 0:
            self.__id = id

    @property
    def cargo(self):
        return self.__cargo

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self,salario):
         if not isinstance(salario,(float,int)):
              raise ValueError("O salario precisa ser digitado em numeros")
         if salario < self.salario:
              raise ValueError("Voce nao pode reduzir salário")
         else:
              self.__salario = salario
    
    def __str__(self):
         return f"----------------------\nNome: {self.nome}\n Id: {self.id}\n idade: {self.idade}\n Cargo:{self.cargo}\n Salário:{self.salario}" 

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def cadastrar_func(self,funcionario:Func):
        if not isinstance(funcionario,Func):
              raise ValueError("Valor incorreto, digite um funcionario")
        else:
            self.funcionarios.append(funcionario)
        
    def remover_func(self,funcionario:Func):
        if funcionario not in self.funcionarios:
             raise ValueError("Funcionario nao existe")
        elif not isinstance(funcionario,Func):
            raise ValueError("Valor incorreto, digite um funcionario")
        else:
            self.funcionarios.remove(funcionario)
            print("Funcionario removido!")

    def buscar_func(self,id):
            if not isinstance(id,(str,int)):
                 raise ValueError("Digite um valor correto")
            for func in self.funcionarios:
                 if id == func.id:
                      return func

    def listar_func(self):
        for func in self.funcionarios:
             print(func)
             
    def calcular_folha(self):
         return sum(func.salario for func in self.funcionarios)
              
            
    def aumentar_salario(self,id, aumento:float):
            funcionario = self.buscar_func(id)
            if not isinstance(funcionario,Func):
                 raise ValueError('Funcionario nao foi achado')
            else:
                 funcionario.salario += aumento

    def maior_salario(self):
          if len(self.funcionarios) == 0:
               raise ValueError("Essa lista esta vázia")
          else:
                maior = max(func.salario for func in self.funcionarios)
                return maior
    
    

    
