from fontTools.ttLib import TTFont
import os
import subprocess

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



in_charset = 0

final_chars = []
c_id = 0

for c in global_charset:
    if c in all_chars:
        in_charset += 1
    else:
        final_chars.append(c)
        if (c_id % 30 == 0):
            final_chars.append("\n")
        print(c, end="")
    c_id += 1

with open("chars.txt", "w+") as out:
    out.write("".join(final_chars))

print()

print(f"在基礎當務字集裡面的字：{in_charset} / {len(global_charset)}")
print(f"覆蓋率： 約 { round(in_charset / len(global_charset) * 100, 2) } %")