def print_rangoli(size):
    # your code goes here
    lines = []
    for i in range(1, size + 1):
        lines.append(
            '-' * (i - 1) * 2 +
            '-'.join([chr(x+97) for x in range(size - 1, i - 2, -1)].__add__(
                [chr(x+97) for x in range(i, size)])) + '-' * (i - 1) * 2
                )
    [print(a) for a in list(reversed(lines)).__add__(lines[1:])]
    return ()
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)