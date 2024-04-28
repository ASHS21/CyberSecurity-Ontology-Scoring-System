# 🌐 Welcome to the Cyber Eye

Welcome to your guide for navigating through our repositories and setting up the project. Follow the steps below to get everything up and running smoothly. 🚀

## 📑 Table of Contents
- [🌐 Welcome to the Cyber Eye](#-welcome-to-the-cyber-eye)
  - [📑 Table of Contents](#-table-of-contents)
  - [📋 Pre-requisites](#-pre-requisites)
  - [🗂 Project Layout](#-project-layout)
  - [📦 Cloning the GitHub Repository](#-cloning-the-github-repository)
  - [📚 Installing Protege (Ontology Editor)](#-installing-protege-ontology-editor)
  - [🖥 Installing Neo4j Desktop (GraphDB)](#-installing-neo4j-desktop-graphdb)
  - [📊 Running the Dashboard and the Evaluation](#-running-the-dashboard-and-the-evaluation)
    - [📋 Running the Evaluation](#-running-the-evaluation)

## 📋 Pre-requisites
Ensure you have the following software installed:
- **Python3** 🐍
- **Neo4j** 🌐
- **Protege** 🦉

## 🗂 Project Layout
Here's an overview to help you set up the software:
- Cloning the GitHub repository 📦
- Installing Protege (Ontology Editor) 📚
- Installing Neo4j Desktop (GraphDB) 🖥
- Running the Dashboard 📊

## 📦 Cloning the GitHub Repository
Clone the repository including submodules with the following command:
```bash
git clone --recurse-submodules https://github.com/uol-feps-soc-comp3931-2324-classroom/final-year-project-ASHS21.git
```
Navigate to the directory:
```bash
cd final-year-project-ASHS21/
```

## 📚 Installing Protege (Ontology Editor)
Choose the installation guide based on your operating system:
- [Windows Installation Page](https://protegeproject.github.io/protege/installation/windows/)
- [Mac Installation Page](https://protegeproject.github.io/protege/installation/osx/)
- [Linux Installation Page](https://protegeproject.github.io/protege/installation/linux/)

For beginners:
[Getting Started with Protege](https://protegeproject.github.io/protege/getting-started/)

## 🖥 Installing Neo4j Desktop (GraphDB)
Download Neo4j Desktop for your OS:
[Download Neo4j Desktop](https://neo4j.com/docs/desktop-manual/current/)

## 📊 Running the Dashboard and the Evaluation
Start by navigating to the working directory inside the repo:
```bash
cd csonto/target/csonto/
```
Install the required Python packages:
```bash
pip install -r requirements.txt
```
Ensure the Neo4j database is running, then launch the dashboard:
```bash
streamlit run streamlit_app.py
```
Follow the pop-up page or the link on the terminal.

### 📋 Running the Evaluation
Navigate to the main directory in the repo:
```bash
cd csonto/target/csonto/
```
Go to the evaluation directory:
```bash
cd evaluation/
```
Execute the following files to evaluate the ontology and knowledge graph:
```bash
python3 modelEval.py 
python3 ontologyEval.py
python3 kgEval.py
python3 ML-LinkPredict.py
```

