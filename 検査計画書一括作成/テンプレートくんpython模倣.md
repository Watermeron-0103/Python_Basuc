# 01_前情報取得(改訂用)

| 処理内容                 | VBAでのやり方                         | Pythonでのやり方（再実装）                      |
| -------------------- | -------------------------------- | ------------------------------------- |
| ① 前情報取得(改定用)         | `前回の検査計画書`から必要項目を読み出して、現在のシートに転記 | `openpyxl`で前ファイルからセルを読み出し、テンプレートに書き戻す |
| ② 空欄セルの色塗り（警告）       | `ColorIndexClear()` でセルに背景色を設定   | `openpyxl.styles.PatternFill` で色を塗る   |
| ③ 検査内容の補完（1枚目などから）   | VBAで「1枚目」「外観検査」などから転記            | `pandas`や`openpyxl`で外部シートを検索して転記      |
| ④ 検査種類（抜取・全数など）の自動判定 | `kensasyurui()` 関数               | Pythonで同じロジックをif文で再現                  |

- 以下のVBAコードをpython化
vba
```vba
With Worksheets("検査計画書")
  For i = 7 To 50
    If .Cells(i, 27) = "" Then Exit For
    .Cells(i, 27).Value = Worksheets("前回").Cells(i, 27).Value
    .Cells(i, 30).Value = Worksheets("前回").Cells(i, 30).Value
    ' ...
  Next i
End With
```

python
```python
for row in range(7, max_row + 1):
    for col_name, col_num in COLUMNS_TO_COPY.items():
        value = prev_ws.cell(row=row, column=col_num).value
        new_ws.cell(row=row, column=col_num).value = value

```
