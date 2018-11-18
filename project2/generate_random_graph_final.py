
#!/usr/bin/env python3

################################################################################################
################################## README ######################################################
################################################################################################
## 
##  Author:      Monica Bernard
##  Date:        10/13/2018
##  Assignment:  Programming Assignment 2
##  
##  Description: This program has been written for Python 3. It requires the 
##               numpy, matplotlib, tkinter and networkx modules in order to run.   
##               These can be easily installed by typing pip3 install --upgrade <MODULE>
##               in the terminal. Sudo priviledges may be required depending 
##               on the installation.
##
################################################################################################

try:
    import networkx as nx
    from numpy.random import choice, randint, seed
    import sys
    from time import time
    import matplotlib
except ModuleNotFoundError:
    print("\nRequired modules not found!")
    print("Please make sure that you have numpy, tkinter, matplotlib and networkx modules for python...\n")
    exit()

seed(0)

totalTime = 50000

# define as global variables
G=nx.Graph()

birth_probs = [0.6, 0.75, 0.8, 0.9]
# birth_probs = [0.8]
final_data  = [[[], [], [], []] for p in birth_probs]

degree_list = [[] for p in birth_probs]
p_k_list = []
p_k_prime_list = [[] for p in birth_probs]

def initGraph():
    global G
    global node_index
    node_index = 1
    G=nx.Graph()
    G.add_node(node_index) # Create first node
    G.add_edge(node_index, node_index) # Loop back edge

def get_birth_probability(G):
    nodes = G.nodes()
    totalNodes = len(nodes)
    totalEdges = 0
    degrees = []

    for node in nodes:
        degrees.append(G.degree(node))
        totalEdges += G.degree(node)

    # print("\n  Total Nodes:", totalNodes, "Total Edges:", totalEdges, "Edges", edges)

    # Initalize birth probabilities list
    birth_probabilities = [0 for x in range(totalNodes)]

    # Populate the birth probabilities list based on equation
    for i, probability in enumerate(birth_probabilities):
        birth_probabilities[i] = degrees[i]/(2*totalEdges)

    # print("  birth prob:", birth_probabilities, "sum:", sum(birth_probabilities))

    factorProb = 1/sum(birth_probabilities)

    # numpy choice requires that total sum of probabilities equals 1
    # so multiply all probabilities by the same factor to make it so. 
    # this does not change the weighting.

    for i, probability in enumerate(birth_probabilities):
        birth_probabilities[i] = birth_probabilities[i] * factorProb

    return birth_probabilities

def get_death_probability(G):
    nodes = G.nodes()
    totalNodes = len(nodes)
    totalEdges = 0
    degrees = []

    for node in nodes:
        degrees.append(G.degree(node))
        totalEdges += G.degree(node)

    # print("\n  Total Nodes:", totalNodes, "Total Edges:", totalEdges, "degrees", degrees)
    # print("  Edges:", G.edges())

    # Initalize birth probabilities list
    death_probabilities = [0 for x in range(totalNodes)]

    # Populate the birth probabilities list based on equation
    for i, probability in enumerate(death_probabilities):
        # death_probabilities[i] = (totalNodes - edges[i])/(pow(totalNodes, 2) - (2 * totalEdges))
        death_probabilities[i] = ((2 * totalEdges) - degrees[i])/((2 * totalEdges) * (totalNodes - 1))

    # print("  death prob:", death_probabilities)

    factorProb = 1/sum(death_probabilities)

    # numpy choice requires that total sum of probabilities equals 1
    # so multiply all probabilities by the same factor to make it so. 
    # this does not change the weighting.

    for i, probability in enumerate(death_probabilities):
        death_probabilities[i] = death_probabilities[i] * factorProb

    return death_probabilities

def get_birth_or_death(p):
    birth = 100 * p
    death = 100 * (1 - p)
    
    random_choice = randint(1, 100)

    if (random_choice > 0) and (random_choice <= birth):
        result = 1 # birth
    elif (random_choice > birth) and (random_choice <= 100):
        result = 0 # death

    return result

