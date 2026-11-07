from fontTools.ttLib import TTFont
import os
import subprocess
import datetime

from rich import print

from fnt_path_connector import local_base_dir

subprocess.call("clear")

base_dir = os.path.dirname(os.path.abspath(__file__))


chars = []

with open(os.path.join(base_dir, f"assets/jf7000.txt"), "r+") as curr_out:
    for c in curr_out.read():
        if c == "\n" or c == " ":
            continue
        char_code = ord(c)
        chars.append(c)
    chars.sort(key=(lambda x: ord(x)))
    output_content = "\n".join("".join(chars[i:i+30]) for i in range(0, len(chars), 30))
    
    with open(os.path.join(base_dir, f"assets/jf7000.txt"), "r+") as out:
        out.write(output_content)

print(f"[green bold]成功！共有 {len(chars)} 個字元[/green bold]")