# N을 받는다 N은 강의실 수
N = int(input())

# N개의 수를 받는다.
classes = list(map(int, input().split()))

m_teacher, s_teacher = map(int, input().split())

# 총감독 수는 강의실 수와 같다
num_m_teacher = N

# 총감독 수를 구하기 - input은 classes, m_teacher
# output은 총감독이 보는 학생 수를 제외한 새로운 classes list
def get_m_teacher(classes, m_teacher):
  new_classes = []
  for e_class in classes:
    remain_student = e_class - m_teacher
    if remain_student > 0:
      new_classes.append(remain_student)
    else:
      new_classes.append(0)
      
  return new_classes

def get_s_teacher(classes, s_teacher):
  sub_teacher = []
  for e_class in classes:
    if e_class > 0:
      if e_class >= s_teacher:
        if e_class % s_teacher == 0:
          sub_teacher.append(e_class//s_teacher)
        else:
          sub_num = e_class // s_teacher + 1
          sub_teacher.append(sub_num)
      else:
        sub_teacher.append(1)
    else:
      sub_teacher.append(0)
  return sub_teacher

left_array = get_m_teacher(classes, m_teacher)
sub_teacher_array = get_s_teacher(left_array, s_teacher)

all_teacher = num_m_teacher + sum(sub_teacher_array)
print(all_teacher)


# 나영서