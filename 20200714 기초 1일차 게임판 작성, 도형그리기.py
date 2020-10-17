import pygame as p

p.init() # 라이브러리 초기화

# 빛의 3원색 RGB
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Blue = (0,0,255)
Green = (0,255,0)

#해상도
size = [400,400]
screen = p.display.set_mode(size)

#창제목
p.display.set_caption("Game Title")


done = False
clock = p.time.Clock() # FPS = 초당 프레임  

while not done: 

    clock.tick(10) # 1초에 10번 사진을 찍는다
    
    for event in p.event.get(): #우리가 누르는 버튼 체크 
        if event.type == p.QUIT: #만일 창 옆에 x버튼을 누르면 
            done = True # 계속반복 멈춤

    
    screen.fill(Green)

    p.draw.rect(screen,Red,[75,175,50,50],2) #사각형 [x좌표,y좌표,가로,세로],선두게 
    p.draw.polygon(screen,Black,[[30,150],[125,100],[220,150]],1)
    #                           [꼭지점1],[꼭지점2].[꼭지점3],선두께 - 



    p.display.flip() # 화면 업데이트 


    

    













