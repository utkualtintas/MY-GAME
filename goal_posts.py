import pygame


class GoalPost:

    def __init__(self, which_side, top_or_bottom):
        post_length = 4
        post_width = 20
        self.surface = pygame.Surface((post_length, post_width))
        post_color = (255, 0, 255)
        self.surface.fill(post_color)
        self.rectangle = self.surface.get_rect()
        leftx_coordinate_of_left_posts = 0
        rightx_coordinate_of_right_posts = 1200
        topy_coordinate_for_top_posts = 120
        topy_coordinate_for_bottom_posts = 640

        if which_side == "left":
            self.rectangle.left = leftx_coordinate_of_left_posts
        else:
            self.rectangle.right = rightx_coordinate_of_right_posts
        if top_or_bottom == "top":
            self.rectangle.top = topy_coordinate_for_top_posts
        else:
            self.rectangle.top = topy_coordinate_for_bottom_posts

    def put_me_on_the_screen(self, screen):
        screen.blit(self.surface, (self.rectangle.left, self.rectangle.top))
