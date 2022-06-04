import pygame

# polygon


# Arc
def make_arc( surface, color , rect , start_angle, stop_angle , width ):
    pygame.draw.arc(surface,color,rect,start_angle,stop_angle,width)
