#
# CS1010FC --- Programming Methodology
#
# Mission N Solutions
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import random
import constants as c

###########
# Task 1a #
###########

"""
1. n x n의 0으로 이루어진 matrix를 만들고
2. add_two함수를 호출하여 2번 호출하여서 matrix에 숫자 2개가 랜덤하게 위치하도록 해주고
3. matrix를 반환해주세요.
"""
def new_game(n): # n도 활용해주세요 ***********
    # 1
    matrix = ([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]) # <- for문 사용하셔서 작성해보세요 [0, 0, 0, 0]은 반복이라 [0] * 4로 할 수 있어요 그리고 4 대신 n을 이용해서 판의 크기가 달라도 실행되게끔 해주세요 ***********
    
    # 2
    add_two(mat) # <- 함수를 불러준다음 새로운 mat를 변수에 넣어줘야해요. 그리고 함수 두번 호출해줘야해요 ***********
    
    # 3
    return ...

###########
# Task 1b #
###########

"""
1. 주어진 mat에 랜덤하게 index를 선택하되
2. 선택된 index는 0이 아닌 값을 가지게 하고
3. 그 index에 숫자 2를 넣어주고
4. mat을 반환해주세요.
"""

def add_two(mat): # 한번에 한 숫자만 넣는 함수에요! ***********
    # 1
    # random의 randint를 이용하여 랜덤한 index 값 생성하기
    a = 0 # random 라이브러리 이용하셔서 0부터 n-1까지의 랜덤 숫자 2개(가로, 세로) 생성해주세요 ***********
    b = 0
    c = 0
    d = 0

    # 2
    while a==c and b==d: # mat[가로][세로]의 값이 0이 아니면 계속 반복하게 해주세요 ***********
        a = random.randint(0,3)
        b = random.randint(0,3)
        c = random.randint(0,3)
        d = random.randint(0,3)
    
    # 3
    matrix[a,b] = 2 # 인덱싱은 matrix[a][b]로 해야해요 ***********
    matrix[c,d] = 2

    # 4
    return mat

###########
# Task 1c #
###########

"""
게임 상태를 확인하기 위한 함수로
1. mat에 숫자 2048이 있는 경우 유저가 이겼으므로 'win'을 반환한다
2. 만약 mat에 0이 있는 경우 아직 게임이 안 끝났으므로 'not over'를 반환해준다
3. 만약 이웃한 칸이 같은 숫자인 경우 게임이 안 끝났으므로 'not over'를 반환해준다
    3-0. n-1만큼 세로 가로를 돌면서 오른쪽과 아래의 숫자가 같은지 확인해준다
    3-1. 마지막 가로의 오른쪽과 왼쪽의 숫자가 같은지 확인해준다
    3-2. 마지막 세로의 위와 아래의 숫자가 같은지 확인해준다
4. 모든 위의 경우가 아닐경우 유저가 졌으므로 'lose'를 반환한다
"""

def game_state(mat):
    # 1
    # check for win cell
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat == 2048: # mat은 판 전체를 의미해요 ***********
                mat = "win" # 'win' 문자열을 반환해야해요 ***********
            return
        
    # 2
    # check for any zero entries
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat == 0:
                mat = "win"
            return

    # 3-0
    # check for same cells that touch each other
    for i in range(len(mat)-1):
        # intentionally reduced to check the row on the right and below
        # more elegant to use exceptions but most likely this will be their solution
        for j in range(len(mat[0])-1):
            if mat(i,j) == mat(i+1,j) or mat(i,j) == mat(i,j+1): # 2중 리스트 인덱싱은 list[i][j] 이렇게 해요 ***********
                mat = "not over"
            
    # 3-1
    for k in range(len(mat)-1):  # to check the left/right entries on the last row
        if mat(4,k) == mat(4,k+1): # 4 대신 판의 크기를 가져와서 판 크기가 달라도 정상적으로 실행되는 코드로 만들어주세요 ***********
            mat = "not over"

    # 3-2
    for j in range(len(mat)-1):  # check up/down entries on last column
        if mat(j,4) == mat(j+1,4):
            mat = "not over"

    # 4
    return mat = "lose"

