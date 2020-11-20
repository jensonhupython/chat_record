# 第二種讀取聊天紀錄
# 做統計, 圖片, 對話內容, 符號 ...
# 怎麼分別取出 時間 人名 對話 ?  split

def read_file(filename):
    lines = []
    with open (filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())  #strip()將換行符號去掉
    return lines

def convert(lines):
    person = None   #就是 NULL 的意思
    new_list = []
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count = 0
    viki_image_count = 0
    for line in lines:
        split_list = line.split(' ')  #字串用split功能, 遇到空白分割
        time = split_list[0]
        name = split_list[1]
        if name == 'Allen':
            #print(split_list[2:])  # 取s[2]後面的資料
            if split_list[2] == '貼圖':
                allen_sticker_count += 1
            elif split_list[2] == '圖片':
                allen_image_count += 1
            else: 
                for msg in split_list[2:]:
                    allen_word_count += len(msg)

        elif name == 'Viki':
            #print(split_list[2:])
            if split_list[2] == '貼圖':
                viki_sticker_count += 1  
            elif split_list[2] == '圖片':
                 viki_image_count += 1
            else:          
                for msg in split_list[2:]:
                    viki_word_count += len(msg)
       
    print('Allen 說了', allen_word_count, '個字')               
    print('Allen 說了', allen_sticker_count, '個貼圖')
    print('Allen 說了', allen_image_count, '張圖片')
    print('Viki 說了', viki_word_count, '個字')
    print('Viki 說了', viki_sticker_count, '個貼圖')
    print('Viki 說了', viki_image_count, '張圖片')

    return new_list

def write_file(filename, new_lines):
    with open(filename, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

def main():
    lines = read_file('LINE-Viki.txt') 
    new_lines = convert(lines)
    #print(lines) 
    #write_file('output.txt', new_lines)

main()    


