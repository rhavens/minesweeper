import random

global time, m_left, board


def init_board(h,w,m):
	time = 0
	m_left = m
	board = [[0]*w for i in range(h)]
	board = populate_mines(board,h,w,m)
	board = populate_nums(board,h,w)
	print_board(board,h,w)


def populate_mines(b,h,w,m):
	m_array = ([0]*(h*w)) + ([9]*m)
	random.shuffle(m_array)
	for i in range(h):
		for j in range(w):
			b[i][j] = m_array[i*h+j]
	return b

def populate_nums(b,h,w):
	for i in range(h):
		for j in range(w):
			if (b[i][j] != 9):
				b[i][j] = get_neighbor_mine_count(b,h,w,i,j)
	return b



def get_neighbor_mine_count(b,h,w,i,j):
	count = 0
	for m in range(i-1,i+2):
		for n in range(j-1,j+2):
			if ((m > 0) and (m < h) and (n > 0) and (n < w)):
				if (b[m][n] == 9):
					count = count + 1
	return count

def print_board(b,h,w):
	for i in range(h):
		for j in range(w):
			print (b[i][j]),
		print
	print


init_board(16,30,99)