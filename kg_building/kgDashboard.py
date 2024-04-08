# This file is used to create a dashboard for the Knowledge Graph (KG) using Streamlit

# Import the required libraries
import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import tempfile

# Set the title of the dashboard
data = pd.read_csv('/Users/alisami/Desktop/FYP/Code/final-year-project-ASHS21-1/kg_building/bloom-export/graph-export.csv')

# Create a directed graph
G = nx.DiGraph()

# Optionally, create dictionaries to store additional node and edge information
node_labels = {}  
edge_labels = []  

# Add nodes with labels
for _, row in data.iterrows():
    
    # Extract the node and edge information from the DataFrame
    start_node = row['~start_node_id']
    end_node = row['~end_node_id']

    # Assuming you have columns for labels or any other properties you want to include
    start_label = row['~start_node_labels'] 
    end_label = row['~end_node_labels']      
    
    # Add nodes with labels
    node_labels[start_node] = start_label
    node_labels[end_node] = end_label
    
    # Add nodes with labels
    G.add_node(start_node, label=start_label)
    G.add_node(end_node, label=end_label)
    
    # Add edges with titles (or labels) to represent relationships or properties
    relationship = row['~relationship_type']  # Adjust column name as needed
    G.add_edge(start_node, end_node, title=relationship)
    edge_labels.append((start_node, end_node, relationship))

# Use Pyvis to generate an interactive graph
nt = Network('500px', '100%', notebook=True, heading='')

# Set options for nodes and edges to make labels and titles visible
nt.set_options("""
{
  "nodes": {
    "font": {
      "size": 14
    }
  },
  "edges": {
    "font": {
      "size": 10,
      "align": "top"
    },
    "arrows": {
      "to": {
        "enabled": true
      }
    },
    "color": {
      "inherit": true
    },
    "smooth": false
  }
}
""")


# Import the networkx graph
nt.from_nx(G)

# Display the graph in Streamlit using a temporary file
def show_pyvis_graph(network):
    # Generate a temporary HTML file and read it into a string
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmpfile:
        network.show(tmpfile.name)
        with open(tmpfile.name, "r") as f:
            html_string = f.read()
    
    # Use Streamlit's HTML component to display the graph
    st.components.v1.html(html_string, width=700, height=600, scrolling=True)

# Display the graph
show_pyvis_graph(nt)
