import fitz  # PyMuPDF
import m09get_whr as m09

def get_Po_Zs(pdf_document):
    """
    指定された PDF ドキュメントの各ページについて、(x, y, z) 座標を取得します。

    各ページの座標は以下の基準に基づいて決定されます：
    - z 座標は A4 縦の高さ (210 mm) を基準にした縮尺係数として計算。
    - x, y 座標はページの回転角度 (0, 90, 180, 270 度) に応じて設定。

    Args:
        pdf_document (fitz.Document): 座標情報を取得する PDF ドキュメント。

    Returns:
        dict: 各ページの座標情報を格納した辞書。
              - キー: ページ番号 (1-based)
              - 値: (x, y, z) のタプル

    Raises:
        ValueError: 回転角度が 0, 90, 180, 270 のいずれでもない場合。

    例:
        >>> pdf = fitz.open("example.pdf")
        >>> get_Po_Zs(pdf)
        {1: (0.0, 0.0, 0.75), 2: (0.0, 841.89, 0.75), ...}
    """
    whr=m09.get_pdf_page_xyr(pdf_document)

    points = {}

    for page, (width, height, rotation) in whr.items():
        # 条件に基づいて (x, y, z) を決定 
        z = 210 / height
        # mm を PDF 単位 (pt) に変換 (1 inch = 25.4 mm, 1 inch = 72 pt)
        width_pt = width / 25.4 * 72
        height_pt = height / 25.4 * 72
        if rotation == 0:
            x, y = 0.0, 0.0
        elif rotation == 90:
            x, y = 0.0, height_pt
        elif rotation == 180:
            x, y = width_pt, height_pt
        elif rotation == 270:
            x, y = width_pt, 0.0
        else:
            raise ValueError("Invalid rotation value. Expected 0, 90, 180, or 270.")

        points[page] = (x, y, z)

    return points

if __name__ == "__main__":
    pdf_document = fitz.open(r"C:\Users\uboni\Desktop\検査用栞付結合データ.pdf")
    points = get_Po_Zs(pdf_document)

    # 結果を表示
    for page, (x, y, z) in points.items():
        print(f"Page {page}: x = {x:.2f}, y = {y:.2f}, z = {z:.2f}")
    print(pdf_document.get_toc())