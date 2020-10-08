import pygame
from goal_posts import GoalPost
from players import Players
import random

player1 = Players("left")
player2 = Players("right")


class TheBall:

    def __init__(self):
        self.create_ball_surface_and_draw_the_ball()
        self.randomize_the_initial_ball_movement()

    def update(self):

        self.put_the_wall_physics()
        self.set_player_interventions()
        self.deal_with_scoring()
        self.put_the_goalpost_physics()
        self.update_player_posiitions()

    def put_me_on_the_screen(self, screen):
        screen.blit(self.surface, (self.rectangle.left, self.rectangle.top))

    def player2_intervention(self):

        if self.rectangle.right == player2.rectangle.left and player2.rectangle.top <= self.rectangle.centery \
                <= player2.rectangle.bottom:
            self.is_moving_left = True
            self.is_moving_right = False

    def set_player_interventions(self):
        self.player1_intervention()
        self.player2_intervention()

    def player1_intervention(self):

        if self.rectangle.left == player1.rectangle.right and player1.rectangle.top <= self.rectangle.centery \
                <= player1.rectangle.bottom:
            self.is_moving_left = False
            self.is_moving_right = True

    def hitting_the_post3(self):
        goal_post3 = GoalPost("right", "bottom")
        if self.rectangle.right == goal_post3.rectangle.left and goal_post3.rectangle.top <= self.rectangle.centery \
                <= goal_post3.rectangle.bottom:
            self.is_moving_left = True
            self.is_moving_right = False

    def hitting_the_post4(self):
        goal_post4 = GoalPost("right", "top")
        if self.rectangle.right == goal_post4.rectangle.left and goal_post4.rectangle.top <= self.rectangle.centery \
                <= goal_post4.rectangle.bottom:
            self.is_moving_left = True
            self.is_moving_right = False

    def hitting_the_post2(self):
        goal_post2 = GoalPost("left", "bottom")
        if self.rectangle.left == goal_post2.rectangle.right and goal_post2.rectangle.top <= self.rectangle.centery \
                <= goal_post2.rectangle.bottom:
            self.is_moving_left = False
            self.is_moving_right = True

    def hitting_the_post1(self):
        goal_post1 = GoalPost("left", "top")
        if self.rectangle.bottom == goal_post1.rectangle.top and self.rectangle.centerx <= goal_post1.rectangle.right:
            self.is_moving_down = False
            self.is_moving_up = True
        if self.rectangle.top == goal_post1.rectangle.bottom and self.rectangle.centerx <= goal_post1.rectangle.right:
            self.is_moving_down = True
            self.is_moving_up = False
        if self.rectangle.left == goal_post1.rectangle.right and goal_post1.rectangle.top <= self.rectangle.centery \
                <= goal_post1.rectangle.bottom:
            self.is_moving_left = False
            self.is_moving_right = True

    def deal_with_scoring(self):
        self.check_if_goal_on_right()
        self.check_if_goal_on_left()

    def put_the_goalpost_physics(self):
        self.hitting_the_post1()
        self.hitting_the_post2()
        self.hitting_the_post4()
        self.hitting_the_post3()

    def check_if_goal_on_left(self):
        if self.rectangle.left <= 0:
            if self.rectangle.top <= 100 or self.rectangle.top >= 660:
                self.rectangle.left = 0
                self.is_moving_right = True
                self.is_moving_left = False
            else:
                if self.rectangle.left <= -40:
                    self.rectangle.right = 596
                    self.rectangle.top = 370
                    player2.score_value += 1
                    value1 = random.randint(0, 1)
                    value2 = random.randint(0, 1)
                    self.is_moving_up = False
                    self.is_moving_down = False
                    self.is_moving_left = False
                    self.is_moving_right = False
                    if value1 == 1:
                        self.is_moving_up = True
                    else:
                        self.is_moving_down = True
                    if value2 == 1:
                        self.is_moving_left = True
                    else:
                        self.is_moving_right = True

    def check_if_goal_on_right(self):
        if self.rectangle.right >= 1200:
            if self.rectangle.centery <= 120 or self.rectangle.centery >= 660:
                self.rectangle.right = 1200
                self.is_moving_right = False
                self.is_moving_left = True
            else:
                if self.rectangle.left >= 1200:
                    self.rectangle.right = 596
                    self.rectangle.top = 370
                    player1.score_value += 1
                    value1 = random.randint(0, 1)
                    value2 = random.randint(0, 1)
                    self.is_moving_up = False
                    self.is_moving_down = False
                    self.is_moving_left = False
                    self.is_moving_right = False
                    if value1 == 1:
                        self.is_moving_up = True
                    else:
                        self.is_moving_down = True
                    if value2 == 1:
                        self.is_moving_left = True
                    else:
                        self.is_moving_right = True

    def put_the_wall_physics(self):
        if self.is_moving_up:
            self.rectangle.top -= 4
        if self.is_moving_down:
            self.rectangle.top += 4
        if self.is_moving_right:
            self.rectangle.left += 4
        if self.is_moving_left:
            self.rectangle.left -= 4
        if self.rectangle.bottom >= 780:
            self.rectangle.bottom = 780
            self.is_moving_down = False
            self.is_moving_up = True
        if self.rectangle.top <= 0:
            self.rectangle.top = 0
            self.is_moving_up = False
            self.is_moving_down = True

    def create_ball_surface_and_draw_the_ball(self):
        self.radius = 4
        self.surface = pygame.Surface((8, 8))
        self.rectangle = self.surface.get_rect()
        self.rectangle.right = 504
        self.rectangle.top = 433
        pygame.draw.circle(self.surface, (255, 255, 0), (4, 4), 4)

    def randomize_the_initial_ball_movement(self):
        value1 = random.randint(0, 1)
        value2 = random.randint(0, 1)
        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_left = False
        self.is_moving_right = False

        if value1 == 1:
            self.is_moving_up = True
        else:
            self.is_moving_down = True
        if value2 == 1:
            self.is_moving_left = True
        else:
            self.is_moving_right = True

    def update_player_positions(self):
        player1.update()
        player2.update()
