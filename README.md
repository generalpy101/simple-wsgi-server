
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
simple-wsgi-server
</h1>
<h3 align="center">📍 Simple. Powerful. Striped-Down WSGI Server.</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="mypy-extensions" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 📍Overview

The GitHub project simple-wsgi-server is a basic, lightweight Python WSGI server that allows developers to easily run, test, and debug their WSGI applications. It supports the latest

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
repo
├── docker-compose.yaml
├── init_hooks.sh
├── lint.py
├── pyproject.toml
└── src
    ├── __init__.py
    ├── dockerfile
    ├── libs
    │   ├── __init__.py
    │   └── logger.py
    ├── main.py
    ├── models
    │   ├── __init__.py
    │   └── http_request.py
    ├── parsers
    │   ├── __init__.py
    │   └── http_parser.py
    └── requirements.txt

4 directories, 14 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>Libs</summary>

| File      | Summary                                                                                                                                                                                                        | Module             |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| logger.py | This code creates a logger object with the given name and sets the log level based on the environment variable LOG_LEVEL . It also adds a StreamHandler to the logger and sets the formatter for the handler . | src/libs/logger.py |

</details>

<details closed><summary>Models</summary>

| File            | Summary                                                                                                                                                                                                                                     | Module                     |
|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| http_request.py | This code creates a class called HTTPRequest which is used to create a request string from a given method , path , protocol , headers , and body . It also uses the StringIO module from the io library to format the body of the request . | src/models/http_request.py |

</details>

<details closed><summary>Parsers</summary>

| File           | Summary                                                                                                                                                                                                                                                | Module                     |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| http_parser.py | This code defines a function called parse_http which takes a string as an argument . It splits the string into four parts and assigns them to variables . It then creates a dictionary with the method , path , protocol , headers , and body from the | src/parsers/http_parser.py |

</details>

<details closed><summary>Root</summary>

| File          | Summary                                                                                                                                                                                                          | Module        |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|
| .pylintrc     | This code disables certain warnings for docstrings in Python code . Specifically , it disables warnings C0114 ( missing - module - docstring ) , C0116 ( missing - function - docstring ) , and C0115 ( missing- | .pylintrc     |
| init_hooks.sh | This code creates a pre - commit hook for a git repository that runs a black code formatter on the source files , adds them to the repository , and then runs a python linter on the source files .              | init_hooks.sh |
| lint.py       | This code runs PyLint on a given directory and checks the score against a given threshold . If the score is below the threshold , an exception is raised . Otherwise , the code exits with a success code .      | lint.py       |

</details>

<details closed><summary>Src</summary>

| File          | Summary                                                                                                                                                                                                                                                        | Module            |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| main.py       | This code creates a server that listens on a given host and port , and handles incoming requests using the HTTP protocol . It uses the socket , selectors , and types modules to create a server with a capacity of 1024 , and a buffer size of                | src/main.py       |
| .dockerignore | Pycache is a Python library that provides a caching system for Python applications . It allows developers to store and retrieve data from a cache , and provides a range of features such as expiration , eviction , and invalidation . Pycache is designed to | src/.dockerignore |
| dockerfile    | This code creates a Python 3.12.0a5 - slim environment , installs build - essential and python3 - pip , copies the current directory into the environment , installs the requirements from the requirements.txt file , sets an                                 | src/dockerfile    |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the simple-wsgi-server repository:
```sh
git clone https://github.com/generalpy101/simple-wsgi-server
```

2. Change to the project directory:
```sh
cd simple-wsgi-server
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using simple-wsgi-server

```sh
python main.py
```

### 🧪 Running Tests
```sh
#run tests
```

<hr />

## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


---

## 🤝 Contributing
Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

[📌  INSERT-DESCRIPTION]


---

