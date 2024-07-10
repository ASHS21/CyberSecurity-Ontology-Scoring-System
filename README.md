# 🌐 Welcome to the Cyber Eye

## An undergraduate-final-year-project.

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

# 📘 Ontology Guidance

![OOPS Results](https://github.com/uol-feps-soc-comp3931-2324-classroom/final-year-project-ASHS21/blob/main/OOPS%20Results.png) 

Follow this guide to navigate through the various ontology files within the project repository.

## 📂 Accessing Ontology Files

To begin working with the ontology files, please ensure you are in the correct directory within the repository.

1. Navigate to the ontology directory by running the following command in your terminal:
   ```bash
   cd csonto/target/csonto/src/ontology/
   ```

2. Within this directory, you will find several files named `csonto-edit`. You can open any of these files using Protege to view or modify the ontology.

## 🛠 Scripts for Ontology Manipulation

If you need to work with scripts related to the ontology, follow these steps:

1. If you're already in the ontology directory, navigate to the scripts directory by executing:
   ```bash
   cd csonto/target/csonto/src/scripts/
   ```

2. **StatusChecker Script:** This script is responsible for checking the status of various policies within the ontology.

3. **OntologyBuilder Script:** This script aids in building and evolving the ontology throughout the development process.

4. **Onto_Definitions & Updates Script:** Use this script for defining and updating instances within the ontology.

## The ontology documentation 
To find the full ontology documentation, follow this link: 
[CyberSecurity Ontology Docs](https://cybersecurityontologydocs.netlify.app/)
Or, find the alternative docs : [Alternative Ontology Docs](https://cybersecurityontologydocs2.netlify.app/)


# 🌐 Knowledge Graph Guide

Welcome to the guide on accessing the Cybersecurity Knowledge Graph (CSKG) via the Neo4j Desktop. Follow these steps to navigate and execute queries within the Neo4j browser.

## 🚀 Getting Started

Once you have opened Neo4j Desktop, proceed to the Neo4j Browser to start interacting with the database.

## 📊 Querying the CSKG

To explore the complete Cybersecurity Knowledge Graph, execute the following Cypher query. This query retrieves all nodes connected by either `REPORTS_TO` or `PART_OF` relationships, providing a comprehensive view of the graph.

```cypher
MATCH (n:CyberSecurityScore)<-[r:REPORTS_TO]-(m) RETURN n, r, m 
UNION 
MATCH (n)<-[r:PART_OF]-(m) RETURN n, r, m
```

### 🔍 Focused Query for Core CSKG

If you are interested in a more focused view of the CSKG's core elements, use the query below. This query specifically retrieves nodes and relationships where nodes report directly to a `CyberSecurityScore`.

```cypher
MATCH (n:CyberSecurityScore)<-[r:REPORTS_TO]-(m) RETURN n, r, m
```

Depending on your needs for analysis or data visualization, you can utilize these queries to delve into different aspects of the CSKG.

