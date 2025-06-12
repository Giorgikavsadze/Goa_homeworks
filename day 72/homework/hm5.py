# Find the next perfect square!

def find_next_square(sq):
    root = int(sq ** 0.5)
    if root * root != sq:
        return -1
    return (root + 1) ** 2