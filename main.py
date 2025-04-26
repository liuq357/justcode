# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from neetcode import (
    array_hash,
    two_pointers,
    sliding_window,
    stack
)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    so = stack.Solution()
    tokens = ["4", "13", "5", "/", "+"]
    res = so.eval_RPN(tokens)
    print("res", res)
