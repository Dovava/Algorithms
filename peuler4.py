question = []
ans = []
anse = 0
anse2 = 0
for i in range(100,999):
                for i2 in range(100,999):

                                if int(str(i*i2)[::-1]) == i * i2:
                                                ans.append(i*i2)
                                                question.append(f'{i}x{i2}')
for i3 in range(0,len(ans)):
                if anse < ans[i3]:
                                anse = ans[i3]
                                anse2 = question[i3]
print(anse)
print(anse2)

