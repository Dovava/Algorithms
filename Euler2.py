prior = 1
current = 2
data = []
ans = 0
while not current > 4000000:
                current += prior
                prior = current - prior
                if current % 2 == 0:
                                data.append(current)
for i in range(0,len(data)):
                ans += data[i]
print(ans)
