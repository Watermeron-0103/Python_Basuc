# Here's how to move and copy files. *（shutil:シュータイル）*
Just import shutil to get started.

- shutil is a Python standard library that copies, moves, and deletes files and directories.
    - Copy source.txt to destination.txt (only the contents, timestamp will change)
    ```python
    import shutil
    
    shutil.copy('source.txt', 'destination.txt')
    ```

    - Copy timestamps etc. as is (including metadata)
    ```python
    shutil.copy2('source.txt', 'destination.txt')
    ```

    - Move and rename old_name.txt to new_folder/new_name.txt (renam)
    ```
    shutil.move('old_name.txt', 'new_folder/new_name.txt')
    ```

    - Copy src_folder with all its contents to dst_folder
    ```python
    shutil.copytree('src_folder', 'dst_folder')
    ```

    - Delete the entire folder_to_delete (including its contents!)
    ```python
    shutil.rmtree('folder_to_delete')
    ```
***【まとめ：一行レシピ】***
|      操作      |                コード例               |
| :----------: | :-------------------------------: |
|      コピー     |   shutil.copy("a.txt", "b.txt")   |
| コピー（メタデータ付き） |   shutil.copy2("a.txt", "b.txt")  |
|    移動/リネーム   | shutil.move("a.txt", "dir/b.txt") |
|  ディレクトリごとコピー |   shutil.copytree("src", "dst")   |
|  ディレクトリごと削除  |        shutil.rmtree("dir")       |
