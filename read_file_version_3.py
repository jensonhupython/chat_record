# 流程: 
# 1. 解釋流程目標
# 2. 寫程式碼來讀取檔案
# 3. 解釋字串的切割
#    清單分割法
# 4. 建立版本上傳
# note: 檔案如果有中文, compile容易有編碼問題

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    #print('時間: ', time) 
    print('人名: ', name)       