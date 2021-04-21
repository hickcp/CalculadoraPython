def seep():
    sep = "-" * 40
def soma(x,y):
    a = x + y
    return(print(x,"+",y,"=",a))

def sub(x, y):
    a = x - y
    return(print(x,"-",y,"=",a))

def div (x, y):
    a = x/y
    return(print(x,"/",y,"=",a))

def mult (x, y):
    a = x * y
    return(print(x,"*",y,"=",a))

seep()

def teste():
    while True:
        print("Bem vindo a minha cálculadora ")
        print("Escolha entre: \n Somar \n subtrair \n dividir \n multiplicar\n Digite o valor: ")
        b = str(input())
        if b == str('somar') or b == str('Somar'):
            print("Você escolheu somar \n")
            x = eval(input("Digite o primeiro valor: "))
            y = eval(input("Digite o segundo valor: "))
            seep()
            soma(x, y)
            if input("Deseja reiniciar (S/N)? ") not in ('S', 's'):
                break

        if b == str('subtrair') or b == str('Subtrair'):
            print("Você escolheu subtrair \n")
            x = eval(input("Digite o primeiro valor: "))
            y = eval(input("Digite o segundo valor: "))
            seep()
            sub(x, y)
            if input("Deseja reiniciar (S/N)? ") not in ('S', 's'):
                break
        if b == str('dividir') or b == str('Dividir'):
            print("Você escolheu dividir \n")
            x = eval(input("Digite o primeiro valor: "))
            y = eval(input("Digite o segundo valor: "))
            seep()
            div(x, y)
            if input("Deseja reiniciar (S/N)? ") not in ('S', 's'):
                break
        if b == str('multiplicar') or b == str('Multiplicar'):
            print("Você escolheu multiplicar \n")
            x = eval(input("Digite o primeiro valor: "))
            y = eval(input("Digite o segundo valor: "))
            seep()
            mult(x, y)
            if input("Deseja reiniciar (S/N)? ") not in ('S', 's'):
                break
teste()
