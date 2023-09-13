# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from neetcode import array_hash, blind


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    so = blind.Solution()
    s = " "
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print("result", so.maxSubArray(nums))
