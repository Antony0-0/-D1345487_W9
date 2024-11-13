def collatz(n):
    if n <= 0:
        return "請輸入正整數！"
    steps = 0
    sequence = [n]
    while n != 1:
        if n % 2 == 0: 
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        steps += 1
    print(" -> ".join(map(str, sequence)))
    print(f"總共步數：{steps}")
n = int(input("請輸入一個正整數："))
collatz(n)