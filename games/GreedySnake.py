# pygame游戏库，sys操控python运行的环境
import pygame, sys, random
# 这个模块包含所有pygame所使用的常亮
from pygame.locals import *
from games.feiji.setting import *

# 1,定义颜色变量
# 0-255  0黑色  255白色
redColor = pygame.Color(255, 0, 0)
# 背景为黑色
blackColor = pygame.Color(0, 0, 0)
# 贪吃蛇为白色
whiteColor = pygame.Color(255, 255, 255)
# 界面大小
bg_size = width, height = 640, 480


# 定义游戏结束的函数
def gameover():
    pygame.quit()


# 定义main函数--》定义我们的入口函数
def main():
    # 初始化pygame
    pygame.init()
    # 定义一个变量来控制速度
    fpsClock = pygame.time.Clock()
    # 创建pygame显示层，创建一个界面
    playsurface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('贪吃蛇')
    background = pygame.image.load("images/background_GreedySnake.jpg").convert_alpha()
    # 初始化变量
    # 贪吃蛇初始坐标位置   （先以100,100为基准）
    snakePosition = [100, 100]
    # 初始化贪吃蛇的长度列表中有个元素就代表有几段身体
    snakeBody = [[100, 100], [80, 100], [60, 100]]
    # 初始化目标方向额位置
    targetPosition = [300, 300]
    # 目标方块的标记 目的：判断是否吃掉了这个目标方块1 就是没有吃 0就是吃掉
    targetflag = 1
    # 初始化方向   --》往右
    direction = 'right'
    # 定义一个方向变量（人为控制  按键）
    changeDirection = direction
    # 游戏结束画面
    gameover_font = pygame.font.SysFont("arial", 35)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()
    # 标志是否暂停游戏
    paused = False
    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = pause_nor_image
    running = True
    while running:

        for event in pygame.event.get():  # 从队列中获取事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = pause_nor_image
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    changeDirection = 'right'
                if event.key == K_a:
                    changeDirection = 'left'
                if event.key == K_w:
                    changeDirection = 'up'
                if event.key == K_s:
                    changeDirection = 'down'
                    # 对应键盘上的esc文件
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        if paused:
            # 暂停
            again_rect.left, again_rect.top = \
                (width - again_rect.width) // 2, 50
            playsurface.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                (width - again_rect.width) // 2, \
                again_rect.bottom + 10
            playsurface.blit(gameover_image, gameover_rect)
            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and \
                        again_rect.top < pos[1] < again_rect.bottom:
                    # 调用main函数，重新开始游戏
                    main()
                # 如果用户点击“结束游戏”
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                        gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    sys.exit()
        else:
            pass

        # 确定方向
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        if not paused:
            # 根据方向移动蛇头
            if direction == 'right':
                snakePosition[0] += 20
            if direction == 'left':
                snakePosition[0] -= 20
            if direction == 'up':
                snakePosition[1] -= 20
            if direction == 'down':
                snakePosition[1] += 20
            # 增加蛇的长度
            snakeBody.insert(0, list(snakePosition))
            # 如果贪吃蛇和目标方块的位置重合
            if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
                targetflag = 0
            else:
                temp = snakeBody.pop()
                pygame.draw.rect(playsurface, blackColor, Rect(temp[0], temp[1], 20, 20))
            if targetflag == 0:
                x = random.randrange(1, 32)
                y = random.randrange(1, 24)
                targetPosition = [int(x * 20), int(y * 20)]
                targetflag = 1
            # 填充背景颜色
            playsurface.blit(background, (0, 0))
            for position in snakeBody:
                # 第一个参数serface指定一个serface编辑区，在这个区域内绘制
                # 第二个参数color：颜色
                # 第三个参数:rect:返回一个矩形(xy),(width,height)
                # 第四个参数：width：表示线条的粗细  width0填充  实心
                # 化蛇
                pygame.draw.rect(playsurface, redColor, Rect(position[0], position[1], 20, 20))
                pygame.draw.rect(playsurface, whiteColor, Rect(targetPosition[0], targetPosition[1], 20, 20))

        # 判断是否游戏结束
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            running = False
            gameover()
        elif snakePosition[1] > 460 or snakePosition[1] < 0:
            running = False
            gameover()
        elif snakeBody.count(snakePosition) > 1:
            running = False
            gameover()

        # 绘制暂停按钮
        pygame.draw.rect(playsurface, blackColor, paused_rect)
        playsurface.blit(paused_image, paused_rect)
        # 更新显示到屏幕表面
        pygame.display.flip()
        # 控制游戏速度
        fpsClock.tick(10)


#   启动入口函数


if __name__ == '__main__':
    main()
