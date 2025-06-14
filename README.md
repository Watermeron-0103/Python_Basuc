# Python_Basuc to library in re

# Tips for Using Pandas

- Always check for missing values:
    ```python
    df.isnull().sum()
    ```
- To avoid "SettingWithCopyWarning", use `.loc`:
    ```python
    df.loc[condition, 'col'] = value
    ```
