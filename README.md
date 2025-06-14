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


- To avoid "SettingWithCopyWarning", use `.loc`:
    ```python
    df.loc[condition, 'col'] = value
    ```
