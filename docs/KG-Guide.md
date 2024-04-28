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

If you are interested in a more focused view of the core elements of the CSKG, use the query below. This query specifically retrieves nodes and relationships where nodes report directly to a `CyberSecurityScore`.

```cypher
MATCH (n:CyberSecurityScore)<-[r:REPORTS_TO]-(m) RETURN n, r, m
```

Utilize these queries to delve into different aspects of the CSKG, depending on your needs for analysis or data visualization.
```
