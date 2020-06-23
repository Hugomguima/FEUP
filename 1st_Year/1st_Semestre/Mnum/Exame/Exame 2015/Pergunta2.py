# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:29:27 2020

@author: Hugo
"""


#1.
#Ao usar este iterador, cosnsegue-se obter o resultado desejado,
#já que caso haja algum erro de arredondamento, ao definirmos o numero
#como inteiro, estamos a eliminar quaisquer erros obtidos.
#
#2.
#Sendo x e h floats, é provável que hajam erros de arredondamento,já que 
#estamos a permitir a existencia de erros da calculadora do computador 
#já que valores inteiros em numeração decimal não são obrigatoriamente
#inteiros m numeração binária, pelo que a iteração pode ter erros associados
#á alteração indesejada do valor a ser iterado, afetando o esperado momento 
#para a condição de paragem
#
#3.
#Se em vez de estarmos a alterar o valor a ser iterado em cada iteração do ciclo,
#fizermos esta multipicação a cada iteração, estamos a fazer uma conta de
#multiplicar, em vez de várias de somar, pelo que são reduzidos os erros 
#de aproximação associados ás operações aritméricas. Menos opreações implicam
#menos erros associados ás mesmas.
#
#4.
#Este método de iteração é o mais vantajoso de todos, pelo que está a usar
#valores multiplos de 2, e como as operações do computador são feitas em
#base binária, evitam-se os erros associados ás operações, pois todos os 
#valores a utilizar serão inteiros em base binária
