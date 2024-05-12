import sys

n, game = sys.stdin.readline().split()
n = int(n)
player = set()
for _ in range(n):
    player.add(sys.stdin.readline().strip())
    
if game == "Y":
    print(len(player))
elif game == "F":
    print(len(player) // 2)
else:
    print(len(player) // 3)