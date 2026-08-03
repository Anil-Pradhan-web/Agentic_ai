# 📄 Document Conversion to Markdown (Docling & AnythingLLM)

While tools like `markitdown` are great for basic text extraction, **Docling** provides superior structural extraction (tables, charts, layout awareness) from PDFs and Word documents, making the resulting Markdown significantly better for RAG (Retrieval-Augmented Generation) in AnythingLLM.

## 1. Why Docling?
- **Layout Preservation:** Understands columns and sidebars in PDFs.
- **Table Extraction:** Converts complex PDF tables directly into Markdown tables.
- **Image Extraction:** Can extract embedded images and caption them.

## 2. Docling Python Setup
First, install the Docling package:
```bash
pip install docling
```

### Python Conversion Script
Here is a robust script to convert any document into RAG-ready markdown:

```python
import os
from docling.document_converter import DocumentConverter

def convert_document(file_path, output_dir):
    converter = DocumentConverter()
    
    print(f"Processing: {file_path}")
    result = converter.convert(file_path)
    
    # Export to markdown
    markdown_content = result.document.export_to_markdown()
    
    # Save the output
    base_name = os.path.basename(file_path).split('.')[0]
    output_path = os.path.join(output_dir, f"{base_name}.md")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    print(f"Successfully saved to: {output_path}")

if __name__ == "__main__":
    convert_document("sample_corporate_report.pdf", "./markdown_outputs")
```

## 3. Connecting to AnythingLLM
Once you have the high-quality `.md` files from Docling:
1. Open **AnythingLLM**.
2. Go to your **Workspace**.
3. Navigate to **Data Sources / Document Upload**.
4. Drag and drop the generated `.md` files.
5. Because Docling preserved the tables and headers perfectly, AnythingLLM's internal vector database (LanceDB/Qdrant) will chunk the data semantically by section, drastically improving retrieval accuracy compared to raw text extraction!
