# *How to rename files and folders in the os library*

Renaming a file or folder in the os library is very simple.
- Basic usage
    ```python
    import os

    # 例：ファイル名を変更
    old_path = "old_name.txt"
    new_path = "new_name.txt"
    
    os.rename(old_path, new_path)
    ```

- Same for folders
    ```python
    import os
    
    old_folder = "old_folder"
    new_folder = "new_folder"
    
    os.rename(old_folder, new_folder)
    ```

- Application example: Bulk change of file extensions (example)
    ```python
    import os
    
    for file in os.listdir('.'):
        if file.endswith('.txt'):
            new_name = file.replace('.txt', '.md')
            os.rename(file, new_name)
    ```
