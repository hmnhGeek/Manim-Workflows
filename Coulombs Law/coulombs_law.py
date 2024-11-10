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