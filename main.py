# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from neetcode import array_hash, two_pointers, sliding_window


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    so = sliding_window.Solution()
    nums = [7, 2, 4]
    k = 2

    res = so.max_sliding_window(nums, k)
    print('result', res)
