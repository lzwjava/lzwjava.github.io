import graphviz

# Create a new directed graph
dot = graphviz.Digraph(comment='Example Graph')

# Add nodes
dot.node('A', 'Node A')
dot.node('B', 'Node B')
dot.node('C', 'Node C')

# Add edges
dot.edges(['AB', 'AC'])
dot.edge('B', 'C', constraint='false')

# Render and save the graph
dot.render('example_graph', format='png', view=True)

print("Graph rendered to 'example_graph.png'")
