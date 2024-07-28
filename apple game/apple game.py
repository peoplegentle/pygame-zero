import pgzrun
from random import randint  # 이것은 랜덤한 값을 가져옴

apple = Actor("apple.png")      # Actor를 쓰면 images폴더의 이미지를 가지고옴
click = 0                   # click횟수
timer = 1                   # 1초를 세는 거
game_over = False           # 게임 종료 상태 저장


def draw():                 # draw는 화면에 그림을 그림
    screen.clear()
    apple.draw()

    if(game_over) :         # 게임이 끝난 경우
        if(timer<0) :       # 시간 초과
            screen.draw.text("Time out", center=(400, 300), fontsize=100)
        elif(click>=20) :   # 성공
            screen.draw.text("Clear", center=(400, 300), fontsize=100)
        else :              # 실패
            screen.draw.text("Fail", center=(400, 300), fontsize=100)
        screen.draw.text("Retry : Enter key", center=(400, 350), fontsize=50)


def place_apple():
    apple.x = randint(10,800)       # randint(시작, 끝) 함수는 시작 부터 끝 사이에 있는 정수 한개를 리턴
    apple.y = randint(10,600)       # 10부터 600 사이의 정수 한개를 리턴 받아 y 좌표를 변경


def on_mouse_down(pos):             # 마우스를 클릭했을때 동작한다, pos는 마우스 클릭 좌표

    global click                    # 함수 밖에서 만든 변수를 함수 안에서 수정 하려면 global을 꼭 써야함
    global timer, game_over

    if(not(game_over)) :                # not을 붙여 결과를 뒤집음, 즉 게임이 진행 중
        if(apple.collidepoint(pos)):    # collidepoint() 함수는 겹치는지 결과를 True, False로 알려줌, 
                                        # 겹치는대상.collidepoint(겹칠거) 이렇게 사용
                                        # apple이랑 마우스 클릭한 곳이 겹치는지 확인 
            print("Good shot!")         # 탭키를 한 문은 탭키를 또한다
            click = click+1
            print(click)
            place_apple()
            if(click>=20):
                print("clear")
                game_over = True
                # quit()
            timer = 1
        else:
            print("You missed")     
            game_over = True
            # quit()                      # quit()은 프로그램을 종료한다


def update():                           # Update() 함수는 게임 진행 동안 계속 실행 되는 함수
    global timer, game_over, click

    if(not(game_over)) :
        if(click>0) :                   # 처음 클릭한 후 부터 1초 카운트
            timer -= 1/60               # timer = timer - (1 / 60) 와 같은 뜻, 0.1초씩 줄어듬
        
        if(timer<0) :
            print("Time out")
            game_over = True
            # quit()
        print(timer)
    else :
        if(keyboard.RETURN) :
            game_over = False
            click = 0
            timer = 1


place_apple()
pgzrun.go() # import pgzrun 에서 pgzrun.go()사이에 함수를 만듬
