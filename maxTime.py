#This is my inital code. but this will fail fir this test case as here the counter is 7 as it is only counting the '.'
def reachTheEnd1(grid, maxTime):
    row = len(grid)
    columns = len(grid[0])
    counter = 0
    for i in grid:
        for j in i:
            if(j == '.'):
                counter += 1
    counter -= 1
    print(counter)
    if(counter == maxTime):
        return "yes"
    else:
        return "no"

#A much better and corrected version is:
def reachTheEnd(grid, maxTime):
    rows = len(grid)
    cols = len(grid[0])

    visited = set() #To make sure we are visiting a . only ones
    '''
    0: The row index of the current cell
    0: The column index of the current cell
    0: The time taken to reach the current cell 
    '''
    queue = [(0, 0, 0)]
    while queue:
        row, col, time = queue.pop(0)

        if row == rows - 1 and col == cols - 1:
            return "Yes"

        if (row, col) in visited or time > maxTime:
            continue

        visited.add((row, col))
        '''
        (1, 0) : down
        (-1, 0) : Up
        (0, 1) : left
        (0, -1) : Right
        How is this BSF?
        because by this code we are visiting the adjacent vertices. for a node in this question the adjacent vertices are to its left
        and to its down or up.
        '''
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '.':
                queue.append((new_row, new_col, time + 1))

    return "No"

if __name__ == '__main__':
    print(reachTheEnd(['..','#.'],2))