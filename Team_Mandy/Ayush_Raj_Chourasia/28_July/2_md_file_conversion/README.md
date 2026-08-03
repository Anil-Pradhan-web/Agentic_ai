# Document to Markdown Conversion Pipeline

This folder contains a Python script that converts complex documents (PDFs, Word docs, Excel sheets, PowerPoint) into clean Markdown (`.md`) format using Microsoft's `markitdown` library. 

This is crucial because LLMs and Vector DBs (like those in AnythingLLM) parse clean Markdown far better than raw binary PDFs.

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install markitdown
   ```

2. **Run the Script:**
   Use the script via the command line, passing the input file and the desired output file name.
   ```bash
   python convert.py sample_report.pdf output_report.md
   ```
   *Note: MarkItDown supports `.pdf`, `.docx`, `.xlsx`, `.pptx`, and `.html`.*

## Connecting to AnythingLLM

Once you have generated the clean `.md` files:
1. Open your **AnythingLLM** workspace.
2. Go to the **Data** tab (the paperclip icon).
3. Drag and drop the generated `output_report.md` file into the upload area.
4. Click **"Save and Embed"**.
5. AnythingLLM will now chunk the markdown based on its natural headers (`#`, `##`), leading to significantly more accurate retrieval and RAG performance compared to uploading a raw PDF.
