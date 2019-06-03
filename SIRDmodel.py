import random
import time
from tkinter import *

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

class Node:

	def __init__(self, idnum, neighbors):
		self.id = idnum
		self.S = True  # Susceptible
		self.I = False # Infected
		self.R = False # Removed
		self.D = False # Died
		self.neighbors = neighbors # Neighbors of Node
		self.i = 0 # Node vertical position (for quadratic graph)
		self.j = 0 # Node horisobtal position (for quadratic graph)

class SIRDmodel:

	def __init__(self, probI, probR, probD, Nodes):
		self.iteration = 0 # The current number of the iteration
		self.probI = probI # Probability of infection
		self.probR = probR # Probability of remove
		self.probD = probD # Probability of die
		self.Nodes = Nodes # List of Nodes
		self.S = [] # List of Susceptible Nodes
		self.I = [] # List of Infected Nodes
		self.R = [] # List of Removed Nodes
		self.D = [] # List of Died Nodes
		self.speed = 1 # Pause between iterations (seconds)
		self.iterations = 0 # The number of the iterations

	def Start(self, I, speed, iterations):
		self.S = []
		self.I = I
		self.speed = speed
		self.iterations = iterations
		for Node in self.Nodes:
			self.S.append(Node.id)
		for i in self.I:
			self.Nodes[i].I = True 
		print(self.getInfo())
		self.step()

	def Stop(self):
		print('Model stopped')

	def getInfo(self):
		info = 'Iteration: ' + str(self.iteration) + '\n'
		info += 'S: ' + str(len(self.S)) + ' | ' + str(self.S) + '\n'
		info += 'I: ' + str(len(self.I)) + ' | ' + str(self.I) + '\n'
		info += 'R: ' + str(len(self.R)) + ' | ' + str(self.R) + '\n'
		info += 'D: ' + str(len(self.D)) + ' | ' + str(self.D) + '\n---'
		return info
	
	def step(self):
		if len(self.I) > 0 and self.iteration < self.iterations:
			self.iteration = self.iteration + 1
			bufI = []
			bufS = []
			for i in self.I:
				for neighbor in self.Nodes[i].neighbors: # Sort out the neighbors of the Infected Node
					if self.Nodes[neighbor].I == False and self.Nodes[neighbor].R == False and self.Nodes[neighbor].D == False and random.random() < self.probI: # If the neighbor is healthy and the probability is successful	make him infected	
						self.Nodes[neighbor].I = True
						bufI.append(neighbor)
				if self.Nodes[i].D == False: 
					if self.probD != 0 and random.random() < self.probD: 
							self.Nodes[i].D = True
							self.Nodes[i].I = False
							self.D.append(i)
					else:
						if random.random() < self.probR:	
							self.Nodes[i].I = False
							if self.probR != 0:
								self.Nodes[i].R = True
								self.R.append(i)
						else:  
							bufI.append(i)
			for Node in self.Nodes:
				if Node.S == True and Node.I == False and Node.R == False and Node.D == False:
					bufS.append(Node.id)
			self.S = bufS[:]
			self.I = bufI[:]
			print(self.getInfo())
			time.sleep(self.speed)
			self.step()
		else:
			self.Stop()
		

print('Model setup:')

modelType = input('Model type SIS/SIR')
probI = float(input('Probability of i (%): '))
probR = float(input('Probability of r (%): '))
n,m = map(int, input('The size of the quadratic graph is NxM: ').split()) # You can use your graph, not necessarily square
I = list(map(int, input('I Nodes: ').split()))	
speed = int(input('Pause between iterations (seconds): '))
iterations = int(input('The number of the iterations: '))

ModelSIS = SIRDmodel(probI, probR, probD, generateQuadraticGraph(n,m))
ModelSIS.Start(I,speed,iterations)


input()
