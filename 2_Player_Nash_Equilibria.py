# Pure Strategy Nash Equilibria Solver For Finite 2-Player Simultaneous Move Games 2022.1 | Eslam Abdullah
def transpose(matrix):
    trans = [[None for col in range(len(matrix))] for row in range(len(matrix[0]))]
    for row in range(len(trans)):
        for col in range(len(trans[row])):
            trans[row][col] = matrix[col][row]
    return trans


def rows_max(matrix):
    maxima = [None for row in range(len(matrix))]
    for row in range(len(matrix)):
        maxima[row] = max(matrix[row])
    return maxima


def rows_n(matrix):
    maxima = rows_max(matrix)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = 'N' if matrix[row][col] == maxima[row] else matrix[row][col]
    return matrix


def compare_n(row_mat, col_mat):
    pair_n = []
    for row in range(len(row_mat)):
        for col in range(len(col_mat[row])):
            if row_mat[row][col] == 'N' and col_mat[row][col] == 'N':
                pair = [row, col]
                pair_n.append(pair)
    return pair_n


def nash(row_mat, col_mat):
    row_trans = transpose(row_mat)
    row_tn = rows_n(row_trans)
    row_mat = transpose(row_tn)
    col_mat = rows_n(col_mat)
    pair_n = compare_n(row_mat, col_mat)
    return pair_n


def print_mat(row_mat, col_mat, row_name, col_name):
    text = '\t'
    for col in range(len(col_name)):
        text += f'{col_name[col]}\t'
    text += '\n'
    for row in range(len(row_mat)):
        text += f'{row_name[row]}\t'
        for col in range(len(col_mat[0])):
            text += f'({row_mat[row][col]},{col_mat[row][col]})\t'
        text += '\n'
    print(f'\n{text}')
    return text


def write_f(file_name, text):
    file_name = f'{file_name}.txt'
    f = open(file_name, 'w')
    f.write(text)
    f.close()


def print_n(row_mat, col_mat, row_name, col_name):
    text = f'{print_mat(row_mat, col_mat, row_name, col_name)}\n'
    pair_n = nash(row_mat, col_mat)
    result = ''
    if len(pair_n) == 0:
        result = 'No Nash Equilibria Points Found!'
    elif len(pair_n) == 1:
        result = '1 Nash Equilibrium Point Found:'
    else:
        result = f'{len(pair_n)} Nash Equilibria Points Found:'
    text += f'{result}\n'
    print(result)
    pair_text = ''
    for index in range(len(pair_n)):
        pair_text += f'({row_name[pair_n[index][0]]},{col_name[pair_n[index][1]]})\n'
    print(pair_text)
    text += pair_text
    return text


def read_n(file_name):
    print('Not Available Yet :(')
    input('> ')
    quit()


def write_n(file_name):
    row_no = 0
    col_no = 0
    while row_no < 2:
        row_no = input('Row no > ')
        row_no = int(row_no) if row_no.isnumeric() else 0
    while col_no < 2:
        col_no = input('Col no > ')
        col_no = int(col_no) if col_no.isnumeric() else 0
    row_name = [None for row in range(row_no)]
    col_name = [None for col in range(col_no)]
    print('Row player strategies:')
    for row in range(len(row_name)):
        row_name[row] = input(f'Row {row + 1} strategy > ')
        row_name[row] = row + 1 if row_name[row] == '' else row_name[row]
    print('Col player strategies:')
    for col in range(len(col_name)):
        col_name[col] = input(f'Col {col + 1} strategy > ')
        col_name[col] = col + 1 if col_name[col] == '' else col_name[col]
    row_mat = [[None for col in range(col_no)] for row in range(row_no)]
    col_mat = [[None for col in range(col_no)] for row in range(row_no)]
    print('Row player payoff:')
    for row in range(row_no):
        for col in range(col_no):
            eval_ok = False
            while not eval_ok:
                row_mat[row][col] = input(f'({row_name[row]},{col_name[col]}) > ')
                try:
                    row_mat[row][col] = eval(row_mat[row][col])
                    eval_ok = True
                except Exception:
                    pass
    print('Col player payoff:')
    for row in range(row_no):
        for col in range(col_no):
            eval_ok = False
            while not eval_ok:
                col_mat[row][col] = input(f'({row_name[row]},{col_name[col]}) > ')
                try:
                    col_mat[row][col] = eval(col_mat[row][col])
                    eval_ok = True
                except Exception:
                    pass
    write_f(file_name, print_n(row_mat, col_mat, row_name, col_name))
    input('> ')
    quit()


def remove_char(text, chars):
    text = text.strip()
    for char in chars:
        text = text.replace(char, '_')
    return text


def input_n():
    print('Pure Strategy Nash Equilibria Solver For Finite 2-Player Simultaneous Move Games 2022.1 | Eslam Abdullah\n')
    chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    file_name = ''
    while file_name == '':
        file_name = input('File name > ')
        file_name = remove_char(file_name, chars)
    write_n(file_name)  #
    '''r_w = ''
    while r_w == '':
        r_we = input('Read [R] or Write [W] > ')
        r_we = r_we.upper()
        if r_we == 'R':
            read_n(file_name)
        elif r_we == 'W':
            write_n(file_name)
        else:
            r_we = ''
    '''


input_n()
