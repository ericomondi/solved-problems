# You are given a string s and width  w.
# Your task is to wrap the string into a paragraph of width w.
import textwrap
def wrap(string, max_width):
    s = textwrap.fill(string, max_width)
    return s


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

