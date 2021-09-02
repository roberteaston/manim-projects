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
      MathTex("f(x)=x^2")
      .next_to(graph1, UR, buff=0.2)
      .set_color(RED)
      .scale(0.8)
    )

    c = ValueTracker(-4)

    graph2 = always_redraw(
        lambda: plane.get_graph(
            lambda x: x**2 + c.get_value(), x_range=[-3,3], color=YELLOW
        )
    )

    graph2_lab = always_redraw(
        lambda: MathTex("f(x)=x^2+c")
        .next_to(graph2, UR, buff=0.2)
        .set_color(YELLOW)
        .scale(0.8)
    )

    k = ValueTracker(-3)
    dot1 = always_redraw(
        lambda: Dot().move_to(
            plane.coords_to_point(
                k.get_value(), graph1.underlying_function(k.get_value())
            )
        )
    )
    slope1 = always_redraw(
        lambda: plane.get_secant_slope_group(
            x=k.get_value(), graph=graph1, dx=0.01, secant_line_length = 5
        )
    )

    slope2 = always_redraw(
        lambda: plane.get_secant_slope_group(
            x=k.get_value(), graph=graph2, dx=0.01, secant_line_length = 5
        )
    )

    dot2 = always_redraw(
        lambda: Dot().move_to(
            plane.coords_to_point(
                k.get_value(), graph2.underlying_function(k.get_value())
            )
        )
    )

    self.play(
        LaggedStart(DrawBorderThenFill(plane), Create(graph1), Create(graph2)),
        run_time = 5,
        lag_ratio = 1,
        )
    self.add(slope1, slope2, dot1, dot2, graph1_lab, graph2_lab)
    self.play(
        k.animate.set_value(0), c.animate.set_value(2), run_time=5, rate_func =linear
    )
    self.play(
        k.animate.set_value(3),
        c.animate.set_value(-2),
        run_time = 5,
        rate_func = linear,
    )
    self.wait()
