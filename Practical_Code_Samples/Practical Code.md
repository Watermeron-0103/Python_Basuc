# Practical Code [Office 365 Edition]
- Save SharePoint files locally
    ```python
    import pandas as pd
    import datetime
    import shutil
    from office365.sharepoint.client_context import ClientContext
    from office365.runtime.auth.user_credential import UserCredential
    
    
    today = datetime.datetime.now().strftime("%Y%m%d")
    
    # SharePoint接続情報
    site_url = "https://fujifilm0.sharepoint.com/sites/jp-dms-hcm1"
    username = "11064667@003.fujifilm.com"
    password = "Watermelon02"
    
    ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
    
    # ダウンロード元ファイルの相対パス（SharePoint上）
    server_relative_url = "/sites/jp-dms-hcm1/08/DocLib4/18. 検査計画書/受入れ検査品リストVer1_2021.5.31  .xlsx"
    old_server_relative_url = "/sites/jp-dms-hcm1/08/DocLib4/18. 検査計画書/受入れ検査品リストVer1_2021.5.31  (旧文書).xlsx"
    
    
    # 保存先のローカルフルパス
    local_file_path = rf"C:\Users\zlocal\OneDrive - FUJIFILM\02. 検査計画書\受入れ検査品リストVer1_2021.5.31\受入れ検査品リストVer1_2021.5.31_output\{today}_受入れ検査品リストVer1_2021.5.31  .xlsx"
    old_local_file_path = rf"C:\Users\zlocal\OneDrive - FUJIFILM\02. 検査計画書\受入れ検査品リストVer1_2021.5.31\受入れ検査品リストVer1_2021.5.31旧文書_output\{today}_受入れ検査品リストVer1_2021.5.31  (旧文書).xlsx"
    
    # SharePointからダウンロードしてローカルに保存
    with open(local_file_path, "wb") as local_file:
        file_response = ctx.web.get_file_by_server_relative_url(server_relative_url).download(local_file).execute_query()
    # SharePointからダウンロードしてローカルに保存
    with open(old_local_file_path, "wb") as local_file:
        file_response = ctx.web.get_file_by_server_relative_url(old_server_relative_url).download(old_local_file_path).execute_query()
    
    
    print("✅ Download complete.")
    
    
    # ログ書き込み関数の定義
    def log(message):
        with open(r'C:\Users\zlocal\OneDrive - FUJIFILM\02. 検査計画書\tool\Projects__\Scheduled_execution_dicts\task_log.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()} {message}\n")
    
    log("スクリプト開始")
    
    today = datetime.datetime.now().strftime("%Y%m%d")
    
    old_file_path = rf'C:\Users\zlocal\OneDrive - FUJIFILM\02. 検査計画書\受入れ検査品リストVer1_2021.5.31\受入れ検査品リストVer1_2021.5.31_output\{today}_受入れ検査品リストVer1_2021.5.31  .xlsx'
    isp_path = f"C:/Users/zlocal/OneDrive - FUJIFILM/02. 検査計画書/tool/クリティカル整合チェック_output/Critical-{today}.xlsx"
    flag_path = r'\\10.209.52.211\profile\一時保存\受検\佐野\重要部品フラグ\重要部品フラグ.xlsx'
    
    try:
        log("ファイルのコピー開始")
        shutil.copy(old_file_path, isp_path)
        log("ファイルのコピー成功")
    
        log("Excel読み込み開始")
        df_isp = pd.read_excel(isp_path, sheet_name='検査計画書')
        df_flag = pd.read_excel(flag_path, sheet_name=0)
        log("Excel読み込み成功")
    
        log("不要列の削除開始")
        df_flag = df_flag.drop(['人体接触', 'ＣＰ', 'ＩＳＰ', '安全リスク'], axis=1)
    
        df_isp = df_isp.drop([ # 非常に長いのでここは省略していますが、元のdropリストをそのまま貼り付けてください。
            # 元のコードのdropリストをここに貼り付け
        ], axis=1)
        log("不要列の削除成功")
    
        log("列名変更開始")
        df_isp = df_isp.rename(columns={
            '部品番号\nPart number': '部品番号', 
            '種類 Type\n  クリティカル    Critical\n  非クリティカル Non-Critical': '種類', 
            '名称\nPart name': '名称', 
            '文書番号\nDocument number': '文書番号', 
            '認定\nCertification': '認定', 
            '検査方法\nInspection method': '検査方法', 
            '検査項目\nInspection items': '検査項目', 
            '検査基準\nInspection criteria': '検査基準', 
            '検査結果\nInspection results': '検査結果', 
            '備考\nRemark': '備考'
        })
        log("列名変更成功")
    
        Same_doc = [
            "PA-IP27-442",
            "PA-IP27-444",
            "PA-IP27-441",
            "PA-IP27-440",
            "PA-IP28-312",
            "PA-IP28-313",
            "PA-IP28-314",
            "PA-IP28-315",
            "PA-IP28-316",
            "PA-IP28-317",
            "PA-IP28-318",
            "PA-IP28-319",
            "PA-IP28-959",
            "PA-IP28-960",
            "PA-IP28-961",
            "PA-IP28-962",
            "PA-IP29-136",
            "PA-IP29-646",
            "PA-IP30-227",
            "PA-IP38-618",
            "PA-IP38-681",
            "PA-IP38-682",
            "PA-IP41-021",
            "PA-IP41-039",
            'PA-IP41-092',
            'PA-IP41-374',
            'PA-IP22-610',
            'PA-IP19-903',
            'PA-IP25-595',
            'PA-IP00-000',
            'PA-IP25-654',
            'PA-IP25-655',
            'PA-IP25-656',
            'PA-IP25-657',
        ]
    
        log("文書番号による行削除開始")
        for doc in Same_doc:
            df_isp = df_isp[df_isp["文書番号"] != doc]
    
        df_isp = df_isp[df_isp['文書番号'] != 'PA-IP00-000']
        log("文書番号による行削除成功")
    
        log("認定がNaNの行のみ抽出")
        df_isp = df_isp[df_isp["認定"].isna()]
        df_isp = df_isp.drop(['認定'], axis=1)
        log("認定列削除成功")
    
        log("品目コード作成開始")
        df_isp["Ver."] = df_isp['Ver.'].astype(str).str.replace('_', '').str.replace(' ', '').str.replace('　', '')
        df_isp["品目コード"] = df_isp["部品番号"].astype(str) + df_isp["Ver."]
        log("品目コード作成成功")
    
        log("データマージ開始")
        df_merged = pd.merge(df_isp, df_flag, on='品目コード', how='inner', suffixes=('_isp', '_flag'))
    
        log("CP列とBECPBACA列の不一致行抽出開始")
        df_not_equal = df_merged[df_merged['CP'] != df_merged['BECPBACA']]
    
        log("Excel保存開始")
        df_not_equal.to_excel(isp_path, index=False)
        log("Excel保存成功")
    
    except Exception as e:
        log(f"エラー発生: {str(e)}")
    
    log("スクリプト終了")
    ```
