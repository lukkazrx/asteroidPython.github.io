import pgzrun

# Definindo variáveis globais
WIDTH = 300
HEIGHT = 300
GAME_OVER = False

# Definindo variáveis do nosso personagem
nave = Actor('nave.png', (WIDTH / 2, HEIGHT / 2))

# Função para desenhar a "tela inicial" do jogo
def draw():
    # Por boa prática, limpa a tela do jogo caso tenha lixo desenhado
    screen.clear()
    
    if GAME_OVER == False:
        
        # Preenche a tela de branco
        screen.fill( (255, 255, 255) )
        
        # Desenha a nave
        nave.draw()
        
    elif GAME_OVER == True:
        game_over()

def game_over():
    # Limpa a tela
    screen.clear()
    
    # Escreve alguma mensagem de GAME OVER
    screen.draw.text('GAME OVER!!!!!!', (70, 150))
    
# Função chamada 1 vez por frame
def update():
    
    # Retorna o angulo da nave para 0 graus
    nave.angle = 0
    
    # Movimentação da nave
    if keyboard.left and GAME_OVER == False:
        nave.x  -= 3
        nave.angle = 15
    elif keyboard.right and GAME_OVER == False:
        nave.x += 3
        nave.angle = 345
        
    if keyboard.up and GAME_OVER == False:
        nave.y -= 3
    elif keyboard.down and GAME_OVER == False:
        nave.y += 3

pgzrun.go()






