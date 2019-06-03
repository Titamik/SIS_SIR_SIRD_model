import random
import time

class Node:

	def __init__(self, idnum, neighbors):
		self.id = idnum # Node ID
		self.D = False # Diseased tag
		self.neighbors = neighbors # Neighbors of Node

		self.i = 0 # Node vertical position (for quadratic graph)
		self.j = 0 # Node horisobtal position (for quadratic graph)

	def getInfo(self):
		return str(self.id) + " " + str(self.D) + " "+ str(self.neighbors)

def generateQuadraticGraph(n,m): # Creating list of Nodes with quadratic graph
	Nodes = []
	k = 0
	for i in range(n):
		for j in range(m):	
			neighbors = []
			
			if i==0:
				if j==0:				
					neighbors.append(k+1)
					neighbors.append(k+m)
				else:
					if j==m-1:
						neighbors.append(k-1)
						neighbors.append(k+m)
					else:
						neighbors.append(k-1)
						neighbors.append(k+1)
						neighbors.append(k+m)
			else:
				if i==n-1:
					if j==m-1:
						neighbors.append(k-m)				
						neighbors.append(k-1)
					else:
						if j==0:
							neighbors.append(k-m)
							neighbors.append(k+1)
						else:
							neighbors.append(k-m)				
							neighbors.append(k-1)
							neighbors.append(k+1)
				else:
					neighbors.append(k-m)
					neighbors.append(k-1)				
					neighbors.append(k+1)	
					neighbors.append(k+m)	

			Nodes.append(Node(k, neighbors))
			Nodes[k].i = i
			Nodes[k].j = j
			k = k + 1
	return Nodes

class SISmodel:
	def __init__(self, probInfection, probRecovery, Nodes):
		self.iteration = 0 # The current number of the iteration
		self.probInfection = probInfection # Probability of infection
		self.probRecovery = probRecovery # Probability of recovery
		self.Nodes = Nodes # List of Nodes
		self.Diseased = [] # List of diseased Nodes
		self.speed = 1 # Pause between iterations (seconds)
		self.iterations = 0 # The number of the iterations

	def Start(self, Diseased, speed, iterations):
		self.Diseased = Diseased # Note infected
		for disease in self.Diseased:
			self.Nodes[disease].D = True 
		self.speed = speed
		self.iterations = iterations
		print(self.getInfo())
		self.__step()

	def Stop(self):
		print('Model stopped')

	def getInfo(self):
		info = 'Iteration: ' + str(self.iteration) + '\n'
		info += 'Number of Diseased Nodes: ' + str(len(self.Diseased)) + '\n'
		info += 'Diseased Nodes: ' + str(self.Diseased) + '\n---'
		return info
	
	def __step(self):
		if len(self.Diseased) > 0 and self.iteration < self.iterations:
			self.iteration = self.iteration + 1
			buf = []
			for i in self.Diseased: # Sort out the diseased
				for neighbor in self.Nodes[i].neighbors: # Sort out the neighbors of the sick
					if self.Nodes[neighbor].D == False and random.random() < self.probInfection: # If the neighbor is healthy and the probability is successful	make him infected	
						self.Nodes[neighbor].D = True
						buf.append(neighbor)
				if random.random() < self.probRecovery: # If probability is successful make it healthy			
					self.Nodes[i].D = False
				else:  #Else mark him infected
					buf.append(i)
			self.Diseased = buf[:]
			print(self.getInfo())
			time.sleep(self.speed)
			self.__step()
		else:
			self.Stop()


print('Model setup:')

probInfection = float(input('Probability of infection (%): '))
probRecovery = float(input('Probability of recovery (%): '))
n,m = map(int, input('The size of the quadratic graph is NxM: ').split()) # You can use your graph, not necessarily square
diseased = list(map(int, input('Diseased Nodes: ').split()))	
speed = int(input('Pause between iterations (seconds): '))
iterations = int(input('The number of the iterations: '))

ModelSIS = SISmodel(probInfection,probRecovery,generateQuadraticGraph(n,m))
ModelSIS.Start(diseased, speed, iterations)

input()
