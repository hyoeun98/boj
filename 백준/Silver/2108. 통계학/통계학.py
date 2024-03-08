import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
print(round(sum(nums) / len(nums)))
print(nums[len(nums) // 2])
most_common = Counter(nums).most_common(2)
if len(most_common) == 1:
    print(nums[0])
else:
    if most_common[0][1] > most_common[1][1]:
        print(most_common[0][0])
    else:
        print(most_common[1][0])
print(abs(nums[-1] - nums[0]))