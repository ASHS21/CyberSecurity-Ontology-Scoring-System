import json
from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.driver = GraphDatabase.driver(self.config['neo4j']['uri'], 
                                           auth=(self.config['neo4j']['user'], 
                                                 self.config['neo4j']['password']))
    
    @staticmethod
    def load_config(config_path):
        with open(config_path, 'r') as file:
            return json.load(file)
    
    def close(self):
        if self.driver:
            self.driver.close()
    
    def add_cyber_security_score(self, score=None, description=None):
        with self.driver.session() as session:
            session.run("CREATE (css:CyberSecurityScore {score: $score, description: $description})",
                        score=score, description=description)
    def add_nodes_and_relationships(self):
        mainClasses = [
        "EmergingTechnologies", "Governance", "SecurityOperations",
        "AssetManagement", "ChangeManagement", "Assurance"
        ]
    
        with self.driver.session() as session:
         for className in mainClasses:
            session.run(
                f"""
                MERGE (css:CyberSecurityScore) 
                MERGE (n:{className} {{name: "{className}"}}) 
                MERGE (n)-[:REPORTS_TO]->(css)
                """
            )

def main():
    config_path = 'config.json'  
    
    # Initialize connection
    conn = Neo4jConnection(config_path)
    
    # Use the connection to add nodes
    conn.add_cyber_security_score(0, "Initial cybersecurity assessment score")
    conn.add_nodes_and_relationships()
    
    # Close the connection when done
    conn.close()
    
    print("Main execution complete.")

if __name__ == "__main__":
    main()
