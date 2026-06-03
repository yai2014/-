with open('dataset_3363_2 (12).txt', 'r') as inf:
    s = inf.readline().strip()

result = ''
i = 0
while i < len(s):
    letter = s[i]
    i += 1
    num_str = ''
    while i < len(s) and s[i].isdigit():
        num_str += s[i]
        i += 1
    if num_str:
        result += letter * int(num_str)

print(result)