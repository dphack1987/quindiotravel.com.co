import docx2txt

def read_docx_simple(file_path):
    try:
        print("Opening file: " + file_path)
        text = docx2txt.process(file_path)
        
        # Save to file instead of printing to avoid encoding issues
        output_file = r"C:\Users\user\Documents\www.quindiotravel.com\docs\Pagina_www_quindiotravel_com_co_content.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print("Content saved to: " + output_file)
        print("Length of content: " + str(len(text)) + " characters")
        
        # Print first 500 characters as preview
        print("\nPREVIEW (first 500 characters):")
        print(text[:500])
        
        return True
    except Exception as e:
        print("Error reading file: " + str(e))
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    file_path = r"C:\Users\user\Documents\www.quindiotravel.com\docs\Pagina www.quindiotravel.com.co.docx"
    read_docx_simple(file_path)