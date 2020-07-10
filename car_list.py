import os
cardict = {}
menudict = {#Menu cada novo item é adicionado aqui
    "1": { "description": "informar o que tem na lista", "return": "info" },
    "2": { "description": "Adicionar novo veiculo", "return": "new"},
    "3": { "description": "Remover veiculo", "return": "delete"}
}
class Car:
    def __init__(self):#Contrutor
        self.name = ''
        self.mark = ''
        self.km = None
        self.engine = False
        self.input = None
        os.system('cls')
    def menu(self):#Mostra o Menu
        for i in menudict:
            print(f"{str(i)} - {menudict[i]['description']}")
        try:
            self.input = int(input("Digite sua opção: "))
        except:
            os.system('cls')
            print('Digite apenas numeros')
            self.menu()
        if str(self.input) in menudict:
            self.next = menudict[str(self.input)]["return"]
            self.calling()
    def calling(self):#Intermediario entre o menu e as funções
        if self.next == "info":
            self.info()
        elif self.next == "new":
            self.newCar()
        elif self.next == "delete":
            self.delCar()
    def newCar(self):#para adicionar novo carro
        self.name = input("Digite o nome do carro: ").strip()
        self.mark = input("Digite a marca do carro: ").strip()
        while True:
            try:
                self.km = float(input("Digite a KM do carro: "))
            except:
                print("Só numeros aceitos.")
                continue
            break
        cardict[self.name] = {"Name": self.name, "Mark": self.mark, "KM": self.km, "Engine": "OFF"}
        os.system("cls")
        self.menu()
    def delCar(self):# Para deletar carro
        self.input = input("Digite o nome do carro que quer deletar: ").strip()
        if self.input in cardict:
            del cardict[self.input]
        self.menu()
    def info(self):# Mostra os carros
        os.system('cls')
        print('-'*20)
        for i in cardict:
            print(cardict[i]["Name"])
            print(cardict[i]["Mark"])
            print(cardict[i]["KM"])
            print(cardict[i]["Engine"])
            print('-'*20)
        print(cardict)
        self.menu()
carro = Car()
carro.menu()