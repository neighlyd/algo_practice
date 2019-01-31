from collections import deque


def palindrome_check(word):
    char_deque = deque(word)

    while len(char_deque) > 1:
        left = char_deque.popleft()
        right = char_deque.pop()
        if left != right:
            return False

    return True


assert palindrome_check('lkasdjfubu') is False
assert palindrome_check('radar') is True

