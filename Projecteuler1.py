data = []
ans = 0
for i in range(999):
                if i / 3 == i // 3 or i / 5 == i // 5:
                                data.append(i)
for i2 in range(0,len(data)):
                ans += data[i2]
print(ans)
