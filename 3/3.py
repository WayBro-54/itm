lst = [int(i) for i in input().split()]

i = 0
curr_res = 0

while i <= len(lst):
    curr_res += lst[0]
    i += 1

res = curr_res / 2

print(res)
