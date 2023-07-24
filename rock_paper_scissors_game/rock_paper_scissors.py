# 가위바위보 게임 만들기
# ...으로 적힌 부분을 채워주시면 됩니다.

# random 모듈 import하기
import random

# 가이드라인 출력
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

# 게임 시작
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    
    # 유저로부터 입력값 받기
    choice=int(input())
     
    # 유저가 유효한 입력값을 줄 때까지 반복한다
    while True: # <- 조건문 True 말고 다른걸로
        if choice == 1 or choice == 2 or choice == 3:
            break 
        choice=int(input())
         
    # 유저의 입력값을 문자열로 변환
    # 문자열의 변수 이름은 choice_name으로 정의할 것
    # ex) 1 -> 'Rock'
    #     2 -> 'Paper'
    #     3 -> 'Scissors'
    if choice ==1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"
    
    # 유저의 선택(choice_name) 출력하기
    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')
    
    # random 안에 있는 randint 함수를 사용하여 1부터 3까지 랜덤한 숫자 가져오기
    comp_choice = random.randint(1, 3)
         
    # 컴퓨터의 입력값을 문자열로 변환
    # 문자열의 변수 이름은 comp_choice_name으로 정의할 것
    # ex) 1 -> 'Rock'
    #     2 -> 'Paper'
    #     3 -> 'Scissors'
    if comp_choice ==1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"

    # 컴퓨터의 선택(comp_choice_name) 출력하기
    print("Computer choice is \n", comp_choice_name)
    print(choice_name,'Vs',comp_choice_name)

    # 비긴 경우 변수 result에 "DRAW"를 넣어준다
    if choice == comp_choice:
        result = "DRAW"
    
    # 비기지 않은 경우 누가 이겼는지 확인한다
    # result의 값에 유저가 이긴 경우 "USER", 컴퓨터가 이긴 경우 "COMPUTER"를 넣어준다
    if choice_name == "Rock":
        if comp_choice_name == "Scissors":
            result = "User"
        elif comp_choice_name == "Paper":
            result = "Computer"
    
    if choice_name == "Scissors":
        if comp_choice_name == "Paper":
            result = "User"
        elif comp_choice_name == "Rock":
            result = "Computer"
     
    if choice_name == "Paper":
        if comp_choice_name == "Rock":
            result = "User"
        elif comp_choice_name == "Scissors":
            result = "Computer"
    

    # 누가 이겼는지 혹은 비겼는지 출력해준다
    print(result)

    # 다시 게임을 시작하고 싶은지 확인하기
    print("Do you want to play again? (Y/N)")

    # 유저의 입력값은 대문자와 소문자 모두 유효하고 소문자로 변수에 넣어준다
    # 유저의 입력값이 유효할 때까지 반복해서 입력값을 물어본다
    # 유저의 입력값 변수는 ans로 정의한다
    ...
    
    # 만약 유저의 입력값이 n/N인 경우 게임을 끝낸다
    ...

print("thanks for playing")