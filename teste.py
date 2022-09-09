# importa a biblioteca principal do framework
import pgzrun

# definindo constantes pertinentes ao tamanho da tela
WIDTH = 450
HEIGHT = 300

# Variaveis pertinentes a nosso sprite
sprite = Actor('troll.png')

# Define posição inicial do sprite
sprite.pos = 0,100

# Função de desenho inicial (tela inicial do jogo)
def draw ():
    # Limpa a tela
    screen.clear()
    # Pinta a tela 
    screen.fill( (255,0,0) )
    # Desenha nosso sprite 
    sprite.draw()


# Função chamada X vezes por segundo, baseado nos frames
def update():
    sprite.left += 2
    





# mandatório ser a última linha de código
pgzrun.go()