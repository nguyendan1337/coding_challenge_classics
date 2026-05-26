'''
Main Problem (West to East)

Design an algorithm that processes buildings as they are presented to it and
tracks the buildings that have a view of the sunset. The number of buildings is
not known in advance.

Buildings are given in West to East order and are
specified by their heights.

The amount of memory your algorithm uses should
depend solely on the number of buildings that have a view; in particular it
should not depend on the number of buildings processed.

example_input = [1, 1, 2, 1, 0.1]

                                       +--------+
                                       |   3    |
                         +----+
\\                       |    |
 \\       +----+  +----+ |    |  +----+
Sunset    |  1 |  |  1 | |  2 |  |  1 |         +--0.1--+
   \\     +----+  +----+ +----+  +----+         +----+
'''
class ViewCounter:
    def __init__(self):
        self.buildings_with_view = []

    def number_with_view(self):
        return len(self.buildings_with_view)

    def new_building(self, height):
        while self.buildings_with_view and self.buildings_with_view[-1] < height:
            self.buildings_with_view.pop()
        self.buildings_with_view.append(height)

#sunset at left
### East to West tests
count = ViewCounter()
assert count.number_with_view() == 0
count.new_building(1)
assert count.number_with_view() == 1
count.new_building(1)
assert count.number_with_view() == 2
count.new_building(2)
assert count.number_with_view() == 1
count.new_building(1)
assert count.number_with_view() == 2
count.new_building(0.1)
assert count.number_with_view() == 3