import pygame as p#파이게임생성

p.init  #라이브러리 초기화
white = (255,255,255)   #rgb빛의 3원색
size = (900,500)    #가로,세로
sc = p.display.set_mode(size)   #해상도크기설정
p.display.set_caption("게임판")    #게임창제목 display:해상도설정

playing = True


while playing: #while True - 계속 반복하기

    for event in p.event.get():  #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT:    #게임창x버튼을누르면
            playing = False
            p.quit()    #게임창 종료
            quit()  #shell 창 종료
    sc.fill(white)  #배경화면색 설정
    p.display.flip()    #화면업데이트
