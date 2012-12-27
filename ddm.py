import random


class Level():
    def __init__(self):
        x0 = 0
        y0 = 0
        self.rooms = [(x0, y0)]
        self.walls = []
        # recursively set up map starting at center
        self.makeNeighbors(x0, y0)

    def makeNeighbors(self, x, y):
        """
        Recursively create a map of rooms around given position and add them
        to the rooms/walls lists.
        """
        # we go through all 4 neighboring spaces
        for x, y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            # if we get None back, then the state of the map at this
            # coordinate is not defined yet (room or not) and we have to handle
            # this space now
            if self.isRoom(x, y) is None:
                # draw random int of 0 (wall) or 1 (room)
                if random.randint(0, 1) == 0:
                    self.walls.append((x, y))
                else:
                    self.rooms.append((x, y))
                    self.makeNeighbors(x, y)

    def isRoom(self, x, y):
        """
        Returns the state of the map at the specified position.
        True: Room
        False: Wall
        None: not determined yet / outside of map
        """
        if (x, y) in self.rooms:
            return True
        if (x, y) in self.walls:
            return False
        return None

    def getBounds(self):
        """
        Returns minimum and maximum x and minimum and maximum y coordinates of
        rooms: x_min, x_max, y_min, y_max
        """
        x_min = min([x for x, y in self.rooms])
        x_max = max([x for x, y in self.rooms])
        y_min = min([y for x, y in self.rooms])
        y_max = max([y for x, y in self.rooms])
        return x_min, x_max, y_min, y_max

    def draw(self):
        """
        Print ASCII representation of map.
        """
        x_min, x_max, y_min, y_max = self.getBounds()
        for y in range(y_max, y_min - 1, -1):
            for x in range(x_min, x_max + 1):
                state = self.isRoom(x, y)
                if state is True:
                    symbol = "o"
                else:
                    symbol = " "
                print symbol,
            print
