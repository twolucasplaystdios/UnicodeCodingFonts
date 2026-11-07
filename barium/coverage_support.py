from fontTools.ttLib import TTFont
import os
import subprocess
import datetime

from rich import print

from fnt_path_connector import local_base_dir

subprocess.call("clear")

def get_font_characters(font_path):
    # 載入字型檔案 (支援 ttf, otf, woff 等)
    font = TTFont(font_path)
    
    # 用來儲存所有字元的集合（避免不同 cmap 表格重複紀錄）
    characters = set()
    
    # 取得字型的 cmap 表格
    cmap_table = font['cmap']
    
    # 遍歷所有的子表格 (不同平台或編碼的映射表)
    for table in cmap_table.tables:
        # table.cmap 是一個字典，Key 是 Unicode 的 10 進位碼 (int)，Value 是字形名稱
        for char_code in table.cmap.keys():
            try:
                # 將 10 進位編碼轉換為真正的字元
                if char_code < 32: continue
                char = chr(char_code)
                characters.add(char)
            except ValueError:
                # 忽略超出 Unicode 範圍的異常編碼
                continue
                
    font.close()
    
    # 將結果排序後回傳（依 Unicode 順序）
    return sorted(list(characters))


base_dir = os.path.dirname(os.path.abspath(__file__))
font_file = os.path.join(base_dir, "barium.ttf")

all_chars = get_font_characters(font_file)

# 印出總共支援多少個字元
print(f"總共找到 {len(all_chars)} 個可用字元")

global_charset = ""
global_charset_dir = os.path.join(local_base_dir, "globals/jf7000.txt")

with open(global_charset_dir, "r") as file:
    global_charset = file.read()

# with open("filled_chars.txt", "w+") as out:
#     out.write("".join(all_chars))


final_chars = []
in_charset = 0
c_id = 0

for c in global_charset:
    if c in all_chars:
        in_charset += 1
    else:
        c_id += 1
        final_chars.append(c)        

final_str = "".join(final_chars)

output_content = "\n".join(final_str[i:i+30] for i in range(0, len(final_str), 30))

curr_datetime = datetime.datetime.now()  # 當前本地日期與時間
str_dt = curr_datetime.strftime("%Y-%m-%d-%H-%M-%S")

with open(os.path.join(base_dir, f"chars_missed.txt"), "w+") as curr_out:
    with open(os.path.join(base_dir, f"chars_missed-{str_dt}.txt"), "w+") as old_out:
        final = curr_out.read()
        old_out.write(final)
        curr_out.write(output_content)

print()
print(f"資料（尚未在字集）已儲存成功！")

print(f"在基礎當務字集裡面的字：{in_charset} / {len(global_charset)}")
print(f"覆蓋率： 約 { round(in_charset / len(global_charset) * 100, 2) } %")