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
    # Create the subnodes for Asset Management
    def create_subnodes_for_asset_management(self):
        subnodes = [
        {"name": "Asset Management Policies", "label": "Asset_Management_Policies"},
        {"name": "Assets List", "label": "AssetsList"},
        {"name": "Capacity and Performance Planning", "label": "Capacity_And_Performance_Planning"},
        {"name": "Configuration Management", "label": "Configuration_Management"},
        {"name": "Mobile Device Management", "label": "Mobile_Device_Management"}
         ]

        with self.driver.session() as session:
             for subnode in subnodes:
                label = subnode["label"]
                name = subnode["name"]
                query = f"""
                MATCH (p:AssetManagement)
                CREATE (s:{label} {{name: $name}})-[:PART_OF]->(p)
                """
                session.run(query, name=name)
                
    # Create the subnodes for Assurance
    def create_subnodes_for_assurance(self):
        subnodes = [
        {"name": "Assurance Policies", "label": "Assurance_Policies"},
        {"name": "Compliance", "label": "Compliance"},
        {"name": "Security Awareness and Training", "label": "Security_Awareness_and_Training"},
         ]

        with self.driver.session() as session:
             for subnode in subnodes:
                label = subnode["label"]
                name = subnode["name"]
                query = f"""
                MATCH (p:Assurance)
                CREATE (s:{label} {{name: $name}})-[:PART_OF]->(p)
                """
                session.run(query, name=name)

    # Create the subnodes for Change Management
    def create_subnode_for_change_management(self):
        subnodes = [
        {"name": "Change Management Policies", "label": "Change_Management_Policies"},
        {"name": "Risk Management ", "label": "Risk_Management"},
        {"name": "Secure Engineering and Architecture", "label": "Secure_Engineering_and_Architecture"},
        {"name": "Technology Development and Acquistion", "label": "Technology_Development_and_Acquistion"},
        {"name": "Third Party Management", "label": "Third_Party_Management"} 
            ]
        with self.driver.session() as session:
             for subnode in subnodes:
                label = subnode["label"]
                name = subnode["name"]
                query = f"""
                MATCH (p:ChangeManagement)
                CREATE (s:{label} {{name: $name}})-[:PART_OF]->(p)
                """
                session.run(query, name=name)

    # Create the subnodes for Emerging Technologies
    def create_subnode_for_emerging_technologies(self):
        subnodes = [
        {"name": "Emerging Technologies Policies", "label": "Emerging_Technologies_Policies"}
            ]
        with self.driver.session() as session:
             for subnode in subnodes:
                label = subnode["label"]
                name = subnode["name"]
                query = f"""
                MATCH (p:EmergingTechnologies)
                CREATE (s:{label} {{name: $name}})-[:PART_OF]->(p)
                """
                session.run(query, name=name)

    # Create the subnodes for Governance
    def create_subnodes_for_governance(self):
        subnodes = [
        {"name": "Governance Policies", "label": "Governance_Policies"}
            ]
        with self.driver.session() as session:
             for subnode in subnodes:
                label = subnode["label"]
                name = subnode["name"]
                query = f"""
                MATCH (p:Governance)
                CREATE (s:{label} {{name: $name}})-[:PART_OF]->(p)
                """
                session.run(query, name=name)

    # Create the subnodes for Security Operations
    def create_subnodes_for_security_operations(self):
        subnodes = [
        {"name": "Security Operations Policies", "label": "Security_Operations_Policies"},
        {"name": "Data Protection", "label": "Data_Protection"},
        {"name": "Embdded Technologies", "label": "Embdded_Technologies"},
        {"name": "Infracstructure and Identity Management", "label": "Infracstructure_and_Identity_Management"},
        {"name": "Threat Management", "label": "Threat_Management"}, 
        {"name":"Vulnerability and Web Management", "label": "Vulnerability_and_Web_Management"}
            ]
        with self.driver.session() as session:
             for subnode in subnodes:
                label = subnode["label"]
                name = subnode["name"]
                query = f"""
                MATCH (p:SecurityOperations)
                CREATE (s:{label} {{name: $name}})-[:PART_OF]->(p)
                """
                session.run(query, name=name)

    # Create the subnodes for Risk Management
    def create_risk_cases_subnode(self):
            with self.driver.session() as session:
                session.run(
                """
                 MATCH (rm:Risk_Management)
                CREATE (rc:RiskCases {name: "Risk Cases"})
                CREATE (rm)-[:MANAGES]->(rc)
                """
                )
    # Create the subnodes for Threat Management
    def create_subnode_for_Threat_Management(self):
        subnodes = [
        {"name": "Business Continuity and Disaster Recovery", "label": "Business_Continuity_and_Disaster_Recovery"},
        {"name": "Incident Response", "label": "Incident_Response"},
        {"name": "Continuous Monitoring", "label": "Continuous_Monitoring"}
            ]           
        with self.driver.session() as session:
             for subnode in subnodes:
                label = subnode["label"]
                name = subnode["name"]
                query = f"""
                MATCH (p:Threat_Management)
                CREATE (s:{label} {{name: $name}})-[:PART_OF]->(p)
                """
                session.run(query, name=name)

    def create_vulnerability_and_patch_nodes(self):
        with self.driver.session() as session:
        # Create VulnerabilityList and PatchList managed by Vulnerability_and_Web_Management
            session.run(
            """
            MATCH (vwm:Vulnerability_and_Web_Management)
            CREATE (vwm)-[:MANAGES]->(vl:VulnerabilityList {name: "Vulnerability List"})
            CREATE (vwm)-[:MANAGES]->(pl:PatchList {name: "Patch List"})
            """
        )
    def link_vulnerability_to_patch(self):
        with self.driver.session() as session:
        # Create a Vulnerability and a Patch, and establish their relationships
            session.run(
            """
            MATCH (vl:VulnerabilityList), (pl:PatchList)
            CREATE (v:Vulnerability {name: "Example Vulnerability"})-[:HAS_PATCH]->(p:Patch {name: "Example Patch"})
            CREATE (p)-[:REMEDIATES]->(v)
            MERGE (vl)-[:CONTAINS]->(v)
            MERGE (pl)-[:CONTAINS]->(p)
            """
        )
            
    def create_define_policy_relations_for_domains(self):
        policy_labels = [
        "Emerging_Technologies_Policies",
        "Governance_Policies",
        "Security_Operations_Policies",
        "Assurance_Policies",
        "Change_Management_Policies",
        "Asset_Management_Policies"
    ]
    
        with self.driver.session() as session:
            for label in policy_labels:
                session.run(
                f"""
                MATCH (g:Governance), (p:{label})
                MERGE (g)-[:DEFINE_POLICY]->(p)
                """
            )



def main():
    config_path = 'config.json'  
    
    # Initialize connection
    conn = Neo4jConnection(config_path)
    
    # Use the connection to add nodes and the classes of the Cyber Security Score
    #conn.add_cyber_security_score(0, "Starting point")
    #conn.add_nodes_and_relationships()
    #conn.create_subnodes_for_asset_management()
    #conn.create_subnodes_for_assurance() 
    #conn.create_subnode_for_change_management()
    #conn.create_subnode_for_emerging_technologies()
    #conn.create_subnodes_for_governance()
    #conn.create_subnodes_for_security_operations()
    #conn.create_risk_cases_subnode()
    #conn.create_subnode_for_Threat_Management()
    #conn.create_vulnerability_and_patch_nodes()
    #conn.link_vulnerability_to_patch()
    #conn.create_define_policy_relations_for_domains()
    # Close the connection when done
    conn.close()
    
    print("Main execution complete.")

if __name__ == "__main__":
    main()
