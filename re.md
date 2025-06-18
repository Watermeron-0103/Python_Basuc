# Python_Basuc to library in re

- Extract only the specified `string`:
    ```python
    import re

    
    def extract_document_number(s):
        match = re.search(r'\((PA-IP\d{2,}-\d{3})[A-Z]?\)', s)
        if match:
            return match.group(1)
    
        match = re.search(r'\((PA-IP\d{2,}-\d{3})[A-Z]?\((KAF)\)\)', s)
        if match:
            return match.group(1)
    
        return None
    ```

- Below is a practical example:
    ```python
    
    import pandas as pd
    import re
    
    
    file_path = "Document_KMS_summary.xlsx"
    df = pd.read_excel(file_path, sheet_name="3_or_more_KMS_summary")
    
    def extract_document_number(s):
        match = re.search(r'\((PA-IP\d{2,}-\d{3})[A-Z]?\)', s)
        if match:
            return match.group(1)
    
        match = re.search(r'\((PA-IP\d{2,}-\d{3})[A-Z]?\((KAF)\)\)', s)
        if match:
            return match.group(1)
    
        return None
    
    df['文書番号'] = df['検査計画書品番'].apply(extract_document_number)
    
    cols = df.columns.tolist()
    cols = ['文書番号'] + [col for col in cols if col != '文書番号']
    df = df[cols]
    
    with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        # Write the DataFrame to the Excel file
        df.to_excel(writer, index=False, sheet_name="document_number_contains_3_or_more_KMS")
    ```

- To avoid "SettingWithCopyWarning", use `.loc`:
    ```python
    df.loc[condition, 'col'] = value
    ```
