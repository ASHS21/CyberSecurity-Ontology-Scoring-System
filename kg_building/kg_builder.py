# This script is used to build the Knowledge Graph in Neo4j

# Import the necessary libraries
import json
from neo4j import GraphDatabase
import pandas as pd
from kg_builder import KGBuilder

# Constants
SCF_ID_LABEL = 'SCF #'
SCF_CONTROL_LABEL = 'SCF Control'
DESCRIPTION_LABEL = 'Secure Controls Framework (SCF)\nControl Description'
RELATIVE_CONTROL_WEIGHTING = 'Relative Control Weighting'

# Define the Neo4jConnection class
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

    # Add the Cyber Security Score node
    def add_cyber_security_score(self, score=None, description=None):
        with self.driver.session() as session:
            session.run("CREATE (css:CyberSecurityScore {score: $score, description: $description})",
                        score=score, description=description)
            
    # Add the main classes of the Cyber Security Score
    def add_nodes_and_relationships(self):
        main_classes = [
        "EmergingTechnologies", "Governance", "SecurityOperations",
        "AssetManagement", "ChangeManagement", "Assurance"
        ]
    
        with self.driver.session() as session:
         for class_name in main_classes:
            session.run(
                f"""
                MERGE (css:CyberSecurityScore) 
                MERGE (n:{class_name} {{name: "{class_name}"}}) 
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
    def create_subnode_for_threat_management(self):
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

    # Create the Vulnerability and Patch nodes
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
    
    # Link the Vulnerability and Patch nodes
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

     # Create the relationships between the main classes and the policies       
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
    # Add the sub-nodes for the Policies nodes
    def add_asset_management_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                session.write_transaction(self._create_and_link_subnode, row)

        @staticmethod
        def _create_and_link_subnode(tx, row):
            
            
            query = (
                "MERGE (parent:Asset_Management_Policies {name: 'Asset Management Policies'}) "
                "MERGE (subnode:Policy {scf_id:$scf_id, name: $name, description: $description, strength: $strength}) "
                "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
            )
            tx.run(query, 
                   scf_id=row[KGBuilder.SCF_ID_LABEL], 
                   name=row[KGBuilder.SCF_CONTROL_LABEL], 
                   description=row[DESCRIPTION_LABEL], 
                   strength=row[RELATIVE_CONTROL_WEIGHTING])

    # Add the sub-nodes for the Asset Mangement nodes
    def add_asset_management_subnodes_for_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                # Prepend "AST -" to the scf_id before passing it to the transaction function
                modified_scf_id = f"AST - {row[SCF_ID_LABEL]}"
                session.execute_write(self._create_and_link_subnode, row, modified_scf_id)

    @staticmethod
    def _create_and_link_subnode(tx, row, parent_label, child_label):
        query = (
        f"MERGE (parent:{parent_label} {{name: $parent_name}}) "
        f"MERGE (subnode:{child_label} {{scf_id:$scf_id, name: $name, description: $description, strength: $strength}}) "
        "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
    )
        tx.run(query, 
           parent_name=f"{parent_label.replace('_', ' ')}",
           scf_id=row[SCF_ID_LABEL], 
           name=row[SCF_CONTROL_LABEL], 
           description=row[DESCRIPTION_LABEL], 
           strength=row[RELATIVE_CONTROL_WEIGHTING])
    
    # Add the sub-nodes for the Asset nodes
    def add_asset_management_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                session.write_transaction(self._create_and_link_subnode, row, "Asset_Management_Policies", "Policy")

    # Add the sub-nodes for the Governance nodes
    def add_governance_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                session.write_transaction(self._create_and_link_subnode, row)

    @staticmethod
    # Create and link the sub-nodes for the Governance nodes
    def _create_and_link_subnode(tx, row):
        query = (
            "MERGE (parent:Governance_Policies {name: 'Governance Policies'}) "
            "MERGE (subnode:Policy {scf_id:$scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               scf_id=row[KGBuilder.SCF_ID_LABEL], 
               name=row[KGBuilder.SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])

    # Add the sub-nodes for the Governance nodes
    def add_governance_subnodes_for_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                # Prepend "GOV -" to the scf_id before passing it to the transaction function
                modified_scf_id = f"GOV - {row[SCF_ID_LABEL]}"
                session.execute_write(self._create_and_link_subnode, row, modified_scf_id)

    @staticmethod
    # Create and link the sub-nodes for the Governance nodes
    def _create_and_link_subnode(tx, row, modified_scf_id):
        query = (
            "MERGE (parent:Governance_Policies {name: 'Governance Policies'}) "
            "MERGE (subnode:Policy {scf_id: $modified_scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               modified_scf_id=modified_scf_id,
               name=row[KGBuilder.SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])
    
    # Add the sub-nodes for the Emerging Technologies nodes
    def add_emerging_technologies_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                session.write_transaction(self._create_and_link_subnode_emerging_technologies, row)

    @staticmethod
    # Create and link the sub-nodes for the Emerging Technologies nodes
    def _create_and_link_subnode_emerging_technologies(tx, row):
        query = (
            "MERGE (parent:Emerging_Technologies_Policies {name: 'Emerging Technologies Policies'}) "
            "MERGE (subnode:Policy {scf_id:$scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               scf_id=row[SCF_ID_LABEL], 
               name=row[SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])

    @staticmethod
    # Create and link the sub-nodes for the Change Management nodes
    def _create_and_link_subnode_change_management(tx, row):
        query = (
            "MERGE (parent:Change_Management_Policies {name: 'Change Management Policies'}) "
            "MERGE (subnode:Policy {scf_id:$scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               scf_id=row[SCF_ID_LABEL], 
               name=row[SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])
    
    # Add the sub-nodes for the Change Management nodes
    def add_emerging_technologies_subnodes_for_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                # Prepend "AAT -" to the scf_id before passing it to the transaction function
                modified_scf_id = f"AAT - {row['SCF #']}"
                session.execute_write(self._create_and_link_subnode, row, modified_scf_id)

    @staticmethod
    # Create and link the sub-nodes for the Emerging Technologies nodes
    def _create_and_link_subnode(tx, row, modified_scf_id):
        query = (
            "MERGE (parent:Emerging_Technologies_Policies {name: 'Emerging Technologies Policies'}) "
            "MERGE (subnode:Policy {scf_id: $modified_scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               modified_scf_id=modified_scf_id,
               name=row[SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])
    
    # Add the sub-nodes for the Change Management nodes
    def add_change_management_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                session.write_transaction(self._create_and_link_subnode_change_management, row)

    @staticmethod
    # Create and link the sub-nodes for the Change Management nodes
    def _create_and_link_subnode(tx, row):
        query = (
            "MERGE (parent:Change_Management_Policies {name: 'Change Management Policies'}) "
            "MERGE (subnode:Policy {scf_id:$scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               scf_id=row['SCF #'], 
               name=row['SCF Control'], 
               description=row['Secure Controls Framework (SCF)\nControl Description'], 
               strength=row['Relative Control Weighting']) 
    
    # Add the sub-nodes for the Change Management nodes
    def add_change_management_subnodes_for_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                # Prepend "CHG -" to the scf_id before passing it to the transaction function
                modified_scf_id = f"CHG - {row['SCF #']}"
                session.execute_write(self._create_and_link_subnode, row, modified_scf_id)

    @staticmethod
    # Create and link the sub-nodes for the Emergin Technologies nodes
    def _create_and_link_subnode_emerging_technologies_modified(tx, row, modified_scf_id):
        query = (
            "MERGE (parent:Emerging_Technologies_Policies {name: 'Emerging Technologies Policies'}) "
            "MERGE (subnode:Policy {scf_id: $modified_scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               modified_scf_id=modified_scf_id,
               name=row[SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])
    
    # Add the sub-nodes for the Assurance nodes
    def add_assurance_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                session.write_transaction(self._create_and_link_subnode_assurance, row)

    @staticmethod
    # Create and link the sub-nodes for the Assurance nodes
    def _create_and_link_subnode_assurance(tx, row):
        query = (
            "MERGE (parent:Assurance_Policies {name: 'Assurance Policies'}) "
            "MERGE (subnode:Policy {scf_id:$scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               scf_id=row[SCF_ID_LABEL], 
               name=row[SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])
    
    @staticmethod
    # Create and link the sub-nodes for the Assurance nodes
    def _create_and_link_subnode_assurance(tx, row):
        query = (
            "MERGE (parent:Assurance_Policies {name: 'Assurance Policies'}) "
            "MERGE (subnode:Policy {scf_id:$scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               scf_id=row[SCF_ID_LABEL], 
               name=row[SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])
    
    # Add the sub-nodes for the Assurance nodes
    def add_assurance_subnodes_for_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                # Prepend "CHG -" to the scf_id before passing it to the transaction function
                modified_scf_id = f"IAO - {row['SCF #']}"
                session.execute_write(self._create_and_link_subnode, row, modified_scf_id)

    @staticmethod
    # Create and link the sub-nodes for the Assurance nodes
    def _create_and_link_subnode(tx, row, modified_scf_id):
        query = (
            "MERGE (parent:Assurance_Policies {name: 'Assurance Policies'}) "
            "MERGE (subnode:Policy {scf_id: $modified_scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               modified_scf_id=modified_scf_id,
               name=row[SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING]) 

    # Add the sub-nodes for the Security Operations nodes
    def add_secops_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                session.write_transaction(self._create_and_link_subnode_secops, row)

    @staticmethod
    # Create and link the sub-nodes for the Security Operations nodes
    def _create_and_link_subnode_secops(tx, row):
        query = (
            "MERGE (parent:Security_Operations_Policies {name: 'Security Operations Policies'}) "
            "MERGE (subnode:Policy {scf_id:$scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               scf_id=row[SCF_ID_LABEL], 
               name=row[SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])
    
    @staticmethod
    # Create and link the sub-nodes for the Security Operations nodes
    def _create_and_link_subnode_secops_v2(tx, row):
        query = (
            "MERGE (parent:Security_Operations_Policies {name: 'Security Operations Policies'}) "
            "MERGE (subnode:Policy {scf_id:$scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               scf_id=row[SCF_ID_LABEL], 
               name=row[SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])

    # Add the sub-nodes for the Security Operations nodes
    def add_secops_subnodes_for_subnodes(self, df):
        with self.driver.session() as session:
            for index, row in df.iterrows():
                # Prepend "OPS -" to the scf_id before passing it to the transaction function
                modified_scf_id = f"OPS - {row['SCF #']}"
                session.execute_write(self._create_and_link_subnode, row, modified_scf_id)

    @staticmethod
    # Create and link the sub-nodes for the Security Operations nodes
    def _create_and_link_subnode(tx, row, modified_scf_id):
        query = (
            "MERGE (parent:Security_Operations_Policies {name: 'Security Operations Policies'}) "
            "MERGE (subnode:Policy {scf_id: $modified_scf_id, name: $name, description: $description, strength: $strength}) "
            "MERGE (subnode)-[:CONTRIBUTES_WEIGHT_TO]->(parent)"
        )
        tx.run(query, 
               modified_scf_id=modified_scf_id,
               name=row[SCF_CONTROL_LABEL], 
               description=row[DESCRIPTION_LABEL], 
               strength=row[RELATIVE_CONTROL_WEIGHTING])  
        
# Define the main function
def main():
    # Define the path to the configuration file
    config_path = 'config.json'  
    
    # Initialize connection
    conn = Neo4jConnection(config_path)
    
    # Use the connection to add nodes and the classes of the Cyber Security Score
    conn.add_cyber_security_score(0, "Starting point")
    conn.add_nodes_and_relationships()
    conn.create_subnodes_for_asset_management()
    conn.create_subnodes_for_assurance() 
    conn.create_subnode_for_change_management()
    conn.create_subnode_for_emerging_technologies()
    conn.create_subnodes_for_governance()
    conn.create_subnodes_for_security_operations()
    conn.create_risk_cases_subnode()
    conn.create_subnode_for_Threat_Management()
    conn.create_vulnerability_and_patch_nodes()
    conn.link_vulnerability_to_patch()
    conn.create_define_policy_relations_for_domains()

    # Define the path to the Excel file
    excel_file_path = '~/Desktop/FYP/Resources/SCF-OneSheet.xlsx'

    # Read the Excel file
    df = pd.read_excel(excel_file_path)

    # Filter the data for the Policies nodes
    policies_df = df[df['SCF Domain'].str.contains('Web Security', na=False)]

     # Add sub-nodes for all Policies nodes
    conn.add_asset_management_subnodes_for_subnodes(policies_df)
    conn.add_governance_subnodes(policies_df)
    conn.add_governance_subnodes_for_subnodes(policies_df)
    conn.add_emergingTechnologies_subnodes(policies_df)
    conn.add_emergingTechnologies_subnodes_for_subnodes(policies_df)
    conn.add_changeManagement_subnodes(policies_df)
    conn.add_changeManagement_subnodes_for_subnodes(policies_df)
    conn.add_assurance_subnodes(policies_df)
    conn.add_assurance_subnodes_for_subnodes(policies_df)
    conn.add_SecOps_subnodes(policies_df)
    conn.add_secops_subnodes_for_subnodes(policies_df)

    # Print a message to indicate that the sub-nodes have been added
    print("Sub-nodes for Policies have been added.")

    # Close the connection when done
    conn.close()
    
    # Print a message to indicate that the connection has been closed
    print("Main execution complete.")

if __name__ == "__main__":
    main()
