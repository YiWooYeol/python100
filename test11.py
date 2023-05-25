import pygame
import math

pygame.init()

# 화면 크기 설정
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# 삼각형 좌표 초기값 설정
point_1 = (295, 581)
point_2 = (647, 589)
point_3 = (462, 324)

# 삼각형 좌표 변경 함수
def update_points():
    global point_1, point_2, point_3

    # 마우스 이벤트 처리
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()

        if point_1[0] - 20 <= mouse_pos[0] <= point_1[0] + 20 and point_1[1] - 20 <= mouse_pos[1] <= point_1[1] + 20:
            point_1 = mouse_pos
        elif point_2[0] - 20 <= mouse_pos[0] <= point_2[0] + 20 and point_2[1] - 20 <= mouse_pos[1] <= point_2[1] + 20:
            point_2 = mouse_pos
        elif point_3[0] - 20 <= mouse_pos[0] <= point_3[0] + 20 and point_3[1] - 20 <= mouse_pos[1] <= point_3[1] + 20:
            point_3 = mouse_pos

    # 삼각형 그리기
    pygame.draw.line(screen, (0, 0, 0), point_1, point_2)
    pygame.draw.line(screen, (0, 0, 0), point_2, point_3)
    pygame.draw.line(screen, (0, 0, 0), point_3, point_1)
    
    # 중선 그리기
    
    midpoint = get_midpoints(point_1,point_2,point_3)
    center = get_center(point_3, midpoint[0],point_1, midpoint[1])
    pygame.draw.line(screen, (0, 0, 0), point_3, midpoint[0])
    pygame.draw.line(screen, (0, 0, 0), point_1, midpoint[1])
    pygame.draw.line(screen, (0, 0, 0), point_2, midpoint[2])
    pygame.draw.circle(screen, (255,0,0), center, 5)
    pygame.draw.circle(screen, (255,0,0), midpoint[0], 5)
    pygame.draw.circle(screen, (255,0,0), midpoint[1], 5)
    pygame.draw.circle(screen, (255,0,0), midpoint[2], 5)
    
    # 이부분부터 세 개의 점을 받아서 내심을 구하고 원을 그리는 부분코드삽입
    
def get_center(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    if x1 == x2:
        a2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - a2 * x3
        x = x1
        y = a2 * x + b2
    elif x3 == x4:
        a1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - a1 * x1
        x = x3
        y = a1 * x + b1
    else:
        a1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - a1 * x1
        a2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - a2 * x3
        if a1 == a2:
            return None
        x = (b2 - b1) / (a1 - a2)
        y = a1 * x + b1
    if (x1 <= x <= x2 or x2 <= x <= x1) and (y1 <= y <= y2 or y2 <= y <= y1) and (x3 <= x <= x4 or x4 <= x <= x3) and (y3 <= y <= y4 or y4 <= y <= y3):
        return (x, y)
    else:
        return None


def get_midpoints(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    midpoint1_x = (x1 + x2) / 2
    midpoint1_y = (y1 + y2) / 2
    midpoint2_x = (x2 + x3) / 2
    midpoint2_y = (y2 + y3) / 2
    midpoint3_x = (x3 + x1) / 2
    midpoint3_y = (y3 + y1) / 2
    return ((midpoint1_x, midpoint1_y), (midpoint2_x, midpoint2_y), (midpoint3_x, midpoint3_y))

def draw_line(a,b,c):
    # 원의 중심과 반지름을 구합니다.
   # center = get_center(a,b,c)
    midpoint = get_midpoints(a,b,c)
    
    # 창 제목 설정
    pygame.display.set_caption("삼각형의 무게중심")
    
    # 색상 설정
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # 프로그램 실행 여부
    done = False
    
    # 프로그램이 실행되는 동안 반복문 실행
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # 배경색 설정
        screen.fill(WHITE)
        
        # 세 점 그리기
        pygame.draw.circle(screen, (255,0,0), a, 5)
        pygame.draw.circle(screen, (255,0,0), b, 5)
        pygame.draw.circle(screen, (255,0,0), c, 5)
        
        
        # 세 중선 그리기
        pygame.draw.circle(screen, (0,0,255), center, int(radius), 5)
        
        # 화면 업데이트
        pygame.display.flip()
    
    # 게임 종료
    pygame.quit()


   
    
# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 배경 색상 설정
    screen.fill((255, 255, 255))

    # 세 개의 점 찍기
    for i in range(3):
        pygame.draw.circle(screen, (255, 0, 0), eval(f"point_{i+1}"), 5) 
    
    # 삼각형 좌표 변경 함수 호출
    update_points()

    # 화면 업데이트
    pygame.display.update()