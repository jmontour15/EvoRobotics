from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER():
    def __init__(self):
        # os.system("del /Q *.nndf")
        os.system("del /Q *.txt")

        self.nextAvailableID = 0
        self.parents = {}
        for robot in range(c.populationSize):
            self.parents[robot] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID +=1
        
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            child = copy.deepcopy(self.parents[parent])
            child.Set_ID(self.nextAvailableID)
            self.nextAvailableID +=1
            self.children[parent] = child

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()
    
    def Evaluate(self, solutions):
        for robot in solutions:
            solutions[robot].Start_Simulation("DIRECT")
        
        for robot in solutions:
            solutions[robot].Wait_For_Simulation_To_End()

    def Select(self):
        for parent in self.parents:
            if self.parents[parent].fitness < self.children[parent].fitness:
                self.parents[parent] = self.children[parent]
    
    def Print(self):
        print("\n")
        for parent in self.parents:
            print(f'Fitness of parent {parent}: {self.parents[parent].fitness}, fitness of child {parent}: {self.children[parent].fitness}')
        print("\n")

    def Show_Best(self):
        best_parent = self.parents[0]
        for parent in self.parents:
            if self.parents[parent].fitness > best_parent.fitness:
                best_parent = self.parents[parent]
        best_parent.Start_Simulation("GUI")
        pass
    