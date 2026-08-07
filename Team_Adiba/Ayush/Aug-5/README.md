# Aug-5 Tasks

This repository directory contains the deliverables for the **Aug-5** module of the Agentic AI Workshop.

---

## Completed Tasks

- **API vs MCP Technical Comparison (`MCP_vs_API.md`)**: A detailed technical document analyzing traditional APIs versus Model Context Protocol (MCP), complete with architectural diagrams, feature matrices, advantage analysis, real-world agent use cases, and ecosystem adoption (Claude Desktop, Cursor, OpenClaw, Multica).
- **Bhubaneswar Weather Predictor (`bbsr_weather.py`)**: A clean, modular Python application that queries the OpenWeather API to retrieve live weather parameters for Bhubaneswar and generates context-aware AI recommendations.

---

## Folder Structure

```text
Team_Adiba/
└── Ayush/
    └── Aug-5/
        ├── MCP_vs_API.md
        ├── bbsr_weather.py
        └── README.md
```

---

## Technologies Used

- **Python**: Core programming language for script execution.
- **Requests**: HTTP library for fetching live REST API weather payloads.
- **OpenWeather API**: Web service provider for meteorological metrics.
- **MCP Concepts**: Conceptual framework for Model Context Protocol & AI Agent tooling.
- **Markdown**: Professional GitHub-style documentation with Mermaid diagrams.

---

## Learning Outcomes

1. **Model Context Protocol Understanding**: Understood how MCP standardizes dynamic tool & context delivery to AI agents compared to legacy API integration patterns.
2. **API Consumption & Robust Error Handling**: Mastered standard HTTP REST API interaction patterns, parameter passing, and exception handling for timeouts, invalid keys, and network failures.
3. **Rule-Based AI Recommendation Engine**: Implemented dynamic decision logic to evaluate meteorological metrics and output natural language recommendations.
4. **Clean Code & Document Standards**: Applied PEP 8 standards, modular code separation, and GitHub-ready Markdown practices.

---

## How to Run

### 1. Install Dependencies

Ensure you have `requests` installed:

```bash
pip install requests
```

### 2. Set the OPENWEATHER_API_KEY Environment Variable

Get an API key from [OpenWeatherMap](https://openweathermap.org/api) and export it to your environment:

- **Linux / macOS:**
  ```bash
  export OPENWEATHER_API_KEY="your_actual_api_key_here"
  ```
- **Windows (Command Prompt):**
  ```cmd
  set OPENWEATHER_API_KEY="your_actual_api_key_here"
  ```
- **Windows (PowerShell):**
  ```powershell
  $env:OPENWEATHER_API_KEY="your_actual_api_key_here"
  ```

### 3. Run the Predictor Script

Navigate to the `Aug-5` directory and execute:

```bash
python bbsr_weather.py
```

---

## Expected Output

```text
[INFO] Fetching weather forecast for Bhubaneswar...

=======================================================
       WEATHER REPORT: BHUBANESWAR, IN
=======================================================
 🌡️  Temperature        : 31.5°C (Feels like 36.2°C)
 💧 Humidity           : 78%
 💨 Wind Speed         : 3.6 m/s
 🌤️  Condition          : Overcast Clouds
-------------------------------------------------------
 🤖 AI Recommendation:
    • 💧 Warm & Humid: Keep a water bottle handy and stay hydrated.
=======================================================
```
