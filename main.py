import sys
import pygame
from goal_posts import GoalPost
import ball
import time

from players import Players


def show_score(which_player):
    if which_player == player1:
        score = font.render("Score : " + str(ball.player1.score_value), True, (255, 255, 255))
        screen.blit(score, (10, 10))
    else:
        score = font.render("Score : " + str(ball.player2.score_value), True, (255, 255, 255))
        screen.blit(score, (1050, 10))


def center_player2():
    if game_ball.is_moving_left:
        if player2.rectangle.centery < 390:
            player2.is_moving_down = True
            ball.player2.is_moving_down = True
            player2.is_moving_up = False
            ball.player2.is_moving_up = False
        if player2.rectangle.centery > 390:
            player2.is_moving_down = False
            ball.player2.is_moving_down = False
            player2.is_moving_up = True
            ball.player2.is_moving_up = True
        if player2.rectangle.centery == 390:
            player2.is_moving_down = False
            ball.player2.is_moving_down = False
            player2.is_moving_up = False
            ball.player2.is_moving_up = False


game_loop = True
while game_loop:
    running = True
    intro = True
    outro = True



    pygame.init()
    bot_level = "initial state"
    clock = pygame.time.Clock()
    timer = 180

    dt = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    screen = pygame.display.set_mode((1200, 780))
    pygame.display.set_caption("MY GAME")

    goal_post1 = GoalPost("left", "top")
    goal_post2 = GoalPost("left", "bottom")
    goal_post3 = GoalPost("right", "bottom")
    goal_post4 = GoalPost("right", "top")
    player1 = Players("left")
    player2 = Players("right")
    game_ball = ball.TheBall()

    while intro:
        screen.fill((0, 0, 255))
        easy_one = pygame.Surface((300, 100))
        easy_one_rectangle = easy_one.get_rect()
        easy_one_rectangle.left = 440
        easy_one_rectangle.top = 150
        easy_one.fill((255, 0, 0))
        screen.blit(easy_one, (easy_one_rectangle.left, easy_one_rectangle.top))
        txt = font.render("Easy", True, (0, 0, 139))
        screen.blit(txt, (550, 190))
        hard_one = pygame.Surface((300, 100))
        hard_one_rectangle = hard_one.get_rect()
        hard_one.fill((255, 0, 0))
        hard_one_rectangle.left = 440
        hard_one_rectangle.top = 450
        screen.blit(hard_one, (hard_one_rectangle.left, hard_one_rectangle.top))
        text = font.render("Hard", True, (0, 0, 139))
        screen.blit(text, (550, 490))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                outro = False
                game_loop = False
                intro = False
                running=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if easy_one_rectangle.top <= my <= easy_one_rectangle.bottom and easy_one_rectangle.left <= mx <= \
                        easy_one_rectangle.right:
                    bot_level = "easy"
                    intro = False
                if hard_one_rectangle.top <= my <= hard_one_rectangle.bottom and hard_one_rectangle.left <= mx <= \
                        hard_one_rectangle.right:
                    bot_level = "hard"
                    intro = False
        pygame.display.flip()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                outro = False
                game_loop = False
                intro = False
                running=False
                """FOR THE PLAYER"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player1.is_moving_up = True
                    ball.player1.is_moving_up = True
                if event.key == pygame.K_DOWN:
                    player1.is_moving_down = True
                    ball.player1.is_moving_down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player1.is_moving_up = False
                    ball.player1.is_moving_up = False
                if event.key == pygame.K_DOWN:
                    player1.is_moving_down = False
                    ball.player1.is_moving_down = False
                """FOR THE PLAYER"""

        """FOR THE BOT"""
        if game_ball.is_moving_right and game_ball.rectangle.centerx < 1200:
            if bot_level == "easy":
                if player2.rectangle.centery < game_ball.rectangle.centery and game_ball.is_moving_right and game_ball.rectangle.centerx > 1021:
                    player2.is_moving_down = True
                    ball.player2.is_moving_down = True
                    player2.is_moving_up = False
                    ball.player2.is_moving_up = False
                if player2.rectangle.centery > game_ball.rectangle.centery and game_ball.is_moving_right and game_ball.rectangle.centerx > 1021:
                    player2.is_moving_down = False
                    ball.player2.is_moving_down = False
                    ball.player2.is_moving_up = True
                    player2.is_moving_up = True
            if bot_level == "hard":
                if player2.rectangle.centery < game_ball.rectangle.centery and game_ball.rectangle.centerx > 750 and game_ball.is_moving_right:
                    player2.is_moving_down = True
                    ball.player2.is_moving_down = True
                    player2.is_moving_up = False
                    ball.player2.is_moving_up = False
                if player2.rectangle.centery > game_ball.rectangle.centery and game_ball.is_moving_right and game_ball.rectangle.centerx > 750:
                    player2.is_moving_down = False
                    ball.player2.is_moving_down = False
                    ball.player2.is_moving_up = True
                    player2.is_moving_up = True

        else:
            center_player2()

        """FOR THE BOT"""

        screen.fill((0, 128, 0))
        goal_post1.put_me_on_the_screen(screen)
        goal_post2.put_me_on_the_screen(screen)
        goal_post3.put_me_on_the_screen(screen)
        goal_post4.put_me_on_the_screen(screen)
        player1.put_me_on_the_screen(screen)
        player2.put_me_on_the_screen(screen)
        player1.update()
        player2.update()
        game_ball.put_me_on_the_screen(screen)
        game_ball.update()
        show_score(player1)
        show_score(player2)
        txt = font.render(str(round(timer, 1)), True, (0, 0, 139))
        screen.blit(txt, (570, 10))
        dt = clock.tick(60) / 1000
        timer -= dt
        if timer > 0:
            pygame.display.flip()
        if timer <= 0:
            break

    while outro:


        screen.fill((0, 0, 255))
        result = pygame.Surface((500, 100))
        result_rectangle = result.get_rect()
        result_rectangle.left = 340
        result_rectangle.top = 150
        result.fill((255, 0, 0))
        screen.blit(result, (result_rectangle.left, result_rectangle.top))
        play_again_text = font.render("Play Again", True, (0, 0, 139))
        quit_game = pygame.Surface((300, 100))
        quit_game_rectangle = quit_game.get_rect()
        quit_game.fill((255, 0, 0))
        quit_game_rectangle.left = 440
        quit_game_rectangle.top = 450
        screen.blit(quit_game, (quit_game_rectangle.left, quit_game_rectangle.top))
        text = font.render("QUIT", True, (0, 0, 139))
        screen.blit(text, (550, 490))
        game_over = pygame.Surface((300, 100))
        game_over_rectangle = easy_one.get_rect()
        game_over.fill((255, 0, 0))
        game_over_rectangle.left = 440
        game_over_rectangle.top = 300
        screen.blit(game_over, (game_over_rectangle.left, game_over_rectangle.top))
        if ball.player1.score_value > ball.player2.score_value:
            txt = font.render("Player1 Won", True, (0, 0, 139))
        elif ball.player2.score_value > ball.player1.score_value:
            txt = font.render("Player2 Won", True, (0, 0, 139))
        else:
            txt = font.render("It's a tie", True, (0, 0, 139))
        screen.blit(txt, (510, 190))
        screen.blit(play_again_text, (490, 340))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                outro = False
                game_loop=False
                intro=False
                running=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if game_over_rectangle.top <= my <= game_over_rectangle.bottom and game_over_rectangle.left <= mx <= \
                        game_over_rectangle.right:
                    outro=False
                if quit_game_rectangle.top <= my <= quit_game_rectangle.bottom and quit_game_rectangle.left <= mx <= \
                        quit_game_rectangle.right:
                    outro=False
                    game_loop=False
        pygame.display.flip()
