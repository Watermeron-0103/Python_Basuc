# Practical Example

- Advanced use of the standard library
    ```PYTHON
    import pandas as pd
    import pathlib
    import shutil
    import datetime
    import os

    
    def main():

        # コピー元ファイルパス
        src_file = "sample_excel_file.xlsx"
    
        # コピー先フォルダ
        dest_folder = "sample_directry/"
    
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
