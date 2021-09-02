from manim import *

class CalculusSlopes(Scene):
  def construct(self):

    plane = NumberPlane(
        x_range = [-3,3,1],
        y_range = [-4,14,1],
        y_length=7,
        x_length=6
    ).add_coordinates()

    graph1 = plane.get_graph(lambda x: x**2, x_range=[-3,3], color=RED)
    graph1_lab = (
      MathTex("f(x)=x^2").next_to(graph1, UR, buff=0.2).set_color(RED).scale(0.8)
    )

    self.play(
        LaggedStart(DrawBorderThenFill(plane),Create(graph1)),
        run_time = 5,
        lag_ratio = 1,
    )
