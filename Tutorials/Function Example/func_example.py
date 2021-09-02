from manim import *
import numpy as np

class FunctionExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, .5],
            y_range=[-3, 4, 1],
            x_axis_config={"numbers_to_include": [-4, -3, 3, 4]},
            y_axis_config={"numbers_to_include": [-2, 2, 3]},
            tips=True
        )
        axes_labels=axes.get_axis_labels()
        # Get the graph of a simple functions
        graph = axes.get_graph(lambda x: np.sin(1/x), color=RED)
        # Set up its label
        graph_label = axes.get_graph_label(
            graph, x_val=1, direction=2 * UP + RIGHT,
           label=r'f(x) = \sin(\frac{1}{x})', color=DARK_BLUE
        )

        # Graph the axes components together
        axes_group = VGroup(axes, axes_labels)
        
        # Animate
        self.play(Create(axes_group), run_time=2)
        self.wait(0.25)
        self.play(Create(graph), run_time=3)
        self.play(Write(graph_label), run_time=2)

class ThreeDSurface(ThreeDScene):
    def construct(self):
        res = 30
        self.set_camera_orientation(phi=50*DEGREES, theta=-30*DEGREES)
        
        def ripple(u, v):
            x = u
            y = v
            z = np.sin(10*(x**2 + y**2)) / 10
            return np.array([x, y, z])
        
        ripple_plane = ParametricSurface(
            ripple, resolution=(res, res),
            v_range=[-3, 3],
            u_range=[-3, 3],
            checkerboard_colors=None
        )
        # Set up the ripple plane
        ripple_plane.scale_about_point(1.5, ORIGIN)
        ripple_plane.set_style(fill_opacity=.5, stroke_color=ORANGE)
        # Create 3D axes
        axes = ThreeDAxes()
        # Animate
        self.add(axes)
        self.play(GrowFromCenter(ripple_plane), run_time=3)
        # Rotate around the Z axis for 20 seconds
        self.begin_ambient_camera_rotation()
        self.wait(20)
        self.stop_ambient_camera_rotation()