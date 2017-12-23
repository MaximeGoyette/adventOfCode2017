rules = open('21.txt').read()

rules = rules.split('\n')
rules = {x.split(' => ')[0]: x.split(' => ')[1] for x in rules}

grid = """.#.
..#
###"""

grid = grid.split('\n')
grid = [list(x) for x in grid]

def slice_grid(g, a):
    size = len(g)//a
    new = [[[] for x in range(size)] for y in range(size)]
    
    for y in range(len(g)):
        for x in range(size):
            new[y//a][x] += [g[y][x*a:x*a + a]]
    return new

def join_grid(g, size):
    new = [[] for x in range(len(g)*size)]
    for y in range(len(g)):
        for x in range(len(g)):
            for z in range(size):
                new[y*size + z] += g[y][x][z]
    return new

def rot90_grid(g):
    return zip(*g[::-1])

def flip_grid(g):
    return [x[::-1] for x in g]

def get_new_grid(g):
    for i in range(2):
        for i in range(4):
            g = rot90_grid(g)
            joined = '/'.join([''.join(x) for x in g])
            if joined in rules:
                new = rules[joined].split('/')
                new = [list(x) for x in new]
                return new
        g = flip_grid(g)
    print 'none'

def count_pixels(g):
    total = 0
    for y in g:
        for x in y:
            total += x.count('#')
    return total
 
for i in range(5):
    
    if len(grid)%2 == 0:
        grid = slice_grid(grid, 2)
        for y in range(len(grid)):
                for x in range(len(grid)):
                    grid[y][x] = get_new_grid(grid[y][x])
        grid = join_grid(grid, 3)
    else:
        grid = slice_grid(grid, 3)
        for y in range(len(grid)):
            for x in range(len(grid)):
                grid[y][x] = get_new_grid(grid[y][x])
        grid = join_grid(grid, 4)

print count_pixels(grid)

