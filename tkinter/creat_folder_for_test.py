import os
import shutil
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox


excel_path = r"\\fujifilm0.sharepoint.com@ssl\DavWWWRoot\sites\jp-dms-hcm1\08\DocLib4\18. 検査計画書\受入れ検査品リスト(次回申請リスト).xlsx"
search_dir = r"\\fujifilm0.sharepoint.com@ssl\DavWWWRoot\sites\jp-dms-hcm1\08\DocLib4\18. 検査計画書\図面+EXCEL(申請前)\●検査計画書回覧\06. 赤坂"
output_parent = r"\\fujifilm0.sharepoint.com@ssl\DavWWWRoot\sites\jp-dms-hcm1\08\DocLib4\18. 検査計画書\図面+EXCEL(申請前)\●検査計画書回覧\07. 回覧終了済"

sheet_names = pd.ExcelFile(excel_path).sheet_names

# --- シート名を "2025.6.4" → "20250604" のように正規化 ---
def normalize_sheet_name(sheet_name):
    parts = sheet_name.split('.')
    if len(parts) == 3:
        year = parts[0]
        month = parts[1].zfill(2)
        day = parts[2].zfill(2)
        return f"{year}{month}{day}"
    else:
        # 万一パターンが違う場合はドット削除のみ
        return sheet_name.replace('.', '')

# --- tkinter GUI 設定 ---
root = tk.Tk()
root.title("シート選択してファイル移動")

label = ttk.Label(root, text="シートを選択してください:")
label.pack(pady=5)

selected_sheet = tk.StringVar()
combobox = ttk.Combobox(root, textvariable=selected_sheet, values=sheet_names, state="readonly")
combobox.current(0)
combobox.pack(pady=5)

def make_folder_and_move_files():
    target_sheet = selected_sheet.get()
    folder_name = normalize_sheet_name(target_sheet)
    os.makedirs(output_parent, exist_ok=True)
    full_folder_path = os.path.join(output_parent, folder_name)
    os.makedirs(full_folder_path, exist_ok=True)

    # --- 指定ディレクトリ内でシート名を含むファイルを探して移動 ---
    matched_files = [
        os.path.join(search_dir, name)
        for name in os.listdir(search_dir)
        if os.path.isfile(os.path.join(search_dir, name)) and target_sheet in name
    ]
    for file_path in matched_files:
        dest_path = os.path.join(full_folder_path, os.path.basename(file_path))
        shutil.move(file_path, dest_path)
    messagebox.showinfo("完了", f"フォルダを作成＆ファイルを移動しました：\n{full_folder_path}")

button = ttk.Button(root, text="フォルダ作成とファイル移動", command=make_folder_and_move_files)
button.pack(pady=10)

root.mainloop()
