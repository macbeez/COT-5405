# COT 5405: Programming Assignment 2
## Description
This program simulates the addition and removal of nodes from a random graph process. A node is added to the graph with a probability of *p*. The node on the other end of the edge of the new node is selected based on a linear preferential attachment rule which is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathbb{P}_{t&plus;1}[u]&space;=&space;\frac{{d}_{t}(u)}{2{m}_{t}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathbb{P}_{t&plus;1}[u]&space;=&space;\frac{{d}_{t}(u)}{2{m}_{t}}" title="\mathbb{P}_{t+1}[u] = \frac{{d}_{t}(u)}{2{m}_{t}}" /></a>

Where:
- d<sub>t</sub>(u) is the degree of a given node in graph G<sub>t</sub>
- m<sub>t</sub> is the total number of edges in graph G<sub>t</sub>

A node is removed from a graph with a probability of *q* (where *q = 1-p*). The node selected to delete is chosen based on a probability distribution that favors small degree nodes. When a node is deleted, all edges associated with that node will be removed as well. The probability is determined based on the following formula:

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathbb{P}_{t&plus;1}[u]&space;=&space;\frac{2{m}_{t}-{d}_{t}(u)}{2{m}_{t}({n}_{t}-1)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathbb{P}_{t&plus;1}[u]&space;=&space;\frac{2{m}_{t}-{d}_{t}(u)}{2{m}_{t}({n}_{t}-1)}" title="\mathbb{P}_{t+1}[u] = \frac{2{m}_{t}-{d}_{t}(u)}{2{m}_{t}({n}_{t}-1)}" /></a>

Where:
- d<sub>t</sub>(u) is the degree of a given node in graph G<sub>t</sub>
- n<sub>t</sub> is the total number of nodes in graph G<sub>t</sub>
- m<sub>t</sub> is the total number of edges in graph G<sub>t</sub>

In this script, the behavior of G<sub>t</sub> is analyzed with p = 0.6. 0.75, 0.8 and 0.9. The output will display the following graphs (using matplotlib):

- Number of Nodes vs. Time
- Number of Edges vs. Time
- Degree Distribution of Nodes
 
 
## Requirements
This script is written for Python 3 and requires the following modules in order to run properly:
- matplotlib
- numpy
- networkx
- tkinter

To install in Windows:
```bash
pip3 install --upgrade matplotlib numpy networkx
```
To install in macOS:
```bash
sudo -H pip3 install --upgrade matplotlib numpy networkx
```

To install in Ubuntu (debian linux):
```bash
sudo -H pip3 install --upgrade matplotlib numpy networkx
sudo apt-get install python3-tk
```
## Usage 
To run the simulation type the following command into the command prompt:
In Windows:
```bash
py -3 generate_random_graph_final.py
```
In macOS and Ubuntu (debian linux):
```bash
python3 generate_random_graph_final.py
```
Output will look like the following:

### Figure 1:
![Figure 1](https://raw.githubusercontent.com/monicabernard/COT-5405/master/project2/figure1_nodes_v_time_mbernard.jpeg)

### Figure 2:
![Figure 2](https://github.com/monicabernard/COT-5405/blob/master/project2/figure2_edges_v_time_mbernard.jpeg?raw=true)

### Figure 3:
![Figure 3](https://github.com/monicabernard/COT-5405/blob/master/project2/figure3_degrees_dist_mbernard.jpeg?raw=true)
