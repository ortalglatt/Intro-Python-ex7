OPEN_PAR = '('
CLOSE_PAR = ')'
RIGHT = 'r'
UP = 'u'
STAR = '*'
DOT = '.'
ROW = 0
COL = 1


# Part A


def print_to_n(n):
    """This function gets an int 'n'. If n is bigger then 0, the function will
    print all the numbers from 1 to n, every number in a different line."""
    if n == 1:
        print(1)
    elif n > 1:
        print_to_n(n-1)
        print(n)
    return


def print_reversed(n):
    """This function gets an int 'n'. If n is bigger then 0, the function will
    print all the numbers from 1 to n when the numbers are going down.
    every number is printed in a different line."""
    if n == 1:
        print(1)
    elif n > 1:
        print(n)
        print_reversed(n-1)
    return


def is_prime(n):
    """This function gets a number and return True if it's a prime number, and
    False if it's not prime."""
    if 1 >= n or n % 1 != 0:
        return False
    else:
        return not has_divisor_smaller_then(n, int((n ** 0.5) + 1))


def has_divisor_smaller_then(n, i):
    """This function gets two ints - 'n' and 'i'. If n divided by a number
    between 1 to i, the function returns True. Otherwise, the function returns
    False."""
    if 2 >= i:
        return False
    elif n % (i-1) == 0:
        return True
    return has_divisor_smaller_then(n, i-1)


def exp_n_x(n, x):
    """This function gets 2 numbers, 'n' - int and 'x' - float.
    The function returns the exponential sum function of (n, x), an
    approximation for e^x."""
    if n == 0:
        return 1
    else:
        return exp_n_x(n-1, x) + (x ** n)/factorial(n)


def factorial(n):
    """This function gets a number typed int, and returns the factorial of the
    number."""
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n


# Part B


def play_hanoi(hanoi, n, src, dest, temp):
    """This function solve the game 'Towers of Hanoi'.
    The function gets the graphic object - 'hanoi', the number of discs - 'n',
    the rod that the discs will be on when the game begin - 'src', the rod that
    the discs will be on at the end of the game - 'dest', and the third rod -
    'temp'."""
    if n == 1:
        hanoi.move(src, dest)
    elif n > 1:
        play_hanoi(hanoi, n-1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n-1, temp, dest, src)


def print_sequences(char_list, n, string=""):
    """This function gets a list of different characters - 'char_list and a
    number -'n'. The function will print all the combinations of the characters
    in the list that their length is n (with repetition)."""
    if n == 0:
        if string != "":
            print(string)
    else:
        for char in char_list:
            print_sequences(char_list, n-1, string + char)


def print_no_repetition_sequences(char_list, n, string=""):
    """This function gets a list of different characters - 'char_list and a
    number -'n'. The function will print all the combinations of the characters
    in the list that their length is n without repetition."""
    if n == 0:
        if string != "":
            print(string)
    else:
        for i in range(len(char_list)):
            print_no_repetition_sequences(char_list[:i] + char_list[i+1:], n-1,
                                          string + char_list[i])


def parentheses(n):
    """This function gets a number, and return a list of all the mathematically
    legal combinations of n pairs of parentheses."""
    result = list()
    help_parentheses(n, result)
    return result


def help_parentheses(n, result, string=OPEN_PAR):
    """This function gets a number, a result list (empty), and add all the
    mathematically legal combinations of n pairs of parentheses to the result
    list."""
    open_num = string.count(OPEN_PAR)
    close_num = string.count(CLOSE_PAR)
    if len(string) == 2 * n:
        result.append(string)
        return
    if open_num < n:
        help_parentheses(n, result, string + OPEN_PAR)
    if open_num > close_num:
        help_parentheses(n, result, string + CLOSE_PAR)


def up_and_right(n, k, string=""):
    """This function gets two numbers - 'n' is the number of steps to the
    right, and 'k' is the numbers of steps up. The function prints all the
    optional ways to go from the point (0,0) to the point (n,k) when every step
    can be only up or right."""
    right_num = string.count(RIGHT)
    up_num = string.count(UP)
    if len(string) == n+k:
        if string != "":
            print(string)
            return
    if right_num < n:
        up_and_right(n, k, string + RIGHT)
    if up_num < k:
        up_and_right(n, k, string + UP)


def flood_fill(image, start):
    """This function gets an image -  list of sub-lists of stars and dots, and
    a start point. The function will change every point in the image that you
    can reach from the start point without passing on stars, to a star."""
    row = start[ROW]
    col = start[COL]
    image[row][col] = STAR
    if image[row][col - 1] == DOT:
        flood_fill(image, (row, col - 1))
    if image[row][col + 1] == DOT:
        flood_fill(image, (row, col + 1))
    if image[row + 1][col] == DOT:
        flood_fill(image, (row + 1, col))
    if image[row - 1][col] == DOT:
        flood_fill(image, (row - 1, col))
