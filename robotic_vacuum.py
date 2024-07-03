class robot:
    def __init__(self, row, col, direction, rooms_status):
        self.row = row
        self.col = col
        self.direction = direction
        self.rooms_status = rooms_status # 현재 방 상태 확인 (청소 되었으면 None임)
        self.north = [row-1, col]
        self.east = [row, col+1]
        self.south = [row+1, col]
        self.west = [row, col-1]
        self.cleared_block_num = 0 # 청소 정보 저장
        self.status = True

    def get_4blocks(self): # 주위 4개의 block을 반환함. north이면 block position의 1 index가 반시계 방향임.
        block_positions = [] # 블럭 위치 지정
        block_positions.append(self.north) #front
        block_positions.append(self.east) #right
        block_positions.append(self.south) #back
        block_positions.append(self.west) #left

        return block_positions

    def get_back(self): # 후진할 방향
        block_position = self.get_4blocks()
        back_position = (self.direction+2)%4
        return block_position[back_position]

    def get_front(self): # 전진할 방향
        block_position = self.get_4blocks()
        return block_position[self.direction]

    def move(self, move_row, move_col): # 이동
        self.row = move_row
        self.col = move_col
        self.change_4blocks()
    
    def change_4blocks(self): # 주위 4개 block 위치 update
        self.north[0] = self.row-1
        self.north[1] = self.col
        self.east[0] = self.row
        self.east[1] = self.col+1
        self.south[0] = self.row+1
        self.south[1] = self.col
        self.west[0] = self.row
        self.west[1] = self.col-1

    def clear(self): # 그 자리 청소
        self.rooms_status[self.row][self.col] = True
        self.cleared_block_num += 1
    
    def check_4block_clear(self): # 청소 되었는지 확인
        north = self.rooms_status[self.north[0]][self.north[1]]
        south = self.rooms_status[self.south[0]][self.south[1]]
        west = self.rooms_status[self.west[0]][self.west[1]]
        east = self.rooms_status[self.east[0]][self.east[1]]

        if (north == 1 or north) and (south == 1 or south) and (west == 1 or west) and (east == 1 or east):
            return True # 청소 됨
        else:
            return False # 청소 안 됨

    def check_clear(self):
        if self.rooms_status[self.row][self.col]:
            return True # 청소 됨
        else:
            return False # 청소 안 됨
        
def step1(robots):
    while(robots.status):
        if not robots.check_clear(): # 청소 안 됨
            robots.clear()
        if robots.check_4block_clear(): # 주변이 모두 청소가 됐을 때
            robots = step2(robots)
        else:
            robots = step3(robots)
    return robots.cleared_block_num

def step2(robots): #빈칸이 없는 경우
    back_row, back_col = robots.get_back()
    status = robots.rooms_status[back_row][back_col]
    if str(status) == 'True':
        robots.move(back_row, back_col)
        return robots
    else:
        robots.status = False
        return robots
    
def step3(robots): #빈칸이 있는 경우
    robots.direction = (robots.direction+3)%4 # 반시계로 90도 회전
    front_row, front_col = robots.get_front()
    post_move = robots.rooms_status[front_row][front_col]
    if post_move == 0 and post_move != 1: # 청소되지 않은 and 빈 칸(이동할 수 있는 칸)
        robots.move(front_row, front_col)
        return robots
    else:
        return robots
    
room_size = list(map(int, input().split()))
robot_row, robot_col, robot_dir = map(int, input().split())
rooms_status = []
for _ in range(room_size[0]):
    rooms_status.append(list(map(int, input().split())))
    
robot_status = robot(robot_row, robot_col, robot_dir, rooms_status)

num = step1(robot_status)
print(num)