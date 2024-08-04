import random

animal = ['abelha','borboleta','camelo','cachorro','cavalo','coelho','formiga','girafa','joaninha','lobo','morcego','peixe','rato','tatu','urso']
comida = ['abacaxi','cebola','chocolate','fruta','laranja','bolo','ovo','sorvete', 'castanhas','pirulito', 'marmelada', 'caramelo', 'pistache']
objeto = ['serra','anel','barco','bola','bota', 'caixote','telefone','telhado','trem','vaso','cama','caneta','carro','celular','chaves','guitarra','cinto','cortina','desenho','escada','esmeralda','ferro','flor','mesa','navio','mamadeira','maca','madeira','parede','pedra','pipa','rede','quadro','roupa','sabao','saco','livro','geladeira','janela']
lugar = ['biblioteca','escola','festa','hotel','igreja','jardim','mar','rio','casa','dentista','praia','lagoa','fazenda', 'montanha', 'serra']

def game():    
    print(' ')
    lista = random.choice([animal, objeto, lugar, comida])
    if lista == animal:
        print('Dica: animal')
    if lista == objeto:
        print('Dica: objeto')
    if lista == lugar:
        print('Dica: lugar')
    if lista == comida:
        print('Dica: comida')
    palavra = random.choice(lista)
    oculto = '_' * len(palavra)  
    print('forca:', oculto)   
    vida = 6
    while '_' in oculto and vida > 0:
        if vida == 6:
            print('''      +---+
      |   |
          |
          |
          |
          |
    =========''')
        if vida == 5:
            print('''      +---+
      |   |
      O   |
          |
          |
          |
    =========''')
        if vida == 4:
            print('''      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''')
        if vida == 3:
            print('''      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''')
        if vida == 2:
            print('''      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''')
        if vida == 1:
            print('''      +---+
      |   |
      O   |
     /|\  |
       \  |
          |
    =========''')
        if vida == 0:
            print('''      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''')   
        print('')  
        letra = str(input("Digite uma letra:")).lower()     
        print('')    
        letra = letra.strip()
        letra = letra[0]

        if letra in palavra:
            new_oculto = list(oculto)
            for i, char in enumerate(palavra):
                if char == letra:
                    new_oculto[i] = letra
            oculto = ''.join(new_oculto)
            print('') 
            print('forca:', oculto)
            print(' ')
        else:
            print('''
Não tem essa letra na palavra
            ''')
            print('') 
            print('forca:', oculto)
            print(' ')
            vida = vida - 1

    if vida > 0:
        print('Parabéns, você acertou a palavra!!')
        print(' ')
    else:
        print('A palavra era {}. Você falhou em descobrir a palavra.'.format(palavra.upper()))
        print(' ') 
game()
again = input('Digite (Enter) para jogar')
print(' ')
if again == '':
    game()   
