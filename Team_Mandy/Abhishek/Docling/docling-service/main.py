import os
import tempfile
from fastapi import FastAPI, File, UploadFile, HTTPException
from docling.document_converter import DocumentConverter

app = FastAPI(title="Docling PDF Parser API")
converter = DocumentConverter()

@app.post("/parse-pdf")
async def parse_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    # Save the uploaded file to a temporary location
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            content = await file.read()
            temp_pdf.write(content)
            temp_pdf_path = temp_pdf.name
        
        # Convert the document using docling
        result = converter.convert(temp_pdf_path)
        md_text = result.document.export_to_markdown()
        
        # Clean up temporary PDF file
        os.remove(temp_pdf_path)
        
        return {"filename": file.filename, "markdown": md_text}
        
    except Exception as e:
        if 'temp_pdf_path' in locals() and os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)
        raise HTTPException(status_code=500, detail=f"Error during conversion: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
