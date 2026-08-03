import os
import argparse
from markitdown import MarkItDown

def convert_to_md(input_path, output_path):
    """
    Converts a given document (PDF, DOCX, PPTX, etc.) to Markdown using MarkItDown.
    """
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return

    print(f"Converting '{input_path}'...")
    
    # Initialize MarkItDown
    md = MarkItDown()
    
    try:
        # Convert the document
        result = md.convert(input_path)
        
        # Save to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
            
        print(f"✅ Successfully converted and saved to '{output_path}'")
        
    except Exception as e:
        print(f"❌ Conversion failed: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert documents to Markdown for AnythingLLM.")
    parser.add_argument("input", help="Path to the input file (e.g., document.pdf)")
    parser.add_argument("output", help="Path to the output Markdown file (e.g., document.md)")
    
    args = parser.parse_args()
    convert_to_md(args.input, args.output)
