import os
import shutil
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox


excel_path = r"\\fujifilm0.sharepoint.com@ssl\DavWWWRoot\sites\jp-dms-hcm1\08\DocLib4\18. 検査計画書\受入れ検査品リスト(次回申請リスト).xlsx"
search_dir = r"\\fujifilm0.sharepoint.com@ssl\DavWWWRoot\sites\jp-dms-hcm1\08\DocLib4\18. 検査計画書\図面+EXCEL(申請前)"
output_parent = r"\\fujifilm0.sharepoint.com@ssl\DavWWWRoot\sites\jp-dms-hcm1\08\DocLib4\18. 検査計画書\図面+EXCEL(申請前)\old"

sheet_names = pd.ExcelFile(excel_path).sheet_names

root = tk.Tk()
root.title("シート選択してフォルダ作成")

label = ttk.Label(root, text="シートを選択してください:")
label.pack(pady=5)

selected_sheet = tk.StringVar()
combobox = ttk.Combobox(root, textvariable=selected_sheet, values=sheet_names, state="readonly")
combobox.current(0)
combobox.pack(pady=5)

def make_folder_and_move():
    target_sheet = selected_sheet.get()
    today_str = datetime.today().strftime("%Y.%m.%d")
    folder_name = f"{today_str}申請_{target_sheet}"
    os.makedirs(output_parent, exist_ok=True)
    full_folder_path = os.path.join(output_parent, folder_name)
    os.makedirs(full_folder_path, exist_ok=True)

    # --- ここから：選択シート名を含むフォルダ検索＆移動 ---
    matched_folders = [
        os.path.join(search_dir, name)
        for name in os.listdir(search_dir)
        if os.path.isdir(os.path.join(search_dir, name)) and target_sheet in name
    ]
    for folder_path in matched_folders:
        dest_path = os.path.join(full_folder_path, os.path.basename(folder_path))
        shutil.move(folder_path, dest_path)
    # --- ここまで ---
    messagebox.showinfo("完了", f"フォルダを作成＆移動しました：\n{full_folder_path}")

button = ttk.Button(root, text="フォルダ作成と移動", command=make_folder_and_move)
button.pack(pady=10)

root.mainloop()
