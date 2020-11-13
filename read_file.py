# 1.寫一個 function 讀出文字檔內容
# 2.寫一個 function 轉換聊天內容格式

def read_file(filename):
    lines = []
    with open (filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())  #strip()將換行符號去掉
    return lines

def convert(lines):
    new_list = []
    person = None   #就是 NULL 的意思
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new_list.append(person + ':' + line)
    #print(new_list)
    return new_list

def write_file(filename, new_lines):
    with open(filename, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt') 
    new_lines = convert(lines)
    #print(lines) 
    write_file('output.txt', new_lines)

main()    


