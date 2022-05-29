from random import randint

my_list = [10,20,30,40,50,60,70,80,90,100]
frame_count = 0
frame_limit = 0
current_position = 0
spawn_num = 0
spawn_count = 0
loop_count = 0
game = True
while game:

    for i in range(current_position,len(my_list)):
        loop_count += 1
        if frame_count == frame_limit:
            if spawn_count == spawn_num :
                current_position += 1
                spawn_num = randint(1,3)
                spawn_count = 0
                frame_limit = randint(4,8)
                frame_count = 0
                print(f"frame limit : {frame_limit} \t spawn limit : {spawn_num}")
                break
            elif spawn_count < spawn_num :
                spawn_count += 1
        elif frame_count<frame_limit:
            frame_count += 1
            print(f"\tframe count : {frame_count}")
            break

        print(f"i:{i} \t my_list[i] : {my_list[i]}")
        if i == len(my_list) - 1:
            game = False

