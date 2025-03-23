# pdfdocument.py
import fitz  # PyMuPDF

def get_fonts(pdf_document):
    """
    PDFからしおりを取得し、対応するページ番号を取得する。
    """
    style_dict = {}
    for bookmark in pdf_document.get_toc():
        level, title, page = bookmark  # しおりのレベル、タイトル、ページ番号
        
        if title.startswith("打_") and ".pdf" in title:
            color = (0.7, 0, 0)  # 赤
            bold = False
            italic = False
        elif not title.startswith("打_") and ".pdf" in title:
            color = (0,0,0.7)  # 青
            bold = False
            italic = False
        else:
            color = (0, 0, 0)  # 黒
            bold = False
            italic = False
        
        style_dict[title,page] = (color, bold, italic)
    
    return style_dict

if __name__ == "__main__":
    pdf_path = r"C:\Users\uboni\Desktop\検査用栞付結合データ.pdf"
    pdf_document = fitz.open(pdf_path)
    
    # しおり情報取得
    bookmark_styles = get_fonts(pdf_document)
    
    # しおりのスタイル情報を表示
    for title, page in bookmark_styles.items():
        print(bookmark_styles.get(title,page))


    
