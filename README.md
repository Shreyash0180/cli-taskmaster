# CLI TaskMaster

**Registration Number:** 24BEC10063

## Overview
CLI TaskMaster is a lightweight, command-line based task management application. It provides users with a distraction-free environment to organize daily tasks, set priorities, and track completion status directly from the terminal.

## Features
- **User Management**: Secure login and registration. Each user has isolated task data.
- **Task Operations**: Add, view, update, and delete tasks.
- **Prioritization & Status**: Tag tasks as High, Medium, or Low priority. Mark as Pending or Completed.
- **Analytics**: View simple statistics on task completion rates.

## Technologies Used
- **Language**: Python 3.8+
- **Libraries**: `json` (storage), `datetime`, `unittest` (testing), `colorama` (for colored CLI output)

## Steps to install & run the project
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cli-taskmaster.git
   cd cli-taskmaster
   ```
2. **Set up a virtual environment (Optional but recommended)**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   # source venv/bin/activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python src/main.py
   ```

## Instructions for testing
To run the unit tests, execute the following command from the root directory:
```bash
python -m unittest discover -s tests
```
