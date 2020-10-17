import pygame as p

p.init()  #라이브러리 초기화
white = (255,255,255)   #rgb빛의 3원색
size = (600,800)    #가로,세로
sc = p.display.set_mode(size)   #해상도크기설정
p.display.set_caption("게임판")    #게임창제목 display:해상도설정
playing = True

#이미지 추가
image = p.image.load("a.png")
i = p.image.load("qwertyuiop.png")
#음악추가

p.mixer.music.load("ss.mp3")    #음악 불러오는 역할
p.mixer.music.play(0)   # (0) 무한재생, (-1) 한번만재생

while playing: #while True - 계속 반복하기
    

    for event in p.event.get():  #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT:    #게임창x버튼을누르면
            playing = False
            p.quit()    #게임창 종료
            
            quit()  #shell 창 종료
            
    sc.fill(white)  #배경화면색 설정

    sc.blit(image,(250,350))

    sc.blit(i,(-5,715))
    
    p.display.flip()    #화면업데이트
