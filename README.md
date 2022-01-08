# Ex4 - pokemon

## Najeeb Abdalla & Yehudit Brickner
__________________________
In this project we had to create an algorithm that makes the agents collect the pokemons.
<br> the object of the algorithm is to collect as many pokeemons as possible-get the highest grade, but to only call the function move upto 10 times per second.
in this project we got the graph agents and pokemons from a server and created a GUI so that you can visualize what the algorithem is doing. 

### how to run the project

<br>First you will need to make sure that you have python downloaded on your computer.
<br>If it isnt downloaded here is the link to download:
<br>python: https://www.python.org/downloads/
<br>then you will need to check if you have pygame and pygame widgets downloaded.
<br> to check if pygame is downlaoded on your computer run this in powerShell as the administrater "python3 -m pygame.examples.aliens" or "python -m pygame.examples.aliens"
<br> to check if pygame widgets is downloaded write "import pygame_widgets" in your python IDE and make sure that it is reconized.
<br> to download pygame run in your IDE's terminal 'python3 -m pip install -U pygame --user"
<br> to download pygame widgets run in your IDE's terminal "python -m pip install pygame-widgets"
<br>Now that you have everything installed, you can download the project or clone the project or download the release.
<br>open up the project in pycharm or another python IDE
<br> in the python terminal run this "java -jar Ex4_Server_v0.0.jar 0" (you can change the last 0 to any number from 0 to 15)
<br> and run the main. 
__________________________
### In this project we have 8 classes:

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

#### main
this class runs the function start_game
_______________________________

###  Here are our results
|case |moves|grade|pokemons|agents|
|:---:|:---:|:---:|:------:|:----:|
|0    |278  |100  | 1      |1     |
|1    |535  |464  | 2      |1     |
|2    |267  |243  | 3      |1     |
|3    |531  |778  |4       |1     |
|4    |260  |238  | 5      |1     |
|5    |521  |658  |6       |1     |
|6    |266  |40   |1       |  1   |
|7    |542  |337  |2       |   1  |
|8    |256  |125  |  3     |1     |
|9    |512  |424  |  4     |1     |
|10   |254  |130  |  5     |1     |
|11   |456  |1523 |   6    |3     |
|12   |263  |40   |  1     |1     |
|13   |502  |269  |   2    | 2    |
|14   |240  |130  |  3     | 3    |
|15   |486  |250  |   4    | 1    |


-------------------------------
here is the UML of the project

![uml](https://github.com/najeebWorld/Ex4/blob/master/uml%20ex4.png)

_____________________________
here is the a video of case 0

![gif](https://github.com/najeebWorld/Ex4/blob/master/final_61d9c9f90cab430105a290c5_594828.gif)
