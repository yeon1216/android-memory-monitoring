import matplotlib.pyplot as plt

f = open('meminfo.txt', mode="rt", encoding='utf-8')
timeMemoryStr = f.read()

timeMemoryList = []
timeList = []
memoryList = []

timeMemoryList = timeMemoryStr.split('\n')

for tempStr in timeMemoryList:
    if tempStr.strip()=='':
        break
    tempList = tempStr.split(',')
    if tempList[1].strip()=='':
        continue
    timeList.append(tempList[0])
    memoryList.append((int)(tempList[1]))

plt.plot(timeList,memoryList)
plt.show()