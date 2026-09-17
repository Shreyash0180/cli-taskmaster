# Project Report: CLI TaskMaster

## 1. Cover Page
**Project Title**: CLI TaskMaster
**Course**: Software Engineering
**Type**: Command-Line Interface (CLI) Application
**Author**: 24BEC10063

## 2. Introduction
CLI TaskMaster is a lightweight, command-line based task management system. It provides a distraction-free, keyboard-centric interface for users to quickly log, manage, and analyze their daily tasks without relying on heavy graphical user interfaces.

## 3. Problem Statement
Many professionals and students spend excessive time navigating complex GUIs to log simple tasks. There is a need for a fast, terminal-based application that allows power users and developers to manage their workflow natively within their development environment.

## 4. Functional Requirements
1. **User Authentication Module**: Users can register and log in securely.
2. **Task Management Module**: Users can perform CRUD operations on tasks (Create, Read, Update, Delete) and assign priorities (High, Medium, Low).
3. **Analytics Module**: Users can view performance metrics (e.g., completion rate, pending tasks).

## 5. Non-functional Requirements
1. **Performance**: File-based I/O ensures task data is read and written almost instantly.
2. **Usability**: The CLI provides clear, color-coded feedback and intuitive navigation menus.
3. **Reliability**: Data is safely committed to the JSON storage immediately after any mutation to prevent data loss.
4. **Maintainability**: The codebase adheres to modular design principles, keeping storage logic separate from UI and business logic.

## 6. System Architecture
The system follows a modular Monolith architecture.
- **Presentation Layer**: `main.py` handles CLI input and output.
- **Business Logic Layer**: `auth.py`, `tasks.py`, and `analytics.py` process the core application rules.
- **Data Access Layer**: `storage.py` manages the persistence of JSON files.

## 7. Design Diagrams

**Use Case Diagram:**
- User -> Register Account
- User -> Login
- User -> Manage Tasks (Add/Delete/Update Status)
- User -> View Analytics

**Workflow Diagram:**
Start Application -> Main Menu -> Authentication (Login/Register) -> Dashboard Menu -> Actions (Add/Update/Delete/Analyze Tasks) -> Save to JSON -> Return to Dashboard.

## 8. Database/Storage Design
Data is stored persistently in lightweight JSON files.
- `users.json`: Stores hashed user credentials.
- `tasks.json`: Maps usernames to an array of their respective Task objects.

## 9. Design Decisions & Rationale
- **JSON Storage**: Chose JSON over a relational database to keep the project completely lightweight and easy to distribute. It requires zero setup from the user.
- **Colorama Library**: Selected to enhance the CLI interface with colors, improving UX without the complexity of building a full TUI (Text User Interface).

## 10. Implementation Details
- Developed purely in Python 3.
- The code is modularized into 5 core domain files (`main.py`, `auth.py`, `models.py`, `tasks.py`, `analytics.py`, `storage.py`) along with a dedicated `tests/` directory.
- Python's `hashlib` is used to hash passwords securely rather than storing them in plain text.

## 11. Screenshots / Results
*(Note: Please refer to your application's terminal output for live execution results. The CLI displays formatted menus with colored success/error indicators).*

## 12. Testing Approach
- **Unit Testing**: Python's built-in `unittest` framework was implemented.
- Tests isolate the core functions (`add_task`, `delete_task`) and run against mocked data states to verify data integrity and business logic.

## 13. Challenges Faced
- **Data Persistence**: Ensuring robust data consistency when manipulating JSON arrays. This was solved by always loading the fresh state, modifying it, and immediately dumping it back to the file atomically.

## 14. Learnings & Key Takeaways
- Deepened understanding of modular architecture and separation of concerns in Python.
- Learned effective ways to manage file I/O operations and build user-friendly CLI flows.

## 15. Future Enhancements
- Integration with SQLite for more complex querying and scalability.
- Adding due dates, sorting features, and automated reminders.
- Implementing an export-to-CSV feature for reporting.

## 16. References
- Python Official Documentation (docs.python.org)
- Markdown Guide (markdownguide.org)
