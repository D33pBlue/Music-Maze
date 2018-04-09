# A maze is a square of r*c cells, each of them consists in a dictionary
# with the following keys:
# -r: the row in the square
# -c: the column in the square
# -n: True if and only if there is a wall at north of the cell
# -s: True if and only if there is a wall at south of the cell
# -e: True if and only if there is a wall at east of the cell
# -w: True if and only if there is a wall at west of the cell
# -state: a string with the state of the cell
# -adj: the adjacency list of the cell

import random
import time

last_cell_id = 0

def make_cell(r,c,n=True,s=True,e=True,w=True,state=""):
	global last_cell_id
	cell=dict()
	cell['id']=last_cell_id
	last_cell_id += 1
	cell['r']=r
	cell['c']=c
	cell['n']=n
	cell['s']=s
	cell['e']=e
	cell['w']=w
	cell['state']=state
	cell['adj']=[]
	return cell

def add_adj(cell,adj):
	present = False
	for x in cell['adj']:
		if x['id'] == adj['id']:
			present = True
			break
	if not present:
		cell['adj'].append(adj)

def get_shape(L):
	return (len(L),len(L[0]))

# L is a array of cells (square)
def check_cell(L,c):
	Lr,Lc = get_shape(L)
	i,j=c
	if i<0 or i>=Lr or j<0 or j>=Lc:
		return False
	return L[i][j] != None


def adjacent(c1,c2):
	if abs(c1[0]-c2[0]) ==1 and c1[1] == c2[1]:
		return True
	if abs(c1[1]-c2[1]) ==1 and c1[0] == c2[0]:
		return True
	return False


def has_cycle(L,end):
	for r in L:
		for v in r:
			v['visited']=False
	for r in L:
		for v in r:
			if not v['visited']:
				stack=[]
				state=(None,v)
				stack.append(state)
				while len(stack)>0:
					prec,c = stack.pop()
					if c['visited']:
						end[0] = c
						return True
					c['visited']=True
					for k in c['adj']:
						if k != prec:
							state=(c,k)
							stack.append(state)
	return False

def find_cycle(start,L):
	if start == None:
		return []
	fifo = []
	for c in start['adj']:
		fifo.insert(0,(c,[start]))
	while len(fifo)>0:
		c,path = fifo.pop()
		path.append(c)
		if c == start:
			return path
		for cell in c['adj']:
			if not cell in path or (cell==start and cell!=path[len(path)-1]):
				fifo.insert(0,(cell,path[:]))
	return []

def find_path(c1,c2):
	stack = []
	stack.append((c1,[]))
	while len(stack)>0:
		c,path = stack.pop()
		path.append(c)
		if c == c2:
			return path
		for cell in c['adj']:
			if not cell in path:
				stack.append((cell,path[:]))
	return []



def findable_cells(c):
	stack=[]
	visited=set()
	stack.append(c)
	while len(stack)> 0:
		c_corr=stack.pop()
		coord=(c_corr['r'],c_corr['c'])
		visited.add(coord)
		for k in c_corr['adj']:
			k_c = (k['r'],k['c'])
			if not k_c in visited:
				stack.append(k)
	return len(visited)


def connected(L):
	r,c=get_shape(L)
	return r*c==findable_cells(L[0][0])


def delete_random_wall(L,cell):
	i,j=cell['r'],cell['c']
	k=(i,j)
	k_n=(i-1,j)
	k_s=(i+1,j)
	k_e=(i,j+1)
	k_w=(i,j-1)
	possible_neighbours=[]
	if check_cell(L,k_n):
		possible_neighbours.append(k_n)
	if check_cell(L,k_s):
		possible_neighbours.append(k_s)
	if check_cell(L,k_e):
		possible_neighbours.append(k_e)
	if check_cell(L,k_w):
		possible_neighbours.append(k_w)
	if len(possible_neighbours)>0:
		random.shuffle(possible_neighbours)
		choosen = possible_neighbours.pop()
		ic,jc=choosen
		neigh=L[ic][jc]
		add_adj(neigh,cell)
		add_adj(cell,neigh)
		if ic<i:
			cell['n']=False
			neigh['s']=False
		elif ic>i:
			cell['s']=False
			neigh['n']=False
		elif jc<j:
			cell['w']=False
			neigh['e']=False
		elif jc>j:
			cell['e']=False
			neigh['w']=False

def delete_wall(cell,neigh):
	i,j=cell['r'],cell['c']
	ic,jc=neigh['r'],neigh['c']
	add_adj(neigh,cell)
	add_adj(cell,neigh)
	if ic<i:
		cell['n']=False
		neigh['s']=False
	elif ic>i:
		cell['s']=False
		neigh['n']=False
	elif jc<j:
		cell['w']=False
		neigh['e']=False
	elif jc>j:
		cell['e']=False
		neigh['w']=False

def low_degree_cells(L):
	m=4
	for r in L:
		for c in r:
			if len(c['adj'])<m:
				m=len(c['adj'])
			if m==0:
				break
	cells=[]
	for r in L:
		for c in r:
			if len(c['adj'])==m:
				cells.append(c)
	return cells


def put_wall(c1,c2):
	c1['adj'].remove(c2)
	c2['adj'].remove(c1)
	i,j=c1['r'],c1['c']
	ic,jc=c2['r'],c2['c']
	if ic<i:
		c1['n']=True
		c2['s']=True
	elif ic>i:
		c1['s']=True
		c2['n']=True
	elif jc<j:
		c1['w']=True
		c2['e']=True
	elif jc>j:
		c1['e']=True
		c2['w']=True


