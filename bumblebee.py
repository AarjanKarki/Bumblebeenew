import pgzrun, random
HEIGHT=500
WIDTH=500
bee=Actor('bee')
bee.pos=100,100
flower=Actor('flower')
flower.pos=250,250
score=0
gameover=False

def draw():
    screen.blit('background',(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text('Score:'+str(score),color='black',topleft=(10,10))
    if gameover:
        screen.fill('red')
        screen.draw.text('Times up! Your final score:'+str(score),midtop=(WIDTH/2,10),
        fontsize=40, color='black')
def place_flower():
    flower.x=random.randint(70,WIDTH-70)
    flower.y=random.randint(70,HEIGHT-70)

def time_up():
    global gameover
    gameover = True
def update():
    global score
    if keyboard.left:
        bee.x-=2+score/10
    if keyboard.right:
        bee.x+=2+score/10
    if keyboard.up:
        bee.y-=2+score/10
    if keyboard.down:
        bee.y+=2+score/10
    if bee.colliderect(flower):
        score=score+10
        place_flower()
    
    

clock.schedule(time_up,10.0)







pgzrun.go()

