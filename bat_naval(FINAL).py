# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
from numpy import zeros
import time
arquivo = open("barcos.txt", 'r')
texto = str(arquivo.readlines())
texto = texto.split('\n')
print (texto)
#Criando as matrizes e definindo os tabuleiros
tab_p1 = zeros((9,9))
tab_p2 = zeros((9,9))

tab2_p1 = zeros((9,9))
tab2_p2 = zeros((9,9))

#Se a pontuaçao for igual ao numero de barcos: Game Over
pontuacao1p1 = 0
pontuacao2p1 = 0
pontuacao3p1 = 0
p1total = pontuacao1p1 + pontuacao2p1 + pontuacao3p1

pontuacao1p2 = 0
pontuacao2p2 = 0
pontuacao3p3 = 0
p2total = pontuacao1p1 + pontuacao2p1 + pontuacao3p1

#Localizar a coluna que o usuario escolheu 
def localizacao_coluna(barco):
     
    i = list(barco)
    
    i[0] == i[0].lower()
            
    if i[0] == 'a':
        coluna = 0
        return int(coluna)
                
    if i[0] == 'b':
        coluna = 1
        return int(coluna)
                
    if i[0] == 'c':
        coluna = 2
        return int(coluna)
                
    if i[0] == 'd':
        coluna = 3
        return int(coluna)
                
    if i[0] == 'e':
        coluna = 4
        return int(coluna)
                
    if i[0] == 'f':
        coluna = 5
        return int(coluna)
                
    if i[0] == 'g':
        coluna = 6
        return int(coluna)
                
    if i[0] == 'h':
        coluna = 7
        return int(coluna)
                
    if i[0] == 'i':
        coluna = 8
        return int(coluna)
        
    else:
        print("Esta coluna não existe, digite novamente")            
        return -1
    
#Localizando as linhas que o usuário escolheu    
def localizacao_linha(barco):
    
    i = list (barco)
    linha = int(i[1])-1
    if linha > 8 or linha < 0:
        return -1
    else:
        return int(linha)
        
    

#Jogador 1 posiciona

