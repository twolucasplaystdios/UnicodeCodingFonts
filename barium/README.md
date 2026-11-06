<div align="center">

[![jf 7000 Core Set Supported](https://img.shields.io/badge/jf_7000-覆蓋率約30%25-66AC35?logo=data:image/svg+xml;base64,PHN2ZyBkYXRhLW5hbWU9IuWcluWxpCAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxOTMuMDcgMjQ3LjM4Ij48Y2lyY2xlIGN4PSI5Ni41MyIgY3k9Ijk2LjU5IiByPSI5Ni40NCIgc3R5bGU9ImZpbGw6I2ZmZiIvPjxwYXRoIGQ9Ik05NjAgNDE2LjMxYTk2LjU0IDk2LjU0IDAgMSAwIDAgMTkzLjA3YzIuOCAwIDUuNS0uMTQgOC4yMy0uMzdWNDg0LjQ0YTI5LjM1IDI5LjM1IDAgMCAxIDI5LjI1LTI5LjI1IDYyLjYgNjIuNiAwIDAgMSAxMi43MyAxLjMzYzMuOC45IDYuMjUgMy44IDYuMjUgNy4zNyAwIDQuNjktMy44IDcuMTQtNy4zNyA3LjE0LTMuNzkgMC02LjQ4LTEuMzMtMTEuNjEtMS4zM2ExNCAxNCAwIDAgMC0xNC4wNiAxNC4wNnYxOC4zaDI1LjY3YTcuMjkgNy4yOSAwIDAgMSA3LjM3IDcuMzcgNy4xIDcuMSAwIDAgMS03LjM3IDcuMTRoLTI1LjY2djg5Ljk0QTk2LjU0IDk2LjU0IDAgMCAwIDk2MCA0MTYuMzEiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC04NjMuNDYgLTQxNi4zMSkiIHN0eWxlPSJmaWxsOiNhOWFhYTkiLz48cGF0aCBkPSJNNjQuNjEgMzguODhhMTAgMTAgMCAwIDAtMTAuMDcgMTAuMDUgMTAuMDUgMTAuMDUgMCAxIDAgMjAuMSAwIDEwIDEwIDAgMCAwLTEwLTEwLjA1bS0uMDMgNDQuNjRhNy42NyA3LjY3IDAgMCAwLTcuNTkgNy41OVYyMDYuM2MwIDE0LjA3LTcuMTQgMjMuODktMTkuNDEgMjYuNzlhNi45MyA2LjkzIDAgMCAwLTUuODEgNi45MiA3LjIzIDcuMjMgMCAwIDAgNy4xNCA3LjM3IDEwIDEwIDAgMCAwIDIuMjQtLjIzYzE4Ljc0LTMuNTcgMzEtMjAuNTQgMzEtNDEuNTJWOTEuMTFhNy42NyA3LjY3IDAgMCAwLTcuNTktNy41OSIgc3R5bGU9ImZpbGw6IzU5NWE1OSIvPjwvc3ZnPg==&style=flat-square)](https://github.com/justfont/jf7000)

</div>

# 一、覆蓋率

在jf-7000當務字集裡面的字元：$2177$個字元

覆蓋率：約$32.1\%$

## 專案根目錄測試方式 （Linux Bash）

```bash
# 下載此專案
git clone https://github.com/twolucasplaystdios/UnicodeCodingFonts.git

# 啟動虛擬環境
python -m venv .venv
source .venv/bin/activate

# 安裝需要模組
pip install -r requirements.txt

# 在專案根目錄
python -m barium.coverage_support
```

# 二、元素週期表預覽

安裝時應顯示（截圖於Arch Linux + KDE Plasma）：

![元素週期表圖（預期SVG）](/readme_img/barium/p_table_sim.png)

字體顯示結果：
![元素週期表圖（SVG）](/readme_img/ptable.svg)


可複製文字：
```
氫　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　氦
鋰鈹　　　　　　　　　　　　　　　　　　　　　　　　硼碳氮氧氟氖
鈉鎂　　　　　　　　　　　　　　　　　　　　　　　　鋁矽磷硫氯氬
鉀鈣　　　　　　　　　　　　　　鈧鈦釩鉻錳鐵鈷鎳銅鋅鎵鍺砷硒溴氪
銣鍶　　　　　　　　　　　　　　釔鋯鈮鉬鎝釕銠鈀銀鎘銦錫銻碲碘氙
銫鋇鑭鈰鐠釹鉕釤銪釓鋱鏑鈥鉺銩鐿鎦鉿鉭鎢錸鋨銥鉑金汞鉈鉛鉍釙砈氡
鍅鐳錒釷鏷鈾錼鈽鋂鋦鉳鎦鑀鐨鍆鍩鐒鑪𨧀𨭎𨨏𨭆䥑鐽錀鎶鉨鈇鏌鉝鿬鿫
```
# 設定
## VS Code
```json
{
    "editor.fontFamily": "Cascadia Code, Barium Mono", // Cascadia Code 當 fallback 是因為尚未支援其他語言、連字或斜體
    "editor.fontLigatures": true, // 啟用連字（不強迫）
}
```
**注意！ `Cascadia Code` 一定要放前面！不然斜體會很醜**


