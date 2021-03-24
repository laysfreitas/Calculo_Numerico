import math

#define a função que será usada no problema
def function(x):
    return x*(math.log10(x)) - 1

#define a função de iteração
def itfunction(x):
    return x - 1.3*(x*(math.log10(x)) - 1)

# intervalo inicial [a,b]
a = 2
b = 3

# z e r servem para salvar os valores iniciais para imprimir na tabela
z = a
r = b

#precisões
erro1 = pow(10,-7)
erro2 = pow(10,-7)

print("_____________________________________________________________________________________________________________________________")
print("|Exemplo 21\t\t|\tDados Iniciais\t|\tRaiz Aproximada\t|\tFuncao da Raiz Aproximada\t|\tErro em x\t|\tNº de iteracoes |")

#-------------------- Bissecção -------------------------------

k = 1
if((b - a) < erro1):
    x = (b+a)/2
else:
    while(1):

        fa = function(a)
        x = (a+b)/2

        if( fa*function(x) > 0):
            a = x
        else:
            b = x
        if ((b - a) < erro1):
            x = (a+b)/2
            break

        k = k + 1

print("|---------------|-------------------|-------------------|-------------------------------|---------------|-------------------|")
print("|Bisseccao\t\t|\t\t[%d,%d]\t\t|\t %.8f \t|\t\t\t%.8f\t\t\t|\t %.8f |\t\t %d \t\t|" % (z, r, x, function(x), b - a, k))

#------------------------ Posiçaõ Falsa ----------------------------------

#Reiniciando os contadores
a = 2
b = 3

# z e r servem para salvar os valores iniciais para imprimir na tabela
z = a
r = b

fa = function(a)
fb = function(b)

#calcular o número de iterações
k = 1

if((b-a) < erro1):
   x = ((a*fb-b*fa)/(fb-fa))
else:
    if ((math.fabs(fa) < erro2) or (math.fabs(fb) < erro2)):
        x = a
    else:
        while(1):
            fa = function(a)
            fb = function(b)
            x = (a*fb - b*fa)/(fb - fa)

            if(math.fabs(function(x)) < erro2):
                break

            if(fa*function(x) > 0):
                a = x
            elif(fa*function(x) < 0):
                b = x

            if((b-a) < erro1):
                break
            k = k + 1

        print("|---------------|-------------------|-------------------|-------------------------------|---------------|-------------------|")
        print("|Posicao Falsa\t|\t\t[%d,%d]\t\t|\t %.8f \t|\t\t\t%.8f\t\t\t|\t %.8f |\t\t %d \t\t\t|" % (z, r, x, function(x), b - a, k))

#-------------------------Ponto Fixo---------------------------------------------

xinicial = 2.5

#z serve para salvar o valor de x inicial
z = xinicial

#calcular o número de iterações
k = 1

if(math.fabs(xinicial) < erro1):
    x = xinicial
else:
    while(1):
        x = itfunction(xinicial)
        if((math.fabs(function(x)) < erro1) or (math.fabs(x - xinicial) < erro2)):
            break
        xinicial = x
        k = k + 1
    print("|---------------|-------------------|-------------------|-------------------------------|---------------|-------------------|")
    print("|MPF\t\t\t|\t x0 = %.1f \t\t|\t %.8f \t|\t\t\t%.8f\t\t\t|\t %.8f |\t\t %d \t\t\t|" % (z, x, function(x), math.fabs(x - xinicial), k))

#----------------------------Newton-Rhapson------------------------------------------------------

#constante que representa 1/log(e,10)
logneperiano = 0.43429

def derivada(x):
    return math.log10(x) + logneperiano

xinicial = 2.5

z = xinicial

#calcular o número de iterações
k = 1

if(abs(function(xinicial)) < erro1):
    x = xinicial
else:
    while(1):
        x = xinicial - (function(xinicial)/derivada(xinicial))
        if(abs(function(x)) < erro1 or abs(x - xinicial) < erro2):
            break

        xinicial = x
        k = k + 1

print("|---------------|-------------------|-------------------|-------------------------------|---------------|-------------------|")
print("|Newton-Rhapsody|\t x0 = %.1f \t\t|\t %.8f \t|\t\t\t%.8f\t\t\t|\t %.8f |\t\t %d \t\t\t|" % (z, x, function(x), abs(x - xinicial), k))

#-------------------------------Secante----------------------------------------------------------

x0 = 2.3
x1 = 2.7

# z e r servem para salvar os valores iniciais para imprimir na tabela
z = x0
r = x1

#calcular o número de iterações
k = 1

if(math.fabs(function(x0)) < erro1):
    x = x0
else:
    if(math.fabs(function(x1)) < erro1 or math.fabs(x1-x0) < erro2):
        x = x1
    else:
        while(1):
            x = x1 - (function(x1))/(function(x1)-function(x0))*(x1-x0)
            if(math.fabs(function(x)) < erro1 or math.fabs(x-x1) < erro2):
                break
            x0 = x1
            x1 = x
            k = k + 1
    print("|---------------|-------------------|-------------------|-------------------------------|---------------|-------------------|")
    print("|Secante\t\t| x0 = %.1f;x1 = %.1f |\t %.8f \t|\t\t\t%.8f\t\t\t|\t %.8f |\t\t %d \t\t\t|" % (z, r, x, function(x), x - x1, k))
    print("|_______________|___________________|___________________|_______________________________|_______________|___________________|")
