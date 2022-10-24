import pgzrun
import random

# Definindo variáveis globais
WIDTH = 500
HEIGHT = 500
GAME_OVER = False

# Definindo variáveis do nosso personagem
nave = Actor('nave.png', (WIDTH / 2, HEIGHT / 2))
asteroide_1 = Actor('t_asteroid_1.png',(WIDTH / 2, -100))
asteroide_2 = Actor('t_asteroid_2.png',(WIDTH / 40, -150))
asteroide_3 = Actor('t_asteroid_3.png',(WIDTH / 40, -150))

# Função para desenhar a "tela inicial" do jogo
def draw():
    # Por boa prática, limpa a tela do jogo caso tenha lixo desenhado
    screen.clear()
    
    if GAME_OVER == False:
        
        # Preenche a tela de branco
        screen.fill( (255, 255, 255) )
        
        # Desenha a nave
        nave.draw()
        
        # Desenha o asteroide 1 e 2
        asteroide_1.draw()
        asteroide_2.draw()
        asteroide_3.draw()
        
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
    # Movimentação do asteroide 1,2 e 3
    asteroide_1.y += 3
    asteroide_1.angle += 2
    
    asteroide_2.y += 2
    asteroide_2.angle += 2
    
    asteroide_3.y += 6
    asteroide_3.x += 5
    asteroide_3.angle += 10
    
    if asteroide_1.y > (HEIGHT + 80): 
        asteroide_1.x = random.randint (0, WIDTH)
        asteroide_1.y = -100   
        
    if asteroide_2.y > (HEIGHT + 80): 
        asteroide_2.x = random.randint (0, WIDTH)
        
    if asteroide_3.y > (HEIGHT + 80): 
        asteroide_3.x = -20
        asteroide_3.y = random.randint (-500, WIDTH / 2)








pgzrun.go()






