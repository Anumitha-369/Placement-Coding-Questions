n = int(input())
words = input().split()

count = 0

for i in range(n):
    if len(words[i]) % 2 != 0:
        print(words[i])
        count = count + 1
        break

if count == 0:
    print("Better luck next time")
