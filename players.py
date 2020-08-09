import pygame


class Players:
    def __init__(self, which_side):
        self.create_player_and_place_it(which_side)
        self.score_value = 0
        self.speed = 2

    def put_me_on_the_screen(self, screen):
        screen.blit(self.my_surface, (self.rectangle.left, self.rectangle.top))

    def update(self):
        self.change_pos_due_speed()
        self.define_player_boundaries()

    def change_pos_due_speed(self):
        if self.is_moving_up:
            self.rectangle.top -= self.speed
        if self.is_moving_down:
            self.rectangle.top += self.speed

    def define_player_boundaries(self):
        top_limit_for_players = 140
        bottom_limit_for_players = 640
        if self.rectangle.top <= top_limit_for_players:
            self.rectangle.top = top_limit_for_players
        if self.rectangle.bottom >= bottom_limit_for_players:
            self.rectangle.bottom = bottom_limit_for_players

    def create_player_and_place_it(self, which_side):
        player_width = 4
        player_length = 100
        self.is_moving_up = False
        self.is_moving_down = False
        self.my_surface = pygame.Surface((player_width, player_length))
        self.rectangle = self.my_surface.get_rect()
        player_color = (0, 0, 139)
        self.my_surface.fill(player_color)
        leftx_coordinate_of_left_player = 0
        leftx_coordinate_of_right_player = 1196
        topy_coordinate_of_players = 300
        if which_side == "left":
            self.rectangle.left = leftx_coordinate_of_left_player
        else:
            self.rectangle.left = leftx_coordinate_of_right_player
        self.rectangle.top = topy_coordinate_of_players
