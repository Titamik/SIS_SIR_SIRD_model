# simpleSISmodel
Simple SIS model written in Python
## class Node
This class is used for building a graph. Properties:

| Property        | Type           | Comment  |
| ------------- |:-------------:| :-----|
| id      | int | Node ID |
| D      | Bool      |   False, if healthy |
| neighbors | int[]      |   IDs of nearest neighbors of the node |
| i | int      |    Node vertical position (for quadratic graph) |
| j |int      |    Node horisobtal position (for quadratic graph) |

List of neighbors used for more quickly single step model processing.
