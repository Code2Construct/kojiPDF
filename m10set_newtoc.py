import fitz  # PyMuPDF evalで文字列なので、認識しないが必要
import m07make_toc as m07
import m08get_Po_Zs as m08
import m13get_fonts as m13
#globals()["fitz"] = fitz  # eval() で fitz を使えるようにする
def set_newtoc(pdf_document):
    """
    PDF の目次 (TOC) にリンクを設定し、更新された PDF ドキュメントを返します。

    この関数は以下の処理を行います:
    1. `get_Po_Zs` を用いて、各ページに適したポイント座標とズーム倍率を取得。
    2. `add_link_to_toc` を用いて、取得した情報を元に TOC を更新。
    3. 更新された TOC を PDF ドキュメントに適用。
    これにより、リンクページが画面にフィットする。

    Args:
        pdf_document (fitz.Document): 編集対象の PDF ドキュメント。

    Returns:
        fitz.Document: 更新後の PDF ドキュメント。
    """
    Bfonts = m13.get_fonts(pdf_document)
    Po_Zs = m08.get_Po_Zs(pdf_document)
    print(Po_Zs)
    pdf_document.set_toc(eval(m07.make_newtoc(pdf_document.get_toc(),Po_Zs,Bfonts)))
    return pdf_document