def posicionar_1():
    
    confirmacao = 'sim'

    b1 = str(input("Selecione a posicao do barco 1 (EX.: F3, B4, E5...)\
    Detalhes: Barco 1 tem dimensões (1x3)\
    Linhas vão de 1 - 9 e Colunas de A - I\n"))
    
    while (localizacao_coluna(b1) >= 7 or localizacao_coluna(b1) < 0) and\
    (list(b1)[0] == "h" or list(b1)[0] == "i"):
        
        print ("Reposicione o barco")
        
        b1 = str(input("Selecione a posicao do barco 1 (EX.: F3, B4, E5...)\
    Detalhes: Barco 1 tem dimensões (1x3)\
    Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
    tab_p1[localizacao_linha(b1)][localizacao_coluna(b1)] = 1
    tab_p1[localizacao_linha(b1)][localizacao_coluna(b1)+1] = 1
    tab_p1[localizacao_linha(b1)][localizacao_coluna(b1)+2] = 1
    
    print(tab_p1)
    
    confirmacao = str(input("Deseja alterar a posição?"))
    
    
    while confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
    
        confirmacao = str(input("Deseja alterar a posição?"))
        
        if confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
            
#Se o usuário quiser trocar, todas as posições serão zeradas 
            
            tab_p1[localizacao_linha(b1)][localizacao_coluna(b1)] = 0
            tab_p1[localizacao_linha(b1)][localizacao_coluna(b1)+1] = 0
            tab_p1[localizacao_linha(b1)][localizacao_coluna(b1)+2] = 0
            
            b1 = str(input("Selecione a posicao do barco 1 (EX.: F3, B4, E5...)\
    Detalhes: Barco 1 tem dimensões (1x3)\
    Linhas vão de 1 - 9 e Colunas de A - I\n"))
            
            tab_p1[localizacao_linha(b1)][localizacao_coluna(b1)] = 1
            tab_p1[localizacao_linha(b1)][localizacao_coluna(b1)+1] = 1
            tab_p1[localizacao_linha(b1)][localizacao_coluna(b1)+2] = 1
            
            print(tab_p1)
        
        else:
        
            pass
        
    

    b2 = str(input("Selecione a posicao do Barco 2 (EX.: F3, B4, E5...)\
    Detalhes: Barco 2 tem dimensões (4x1)\
    Linhas vão de 1 - 9 e Colunas de A - I\n"))
    
    
    while localizacao_linha(b2) > 5 or localizacao_linha(b2)<0 or \
            localizacao_coluna(b2) < 0 :
            
        print ("Reposicione o barco")
        
        b2 = str(input("Selecione a posicao do Barco 2 (EX.: F3, B4, E5...)\
    Detalhes: Barco 2 tem dimensões (4x1)\
    Linhas vão de 1 - 9 e Colunas de A - I\n"))
    
    tab_p1[localizacao_linha(b2)][localizacao_coluna(b2)] = 2
    tab_p1[localizacao_linha(b2)+1][localizacao_coluna(b2)] = 2
    tab_p1[localizacao_linha(b2)+2][localizacao_coluna(b2)] = 2
    tab_p1[localizacao_linha(b2)+3][localizacao_coluna(b2)] = 2
    
    print(tab_p1)
    
    while confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
    
        confirmacao = str(input("Deseja alterar a posição?"))
        
        
        if confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
        
            tab_p1[localizacao_linha(b2)][localizacao_coluna(b2)] = 0
            tab_p1[localizacao_linha(b2)+1][localizacao_coluna(b2)] = 0
            tab_p1[localizacao_linha(b2)+2][localizacao_coluna(b2)] = 0
            tab_p1[localizacao_linha(b2)+3][localizacao_coluna(b2)] = 0
            
            b2 = str(input("Selecione a posicao do Barco 2 (EX.: F3, B4, E5...)\
        Detalhes: Barco 2 tem dimensões (4x1)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
            while localizacao_linha(b2) > 5 or localizacao_linha(b2)<0 or \
            localizacao_coluna(b2) < 0 :
            
                print ("Reposicione o barco")
        
                b2 = str(input("Selecione a posicao do Barco 2 (EX.: F3, B4, E5...)\
        Detalhes: Barco 2 tem dimensões (4x1)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
            
            tab_p1[localizacao_linha(b2)][localizacao_coluna(b2)] =  2
            tab_p1[localizacao_linha(b2)+1][localizacao_coluna(b2)] = 2
            tab_p1[localizacao_linha(b2)+2][localizacao_coluna(b2)] = 2
            tab_p1[localizacao_linha(b2)+3][localizacao_coluna(b2)] = 2
                
            print(tab_p1)
        
        else:
            pass
        
        b3 = str(input("Selecione a posicao do Barco 3 (EX.: F3, B4, E5...)\
        Detalhes: Barco 3 tem dimensões (2x2)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
        while (localizacao_coluna(b3) > 7 or localizacao_coluna(b3) < 0) and\
    (list(b1)[0] == "i"):
        
            print ("Reposicione o barco")
            
            b3 = str(input("Selecione a posicao do Barco 3 (EX.: F3, B4, E5...)\
        Detalhes: Barco 3 tem dimensões (2x2)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
        tab_p1[localizacao_linha(b3)][localizacao_coluna(b3)] = 3
        tab_p1[localizacao_linha(b3)][localizacao_coluna(b3)+1] = 3
        tab_p1[localizacao_linha(b3)+1][localizacao_coluna(b3)] = 3
        tab_p1[localizacao_linha(b3)+1][localizacao_coluna(b3)+1] = 3
        
        print (tab_p1)
        confirmacao = 's'
        
        while confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
    
            confirmacao = str(input("Deseja alterar a posição?"))
        
            if confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
        
                tab_p1[localizacao_linha(b3)][localizacao_coluna(b3)] = 0
                tab_p1[localizacao_linha(b3)][localizacao_coluna(b3)+1] = 0
                tab_p1[localizacao_linha(b3)+1][localizacao_coluna(b3)] = 0
                tab_p1[localizacao_linha(b3)+1][localizacao_coluna(b3)+1] = 0
                
                b3 = str(input("Selecione a posicao do Barco 3 (EX.: F3, B4, E5...)\
        Detalhes: Barco 3 tem dimensões (2x2)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
                while (localizacao_coluna(b3) > 7 or localizacao_coluna(b3) < 0) and\
    (list(b1)[0] == "i"):
        
                    print ("Reposicione o barco")
        
                    b3 = str(input("Selecione a posicao do Barco 3 (EX.: F3, B4, E5...)\
        Detalhes: Barco 3 tem dimensões (2x2)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
                
                tab_p1[localizacao_linha(b3)][localizacao_coluna(b3)] = 3
                tab_p1[localizacao_linha(b3)][localizacao_coluna(b3)+1] = 3
                tab_p1[localizacao_linha(b3)+1][localizacao_coluna(b3)] = 3
                tab_p1[localizacao_linha(b3)+1][localizacao_coluna(b3)+1] = 3
                
                print(tab_p1)
        
            else:
                pass
            
def posicionar_2():
    
    confirmacao = 'sim'

    b1 = str(input("Selecione a posicao do barco 1 (EX.: F3, B4, E5...)\
    Detalhes: Barco 1 tem dimensões (1x3)\
    Linhas vão de 1 - 9 e Colunas de A - I\n"))
    
    while (localizacao_coluna(b1) >= 7 or localizacao_coluna(b1) < 0) and\
    (list(b1)[0] == "h" or list(b1)[0] == "i"):
        
        print ("Reposicione o barco")
        
        b1 = str(input("Selecione a posicao do barco 1 (EX.: F3, B4, E5...)\
    Detalhes: Barco 1 tem dimensões (1x3)\
    Linhas vão de 1 - 9 e Colunas de A - I\n"))
    
    
    tab_p2[localizacao_linha(b1)][localizacao_coluna(b1)] = 1
    tab_p2[localizacao_linha(b1)][localizacao_coluna(b1)+1] = 1
    tab_p2[localizacao_linha(b1)][localizacao_coluna(b1)+2] = 1
    
    print(tab_p2)
    
    while confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
    
        confirmacao = str(input("Deseja alterar a posição?"))
        
        if confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
           
            tab_p2[localizacao_linha(b1)][localizacao_coluna(b1)] = 0
            tab_p2[localizacao_linha(b1)][localizacao_coluna(b1)+1] = 0
            tab_p2[localizacao_linha(b1)][localizacao_coluna(b1)+2] = 0
            
            b1 = str(input("Selecione a posicao do barco 1 (EX.: F3, B4, E5...)\
    Detalhes: Barco 1 tem dimensões (1x3)\
    Linhas vão de 1 - 9 e Colunas de A - I\n"))
            
            tab_p2[localizacao_linha(b1)][localizacao_coluna(b1)] = 1
            tab_p2[localizacao_linha(b1)][localizacao_coluna(b1)+1] = 1
            tab_p2[localizacao_linha(b1)][localizacao_coluna(b1)+2] = 1
            
            print(tab_p2)
        
        else:
        
            pass
        
    confirmacao = 'sim'

    b2 = str(input("Selecione a posicao do Barco 2 (EX.: F3, B4, E5...)\
    Detalhes: Barco 2 tem dimensões (4x1)\
    Linhas vão de 1 - 9 e Colunas de A - I\n"))
    
    while localizacao_linha(b2) > 5 or localizacao_linha(b2)<0 or \
            localizacao_coluna(b2) < 0 :
            
        print ("Reposicione o barco")
        
        b2 = str(input("Selecione a posicao do Barco 2 (EX.: F3, B4, E5...)\
    Detalhes: Barco 2 tem dimensões (4x1)\
    Linhas vão de 1 - 9 e Colunas de A - I\n"))
    
    tab_p2[localizacao_linha(b2)][localizacao_coluna(b2)] = 2
    tab_p2[localizacao_linha(b2)+1][localizacao_coluna(b2)] = 2
    tab_p2[localizacao_linha(b2)+2][localizacao_coluna(b2)] = 2
    tab_p2[localizacao_linha(b2)+3][localizacao_coluna(b2)] = 2
    
    print(tab_p2)
    
    while confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
    
        confirmacao = str(input("Deseja alterar a posição?"))
        
        if confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
        
            tab_p2[localizacao_linha(b2)][localizacao_coluna(b2)] = 0
            tab_p2[localizacao_linha(b2)+1][localizacao_coluna(b2)] = 0
            tab_p2[localizacao_linha(b2)+2][localizacao_coluna(b2)] = 0
            tab_p2[localizacao_linha(b2)+3][localizacao_coluna(b2)] = 0
            
            b2 = str(input("Selecione a posicao do Barco 2 (EX.: F3, B4, E5...)\
        Detalhes: Barco 2 tem dimensões (4x1)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
            while localizacao_linha(b2) > 5 or localizacao_linha(b2)<0 or \
            localizacao_coluna(b2) < 0 :
            
                print ("Reposicione o barco")
        
                b2 = str(input("Selecione a posicao do Barco 2 (EX.: F3, B4, E5...)\
        Detalhes: Barco 2 tem dimensões (4x1)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
            
            tab_p2[localizacao_linha(b2)][localizacao_coluna(b2)] = 2
            tab_p2[localizacao_linha(b2)+1][localizacao_coluna(b2)] = 2
            tab_p2[localizacao_linha(b2)+2][localizacao_coluna(b2)] = 2
            tab_p2[localizacao_linha(b2)+3][localizacao_coluna(b2)] = 2
                
            print(tab_p2)
        
        else:
            pass
        
        b3 = str(input("Selecione a posicao do Barco 3 (EX.: F3, B4, E5...)\
        Detalhes: Barco 3 tem dimensões (2x2)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
        while (localizacao_coluna(b3) > 7 or localizacao_coluna(b3) < 0) and\
    (list(b1)[0] == "i"):
        
            print ("Reposicione o barco")
            
            b3 = str(input("Selecione a posicao do Barco 3 (EX.: F3, B4, E5...)\
        Detalhes: Barco 3 tem dimensões (2x2)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
        tab_p2[localizacao_linha(b3)][localizacao_coluna(b3)] = 3
        tab_p2[localizacao_linha(b3)][localizacao_coluna(b3)+1] = 3
        tab_p2[localizacao_linha(b3)+1][localizacao_coluna(b3)] = 3
        tab_p2[localizacao_linha(b3)+1][localizacao_coluna(b3)+1] = 3
        
        print (tab_p2)
        
        confirmacao = 's'
        
        while confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
    
            confirmacao = str(input("Deseja alterar a posição?"))
        
            if confirmacao == 'sim' or confirmacao == 'Sim' or confirmacao == 's':
        
                tab_p2[localizacao_linha(b3)][localizacao_coluna(b3)] = 0
                tab_p2[localizacao_linha(b3)][localizacao_coluna(b3)+1] = 0
                tab_p2[localizacao_linha(b3)+1][localizacao_coluna(b3)] = 0
                tab_p2[localizacao_linha(b3)+1][localizacao_coluna(b3)+1] = 0
                
                b3 = str(input("Selecione a posicao do Barco 3 (EX.: F3, B4, E5...)\
        Detalhes: Barco 3 tem dimensões (2x2)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
                while (localizacao_coluna(b3) > 7 or localizacao_coluna(b3) < 0) and\
    (list(b1)[0] == "i"):
        
                    print ("Reposicione o barco")
        
                    b3 = str(input("Selecione a posicao do Barco 3 (EX.: F3, B4, E5...)\
        Detalhes: Barco 3 tem dimensões (2x2)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
                
                tab_p2[localizacao_linha(b3)][localizacao_coluna(b3)] = 3
                tab_p2[localizacao_linha(b3)][localizacao_coluna(b3)+1] = 3
                tab_p2[localizacao_linha(b3)+1][localizacao_coluna(b3)] = 3
                tab_p2[localizacao_linha(b3)+1][localizacao_coluna(b3)+1] = 3
                
                print(tab_p1)
        
            else:
                pass
            


def jogo():
    #São 11 possibilidades de ataque
     while p1total < 49 or p2total < 49:  
         
        print("Vez do JOGADOR 1 -- TABULEIRO 1 ABAIXO") 
        print(tab2_p1)
             
        x = str(input("Selecione a posição de ataque (EX.: F3, B4, E5...)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
        while (localizacao_coluna(x) < 0 or localizacao_coluna(x)>8) or \
        (localizacao_linha(x) < 0 or localizacao_linha(x)>8):
           
           x = str(input("Selecione novamente a posição de ataque (EX.: F3, B4, E5...)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
        #tabela onde o P2 colocou os barcos
        if tab_p2[localizacao_linha(x)][localizacao_coluna(x)] == 1:
            
        #Tabela onde o p1 está atacando
            tab2_p1[localizacao_linha(x)][localizacao_coluna(x)] = 1
            global pontuacao1p1
            pontuacao1p1 = pontuacao1p1 + 1
            if pontuacao1p1 == 3:
                pontuacao1p1 = 0
                pontuacao1p1 += 10
                print ("Você ganhou 10 pontos por destruir o barco 1 ")
            else:
                print ("ALVO ATINGIDO NA POSIÇÃO",x)
        elif tab_p2[localizacao_linha(x)][localizacao_coluna(x)] == 2:
            
        #Tabela onde o p1 está atacando
            tab2_p1[localizacao_linha(x)][localizacao_coluna(x)] = 2
            global pontuacao2p1
            pontuacao2p1 = pontuacao2p1 + 1
            if pontuacao2p1 == 4:
                pontuacao2p1 = 0
                pontuacao2p1 += 20
                print ("Você ganhou 20 pontos por destruir o barco 2 ")
            else:
                print ("ALVO ATINGIDO NA POSIÇÃO",x)       
        elif tab_p2[localizacao_linha(x)][localizacao_coluna(x)] == 3:
            
        #Tabela onde o p1 está atacando
            tab2_p1[localizacao_linha(x)][localizacao_coluna(x)] = 3
            global pontuacao3p1
            pontuacao3p1 = pontuacao3p1 + 1
            if pontuacao3p1 == 4:
                pontuacao3p1 = 0
                pontuacao3p1 += 20
                print ("Você ganhou 20 pontos por destruir o barco 3 ")
            else:
                print ("ALVO ATINGIDO NA POSIÇÃO",x)    
            
        else:
            tab2_p1[localizacao_linha(x)][localizacao_coluna(x)] = 7
            print ("ÁGUA!!!")
            
        time.sleep(2)
        
        print(tab2_p1)
        
        time.sleep(2)
        
        print("Vez do JOGADOR 2 -- TABULEIRO 2 ABAIXO") 
        print(tab2_p2)
        
        x = str(input("Selecione a posição de ataque (EX.: F3, B4, E5...)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
        while (localizacao_coluna(x) < 0 or localizacao_coluna(x)>8) or \
        (localizacao_linha(x) < 0 or localizacao_linha(x)>8):
            
             x = str(input("Selecione novamente a posição de ataque (EX.: F3, B4, E5...)\
        Linhas vão de 1 - 9 e Colunas de A - I\n"))
        
        if tab_p1[localizacao_linha(x)][localizacao_coluna(x)] == 1:
            
            tab2_p2[localizacao_linha(x)][localizacao_coluna(x)] = 1
            global pontuacao1p2
            pontuacao1p2 = pontuacao1p2 + 1
            if pontuacao1p2 == 3:
                pontuacao1p2 = 0
                pontuacao1p2 += 10
                print ("Você ganhou 10 pontos por destruir o barco 1 ")
            else:
                print ("ALVO ATINGIDO NA POSIÇÃO",x)                
        elif tab_p1[localizacao_linha(x)][localizacao_coluna(x)] == 2:
            
            tab2_p2[localizacao_linha(x)][localizacao_coluna(x)] = 2
            global pontuacao2p2
            pontuacao2p2 = pontuacao2p2 + 1
            if pontuacao2p2 == 4:
                pontuacao2p2 = 0
                pontuacao2p2 += 20
                print ("Você ganhou 20 pontos por destruir o barco 2 ")
            else:
                print ("ALVO ATINGIDO NA POSIÇÃO",x)
        elif tab_p1[localizacao_linha(x)][localizacao_coluna(x)] == 3:
            
            tab2_p2[localizacao_linha(x)][localizacao_coluna(x)] =  3
            global pontuacao3p2
            pontuacao3p2 = pontuacao3p2 + 1
            if pontuacao3p2 == 4:
                pontuacao3p2 = 0
                pontuacao3p2 += 20
                print ("Você ganhou 20 pontos por destruir o barco 1 ")            
            else:
                print ("ALVO ATINGIDO NA POSIÇÃO",x)
            
            
        else:
            tab2_p2[localizacao_linha(x)][localizacao_coluna(x)] = 7  
            print ("ÁGUA!!!")
            
        time.sleep(2)
        
        print(tab2_p2)
        time.sleep(2)
    
    
print("Passe o comuputador para o Jogador 1 posicionar seus BARCOS")        
print(tab_p1)
posicionar_1()  
print("Agora passe o comuputador para o Jogador 2 posicionar seus BARCOS")  
print(tab_p2)
posicionar_2()
    
print("Agora vamos comecar a jogar! Passe o computador para o jogador 1 começar!")

jogo()
    
    