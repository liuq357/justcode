# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from neetcode import array_hash


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = array_hash.Solution()
    # strs = ["eat","tea","tan","ate","nat","bat"]
    nums = [-1, 1, 0, -3, 3]
    print("result", s.productExceptSelf(nums))
