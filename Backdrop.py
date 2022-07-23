import pygame
import os

from Base_Class import Base_obj
from random import choice,randint
from copy import deepcopy

WIN_WIDTH , WIN_HEIGHT = 800,650

pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.init()

debris_size = [(i,i) for i in range(30,60,10)]
debris_file = {f"Rock{i}.png":debris_size for i in range(1,8)}
debris_startin_coords = [ (WIN_WIDTH,i) for i in range(200,600,20)]
debris_time_interval = [i for i in range(300,360,20)]

planet_size = [(i,i) for i in range(120,150,10)]
planet_file = {"Jupiter.png":planet_size,"Mars.png":planet_size,"Pluto.png":planet_size,"Saturn.png":[(140,90)],"Earth.png":planet_size}
planet_startin_coords = [ (WIN_WIDTH,i) for i in range(200,250,50)]
planet_time_interval = [i for i in range(1900,2100,20)]

comet_size = [(i,i) for i in range(80,110,10)]
comet_file = {"Comet.png":comet_size}
comet_startin_coords = [ *[ (WIN_WIDTH,i) for i in range(0,60,20)], *[ (i,-100) for i in range(350,WIN_WIDTH,100)]]
comet_time_interval = [i for i in range(2400,2700,20)]

galaxy_size = [(i+i*1.6,i) for i in range(320,360,10)]
galaxy_file = {"galaxy.png":galaxy_size}
galaxy_startin_coords = [ (WIN_WIDTH,i) for i in range(-20,10,10)]
galaxy_time_interval = [i for i in range(12000,12300,60)]


class Backdrop(Base_obj):
    def __init__(self,name,x,y,width,height):
        self.name = str(name)
        self.image = None
        Base_obj.__init__(self,x,y,width,height)
        self.make_image()

    def make_image(self):
        self.image = pygame.transform.scale( pygame.image.load(
            os.path.join( 'Assets' , self.name )).convert_alpha() , ( self.width , self.height ))

class Cosmic_obj(Base_obj):
    def __init__(self,name):
        self.name = name
        self.image = self.make_image()

    def make_image(self):
        return pygame.image.load(os.path.join("Assets",str(self.name))).convert_alpha()

    def resize(self,x,y,width,height):
        Base_obj.__init__(self,x,y,width,height)
        self.image = pygame.transform.scale(self.image,(width,height))

    def draw(self,Window):
        Window.blit(self.image,(self.x,self.y))

    def move(self,alter_x = 0.0,alter_y = 0.0):
        self.x -= alter_x
        self.y -= alter_y

class Planet_level(Cosmic_obj):
    def __init__(self,file_name,alter_x = 1.5):
        Cosmic_obj.__init__(self,file_name)
        self.alter_x = alter_x

    def move(self):
        Cosmic_obj.move(self,self.alter_x)

class Debris_level(Cosmic_obj):
    def __init__(self,file_name,alter_x = 3):
        Cosmic_obj.__init__(self,file_name)
        self.alter_x = alter_x

    def move(self):
        Cosmic_obj.move(self,self.alter_x)

class Galaxy_level(Cosmic_obj):
    def __init__(self,file_name,alter_x = 0.5):
        Cosmic_obj.__init__(self,file_name)
        self.alter_x = alter_x

    def move(self):
        Cosmic_obj.move(self,self.alter_x)

class Comet_level(Cosmic_obj):
    def __init__(self,file_name,alter_x = 0.8 ,alter_y = -0.8):
        Cosmic_obj.__init__(self,file_name)
        self.alter_x = alter_x
        self.alter_y = alter_y

    def move(self):
        Cosmic_obj.move(self,self.alter_x,self.alter_y)

class Base_List():
    def __init__(self,obj_class,obj_file,coords,time_interval,alter_x):
        self.obj_class = obj_class
        self.obj_file = obj_file
        self.startin_coords = coords
        self.alter_x = alter_x

        self.time_interval = time_interval
        self.frame_limit = choice(self.time_interval)
        self.frame_count = self.frame_limit//100

        self.list_of_obj = []
        self.current_obj = None
        self.obj_size = None

    def generate_obj(self):
        coords = choice(self.startin_coords)
        self.current_obj = self.obj_class(choice(list(self.obj_file)),self.alter_x)
        self.obj_size = choice(self.obj_file[self.current_obj.name])
        self.current_obj.resize(coords[0],coords[1],self.obj_size[0],self.obj_size[1])
        self.list_of_obj.append(self.current_obj)

    def cycle(self):
        self.frame_count += 1
        if self.frame_count == self.frame_limit:
            self.frame_count = 0
            self.frame_limit = choice(self.time_interval)
            self.generate_obj()

    def handle(self):
        self.cycle()
        for obj in self.list_of_obj[:]:
            obj.move()
            if obj.x + obj.width < 0:
                del(self.list_of_obj[self.list_of_obj.index(obj)])


class List_of_cosmic_stuffs():
    def __init__(self):
        self.Galaxies = Base_List(Galaxy_level,galaxy_file,galaxy_startin_coords,galaxy_time_interval,0.1)
        self.Comets = Base_List(Comet_level,comet_file,comet_startin_coords,comet_time_interval,0.8)
        self.Planets = Base_List(Planet_level,planet_file,planet_startin_coords,planet_time_interval,0.5)
        self.Debrises_L1 = Base_List(Debris_level,debris_file,debris_startin_coords,debris_time_interval,1)
        self.Debrises_L2 = Base_List(Debris_level,debris_file,debris_startin_coords,debris_time_interval,1.2)
        self.Debrises_L3 = Base_List(Debris_level,debris_file,debris_startin_coords,debris_time_interval,1.5)

    def handle_cosmics(self):
        self.Galaxies.handle()
        self.Comets.handle()
        self.Planets.handle()
        self.Debrises_L1.handle()
        self.Debrises_L2.handle()
        self.Debrises_L3.handle()

    def draw(self,win):
        for galaxy in self.Galaxies.list_of_obj:
            galaxy.draw(win)

        for comet in self.Comets.list_of_obj:
            comet.draw(win)

        for planet in self.Planets.list_of_obj:
            planet.draw(win)

        for debris in self.Debrises_L1.list_of_obj:
            debris.draw(win)
        for debris in self.Debrises_L2.list_of_obj:
            debris.draw(win)
        for debris in self.Debrises_L3.list_of_obj:
            debris.draw(win)


COSMIC_STUFFS = List_of_cosmic_stuffs()

SPACE = Backdrop('space.png',0,0,WIN_WIDTH,WIN_HEIGHT)



