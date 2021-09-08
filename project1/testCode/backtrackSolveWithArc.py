




def arc(prop, removals=None, queue=None):
    if queue is None:
        queue = [(Xi, Xk) for Xi in 


def forwardChecking(puzzle, i, j, k):
    global sections

    puzzle[i][j] = k
    check = [(i, j, k)]
    sections = [[0, 3, 0, 3],
                [3, 6, 0, 3],
                [6, 9, 0, 3],
                [0, 3, 3, 6],
                [3, 6, 3, 6],
                [6, 9, 3, 6],
                [0, 3, 6, 9],
                [3, 6, 6, 9],
                [6, 9, 6, 9]]

    for v in range(9):

        tracking = []
        domain = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        # find the missing cells in the sections
        for x in range(sections[v][0], sections[v][1]):
            for y in range(sections[v][2], sections[v][3]):
                if puzzle[x][y] != 0:
                    domain.remove(puzzle[x][y])

        # attach the domain to each empty cell
        for x in range(sections[v][0], sections[v][1]):
            for y in range(sections[v][2], sections[v][3]):
                if puzzle[x][y] == 0:
                    tracking.append([x, y, domain.copy()])

        for n in range(len(tracking)):
            trackingItem = tracking[n]

            # remove the elements in row n
            rowCheck = []
            for x in range(9):
                rowCheck.append(puzzle[trackingItem[0]][x])
            remaining = trackingItem[2].difference(rowCheck)

            # remove the elements in col n
            colCheck = []
            for y in range(9):
                colCheck.append(puzzle[y][trackingItem[1]])
            remaining = remaining.difference(colCheck)

            # check for duplicates of the domain
            if len(remaining) == 1:
                value = remaining.pop()
                if validator(puzzle, trackingItem[0], trackingItem[1], value):
                    puzzle[trackingItem[0]][trackingItem[1]] = value
                    check.append((trackingItem[0], trackingItem[1], value))
    return tracking
