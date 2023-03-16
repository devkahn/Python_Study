import random

random_number = random.randint(1,100)

# print(random_number)


game_count = 1

while True:
    try:
        my_number = int(input("1~100 사이의 숫자를 입력하세요."))
        
        if my_number > random_number:
            print('다운')
        elif my_number > random_number:
            print('업')
        else:
            print(f'축하합니다. {game_count}회 만에 맞췄습니다.')
            break;
        
        
        game_count+=1
    
    except:
        print('숫자만 입력 가능합니다.')