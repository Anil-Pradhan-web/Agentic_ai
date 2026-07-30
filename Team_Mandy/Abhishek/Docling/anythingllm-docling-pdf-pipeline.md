# AnythingLLM + Docling: Custom PDF Parsing Pipeline

## Overview

This document describes the custom PDF ingestion pipeline built for AnythingLLM, which offloads PDF-to-Markdown conversion to a dedicated Docling-powered FastAPI microservice instead of relying on AnythingLLM's default PDF parser.

**High-level flow:**

```
User → AnythingLLM Frontend → hotdir → Collector → asPDF/index.js
     → FastAPI (localhost:8000) → Docling ML models → Markdown
     → asPDF/index.js → AnythingLLM Database → hotdir cleanup
```

---

## Step-by-Step Breakdown

### 1. File Upload
The user drags and drops a PDF into the AnythingLLM web interface. The frontend sends the raw file to the AnythingLLM backend server, which temporarily stores it in a staging directory referred to as the **`hotdir`**.

### 2. Collector Service Picks It Up
AnythingLLM runs a background **Collector** service that watches the `hotdir` for new files. When it detects the `.pdf`, it routes the file to a custom JavaScript handler: **`asPDF/index.js`**.

### 3. Handoff to the Docling Service
Rather than parsing the PDF itself, `asPDF/index.js` packages the file into a `FormData` object and issues an HTTP `POST` request via `fetch` to:

```
http://localhost:8000/parse-pdf
```

This is functionally identical to a browser requesting a webpage from a server — except the request happens locally, between two processes on the same machine.

### 4. Docling Processes the Document
A FastAPI server listening on port `8000` receives the request. It:
1. Unpacks the incoming PDF
2. Saves it temporarily to disk
3. Feeds it into the **Docling** machine learning models

Docling's models analyze the document's pages to identify structural elements — tables, headers, paragraphs, and body text — and produce a clean, structured **Markdown** representation of the content.

### 5. Response Returned
FastAPI wraps the generated Markdown string into a lightweight JSON payload and sends it back to AnythingLLM as the HTTP response.

### 6. Document Saved
`asPDF/index.js` receives the Markdown string and wraps it with internal metadata, including:
- File name
- Upload date
- Word count
- Unique document ID

This enriched record is then saved permanently to AnythingLLM's document store at:

```
server/storage/documents
```

### 7. Cleanup
AnythingLLM deletes the original raw PDF from the `hotdir`, freeing up disk space now that the processed Markdown version is safely stored.

---

## Result

The PDF has been fully converted into structured Markdown and is ready to be indexed, embedded, and queried by the AI within AnythingLLM.

---

## Architecture Diagram

```
┌──────────────┐      1. Upload PDF       ┌────────────────────┐
│   Frontend   │ ───────────────────────▶ │  AnythingLLM Server │
└──────────────┘                          └─────────┬──────────┘
                                                      │ saves to
                                                      ▼
                                              ┌───────────────┐
                                              │    hotdir     │
                                              └───────┬───────┘
                                                      │ 2. watched by
                                                      ▼
                                              ┌───────────────┐
                                              │   Collector   │
                                              └───────┬───────┘
                                                      │ 3. routes to
                                                      ▼
                                         ┌────────────────────────┐
                                         │   asPDF/index.js        │
                                         └───────┬──────────▲─────┘
                             4. POST FormData    │          │ 5. JSON (Markdown)
                                                  ▼          │
                                       ┌────────────────────────────┐
                                       │  FastAPI Server (port 8000) │
                                       │  ┌────────────────────────┐│
                                       │  │  Docling ML Models     ││
                                       │  └────────────────────────┘│
                                       └────────────────────────────┘

                             6. Save with metadata
                                       ┌──────────────────────────┐
                                       │ server/storage/documents │
                                       └──────────────────────────┘

                             7. Cleanup: raw PDF deleted from hotdir
```

---

## Component Reference

| Component | Role | Location |
|---|---|---|
| **Frontend** | Accepts PDF upload from user | AnythingLLM Web UI |
| **hotdir** | Temporary staging folder for uploaded files | AnythingLLM backend |
| **Collector** | Watches `hotdir`, dispatches files to the correct parser | AnythingLLM backend service |
| **asPDF/index.js** | Custom parser override; delegates PDF parsing to Docling service | Custom JS module |
| **FastAPI server** | Receives PDF, orchestrates Docling parsing, returns Markdown | Python service, `localhost:8000` |
| **Docling** | ML models that convert PDF layout/content into structured Markdown | Python ML library |
| **Document store** | Permanent storage for parsed documents + metadata | `server/storage/documents` |

---

## Why This Design?

- **Separation of concerns**: AnythingLLM handles orchestration, storage, and UI; Docling handles the specialized ML-based document understanding.
- **Better parsing quality**: Docling produces richer Markdown (accurate tables, headers, structure) compared to naive text extraction.
- **Local-first**: All communication happens over `localhost`, keeping documents on-machine and avoiding external API dependencies.
- **Automatic cleanup**: The `hotdir` never accumulates stale files, since raw PDFs are deleted once successfully processed.
