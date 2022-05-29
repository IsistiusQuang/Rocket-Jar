

# WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
# def main():
#     clock = pygame.time.Clock()
#     FPS = 60
#     run = True
#     while run:
#         clock.tick(FPS)
#         previous_height = 0
#         previous_width = 0
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

#         WIN.fill((255,255,255))
#         for obj in Astroids.Astroid_list:
#             WIN.blit(obj.image,
#                 (obj.x,obj.y))
#             # print(f"Previous Height : {previous_height}\t Previous Width : {previous_width}")
#             # previous_height += obj.height
#             # previous_width += obj.width
#             pygame.display.update()

#     pygame.quit()

# for obj in Astroids.Astroid_list:
#     print(f"Obj width {obj.width}\t Obj height: {obj.height}")
#     print(f"Obj x: {obj.x}\t Obj y: {obj.y}")
# if __name__ == "__main__":
#     main()