# Print iterations progress
def print_progress(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        bar_length  - Optional  : character length of bar (Int)
    """
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

def run_sim(p, t=1000):

    global node_index

    # Array to store number of nodes for a given time
    totalTime = t
    numberOfNodes = [0 for x in range(totalTime)]
    numberOfEdges = [0 for x in range(totalTime)]

    data = []
    for i, t in enumerate(numberOfNodes):
        # choose death of birth
        action = get_birth_or_death(p)

        numberOfNodes[i] = len(G.nodes())

        # Get degree for each node
        degrees = [G.degree(node)/2 for node in G.nodes()] # sum of all degrees = 2*mt, so to get get mt, divide total degrees by 2

        prefix = 'p='+"{:0.2f}".format(p)
        suffix = " nodes/edges = "+str(numberOfNodes[i])+"/"+str(sum(degrees))

        print_progress(i+1, totalTime, prefix=prefix, suffix=suffix, decimals=2, bar_length=50)
        data.append([i, numberOfNodes[i], sum(degrees)])

        # If the number of nodes goes to 0, reset graph with 1 node and loop back edge
        if (numberOfNodes[i] == 0):
            t = 0
            initGraph()

        elif (action == 0): # death
            try:
                # choose node to delete
                death_weighted_probability = get_death_probability(G)
                node_to_remove = list(choice(list(G.nodes()), 1, p=death_weighted_probability))[0]
                neighbors = G.neighbors(node_to_remove)
                edges_to_remove = []
                for neighbor in neighbors:
                    edges_to_remove.append((node_to_remove, neighbor))

                G.remove_node(node_to_remove)
                G.remove_edges_from(edges_to_remove)
            except ZeroDivisionError:
                # All nodes in graph have degree of zero
                t = 0
                initGraph()
                return False

        elif (action == 1):
            try:
                # choose which node to add new node to
                birth_weighted_probability = get_birth_probability(G)
                node_to_add_to = list(choice(list(G.nodes()), 1, p=birth_weighted_probability))[0]

                # increment node index and create new node
                node_index += 1 
                G.add_node(node_index)
                G.add_edge(node_to_add_to, node_index)
            except ZeroDivisionError:
                # All nodes in graph have degree of zero
                t = 0
                initGraph()

                return False
    return data

def plot_data():

    import matplotlib.pyplot as plt

    # Filter data to get every 5000 points
    data_points = [[[], [], [], []] for p in birth_probs]

    for i, p in enumerate(birth_probs):
        for j, t in enumerate(final_data[i][0]):
            if ((j+1) % (totalTime/10) == 0): ######################### change to 5000
                data_points[i][0].append(final_data[i][0][j])
                data_points[i][1].append(final_data[i][1][j])
                data_points[i][2].append(final_data[i][2][j])

    # Create figure for nodes vs. time

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    color   = ['b', 'c', 'g', 'm']
    markers = ['D', 's', '*', '^']

    for i, p in enumerate(birth_probs):
        if i != 2:
            q = 1-p
            expected_nodes = [((p-q)*t) + (2*q) for t in data_points[i][0]]

            line1, = ax1.plot(data_points[i][0], data_points[i][1], color[i]+markers[i], lw=2, label='p='+str(p))
            line1, = ax1.plot(data_points[i][0], expected_nodes, color[i]+"--", lw=1, label='p='+str(p)+" (expected)")


    ax1.set_title("Nodes vs. Time")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Number of Nodes")
    ax1.legend(loc='upper left')
    ax1.grid(True)


    # Create figure for edges vs. time

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)

    for i, p in enumerate(birth_probs):
        if i != 2:
            q = 1-p
            expected_edges = [(p*(p-q)*t)  for t in data_points[i][0]]

            line2, = ax2.plot(data_points[i][0], data_points[i][2], color[i]+markers[i], lw=2, label='p='+str(p))
            line2, = ax2.plot(data_points[i][0], expected_edges, color[i]+"--", lw=1, label='p='+str(p)+" (expected)")

    ax2.set_title("Edges vs. Time")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Number of Edges")
    ax2.legend(loc='upper left')
    ax2.grid(True)

    # Create figure for degrees distribution

    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)

    # line3, = ax3.plot(degree_list[0], p_k_prime_list[0], color[2]+markers[2], lw=2, label='p='+str(birth_probs[0]))
    line3, = ax3.plot(degree_list[2], p_k_prime_list[2], color[2]+markers[2], lw=2, label='p='+str(birth_probs[2]))

    ax3.set_title("Cumalitive Degree Distribution")
    ax3.set_xlabel("degree (k)")
    ax3.set_ylabel("P'(k)")
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    # ax3.set_xlim([1,1000])
    # ax3.set_ylim([0.00001,1])
    ax3.legend(loc='upper right')
    ax3.grid(True)

    # Save plots to PNG
    fig1.savefig('figure1_nodes_v_time_mbernard.png', dpi=150)
    fig2.savefig('figure2_edges_v_time_mbernard.png', dpi=150)
    fig3.savefig('figure3_degrees_dist_mbernard.png', dpi=150)

    plt.show()

def main():
    print("Running to t ="+str(totalTime))
    start_time = time()
    for i, p in enumerate(birth_probs):
        initGraph()
        run = True
        while run:
            data = run_sim(p, t=totalTime)
            if data != False:
                run = False
            else:
                # restart sim
                G.clear()
                pass

        for point in data:
            final_data[i][0].append(point[0])
            final_data[i][1].append(point[1])
            final_data[i][2].append(point[2])
        #final_data.append(data)

        degrees = []
        for node in G.nodes():
            degrees.append(G.degree(node))

        p_k_list = []
        for j in range(max(degrees)+1):
            noOfNodes = degrees.count(j)
            if noOfNodes > 0:
                degree_list[i].append(j)
                p_k_list.append(degrees.count(j)/len(G.nodes()))

        for m, p_k in enumerate(p_k_list):
            p_k_prime_list[i].append(sum(p_k_list[m:]))

    exec_time = time() - start_time
    print("\nExectution Time:", str(round(exec_time, 4)) + " seconds", "\n")
    print("Simulation completed, plotting data...")
    plot_data()
    

if __name__ == "__main__":
    main()