###########
# Task 2a #
###########

"""
각 가로마다 순서를 역으로 바꿔주는 함수
ex) [[1, 2], [3, 4]] -> [[2, 1], [4, 3]]
바뀐 mat를 반환한다
"""

def reverse(mat):
    mat1 = ([0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat1(i, j) = mat(3-i,j) # i가 가로 인덱스 j가 세로 인덱스에요. 그리고 3말고 크기에 상관없이 실행되는 코드로 작성해주세요 ***********
    return mat1 = mat # 그냥 mat1을 반환하면 됩니다 ***********

###########
# Task 2b #
###########

"""
transpose는 오른쪽 아래를 향하는 대각선을 기준으로 뒤집어준다
ex) [[1, 2], [3, 4]] -> [[1, 3], [2, 4]]
바뀐 mat를 반환한다
"""

def transpose(mat):
    mat2 = ([0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat2(i, j) = mat(j,i)
    return mat2 = mat

##########
# Task 3 #
##########

"""
각 가로마다 0이 아닌 값들을 왼쪽으로 붙여주는 함수!
ex) [[0, 0, 1], [1, 0, 1], [0, 0, 1]] -> [[1, 0, 0], [1, 1, 0], [1, 0, 0]]
"""

def cover_up(mat):
    # mat와 같은 크기의 0으로 이루어진 행렬 생성하기
    new = ([0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0])
    done = False

    # 각 가로마다 0이 아닌 값이 있으면 왼쪽으로 붙여주기
    for i in range(c.GRID_LEN):
        count = 0 # <- 0이 아닌 왼쪽으로 붙여진 값들이 얼마나 있는지 확인해주는 변수
        for j in range(c.GRID_LEN):
            # 0이 아닌 값이면 새로운 행렬 new에서 해당하는 가로줄의 제일 왼쪽에 위치한 곳에 값을 넣어준다
            if mat(i,j) != 0:
                new(count, j) # new[가로][젤 왼쪽]에 값 넣어주기 <- count는 세로 인덱스를 의미해요 ***********
                if j != count:
                    done = True
                count += 1 # 값을 넣어주면 왼쪽으로 붙여진 값이 하나 늘어나서 1을 더해준다
    
    return new, done

"""
0이 아닌 가로로 이웃한 값이 같으면 왼쪽 칸에 해당 값에 2를 곲한 값을 넣어주고 오른쪽 칸에 0을 넣어주는 함수
ex) [[2, 2, 0, 0], [0, 0, 0, 0], [4, 2, 0, 0], [4, 4, 0, 0]] -> [[4, 0, 0, 0], [0, 0, 0, 0], [4, 2, 0, 0], [8, 0, 0, 0]]
"""

def merge(mat, done):
    for i in range(len(mat)-1): # 가로 인덱스는 모두 살펴봐야해요 ***********
        for j in range(len(mat[0])): # 세로 인덱스는 마지막칸은 안 봐도 되겠죠! ***********
            if mat(i,j) == mat(i+1,j) and mat(i,j) !=0: # 왼쪽과 오른쪽의 값이 같고 왼쪽 값이 0이 아니다
                mat(i,j) = mat(i,j) * 2 # 왼쪽 칸에 2를 곱한 값 넣어준다
                mat(i+1,j) = 0 # 오른쪽 칸에 0을 넣어준다
                done = True
    return mat, done

"""
함수 부르는 순서:
    transpose -> cover_up -> merge -> cover_up -> transpose
"""
def up(game):
    print("up")
    ...
    return game, done

"""
함수 부르는 순서:
    transpose -> reverse -> cover_up -> merge -> cover_up -> reverse -> transpose
"""
def down(game):
    print("down")
    ...
    return game, done

"""
함수 부르는 순서:
    cover_up -> merge -> cover_up
"""
def left(game):
    print("left")
    # return matrix after shifting left
    game, done = ...
    game, done = ...
    game = ...
    return game, done

"""
함수 부르는 순서:
    reverse -> cover_up -> merge -> cover_up -> reverse
"""
def right(game):
    print("right")
    game = ...
    game, done = ...
    game, done = ...
    game = ...
    game = ...
    return game, done