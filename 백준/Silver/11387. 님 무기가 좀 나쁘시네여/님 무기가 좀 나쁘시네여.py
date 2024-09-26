import sys

def calc(attack, str, crit, crit_dmg, speed):

    result = attack * (100 + str) * (100 * (100 - min(100, crit)) + min(crit, 100) * crit_dmg) * (100 + speed)
    # print(result)
    return result

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))
score_a = calc(*a)
score_b = calc(*b)

no_weapon_a = [a[i] - c[i] for i in range(5)]
no_weapon_b = [b[i] - d[i] for i in range(5)]

reverse_weapon_a = [no_weapon_a[i] + d[i] for i in range(5)]
reverse_weapon_b = [no_weapon_b[i] + c[i] for i in range(5)]

reverse_score_a = calc(*reverse_weapon_a)
reverse_score_b = calc(*reverse_weapon_b)

if score_a > reverse_score_a:
    print("-")
elif score_a == reverse_score_a:
    print("0")
else:
    print("+")
    
if score_b > reverse_score_b:
    print("-")
elif score_b == reverse_score_b:
    print("0")
else:
    print("+")