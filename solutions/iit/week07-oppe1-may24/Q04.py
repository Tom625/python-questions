def run_length_encoding(num:str) -> str:
    encoding = []
    prev_digit = num[0]
    count = 1
    for digit in num[1:]:
        if digit != prev_digit:
            encoding.extend([count, prev_digit])
            count = 0
        count +=1
        prev_digit=digit
    encoding.extend([count, prev_digit])
    return " ".join(map(str,encoding))

n = int(input())
for i in range(n):
    print(run_length_encoding(input()))
