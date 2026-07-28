# Setting up AnythingLLM for Enterprise Workflows

This document outlines the complete setup of AnythingLLM, including multi-user configuration, API integration, and database connections.

## 1. Installation & Initial Setup
1. **Download:** Download the desktop client from the [AnythingLLM website](https://anythingllm.com/) or run it via Docker for server deployments:
   ```bash
   docker run -d -p 3001:3001 \
     --cap-add SYS_ADMIN \
     -v ${PWD}/anythingllm:/app/server/storage \
     -e STORAGE_DIR="/app/server/storage" \
     mintplexlabs/anythingllm
   ```
2. **Onboarding:** Navigate to `http://localhost:3001` to start the onboarding wizard.

## 2. Enabling Multi-User Mode
By default, the desktop version is single-user. To enable multi-user, you must use the Docker deployment.
1. Go to **Settings > User Management**.
2. Create an `Admin` account.
3. Once the admin is created, you can invite new users, set them as `Manager` or `Default`, and assign them to specific workspaces with role-based access control (RBAC).

## 3. Connecting External APIs
### Nvidia API & OpenRouter
To leverage powerful closed or open-weight models without local hardware:
1. Navigate to **Settings > LLM Provider**.
2. **OpenRouter:** Select `OpenRouter`, paste your API key, and select a model like `meta-llama/llama-3-70b-instruct`.
3. **Nvidia NIM API:** Select `Generic OpenAI API`, enter `https://integrate.api.nvidia.com/v1` as the Base URL, and provide your Nvidia API key.

### Browser Search Integration
AnythingLLM can scrape the web to answer real-time queries.
1. Go to **Settings > Data Connectors > Web Scraper**.
2. Select a scraping engine (e.g., Google Search API or local Puppeteer).

## 4. Vector Database Integration (LanceDB)
AnythingLLM needs a Vector DB for Retrieval-Augmented Generation (RAG).
1. Go to **Settings > Vector Database**.
2. Select **LanceDB** (which runs embedded and is blazingly fast) or **Qdrant** for a highly scalable external server.
3. Configure the embedding model (e.g., `Nomic Embed` or `OpenAI text-embedding-3-small`).

## 5. Relational Database Connection (MySQL / PostgreSQL)
AnythingLLM allows you to connect a relational database so the LLM can query your structured data.
1. Go to **Settings > Data Connectors > SQL Database**.
2. Enter your MySQL/PgSQL credentials (Host, Port, User, Password, DB Name).
3. The agent will now dynamically generate SQL queries based on your natural language questions.

## 6. Trial Run
1. Create a new workspace: "Finance Data".
2. Upload a PDF (e.g., Apple's Q3 Earnings) into the workspace. The system will chunk and embed it into LanceDB.
3. **Query:** "Summarize the key revenue drivers for this quarter."
4. **Result:** The LLM retrieves the exact paragraphs via LanceDB, synthesizes the answer, and provides a citation to the PDF.
