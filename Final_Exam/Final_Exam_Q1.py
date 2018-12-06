from itertools import islice, product
import numpy as np
import networkx as nx
from tabulate import tabulate
from sys import argv


draw_plot = False

# Function to get components from text file
def get_components(filename):
	with open(filename) as f:
		lines = f.readlines()

	number_of_resistors = int(lines[0])

	components = []
	for i in range(number_of_resistors):
		temp = lines[i+1].split("\t")
		components.append([temp[0], int(temp[1]), int(temp[2])])

	# find the largest node number
	max_node = 0
	for component in components:
		for i in range(2):
			if component[i+1] > max_node:
				max_node = component[i+1]
	
	# replace node 0 with 1 and 1 with (max_node+1)
	# to make node numbers sequential
	for i, component in enumerate(components):
		for j in range(2):
			if component[j+1] == 1:
				components[i][j+1] = max_node + 1
			if component[j+1] == 0:
				components[i][j+1] = 1
		# Make sure that node numbering for a resistor is low to high
		# i.e. if input was "!v 5, 4" this would make it "!v 4, 5"
		if components[i][1] > components[i][2]:
			components[i][1], components[i][2] = components[i][2], components[i][1]

	components = np.asarray(components)

	# Get unique variables
	variables = sorted(list(set([var.replace("!", "") for var in list(components[:,0])])))

	return [max_node, variables, components]

def get_truth_table(vars):
	truth_table = list(product([False, True], repeat=len(vars)))
	for i, row in enumerate(truth_table):
		# convert table from tuple to list
		truth_table[i] = list(truth_table[i])

	return truth_table

if len(argv) > 1:
	# get filename from terminal input
	filename = argv[1]
	max_node, variables, components = get_components(filename)

	print("Components from data file:")
	for c, component in enumerate(components):
		print(c, component)

	# Generate truth table
	truth_table = get_truth_table(variables)

	for r, row in enumerate(truth_table):

		G = nx.Graph()

		for n in range(max_node+1):
			G.add_node(n+1)

		variable_values = [row[i] for i, var in enumerate(variables)]

		# print("\nTruth table row:", r, "\nVariables: ", end="")
		# for v, var in enumerate(variables):
		# 	print(variables[v], "=>", variable_values[v], " ", end="")
		# print()

		for component in components:
			val_idx = variables.index(component[0].replace("!", ""))
			val = variable_values[val_idx]
			if "!" in component[0]:
				val = not val

			if val == False:
				G.add_edge(int(component[1]), int(component[2]), weight=1)

		paths = list(nx.all_simple_paths(G, source=1, target=max_node+1))

		# Record the result of the inputs in the truth table 
		if len(list(paths)) > 0:
			truth_table[r].append(False)
		else:
			truth_table[r].append(True)

		# Print if path was found from start to end
		answer = "Yes" if truth_table[r][-1] == False else "No"
		# print("Path from node 1 to " + str(max_node+1) + "?", answer)

		print("Row:", r+1, "of", len(truth_table), "Low Resistance?", answer)

		# If you want to display the graph
		if draw_plot == True:
			import matplotlib.pyplot as plt

			elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]

			pos = nx.spring_layout(G)  # positions for all nodes

			# nodes
			nx.draw_networkx_nodes(G, pos, node_size=700)

			# edges
			nx.draw_networkx_edges(G, pos, edgelist=elarge,
			                       width=6)

			# labels
			nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

			plt.axis('off')
			plt.show()


	# Print results to terminal
	print("\nFinal Results:\n")
	for r, row in enumerate(truth_table):
		truth_table[r] = np.asarray(truth_table[r]).astype(int)
	table = tabulate(truth_table, headers=variables+["Result"])
	print(table, end="\n\n")

	# Write data to file
	print("Writing data to file...")
	output_filename = 'final_exam_q1_' + argv[1].replace(".cir", "") + '.bool'
	with open(output_filename, 'w') as datafile:
		datafile.write("\t".join(variables+[""]) + "\n")
		for row in truth_table:
			for col in row:
				datafile.write(str(col)+"\t")
			datafile.write("\n")
	print("Data written to: " + output_filename, end="\n\n")

else:
	print("Please enter the input filename following the script name.")
	print("i.e. python3 Final_Exam_Q1.py compute1.txt")
