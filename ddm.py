import random

class Player():
    def __init__(self):
        self.xy = (0, 0)
    
class Level():
    def __init__(self, size_min=20, size_max=50):
        if size_min > size_max:
            raise ValueError("Minimum map size is larger than maximum size.")
        x0 = 0
        y0 = 0
        self.rooms = [(x0, y0)]
        self.walls = []
        # recursively set up map starting at center
        self._make_neighbors(x0, y0, size_min, size_max)
        while len(self.rooms) < size_min:
            tmp = self.walls.pop()
            self.rooms.append(tmp)
            self._make_neighbors(tmp[0], tmp[1], size_min, size_max)
        # Place random exit
        num = random.randint(0, len(self.rooms) - 1)
        self.exit = self.rooms[num]

    def _make_neighbors(self, x, y, size_min, size_max):
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
                if random.randint(0, 1) == 0 or len(self.rooms) >= size_max:
                    self.walls.append((x, y))
                else:
                    self.rooms.append((x, y))
                    self._make_neighbors(x, y, size_min, size_max)

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

    def isExit(self, x, y):
        """
        Returns the state of the map at the specified position.
        True: Exit
        False: No Exit
        """
        if (x, y) == self.exit:
            return True
        return False

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
            line = ""
            for x in range(x_min, x_max + 1):
                state = self.isRoom(x, y)
                if state is True:
                    symbol = "O"
                else:
                    symbol = " "
                line += symbol
            print(line)
