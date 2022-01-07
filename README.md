# Ex4 - pokemon

## Najeeb Abdalla & Yehudit Brickner
__________________________
In this project we had to create an algorithm that makes the agents collect the pokemons.
<br> the object of the algorithm is to collect as many pokeemons as possible-get the highest grade, but to only call the function move upto 10 times per second.
in this project we got the graph agents and pokemons from a server and created a GUI so that you can visualize what the algorithem is doing. 

### how to run the project

????????????????????/
__________________________
### In this project we have 7 classes:

#### node
the node has a (x,y,z) coordinance Id, Tag and Dictionaries.

#### edges
the edge is made up of 2 nodes-src and dest and a weight.

#### DiGraph 
the DiGraph has 2 dictionaries, 1 for the nodes the other for the edges, it also has a mode counter.
<br>In this class we have functions for adding and removing nodes and edges and functions to get the data.

#### client
this is a class that was given tous and we were not spoused to touch it.
<br> this class is how we are able to connect to the server,

#### pokemon
the pokemon has a type, value,(x,y,z) coordinance, and an edge.

#### agent
the agent has an id, value src, dest , speed, (x,y,z) coordinance, and a pokemon.

#### play_game
the calss play game has the algorithms and the GUI. the GUI is its own function in the calss so that the GUI and algorithm are intertwined as little as possible.
<br> the atributes of this calss are graph, agD, pokD
<br> this class has the function:
<br>start game, create_graph, add_pokemon, add_agent, shortest_path, dijsktra, centerPoint,
find_distance, find_correct_edge, attach_pokemon_agent, run_Gui, scale, my_sacle
<br>in the wiki there wwill be an explantion for all the functions

_______________________________

###  Here are our results
|case |moves|grade|pokemons|agents|
|:---:|:---:|:---:|:------:|:----:|
|0    |283  |100  | 1      |1     |
|1    |562  |479  | 2      |1     |
|2    |265  |242  | 3      |1     |
|3    |537  |816  |4       |1     |
|4    |273  |258  | 5      |    1 |
|5    |550  |671  |6       |     1|
|6    |264  |40   |1       |  1   |
|7    |561  |337  |2       |   1  |
|8    |270  |125  |  3     |1     |
|9    |565  |481  |  4     |1     |
|10   |262  |130  |  5     |1     |
|11   |537  |1904 |   6    |3     |
|12   |284  |40   |  1     |1     |
|13   |562  |286  |   2    | 2    |
|14   |277  |135  |  3     | 3    |
|15   |565  |250  |   4    | 1    |



