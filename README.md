# Python_Basuc to library in re

- Extract only the specified `string`:
    ```python
    import re


    match = re.search(r'\((PA-IP\d{2,}-\d{3})[A-Z]?\)', s)
    ```
- To avoid "SettingWithCopyWarning", use `.loc`:
    ```python
    df.loc[condition, 'col'] = value
    ```
