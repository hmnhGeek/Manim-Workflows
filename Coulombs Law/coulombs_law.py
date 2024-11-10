from manim import *


class CoulombsLaw(Scene):
    def construct(self):
        text = Text("Coulomb's Law")
        self.play(FadeIn(text), run_time=2)
        self.play(text.animate.to_edge(UP), run_time=2)
        self.wait(2)
        coulomb_law_equation = MathTex(r"F = \frac{1}{4\pi\epsilon_{o}} \frac{q_1 \times q_2}{r^{2}}")
        self.play(Write(coulomb_law_equation))
        self.wait(2)
        self.play(coulomb_law_equation.animate.to_edge(LEFT), run_time=2)
        self.wait(1)
        electron = Dot(color=GREEN).shift(RIGHT/4)
        q1_label = MathTex("q_1").next_to(electron, DOWN)
        proton = Dot(color=BLUE).shift(RIGHT * 6)
        q2_label = MathTex("q_2").next_to(proton, DOWN)
        self.play(FadeIn(electron), FadeIn(proton), FadeIn(q1_label), FadeIn(q2_label))
        self.wait(1)
        arrow = DoubleArrow(start=electron.get_center(), end=proton.get_center())
        distance_label = MathTex("r").next_to(arrow, DOWN)
        self.play(FadeIn(arrow), Write(distance_label))
        self.wait(1)
        up_factor = 1
        self.play(
            electron.animate.shift(UP * up_factor),
            proton.animate.shift(UP * up_factor),
            q1_label.animate.shift(UP * up_factor),
            q2_label.animate.shift(UP * up_factor),
            coulomb_law_equation.animate.shift(UP * up_factor),
            arrow.animate.shift(UP * up_factor),
            distance_label.animate.shift(UP * up_factor)
        )
        self.wait(1)
        definition = Text(
            """
            Coulomb's Law describes the electrostatic force between two point charges. 
            It states that the force is directly proportional to the product of the 
            charges and inversely proportional to the square of the distance between them.
            """
        ).scale_to_fit_width(13)
        self.play(FadeIn(definition), definition.animate.shift(DOWN * 1.5), run_time=2)
        self.wait(5)
        self.play(
            FadeOut(coulomb_law_equation),
            FadeOut(electron),
            FadeOut(proton),
            FadeOut(q1_label),
            FadeOut(q2_label),
            FadeOut(arrow),
            FadeOut(distance_label),
            FadeOut(definition),
        )
        self.wait(1)
        self.play(text.animate.move_to(ORIGIN), run_time=2)
        self.wait(2)
        self.play(FadeOut(text), run_time=2)
        self.wait(1)


class ForceDistanceRelation(Scene):
    @staticmethod
    def force_function(r):
        k = 1  # Assuming k (1/4πε₀) as 1 for simplicity
        return k / r ** 2

    def construct(self):
        # Step 1: Display the Coulomb's Law formula
        coulomb_law_equation = MathTex(r"F = \frac{1}{4\pi\epsilon_{o}} \frac{q_1 \times q_2}{r^2}")
        self.play(Write(coulomb_law_equation))
        self.wait(1)

        # Step 2: Substitute values for the formula
        substituted_equation = MathTex(r"F = \frac{1}{4\times 3.14159 \times 8.85 \times 10^{-12}} \frac{(1) \times (1)}{r^2}").scale(1.5)
        substituted_equation.move_to(coulomb_law_equation)

        # Animate the substitution of values (q1 = q2 = 1)
        self.play(Transform(coulomb_law_equation, substituted_equation))
        self.wait(5)

        self.play(
            FadeOut(coulomb_law_equation),
            FadeOut(substituted_equation)
        )

        self.wait(1)

        axes = Axes(
            x_range=[0.1, 10, 1],
            y_range=[0, 20, 2],
            x_length=7,
            y_length=5,
            x_axis_config={"include_numbers": True, "font_size": 24},
            y_axis_config={"include_numbers": True, "font_size": 24},
            axis_config={"color": BLUE},
            tips=True
        )

        x_label = MathTex("r").next_to(axes.x_axis, RIGHT)
        y_label = MathTex("F").next_to(axes.y_axis, UP)

        force_graph = axes.plot(ForceDistanceRelation.force_function, color=YELLOW, x_range=[0.1, 10])
        graph_label = MathTex("F \\propto \\frac{1}{r^2}").next_to(force_graph, UP, buff=0.5)
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(force_graph), Write(graph_label))

        # Adding some sample points for emphasis
        # sample_points = [
        #     Dot(axes.coords_to_point(r, ForceDistanceRelation.force_function(r)), color=RED)
        #     for r in [0.5, 1, 2, 3, 4]
        # ]
        # self.play(*[FadeIn(point) for point in sample_points])

        # Display the graph
        self.wait(2)