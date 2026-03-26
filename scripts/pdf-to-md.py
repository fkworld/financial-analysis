import os
import sys
from pathlib import Path

from markitdown import MarkItDown

SRC_DIR = Path(__file__).resolve().parent.parent / "src"


def find_pdf_files(directory: Path) -> list[Path]:
    return sorted(directory.rglob("*.pdf"))


def main():
    pdf_files = find_pdf_files(SRC_DIR)

    if not pdf_files:
        print("No PDF files found under src/")
        return

    print(f"Found {len(pdf_files)} PDF file(s)\n")

    converter = MarkItDown()

    for pdf_path in pdf_files:
        md_path = pdf_path.with_suffix(".md")

        if md_path.exists():
            print(f"[SKIP] {md_path} already exists")
            continue

        print(f"[CONVERT] {pdf_path}")
        try:
            result = converter.convert(str(pdf_path))
            md_path.write_text(result.text_content, encoding="utf-8")
            print(f"[DONE] {md_path}")
        except Exception as e:
            print(f"[ERROR] {pdf_path}: {e}", file=sys.stderr)

    print("\nAll done.")


if __name__ == "__main__":
    main()
