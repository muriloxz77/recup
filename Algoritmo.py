from Classes_banco import*
import getpass
import os

class Menu:
    def __init__(self):
        self.opcoes = {
            1: self.opcao1,
            2: self.opcao2,
            3: self.opcao3,
            4: self.opcao4,
            5: self.opcao5,
            6: self.opcao6
        }

    def exibir(self):
        while True:
            print("Menu:")
            print("1. Criar conta")
            print("2. Sacar")
            print("3. Depositar")
            print("4. Transferir")
            print("5. Saldo")
            print("6. Sair")

            escolha = int(input("Escolha uma opção: "))

            if escolha in self.opcoes:
                self.opcoes[escolha]()
            else:
                print("Opção inválida. Tente novamente.")

    def opcao1(self):
        print("Você escolheu a Opção: Criar conta.")

    def opcao2(self):
        print("Você escolheu a Opção: Sacar.")

    def opcao3(self):
        print("Você escolheu a Opção: Depositar.")

    def opcao4(self):
        print("Você escolheu a Opção: Transferir.")

    def opcao5(self):
        print("Você escolheu a Opção: Saldo.")

    def opcao6(self):
        print("Saindo do programa.")
        exit()

