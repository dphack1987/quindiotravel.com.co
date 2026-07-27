from docx import Document
import sys
import traceback

def read_docx(file_path):
    try:
        print("Opening file: " + file_path)
        doc = Document(file_path)
        
        print("=" * 80)
        print("FILE: " + file_path)
        print("=" * 80)
        print("Paragraphs: " + str(len(doc.paragraphs)))
        print("Tables: " + str(len(doc.tables)))
        print("=" * 80)
        print()
        
        # Read ALL paragraphs
        print("--- PARAGRAPH CONTENT ---")
        for i, para in enumerate(doc.paragraphs):
            text = para.text
            print(f"[Para {i+1}] (len: {len(text)}): '{text}'")
            if text.strip():
                print(f"  Content: {text}")
        
        # Read tables if they exist
        if doc.tables:
            print("\n" + "=" * 80)
            print("TABLES FOUND")
            print("=" * 80)
            for table_idx, table in enumerate(doc.tables):
                print(f"\n--- TABLE {table_idx + 1} ---")
                print(f"Dimensions: {len(table.rows)} rows x {len(table.columns)} columns")
                for row_idx, row in enumerate(table.rows):
                    row_text = [cell.text.strip() for cell in row.cells]
                    print(f"Row {row_idx + 1}: {' | '.join(row_text)}")
        else:
            print("\nNo tables found in document.")
        
        return True
    except Exception as e:
        print("Error reading file: " + str(e))
        traceback.print_exc()
        return False

if __name__ == "__main__":
    file_path = r"C:\Users\user\Documents\www.quindiotravel.com\docs\Pagina www.quindiotravel.com.co.docx"
    read_docx(file_path)