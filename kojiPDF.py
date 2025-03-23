import os
import sys
from fitz import open as fitz_open  # PyMuPDF のみ必要
import m01make_treedata as m01
import m02merge_from_treedata as m02
import m03make_bookmark as m03
import m04file_name_replace as m04
import m05select_folder as m05
import m06finish_message as m06
import m10set_newtoc as m10
import m11add_number_bookmarks as m11
import m12last_bookmarks_rename as m12
# ユーザーにフォルダを選択させる
folder_path ,output_file_path= m05.select_folder_and_file()
if folder_path is None or output_file_path is None:
    print("キャンセルされたため処理を中断します。")
    sys.exit(1)  # 終了コード1（異常終了）
print(f"選択されたフォルダ: {folder_path}")

# m01からデータを作成し、フォルダ構造を分解し、フォルダ階層ごとに列を追加する
df, max_levels = m01.main(folder_path)

# データの各カラムのファイル名の変更とページ数をカウントしてDataFrameに格納する
df=m04.modify_pdf_names_in_all_columns(df)

# Excelファイルに保存
#df.to_excel('Treedata.xlsx', index=False)

# PDFをマージ
output_pdf = m02.merge_pdfs_from_df(df)

# マージしたPDFにブックマークを追加する
output_pdf = m03.add_bookmarks_to_pdf(df, max_levels, output_pdf)

# ブックマークの文字列の最後にページ数を追加する。
output_pdf = m11.add_page_number_to_bookmarks(output_pdf)

output_pdf = m12.last_bookmarks_rename(output_pdf)

output_pdf.save(output_file_path[:-4]+"temp.PDF")
output_pdf.close()
output_pdf = fitz_open(output_file_path[:-4]+"temp.PDF")

output_pdf=m10.set_newtoc(output_pdf)
output_pdf.save(output_file_path)
output_pdf.close()
os.remove(output_file_path[:-4]+"temp.PDF")  


m06.main(f'{output_file_path}を保存しました。\nOKボタンを押してください。')
