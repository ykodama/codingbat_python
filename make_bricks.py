# coding:utf-8
def make_bricks(small, big, goal):
	if (small >= (goal % 5)) and (big >= (goal // 5)):
		return True
	elif (small % 5) >= (goal - 5*(small//5))%5 and big >= (goal - 5*(small//5))//5:
		return True
	elif small >= goal-(5*big) and goal-(5*big) >= 0:
		return True
	else:
		return False