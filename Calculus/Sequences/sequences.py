from manim import *

#    __                  _   _
#   / _|_   _ _ __   ___| |_(_) ___  _ __  ___
#  | |_| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#  |  _| |_| | | | | (__| |_| | (_) | | | \__ \
#  |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/

# This function returns data from .csv to an array
def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords
# LEARN MORE HERE:
# https://www.youtube.com/watch?v=Xi52tx6phRU


#        _         _                  _
#   __ _| |__  ___| |_ _ __ __ _  ___| |_
#  / _` | '_ \/ __| __| '__/ _` |/ __| __|
# | (_| | |_) \__ \ |_| | | (_| | (__| |_
#  \__,_|_.__/|___/\__|_|  \__,_|\___|\__|
#   ___  ___ ___ _ __   ___  ___
#  / __|/ __/ _ \ '_ \ / _ \/ __|
#  \__ \ (_|  __/ | | |  __/\__ \
#  |___/\___\___|_| |_|\___||___/
# Abstract scenes

class GraphFromData(GraphScene):
    # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius=0.1):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

#       _
#   ___| | __ _ ___ ___  ___  ___
#  / __| |/ _` / __/ __|/ _ \/ __|
# | (__| | (_| \__ \__ \  __/\__ \
#  \___|_|\__,_|___/___/\___||___/
# This classes returns graphs
class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)

#   ___  ___ ___ _ __   ___  ___
#  / __|/ __/ _ \ '_ \ / _ \/ __|
#  \__ \ (_|  __/ | | |  __/\__ \
#  |___/\___\___|_| |_|\___||___/
# Graph with set of points
class CustomGraph1(GraphFromData):
    def construct(self):
        self.setup_axes()
        coords = get_coords_from_csv("custom_graphs/data")
        dots = self.get_dots_from_coords(coords)
        self.add(dots)

# Discrete Graph
class CustomGraph2(GraphFromData):
    def construct(self):
        self.setup_axes()
        # Get coords
        coords = get_coords_from_csv("custom_graphs/data")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        # Set dots
        dots = self.get_dots_from_coords(coords)
        self.add(dots)
        self.play(ShowCreation(graph,run_time=4))
        self.wait(3)

# Smooth graph
class CustomGraph3(GraphFromData):
    CONFIG = {
        "y_max": 25,
    }
    def construct(self):
        self.setup_axes()
        x = [0 , 1, 2, 3,  4,  5,  6,  7]
        y = [0 , 1, 4, 9, 16, 25, 20, 10]

        coords = [[px,py] for px,py in zip(x,y)]
        # |
        # V
        points = self.get_points_from_coords(coords)

        graph = SmoothGraphFromSetPoints(points,color=GREEN)
        dots = self.get_dots_from_coords(coords)

        self.add(graph,dots)

# But, we can do the same thing with a simple SCENE
class CustomGraph4(Scene):
    def construct(self):
        axes = Axes()
        x = [0 , 1, 2, 3,  4, 5,  6]
        y = [0 , 1, 0, -1, 0,  1, 0]

        coords = [[px,py] for px,py in zip(x,y)]
        # |
        # V
        points = self.get_points_from_coords(axes,coords)

        dots = self.get_dots_from_coords(axes,coords)
        graph = SmoothGraphFromSetPoints(points,color=GREEN)

        self.play(
            LaggedStart(DrawBorderThenFill(axes)),
            run_time = 5,
            lag_ratio = 1,
        )

        self.add(dots)
        self.wait()

    def get_points_from_coords(self,axes,coords):
        return [axes.coords_to_point(px,py)
            for px,py in coords
            ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,axes,coords,radius=0.1):
        points = self.get_points_from_coords(axes,coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots


#               ____          _____ ____
#              | __ ) _   _  |_   _| __ )
#              |  _ \| | | |   | | |  _ \
#              | |_) | |_| |   | | | |_) |
#              |____/ \__, |   |_| |____/
#                     |___/
