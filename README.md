# simpleSISmodel
Simple SIS model written in Python
## class Node
This class is used for building a graph. Properties:

| Property      | Type          | Comment                                       |
 :-------------:|:-------------:|:----------------------------------------------|
| id            | int           | Node ID                                       | 
| S             | Bool          | Susceptible                                   |
| I             | Bool          | Infected                                      |
| R             | Bool          | Removed                                       |
| D             | Bool          | Died                                         |
|neighbors      | int[]         | Neighbors of Node                             |
|i              | int           | Node vertical position (for quadratic graph)  |
|j              | int           | Node horisobtal position (for quadratic graph)|
    
List of neighbors used for more quickly single step model processing. Also, using by this class you can create your own graph. You just need to specify the neighbors of the node as a list:

```python myNodes[1] = Node(1, [3,4])
myNodes[2] = Node(1, [3])
myNodes[3] = Node(2, [1,2])
myNodes[4] = Node(3, [])
```
![Image alt](https://github.com/titamik/SIS_SIR_SIRD_model/graph.png)
As you can see, graph can be oriented.
