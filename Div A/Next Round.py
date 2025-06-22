n, k = map(int, input().split())
a = list(map(int, input().split()))

comp = a[k - 1]
count = 0

for person in a:
    if person >= comp and person > 0:
        count += 1

print(count)
