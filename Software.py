#                           ASSUNTOS PARA ESTUDAR

#import choice

#variável = tipo de codigo/texto=str=string/numero=int

#type = tipo de variável | só pode começar com letra ou _, não com números, pode conter ambos ditos 

#"texto"  'texto'

#quais são  os tipos de dados / oq é um tipo de dado?

#def

#.title()=deixar letras em maiúsculas(?)

#.upper() .lower()

#capitalize()

#if

#elif

#else

#int

#input

#lstrip

#strip 

#split

#[0]

#{}

#\n = quebra de linha

#\t = tabulação =   tab

#end

#args

#** = exponenciação

#(f'oi')

#*multiplica, vale nomes

#(F'   ')

#range

#.sort = ordenação(coloca numeros e letras em ordem abc e crescente)


#                        SOMA SIMPLES


'''print('hello world')

num1 = int(input("Escolha um número"))
num2 = int(input("Escolha outro número"))

print("A sua soma é:", int(num1+num2))'''


#                     CALCULADORA SIMPLES


'''num1 = int(input("Escolha um número"))
num2 = int(input("Escolha um outro"))
op = input("Qual operação você deseja fazer?")
if op == "multiplicação":
 print("O resultado da sua multiplicação é: ", int(num1*num2))

 
elif op == "soma":
 print("O resultado da sua soma é: ", int(num1+num2))


elif op == "subtração":
 print("O resultado da sua subtração é: ", int(num1-num2))

elif op == "divisão":
 print("O resultado da sua divisão é: ", int(num1/num2))

else: 
 print('operação inválida')'''

#                   CALCULADORA PERSONALIZADA

'''print (" ")
print ("="*29)
print ("="*9, "BEM VINDO", "="*9)
print ("="*29)
print (" ")

print (" 1-SOMA", "\n","2-SUBTRAÇÃO", "\n","3-MULTIPLICAÇÃO", "\n","4-DIVISÃO")
num1 = float(input("Escolha um número:"))
num2 = float(input("Escolha outro número: "))
op = input("Qual operação você deseja fazer?")
if op == "1":
    print("O resultado da sua soma é: ", float(num1+num2))
elif op == "2":
    print("O resultado da sua subtração é: ", float(num1-num2))
elif op == "3":
    print("O resultado da sua multiplicação é: ", float(num1*num2))
elif op == "4":
    print("O resultado da sua divisão é: ", float(num1/num2))
else:
    print('operação inválida')'''

#                       PAR OU ÍMPAR

'''x = float(input("escolha um número"))
if x % 2 == 0:
    print("este número é par")
else:
    print("este numero é impar")'''


#                    CALCULADORA DE ÁREA        


'''print("="*42)

print("="*6, "Calcule a área da sua figura", "="*6)

print("="*42)

print("Qual a sua figura geométrica?")

print("\n" "1-triângulo", "\n", "2-quadrado", "\n", "3-retângulo", "\n", "4-trapézio",)

fig = int(input("Escolha o número que representa a figura desejada:"))

if fig == 1:
    c = float(input("Qual é o comprimento da base?"))
    h = float(input("Qual é a altura deste triângulo?"))
    print("Então a sua área é de:", (c*h)/2)


elif fig == 2:
    l = float(input("Qual é o lado desse quadrado?"))
    print("Então a sua área é de:", l**2)

elif fig == 3:
    b = float(input("Qual é o comprimento da base?"))
    h = float(input("Qual é a altura deste retângulo?"))
    print("Então a sua área é de:", b*h)

elif fig == 4:
    B = float(input("Qual é o comprimento daa base maior?"))
    b = float(input("Qual é o comprimento da base menor?"))
    h = float(input("Qual é a altura deste trapézio?"))
    print("Então a sua área é de:", ((B+b)*h/2) )'''


# tarefa 1

'''print("hello world")

#tarefa 2
A = int(input())
B = int(input())

X = A + B
print("X =", X)'''

#tarefa 3

'''r = float(input())
pi = 3.14159
print(f"A={pi*(r**2):.4f}")'''

#tarefa 4
'''n1 = int(input())
n2 = int(input())
print(f"PROD = {n1 * n2}")'''

#tarefa 5
'''A =  float(input())
B =  float(input())
MEDIA = (A*3.5 + B*7.5)/11
print(f"MEDIA = {MEDIA:.5f}")'''

#tarefa 6
'''A = float(input())
B = float(input())
C = float(input())
MEDIA = (A*2 + B*3 + C*5)/10
print (f"MEDIA = {MEDIA:.1f}")'''

#tarefa 7
'''A = int(input())
B = int(input())
C = int(input())
D = int(input())
Dif = A*B-C*D
print(f"DIFERENÇA = {Dif}")'''

#tarefa 8

'''number = int(input())
nh = int(input())
s = float(input())
print(f"NUMBER = {number}")
sal = nh*s
print(f"SALARY = U${sal:.2f}")'''

'''a, b, c, = input().split()

a = float(a)
b = float(b)
c = float(c)
pi = 3.14159'''



'''import random

numero = random.randint(1, 100)
tentativas = 0'''

