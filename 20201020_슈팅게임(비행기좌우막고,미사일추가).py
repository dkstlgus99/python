import pygame as p#파이게임생성

p.init  #라이브러리 초기화
white = (255,255,255)   #rgb빛의 3원색
size = (500,800)    #가로,세로
sc = p.display.set_mode(size)   #해상도크기설정
p.display.set_caption("슈팅게임")    #게임창제목 display:해상도설정
playing = True
#비행기 이미지 변수에 넣기
plane = p.image.load("우주선.png")
p_rect = plane.get_rect(left = 200 , top = 700)
p_x = 0
#배경 변수넣기
bg = p.image.load("우주.png")
#미사일 변수 넣기
bullet = p.image.load("pow.png")
b_list =  []
#미사일 종류 변수


while playing: #while True - 계속 반복하기

    for event in p.event.get():  #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT:    #게임창x버튼을누르면
            playing = False
            p.quit()    #게임창 종료
            quit()  #shell 창 종료
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                p_x = -5
            if event.key == p.K_RIGHT:
                p_x = 5
            if event.key == p.K_SPACE:
                b_rect = bullet.get_rect(left = p_rect.left + 38 , top = p_rect.top)
                b_list.append(b_rect)
                
                
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                p_x = 0
            if event.key == p.K_RIGHT:
                p_x = 0







            

    p_rect.left += p_x    
    sc.fill(white)

    #배경화면색 설정
    sc.blit(bg,(0,0))
    #비행기 화면 업로드
    sc.blit(plane,(p_rect))
    if p_rect.left <= -100: #비행기가 오른쪽벽에 닿으면
        p_rect.left = 499 #비행기 좌표를 499으로 위치시키기 
    if p_rect.left >= 500:
        p_rect.left = -99  #비행기 좌표를 -99으로 위치시키기 

    #미사일 화면 업로드
    for b_rect in b_list:
        sc.blit(bullet,b_rect)  #미사일 화면 업로드
        b_rect.top -= 10
        if b_rect.top <= 0: #총알이 위쪽벽에 닿으면
            b_list.remove(b_rect)

    
    p.display.flip()    #화면업데이트
