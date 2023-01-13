import random

MAX_LINHAS = 3
MIN_APOSTA = 1
MAX_APOSTA = 100


LINHAS = 3
COLUNAS = 3


simbolosQtd = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

simbolosPeso = {
    "A": 6,
    "B": 4,
    "C": 2,
    "D": 1
}



def checkVitoria(array, linhas, aposta):
    resultado = 0
    linhasArray = []
    for linha in range(linhas):
        simbolo = array[0][linha]
        for coluna in array:
            checkSimbolo = coluna[linha]
            if (simbolo != checkSimbolo):
                break
        else:
            resultado += simbolosPeso[simbolo] * aposta
            linhasArray.append(linha + 1)

    return resultado, linhasArray


def roleta(linhas, colunas):
    simbolosArray = []
    for simbolo, simboloQtd in simbolosQtd.items():
        for _ in range(simboloQtd):
            simbolosArray.append(simbolo)

    colunasArray = []
    for _ in range(colunas):
        coluna = []
        simbolosCopia = simbolosArray[:]
        for _ in range(linhas):
            findValue = random.choice(simbolosCopia)
            simbolosCopia.remove(findValue)
            coluna.append(findValue)

        colunasArray.append(coluna)

    return colunasArray


def printRoleta(array):
    for linha in range(len(array[0])):
        for i, item in enumerate(array):
            if (i != len(array) - 1):
                print(item[linha], end=" | ")
            else:
                print(item[linha], end="")

        print()


def deposito():
    while True:
        total = input("Quanto você deseja depositar? R$")
        if (total.isdigit()):
            total = int(total)
            if (total > 0):
                break
            else:
                print("Você precisa digitar um número maior de zero.")
        else:
            print("Você precisa digitar um número")
    return total


def numeroLinhas():
    while True:
        linhas = input(
            "Quantas linha você dejesar apostar (1-" + str(MAX_LINHAS) + ")")
        if (linhas.isdigit()):
            linhas = int(linhas)
            if (1 <= linhas <= MAX_LINHAS):
                break
            else:
                print("Você precisa digitar um número entre um e três.")
        else:
            print("Você precisa digitar um número")
    return linhas


def apostar():
    while True:
        valor = input("Quanto você quer apostar em cada linha? R$")
        if (valor.isdigit()):
            valor = int(valor)
            if (MIN_APOSTA <= valor <= MAX_APOSTA):
                break
            else:
                print(
                    f"Você precisa digitar um valor entra {MIN_APOSTA} e {MAX_APOSTA}")
        else:
            print("Você precisa digitar um número")
    return valor


def girarRoleta(total):
    linhas = numeroLinhas()
    valor = apostar()
    while True:
        totalAposta = valor * linhas
        if (totalAposta > total):
            print(
                f"Você não possui saldo suficiente, o valor depositado foi: R${total}")
            girarRoleta(total)
        else:
            print(
                f"Você apostou R${valor} em {linhas}. O total de sua aposta é: R${totalAposta}")
            break

    resultado = roleta(LINHAS, COLUNAS)
    printRoleta(resultado)
    resultadoVitoria, linhasArray = checkVitoria(resultado, linhas, valor)
    print(f"Você ganhou ${resultadoVitoria}")
    
    if (len(linhasArray) > 0):
        print(f"Você ganhou a aposta na linha:", *linhasArray)
    else:
        print("Tente novamente")

    return resultadoVitoria - totalAposta

def main():
    total = deposito()
    totalSaida = total
    while True:
        print(f"Valor na sua conta: ${total}")
        opcao = input("Aperte enter para continuar ou N, para sair")
        if(opcao.upper() == "N"):
           break
        
        total += girarRoleta(total)

    if(totalSaida < total):
        print(f"Você entrou com ${totalSaida} e saiu com ${total} :)")
    else:
        print(f"Você entrou com ${totalSaida} e saiu com ${total} :(")

main()

