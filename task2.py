import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("mxGraphModel")
root.append(ET.Element("root"))

# Create the Vehicle table
vehicle_cell = ET.SubElement(root[0], "mxCell", id="vehicle", value="Vehicles", style="shape=table;startSize=30;")
ET.SubElement=("vehicle_cell, "mxGeometry", x="40", y="40", width="200", height="150", as="geometry")
for column in ["vehicle_id (PK)", "make", "model", "year", "license_plate", "color", "category", "rental_agreement_id (Unique, FK)"]:
    ET.SubElement(vehicle_cell, "mxCell", value=column, style="shape=tableRow;horizontal=0;startSize=0;")

# Create the Rental Agreements table
rental_cell = ET.SubElement(root[0], "mxCell", id="rental", value="Rental_Agreements", style="shape=table;startSize=30;")
ET.SubElement(rental_cell, "mxGeometry", x="340", y="40", width="200", height="150", as="geometry")
for column in ["rental_agreement_id (PK)", "vehicle_id (Unique, FK)", "customer_id", "start_date", "end_date", "pickup_location", "return_location"]:
    ET.SubElement(rental_cell, "mxCell", value=column, style="shape=tableRow;horizontal=0;startSize=0;")

# Create the relationship
relationship = ET.SubElement(root[0], "mxCell", id="rel_vehicle_rental", style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;endFill=1;")
ET.SubElement(relationship, "mxGeometry", relative="1", as="geometry")
ET.SubElement(relationship, "mxPoint", x="240", y="115", as="sourcePoint")  # Connect to Vehicles
ET.SubElement(relationship, "mxPoint", x="340", y="115", as="targetPoint")  # Connect to Rental_Agreements

# Write the XML to a file
tree = ET.ElementTree(root)
tree.write("autorent_erd.drawio")