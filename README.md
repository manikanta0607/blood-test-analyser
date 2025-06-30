# Project Setup and Execution Guide

## Getting Started

### Install Required Libraries
```sh
pip install -r requirement.txt
```

# You're All Not Set!
🐛 **Debug Mode Activated!** The project has bugs waiting to be squashed - your mission is to fix them and bring it to life.

## Debugging Instructions

1. **Identify the Bug**: Carefully read the code and understand the expected behavior.
2. **Fix the Bug**: Implement the necessary changes to fix the bug.
3. **Test the Fix**: Run the project and verify that the bug is resolved.
4. **Repeat**: Continue this process until all bugs are fixed.





# Blood Test Report Analyser

A creative FastAPI project that analyzes blood test reports using CrewAI agents and custom tools. The agents provide medical, nutritional, and exercise advice (with a humorous twist).

---

## Features

- Upload a blood test PDF and get "expert" analysis from various agents.
- Agents include a doctor, verifier, nutritionist, and exercise specialist.
- Uses CrewAI, FastAPI, and custom tools for PDF reading and (optionally) web search.

---

## Project Structure

```
.
├── main.py
├── agents.py
├── my_tools.py
├── task.py
├── requirements.txt
├── .env
└── ...
```

---

## How This Project Was Created

1. **Initialized a Python project and created a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Installed dependencies:**
    ```bash
    pip install fastapi uvicorn crewai crewai-tools langchain_community python-dotenv
    ```

3. **Created the following main files:**
    - `main.py` – FastAPI app and endpoints.
    - `agents.py` – CrewAI agent definitions.
    - `my_tools.py` – Custom tools (PDF loader, etc.).
    - `task.py` – CrewAI task definitions.

4. **Set up environment variables:**
    - Created a `.env` file with:
      ```
      OPENAI_API_KEY=sk-...your_openai_key_here...
      ```

---

## Where Code Changes Were Made

### 1. **my_tools.py**
- **Purpose:** Houses custom tools for the project.
- **Key changes:**
  - Added a `BloodTestReportTool` class for reading PDF data.
  - (If needed) Added a search tool using `SerperDevTool` from `crewai_tools`.
  - Ensured no circular imports and correct import paths.

### 2. **agents.py**
- **Purpose:** Defines CrewAI agents (doctor, verifier, etc.).
- **Key changes:**
  - Imported tool instances from `my_tools.py`.
  - Used `from crewai import Agent` (not from `crewai.agents`).
  - Loaded the OpenAI API key from the `.env` file.
  - Checked that tool instances inherit from the correct base class.

### 3. **task.py**
- **Purpose:** Defines CrewAI tasks.
- **Key changes:**
  - Wrapped the PDF tool with a `ReadBloodReportTool` class that inherits from `BaseTool`.
  - Instantiated `read_data_tool_instance` and passed it to tasks.
  - Created multiple tasks (`help_patients`, `nutrition_analysis`, `exercise_planning`, `verification`) using the tool and agents.

### 4. **main.py**
- **Purpose:** FastAPI app entry point.
- **Key changes:**
  - Imported agents and tasks.
  - Defined endpoints for uploading and analyzing blood reports.
  - Used the CrewAI workflow to process user queries.

---

## How to Run the Project

1. **Activate your virtual environment:**
    ```bash
    source venv/bin/activate
    ```

2. **Install dependencies (if not already done):**
    ```bash
    pip install -r requirements.txt
    ```
    Or manually:
    ```bash
    pip install fastapi uvicorn crewai crewai-tools langchain_community python-dotenv
    ```

3. **Set up your `.env` file:**
    ```
    OPENAI_API_KEY=sk-...your_openai_key_here...
    ```

4. **Start the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```

5. **Access the API:**
    - Go to [http://127.0.0.1:8000](http://127.0.0.1:8000)
    - Use the `/analyze` endpoint to upload a blood test PDF and get a creative analysis.

---