def exits(L):
	u = []
	r,c= get_shape(L)
	for j in range(c):
		if L[0][j]['n'] == False:
			if not (0,j) in u:
				u.append((0,j))
		if L[r-1][j]['s'] == False:
			if not (r-1,j) in u:
				u.append((r-1,j))
	for i in range(r):
		if L[i][0]['w'] == False:
			if not (i,0) in u:
				u.append((i,0))
		if L[i][c-1]['e'] == False:
			if not (i,c-1) in u:
				u.append((i,c-1))
	return u


def add_exit(L):
	r,c= get_shape(L)
	possible_exits=[]
	for j in range(c):
		possible_exits.append((0,j))
		possible_exits.append((r-1,j))
	for i in range(r):
		possible_exits.append((i,0))
		possible_exits.append((i,c-1))
	random.shuffle(possible_exits)
	u=None
	while len(possible_exits)>0 and u==None:
		u1=possible_exits.pop()
		if not u1 in exits(L):
			u=u1
	if u != None:
		ui,uj=u
		if ui==0:
			L[ui][uj]['n']=False
		elif ui==r-1:
			L[ui][uj]['s']=False
		elif uj==0:
			L[ui][uj]['w']=False
		elif uj==c-1:
			L[ui][uj]['e']=False


def show(L):
	r,c = get_shape(L)
	line=""
	for i in range(r):
		for j in range(c):
			if L[i][j]['n']:
				line+="+---"
			else:
				line+="+   "
		line+= "+"
		print(line)
		line = ""
		for j in range(c):
			if L[i][j]['w']:
				if L[i][j]['state'] == 'Path':
					line+="| X "
				else:
					line+="|   "
			else:
				if L[i][j]['state'] == 'Path':
					line+="  X "
				else:
					line+="    "
		if L[i][c-1]['e']:
			line+= "|"
		print(line)
		line=""
	for j in range(c):
		if L[i][j]['s']:
			line+="+---"
		else:
			line+="+   "
	line+="+"
	print(line)



def perfect(L):
	if L is None:
		return False
	if has_cycle(L,[None]):
		return False
	return connected(L)


def DFS_visited(u,visited):
	u['color'] = 'G'
	visited.append(u)
	for cell in u['adj']:
		if cell['color'] == 'W':
			visited = DFS_visited(cell,visited)
	u['color'] = 'B'
	return visited

def connected_components(L):
	r,c = get_shape(L)
	for i in range(r):
		for j in range(c):
			L[i][j]['color'] = 'W'
	CC = []
	for i in range(r):
		for j in range(c):
			if L[i][j]['color'] == 'W':
				comp = DFS_visited(L[i][j],[])
				CC.append(comp)
	return CC

def join_components(CC):
	c1 = 0
	c2 = 1
	joined = False
	while len(CC) > 1:
		while not joined and c2<len(CC):
			cx1,cx2 = 0,0
			while not joined and cx1<len(CC[c1]):
				while not joined and cx2<len(CC[c2]):
					cell1 = CC[c1][cx1]
					cell2 = CC[c2][cx2]
					if adjacent((cell1['r'],cell1['c']),(cell2['r'],cell2['c'])):
						delete_wall(cell1,cell2)
						for x in CC[c2]:
							CC[c1].append(x)
						del CC[c2]
						joined = True
					else:
						cx2 += 1
				cx1 += 1
				cx2 = 0
			c2 += 1
			cx1,cx2 = 0,0
		joined = False
		c2 = 1


def make_maze(r,c,make_exits=True,verbose=False):
	L = [[make_cell(i,j) for j in range(c)] for i in range(r)]
	for l in L:
		for cell in l:
			delete_random_wall(L,cell)
	while not perfect(L):
		cycle=[]
		end = [None]
		i = 0
		while has_cycle(L,end):
			if verbose:
				print("1.cycle: ",i)
			cycle = find_cycle(end[0],L)
			c1=cycle.pop()
			c2=cycle.pop()
			put_wall(c1,c2)
			end = [None]
			i += 1
		i = 0
		while not connected(L):
			if verbose:
				print("2.connected: ",i)
			join_components(connected_components(L))
			# for k in low_degree_cells(L):
			# 	delete_random_wall(L,k)
			y = 0
			while has_cycle(L,end):
				if verbose:
					print("2.1.cycle: ",y)
				cycle = find_cycle(end[0],L)
				c1=cycle.pop()
				c2=cycle.pop()
				put_wall(c1,c2)
				end = [None]
				y += 1
			i += 1
	if make_exits:
		add_exit(L)
		add_exit(L)
	return L

def solve(L):
	exts = exits(L)
	if len(exts)>=2:
		e1 = L[exts[0][0]][exts[0][1]]
		e2 = L[exts[1][0]][exts[1][1]]
		path = find_path(e1,e2)
		return [(x['r'],x['c']) for x in path]

if __name__ == '__main__':
	L = make_maze(1005,40,False,True)
	r,c = 105,40
	for u in [(0,0),(104,39)]:
		ui,uj=u
		if ui==0:
			L[ui][uj]['n']=False
		elif ui==r-1:
			L[ui][uj]['s']=False
		elif uj==0:
			L[ui][uj]['w']=False
		elif uj==c-1:
			L[ui][uj]['e']=False
	show(L)
	path = solve(L)
	print('path:',path)
	for x in path:
		L[x[0]][x[1]]['state'] = 'Path'
	show(L)
