import sys
import random, time, copy

class GameOfLife:
    # Instantiate game of life object with a matrix having 
    # width x height dimensions and determine if a cell within
    # is alive or dead by flipping a coin 1 or 0.
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.alive = 'o'
        self.dead = ' '
        
        self.nextCells = []
        for x in range(self._width):
            column = []
            for y in range(self._height):
                if random.randint(0, 1) == 1:
                    column.append(self.alive) #add a live cell
                else:
                    column.append(self.dead) #add a dead cell
            self.nextCells.append(column)
    
    # Return total number of neighbors
    def neighbors(self, x, y):
        #set neighbor cell coordinates
        #use mod % operation to wrap around edge cells
        left = (x-1) % self._width
        right = (x+1) % self._width
        above = (y-1) % self._height
        below = (y+1) % self._height
        
        # Add up all neighoring cells
        neighbors = 0
        if self.nextCells[left][above] == self.alive:
            neighbors += 1
        if self.nextCells[x][above] == self.alive:
            neighbors += 1
        if self.nextCells[right][above] == self.alive:
            neighbors += 1
        if self.nextCells[left][y] == self.alive:
            neighbors += 1
        if self.nextCells[right][y] == self.alive:
            neighbors += 1
        if self.nextCells[left][below] == self.alive:
            neighbors += 1
        if self.nextCells[x][below] == self.alive:
            neighbors += 1
        if self.nextCells[right][below] == self.alive:
            neighbors += 1
        return neighbors
    
    def printCells(self):
        for x in range(self._height):
            for y in range(self._width):
                print(self.nextCells[x][y], end='')
    
    # Apply the Conway Game of Life rule
    def nextGen(self):
        for x in range(self._width):
            for y in range(self._height):
                neighbors = self.neighbors(x, y)
                #if cell is alive, total neighbors can be 2 or 3
                if self.nextCells[x][y] == self.alive and\
                    (neighbors == 2 or neighbors == 3):
                    self.nextCells[x][y]=self.alive
                #if cell is dead, total neighbors must be 3
                elif self.nextCells[x][y] == self.dead and\
                    neighbors == 3:
                    self.nextCells[x][y]=self.alive
                #else is dead for the lack of neighbors.
                else:
                    self.nextCells[x][y]=self.dead
             
def main():
    life = GameOfLife(50, 50)
    life.printCells()
    
    try:
        while True:
            life.printCells()
            life.nextGen()
            time.sleep(0.5)
    except KeyboardInterrupt:
        sys.exit(0)
        
if __name__ == '__main__':
    main()
    