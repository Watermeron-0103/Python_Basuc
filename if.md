# About_if_statements

The if statement is a basic branching grammar that says "if the condition is true, perform this process.

- Basic for
    ```python
    if 条件:
        # 条件がTrueのとき実行
    ```

    -sample
    ```python
    score = 80
    if score >= 70:
        print("合格！")  # 70点以上なら「合格！」と表示
    ```

    - else
    ```python
    if score >= 70:
        print("合格！")
    else:
        print("不合格…")
    ```

    - elif
    ```python
    score = 60
    if score >= 80:
        print("とても良い！")
    elif score >= 70:
        print("合格！")
    else:
        print("不合格…")
    ```

Summary
- if condition: → Execute if the condition is True
- elif condition: → When you want to add another condition
- else: → When none of the conditions apply

