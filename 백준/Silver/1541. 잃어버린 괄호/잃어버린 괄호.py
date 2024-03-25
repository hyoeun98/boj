import sys    
import re

method = sys.stdin.readline().strip()
nums = list(map(int, re.findall("[0-9]+", method)))
op = re.findall("[+-]", method)

start = -1
for i, v in enumerate(op):
    if v == "-":
        nums[i + 1] = -nums[i + 1]
        start = i + 1
    
    elif v == "+" and start != -1:
        nums[i + 1] = -nums[i + 1]
    
print(sum(nums))
