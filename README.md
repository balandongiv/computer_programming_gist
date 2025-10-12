# Beginner Python Class – Codespaces Environment

This repository is preconfigured for **GitHub Codespaces**, so students can start coding immediately without needing to install Python locally.

---

## 🚀 Getting Started

### 1️⃣ Open in Codespaces
1. Click the green **“Code”** button at the top of this repo.  
2. Choose **“Create Codespace on main”** (or your branch).  
3. Wait for setup — the environment will:
   - Create a virtual environment `.venv`
   - Install all packages from `requirements.txt`
   - Configure debugging, Jupyter, and formatting tools automatically

---

## 🧰 What’s Included

| Feature | Description |
|----------|--------------|
| 🐍 **Python 3.11** | Preinstalled base image for development |
| 📦 **Automatic dependency install** | Installs everything from `requirements.txt` each start |
| 🐞 **Debugger** | Step through code line-by-line and view variable values |
| 📒 **Jupyter support** | Run and debug `.ipynb` notebooks interactively |
| ✨ **Black & isort** | Auto-format code and manage imports |
| 🧠 **Pylance + IntelliCode** | Intelligent code completion and type hints |
| 🔍 **Variable Viewer** | Inspect all variables while debugging or in notebooks |

---

## 🧩 Debugging Guide

1. Open any `.py` file (e.g. `weeks/week01/task.py`)
2. Set a **breakpoint** (click left of line numbers)
3. Press **F5** → select *Python File*
4. Use **Step Over (F10)** / **Step Into (F11)** to follow code execution
5. View variables in the **Variables panel** or hover over names inline

> 💡 Tip: The variable explorer panel is also available for notebooks (click “Variables” in the top-right).

---

## 📦 Updating Dependencies
If you add or change packages in `requirements.txt`, rebuild the container:

```
Ctrl+Shift+P → “Dev Containers: Rebuild Container”
```

---

## 📝 Folder Structure Example

```
.
├─ .devcontainer/
│  └─ devcontainer.json
├─ requirements.txt
├─ weeks/
│  ├─ week01/
│  ├─ week02/
│  └─ week03/
└─ README.md
```

---

## 🧑‍💻 Submitting Assignments
Each week has its own folder under `weeks/`.  
Students should:
- Write code in `task.py` and `starter.ipynb`
- Save outputs in `output/`
- Commit and push changes each week

---

## 🧹 Troubleshooting
If dependencies aren’t installing:

```bash
. .venv/bin/activate
pip install -r requirements.txt
```

If Python isn’t detected:

* Press `Ctrl+Shift+P` → select **Python: Select Interpreter**
* Choose the one inside `.venv/`

---

Happy coding 🎉
Enjoy debugging and exploring Python line-by-line!

