# This script updates the weights of the policies in the Neo4j database.
# The script is used to update the weights of the policies in the Neo4j database.

# Import the required libraries
import json
from neo4j import GraphDatabase

# Define the Neo4jConnection class
class Neo4jConnection:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.driver = GraphDatabase.driver(self.config['neo4j']['uri'], 
                                           auth=(self.config['neo4j']['user'], 
                                                 self.config['neo4j']['password']))
    
    @staticmethod
    # Load the configuration file
    def load_config(config_path):
        with open(config_path, 'r') as file:
            return json.load(file)
    
    # Close the connection
    def close(self):
        if self.driver:
            self.driver.close()

    # Update the policy weights
    def update_policy_weights(self, policy_types):
        with self.driver.session() as session:
            for policy in policy_types:
                session.run(
                    f"""
                    MATCH (p:{policy})-[r:CONTRIBUTES_WEIGHT_TO]->()
                    WHERE p.status IN ['bypassed', 'ignored', 'violated']
                    SET r.weight = 0
                    """
                )

# Define the main function
def main():

    # Define the path to the configuration file
    config_path = 'config.json'  
    
    # Initialize connection
    conn = Neo4jConnection(config_path)
    
    # Define the policy types
    policy_types = [
        'Governance_Policies',
        'Assurance_Policies',
        'Asset_Management_Policies',
        'Emerging_Technologies_Policies',
        'Security_Operations_Policies',
        'Change_Management_Policies'
    ]

    
    
    # Update policy weights
    conn.update_policy_weights(policy_types)
    
    # Print a confirmation message
    print("Policy weights have been updated.")
    
    # Close the Neo4j connection
    conn.close()

if __name__ == "__main__":
    main()
