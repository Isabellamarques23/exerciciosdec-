# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MruozdfRC7YCyJBFNjZRongAbltr2Phh

Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.
"""

#Exemplo1
nota = float(input("digite uma nota entre zero e dez: "))
while nota > 10 or nota < 0:
 nota = float(input("digite um valor valido: "))
print("sucesso")

"""escreva um programa que solicite ao usuario que insira um numero e,em seguida, imprima a tabuada desse numero ate 10"""

#Exemplo2
numero = int(input("por favor, digite um numero: "))

contador = 1

while contador <= 10:
  resultado = numero * contador
  print(f"{numero} x {contador} = {resultado}")
  contador += 1

""" faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando
a pedir as informações.
"""

#Exercici1

usuario = (input("digite o nome do usuario: "))
senha = (input("digite sua senha: "))
while senha == usuario:
 print("erro, digite a senha novamente")
 usuario = (input("digite o nome do usuario: "))
 senha = (input("digite sua senha: "))
else:
 print("senha correta: ")

"""Escreva um programa que conte de 1 a 10 e imprima cada número."""

#Exercicio2
numero = 0
while numero <= 9:
 numero += 1
 print(numero)

"""Escreva um programa que imprima os números pares de 1 a 20."""

#Exercico3
numero = 2
while numero <= 20:
 print(numero)
 numero += 2

"""Escreva um programa que solicite ao usuário que insira um número e, em
seguida, imprima todos os números de 1 até esse número.
"""

#Exrcicio4

usuario = int(input("digite um numero: "))
contador = 1
while contador <= usuario:
 print(contador)
 contador += 1

"""Escreva um programa que solicite ao usuário que insira um número e, em
seguida, imprima todos os números pares de 2 até esse número.
"""

#Exercicio5

usuario = int(input("digite um numero"))
contador = 2
while contador <= usuario:
  print(contador)
  contador += 2

"""Escreva um programa que solicite ao usuário que insira um número e, em
seguida, imprima a tabuada desse número até 10.
"""

#Exercicio6

numero = int(input("digite um numero: "))
contador = 1
while contador <= 10:
  resultado = numero * contador
  print(f"{numero} x {contador} = {resultado}")
  contador += 1

"""Escreva um programa que solicite ao usuário que insira uma senha. O
programa deve continuar solicitando a senha até que o usuário insira a senha
correta.
"""

#Exercicio7

senha = 2906

senha = int(input("digite sua senha: "))
while senha != 2906:
 print("senha incorreta, digite novamente: ")
 senha = int(input("digite sua senha: "))
else:
 print("senha correta: ")

"""Escreva um programa que calcule a média de uma lista de números fornecida
pelo usuário.
"""

#Exercicio8

numero = int(input("digite a quantidade de numeros: "))
soma = 0
contador = 0
while contador < numeros:
 numero2 = int(input("digite numero para calcular: "))
soma += numero2
contador += 1
resultado = soma / numero
print(f"o resultado e: {resultado}")

"""Escreva um programa que solicite ao usuário que insira números até que ele
insira o número 0. Em seguida, imprima a soma de todos os números inseridos.
"""

from posixpath import supports_unicode_filenames
#Exercicio9

somo = 0
numero = int(input("digite um numero (0 encerra): "))
while numero != 0:
  soma += numero
  numero = int(input("digite um numero (0 encerra): "))
  print(f"a soma dor numeros {soma}")

"""Escreva um programa que solicite ao usuário que insira números até que ele
insira um número negativo. Em seguida, imprima o maior número inserido.
"""

#Exercicio10

numeromaior = 0
numero = int(input("digite um numero (o numero negativo encerra):"))
while numero >= 0:
  numero = int(input("digite um numero (o numero negativo encerra):"))
  if numero > numeromaior:
    numeromaior = numero
    print(f"o numero maior e {numeromaior}")