'''While True:
    chute = int(input("Digite um número entre 1 e 100:"))
    tentativas += 1
    if chute < numero:
        print("Número muito baixo, diga um número maior")
    elif chute > numero:
        print("Número muito alto, diga um número menor")
        
    else:
        print(f"Parabéns, você acertou o número {numero} em {tentativas} tentativas!")
        break
    if tentativas == 10:
            print(f"Suas tenttativas acabaram, o número era {numero}")
            break
    

    jogar = input("Deseja jogar denovo? (s/n)")
    if jogar.lower() == "s":
        continue
    elif jogar.lower() == "n":
     print("Obrigado por jogar!")
     break
    else:
        print("digite uma resposta válida!")'''





'''M = int(input())
a = 0
b = 1
for i in range(M):
    if i == M-1:
     print(a, end=" ")
    
    else:
     print(a, end=" ")
    c = a + b
    a = b
    b = c'''

'''x = int(input())

fatorial = 1
 
for i in range(1, x + 1):
  fatorial *= i

print(fatorial)'''


'''
input()
sal_fix = float(input())
vendas = float(input())
sal_total = sal_fix + (vendas*0.15)
print(f"TOTAL = R$ {sal_total:.2f}")'''



'''A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159
print(f"TRIANGULO: {(A*C)/2:.3f}")
print(f"CIRCULO: {(pi*(C**2)):.3f}")
print(f"TRAPEZIO: {((A+B)*C/2):.3f}")
print(f"QUADRADO: {(B**2):.3f}")
print(f"RETANGULO: {(A*B):.3f}")'''


'''a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
calculo_ab = (a + b + abs(a-b))/2
calculo_ab_c = (calculo_ab + c + abs(calculo_ab - c))/2
print(f"{calculo_ab_c} eh o maior")'''


'''import math
x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

calculo = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"{calculo:.4f}")'''



'''N = int(input())

print(N)

100 = N // 100
N = N % 100

50 = N // 50
N = N % 50

20 = N // 20
N = N % 20

10 = N // 10
N = N % 10

5 = N // 5
N = N % 5

2 = N // 2
N = N % 2

1 = N // 1

print(f"{100} nota(s) de R$ 100,00")
print(f"{50} nota(s) de R$ 50,00")
print(f"{20} nota(s) de R$ 20,00")
print(f"{10} nota(s) de R$ 10,00")
print(f"{5} nota(s) de R$ 5,00")
print(f"{2} nota(s) de R$ 2,00")
print(f"{1} nota(s) de R$ 1,00")'''

'''salary = float(input())

if 2000.00 >= salary >= 0.00:
    print("Isento")

elif 3000.00 >= salary > 2000.00:
    imposto = (salary - 2000.00) * 0.08
    print(f"R$ {imposto:.2f}")

elif 4500.00 >= salary > 3000.00:
    imposto = (salary - 3000.00) * 0.18 + 1000.00 * 0.08
    print(f"R$ {imposto:.2f}")

elif salary > 4500.00:
    imposto = (salary - 4500.00) * 0.28 + 1500.00 * 0.18 + 1000.00 * 0.08
    print(f"R$ {imposto:.2f}")'''


'''num = float(input())

if 25 >= num >= 0:
    print("Intervalo [0,25]")
elif 50 >= num > 25:
    print("Intervalo (25,50]")
elif 75 >= num > 50:
    print("Intervalo (50,75]")
elif 100 >= num > 75:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")'''



'''n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = (n1*2 + n2*3 + n3*4 +n4*1)/10

print(f"Media: {media:.1f}")
if media >= 7:
    print("Aluno aprovado")
elif media < 5:
    print("Aluno reprovado")
elif 7 > media >= 5:
    print("Aluno em exame")
    x = float(input())
    nova_media = (media + x)/2
    if nova_media >= 5:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")
    print(f"Media final: {nova_media:.1f}")'''



'''
x = int(input())
y = int(input())

menor = min(x, y)
maior = max(x, y)

soma = 0

for i in range (menor + 1, maior):
    if i%2 != 0:
        soma += 1
print (soma)
'''



#SEQUENCIA DE FIBONACCI

'''print("-"*30)
print("SEQUÊNCIA DE FIBONACCI")
print("-"*30)
x = int(input("QUANTOS NUMEROS VOCE QUER VER?"))
a1 = 0
a2 = 1
print(a1, end=" ")
print(a2, end=" ")
cont = 2
while cont <= x:
    a3 = a1 + a2
    print(a3, end=" ")
    a1 = a2
    a2 = a3
    cont += 1
print("\n" "FIM")'''

'''n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    
    if x < y:
        num1 = x
        num2 = y
    else:
         num2 = x
         num1 = y 
    k = 0
    for num in range(num1 + 1, num2):
        if num % 2 == 0:
            k += 0
        else:
            k += num
    print(k)
'''


'''x = int(input("Digete o número"))
lista = [100, 50, 20, 10, 5, 2, 1];
for i in lista:
    i = int(i)
    print(f"{x//i} nota(s) de R$ {i}")
    x = x - ((x//i) * i)'''

k = 1
m = 0
for c in range(1, 100):
    n = k/c
    m += n
print(m)