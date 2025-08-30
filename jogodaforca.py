import random
import os
from time import sleep

texto = """
açucena advogado afta
alambique alcachofra algarismo
almanaque almofariz almoxarife
alquimia altivez alvíssaras
amendoim amnésia amplificar
ampulheta ansioso aplaudir
ascensão asterisco atlas
balacobaco bandolim barulhento
basquetebol batráquio beneficente
berimbau bicarbonato brusquidão
bugiganga bumerangue burocracia
caatinga caboclo cacareco
cacto cadarço cãibra
calibrado camuflagem candelabro
cassetete catalisador catequizar
cérebro chamariz cicatriz
cleptomaníaco coincidência companhia
condescender consciente crepúsculo
cronologia deglutir depredar
destruído diapasão digladiar
diretriz dobradiça ecossistema
embaixador empecilho entretido
entrevista envernizar enxaqueca
enxerido escangalhado escaravelho
escombro esculacho esfirra
espinafre esplendor estapafúrdio
estetoscópio exceção excêntrico
excepcional faniquito fascículo
flexível frustrado gargantilha
glândula glicerina glorioso
gnomo grampeador hamster
helicóptero hemisfério herdeiro
hermético hierárquico hieróglifo
hipocrisia humanizar idolatrada
imbróglio inexorável inflamado
influência insignificância interruptor
invertebrado iogurte irascível
lantejoula licenciado losango
madrasta magnético manteigueira
marimbondo mesclar meteorologia
mexerico micróbio microfone
microscópio milionário mordaz
nebulizador oscilação paralisado
pedágio pernóstico perturbar
piripaque plissado pneumático
pneumonia poliomielite potiguar
prescindir presságio privilégio
prodígio prostração prurido
psicanálise psicólogo quadriciclo
quádruplo quinquilharia reciclar
reflorescer reivindicar rescindir
retrógrado retrovisor ritmo
seborreia sensatez serelepe
serpentina simplório simulacro
sincrônico sobrevivente subsídio
supérfluo suscetível termômetro
torácico travesseiro trilogia
universidade vangloriar vaporizador
ventilador xilindró ziguezague
ziquizira zodíaco zumbido"""

palavras = texto.split()

def sorteadorPalavra(palavras):
    palavra = random.choice(palavras)
    return palavra

def telaForca(palavra, chances=6):
    letras_palavra = ['_'] * len(palavra)
    tentativas = []  
    erros_boneco = ['o', '/', '|', '\\', '/', '\\']

    running = True
    while running:        
        erros = len(tentativas)
        cabeca = erros_boneco[0] if erros >= 1 else ' '
        braco_esq = erros_boneco[1] if erros >= 2 else ' '
        tronco = erros_boneco[2] if erros >= 3 else ' '
        braco_dir = erros_boneco[3] if erros >= 4 else ' '
        perna_esq = erros_boneco[4] if erros >= 5 else ' '
        perna_dir = erros_boneco[5] if erros >= 6 else ' '
        print(f'''\tJogo da forca
Chances: {chances}
________
|       |
|       {cabeca}
|      {braco_esq}{tronco}{braco_dir}
|      {perna_esq} {perna_dir}
|
|  {''.join(letras_palavra)}
Tamanho da palavra: {len(palavra)}
Tentativas: {' '.join(tentativas)}''')
        
        if chances == 0:
            print(f'\nA palavra era {palavra}')
            break

        if ''.join(letras_palavra) == palavra:
            print('\nParabéns você acertou!')
            break

        letra = input("Insira uma letra: ").lower()
        os.system('cls')
        if len(letra) != 1 or not letra.isalpha():
            continue

        if letra in palavra:
            for i, char in enumerate(palavra):
                if char == letra:
                    letras_palavra[i] = letra
        else:
            tentativas.append(letra)
            chances -= 1

    sleep(3)
    os.system('cls')
    menu()

def menu():
    op = input(''' Deseja jogar Forca?
        1. Sim
        2. Não
-> ''')
    match op:
        case '1':
            os.system('cls')
            telaForca(sorteadorPalavra(palavras))
        case '2':
            os.system('cls')
            print('Saindo...')
            exit()
        case _:
            os.system('cls')
            menu()

if __name__ == '__main__':
    menu()
