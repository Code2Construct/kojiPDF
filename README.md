# KojiPDF

A PDF merging and bookmark utility for construction inspection documents.

[日本語の説明はこちら](#日本語)

## Overview

KojiPDF is a specialized PDF utility designed for construction inspection document management. This tool combines all PDF files within selected folders into a single PDF document, adding folder names as parent bookmarks and file names as child bookmarks. By creating a structured, unified document with an organized bookmark hierarchy, KojiPDF eliminates the time and effort lost in repeatedly opening numerous individual PDF files, allowing users to easily access specific materials within large document collections.

## Features

- **PDF Merging** - Combines multiple PDF files into a single document
- **Hierarchical Bookmarks** - Creates a structured bookmark system using folder and file names
- **Batch Processing** - Processes multiple PDF documents efficiently
- **Time-Saving** - Eliminates the need to open individual files repeatedly
- **Improved Navigation** - Allows quick access to specific documents through an organized bookmark structure

## Installation

```bash
pip install kojipdf
```

## Quick Start

```python
from kojipdf import KojiPDF

# Select a folder containing PDF files to merge
pdf_merger = KojiPDF("path/to/folder")

# Merge PDFs with automatic bookmark creation
merged_pdf = pdf_merger.merge_with_bookmarks()

# Save the merged document
merged_pdf.save("merged_inspection_document.pdf")
```

## Requirements

- Python 3.7+
- PyMuPDF
- Additional dependencies are listed in requirements.txt

## Documentation

For detailed documentation and examples, visit our [documentation page](https://github.com/Code2Construct/kojiPDF/wiki).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.  
You can find the full text of the license here:  
- [AGPL-3.0 License](https://www.gnu.org/licenses/agpl-3.0.html)

### Freedom to Use
This software is **free and open-source**. You are free to:
- **Use** this software for personal or commercial purposes.
- **Modify** and **redistribute** it, as long as you comply with AGPL-3.0.
- **Run** it on your computer or server.

### PyMuPDF License
This project uses [PyMuPDF](https://pymupdf.readthedocs.io/), which is based on [MuPDF](https://mupdf.com/).  
Both PyMuPDF and MuPDF are licensed under **AGPL-3.0**, which requires that any software using them must also be licensed under AGPL-3.0.  

### Compliance Requirements
By using this software, you agree to:
- **Make any modifications or derived works publicly available under AGPL-3.0** if you distribute or provide them as a service.
- **Include the full source code** when distributing this software.

## Contact

Project Link: [https://github.com/Code2Construct/kojiPDF](https://github.com/Code2Construct/kojiPDF)

---

<a name="日本語"></a>
# KojiPDF - 日本語

## 概要

KojiPDFは、工事検査用PDFファイル作成アプリです。選択したフォルダ内のすべてPDFファイルを結合し、ファイル名をしおり、フォルダ名を親しおりとして追加して一つのPDFファイルとして保存します。膨大なPDFファイルを繰り返しあけることによる時間と手間のロスをなくし、構造化されたしおりを持つ一つにPDFファイルにして、目的の資料に容易にアクセスできるようにすることを目的としています。

## 主な機能

- **PDF結合** - 複数のPDFファイルを一つの文書に結合
- **階層的しおり** - フォルダ名とファイル名を使用した構造化されたしおりシステムの作成
- **バッチ処理** - 複数のPDF文書を効率的に処理
- **時間節約** - 個々のファイルを繰り返し開く必要性を排除
- **ナビゲーション改善** - 整理されたしおり構造により特定の文書へ素早くアクセス可能

## インストール方法

```bash
pip install kojipdf
```

## クイックスタート

```python
from kojipdf import KojiPDF

# 結合するPDFファイルを含むフォルダを選択
pdf_merger = KojiPDF("path/to/folder")

# 自動しおり作成でPDFを結合
merged_pdf = pdf_merger.merge_with_bookmarks()

# 結合された文書を保存
merged_pdf.save("結合済み検査文書.pdf")
```

## 必要条件

- Python 3.7以上
- PyMuPDF
- その他の依存関係はrequirements.txtに記載

## ドキュメント

詳細なドキュメントと例については、[ドキュメントページ](https://github.com/Code2Construct/kojiPDF/wiki)をご覧ください。

## ライセンス

このプロジェクトは**GNU Affero General Public License v3.0 (AGPL-3.0)**の下でライセンスされています。  
ライセンスの全文はこちらでご確認いただけます：  
- [AGPL-3.0 ライセンス](https://www.gnu.org/licenses/agpl-3.0.html)

### 使用の自由
このソフトウェアは**無料でオープンソース**です。以下のことが自由に行えます：
- 個人用または商用目的でこのソフトウェアを**使用**する。
- AGPL-3.0に準拠する限り、**修正**および**再配布**する。
- あなたのコンピュータまたはサーバーで**実行**する。

### PyMuPDFライセンス
このプロジェクトは[PyMuPDF](https://pymupdf.readthedocs.io/)を使用しており、これは[MuPDF](https://mupdf.com/)に基づいています。  
PyMuPDFとMuPDFの両方がAGPL-3.0の下でライセンスされており、これらを使用するソフトウェアもAGPL-3.0の下でライセンスされる必要があります。

### 遵守要件
このソフトウェアを使用することにより、以下に同意したことになります：
- 配布またはサービスとして提供する場合、**すべての修正または派生物をAGPL-3.0の下で公開**する。
- このソフトウェアを配布する際は、**完全なソースコードを含める**。

## 連絡先

プロジェクトリンク: [https://github.com/Code2Construct/kojiPDF](https://github.com/Code2Construct/kojiPDF)
