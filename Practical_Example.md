# Practical Example

- Advanced use of the standard library
    ```PYTHON
    import pandas as pd
    import pathlib
    import shutil
    import datetime
    import os
    
    def main():
        # パス設定Excelの読み込み
        ws_path = pd.read_excel(
            r"c:\Users\11064667.FFWIN\OneDrive - FUJIFILM\02. 検査計画書\tool\Projects__\受入れ検査品リスト○○\format_data\【Python】-受入れ検査品リスト○○.xlsx",
            sheet_name="パス設定",
            header=None
        )
    
        # 各パラメータ（ゼロベースかワンベースかは状況で調整）
        base_path = ws_path.iloc[2, 2]   # C3
        base_folder = ws_path.iloc[2, 3] # D3
        base_file = ws_path.iloc[2, 4]   # E3
    
        # コピー元ファイルパス
        src_file = f"{base_path}/{base_folder}{base_file}"
        print(f"取得したコピー元pathは : {src_file}")
    
        # コピー先フォルダ
        dest_folder = ws_path.iloc[6, 2] # C7
    
        # 今日の日付を YYYYMMDD 形式で取得
        today = datetime.datetime.now().strftime("%Y%m%d")
    
        # 元のファイル名（拡張子付き）
        original_filename = pathlib.Path(src_file).name
    
        # コピー先ファイル名（日付＋元名）
        dest_filename = f"{today}_{original_filename}"
    
        dest_file_path = os.path.join(dest_folder, dest_filename)
    
        # コピー処理
        shutil.copy2(src_file, dest_file_path)
        print(f"copyted file to : {dest_file_path}")
    
    if __name__ == "__main__":
        main()
    ```
