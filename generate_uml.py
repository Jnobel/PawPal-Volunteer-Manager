from graphviz import Digraph

# Create a Digraph object for the UML diagram
uml_diagram = Digraph("UML_Class_Diagram", format="png")
uml_diagram.attr(rankdir="LR")

# Define the User class
uml_diagram.node("User", """User
- username: CharField
- email: EmailField
- password: CharField""", shape="record")

# Define the Volunteer class
uml_diagram.node("Volunteer", """Volunteer
- phone_number: CharField
- skills: TextField
- total_hours: FloatField""", shape="record")

# Define the Shift class
uml_diagram.node("Shift", """Shift
- event_name: CharField
- date: DateField
- start_time: TimeField
- end_time: TimeField
- max_volunteers: IntegerField""", shape="record")

# Define relationships
uml_diagram.edge("User", "Volunteer", label="1 to 1")
uml_diagram.edge("Volunteer", "Shift", label="Many to Many")

# Render the UML diagram
uml_diagram_path = "./static/images/PawPal_UML_Class_Diagram"
uml_diagram.render(uml_diagram_path, format="png", cleanup=False)

print(f"UML diagram saved as {uml_diagram_path}.png")
