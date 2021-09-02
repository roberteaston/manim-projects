from manim import *

class AnimationShowIncreasingSubsets(Scene):
    def construct(self):
        axes = Axes(
            x_range = [0, 10, 1],
            y_range = [0, 10, 1],
        )
        self.play(Create(axes))
        self.wait()

        points = []
        for x in range(1,10):
            points.append(Dot(point=np.array([x, x*x, 0.0])))
        group = VGroup(*points)
        self.play(ShowIncreasingSubsets(group, run_time=10.0))

class MovingCameraOnGraph(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        axes = Axes(
            x_range=[0, 10],
            y_range=[0, 10]
        )
        self.play(Create(axes))
        self.wait()

        graph = axes.get_graph(lambda x: x*x, color=WHITE, x_range=[0, 10])

        dot_1 = Dot(axes.i2gp(graph.t_min, graph))
        dot_2 = Dot(axes.i2gp(graph.t_max, graph))
        # self.add(axes, graph, dot_1, dot_2)

        points = []
        for index in range(0,10):
            points.append(Dot(axes.i2gp(index, graph)))
        group = VGroup(*points)
        self.play(ShowIncreasingSubsets(group, run_time=10.0))

        self.wait()

        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
        self.play(self.camera.frame.animate.move_to(dot_2))
        self.play(Restore(self.camera.frame))
        self.wait()
