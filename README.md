# BriefBridge AI 📚

**Turn assignment briefs into actionable plans with local AI.**

BriefBridge AI helps students understand college assignment instructions by turning them into a structured action plan.

## Features

- Extracts requirements from assignment instructions
- Creates a task checklist
- Suggests an assignment outline
- Organizes a practical work plan
- Highlights details to verify before submission
- Downloads the generated plan as a text file
- Uses a locally running AI model through Ollama

## Tech Stack

- Python
- Streamlit
- Ollama
- Qwen3 0.6B
- Requests

## Prerequisites

- Python
- Ollama
- The `qwen3:0.6b` model downloaded through Ollama

## Setup

Clone or download this repository, then open a terminal in the project folder.

Create and activate a virtual environment on Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the dependencies:

```bash
python -m pip install streamlit requests
```

Download the model if needed:

```bash
ollama pull qwen3:0.6b
```

Run the application:

```bash
python -m streamlit run app.py
```

## Responsible Use

BriefBridge AI provides planning suggestions, not guaranteed interpretations of assignment instructions. Students should verify the generated plan against their original brief and their teacher's requirements.

## License

A license will be added after choosing an appropriate open-source license.
