# SIS SIR SIRD model
Simple SIS SIR SIRD model written in Python
## class Node
This class is used for building a graph. Properties:

| Property      | Type          | Comment                                       |
 :-------------:|:-------------:|:----------------------------------------------|
| id            | int           | Node ID                                       | 
| S             | Bool          | Susceptible                                   |
| I             | Bool          | Infected                                      |
| R             | Bool          | Removed                                       |
| D             | Bool          | Died                                          |
| neighbors     | list          | Neighbors of Node                             |
| i             | int           | Node vertical position (for quadratic graph)  |
| j             | int           | Node horisobtal position (for quadratic graph)|
    
![Image alt](https://github.com/titamik/SIS_SIR_SIRD_model/blob/master/graph.png)
List of neighbors used for more quickly single step model processing. Also, using by this class you can create your own graph. You just need to specify the neighbors of the node as a list:

```python myNodes[1] = Node(1, [3,4])
myNodes[1] = Node(1, [3])
myNodes[2] = Node(2, [1,2])
myNodes[3] = Node(3, [])
```

As you can see, graph can be oriented. The node can go into itself.
## class SIRDmodel
| Property      | Type          | Comment                                       |
 :-------------:|:-------------:|:----------------------------------------------|
| iteration     | int           | The current number of the iteration           | 
| probI         | float         | Probability of infection                      |
| probR         | float         | Probability of remove                         |
| probD         | float         | Probability of die                            |
| Nodes         | list          | List of Nodes                                 |
| S             | list          | List of Susceptible Nodes                     |
| I             | list          | List of Infected Nodes                        |
| R             | list          | List of Removed Nodes                         |
| D             | list          | List of Died Nodes                            |
| speed         | int           | Pause between iterations (seconds)            |
| iterations    | int           | The number of the iterations                  |
