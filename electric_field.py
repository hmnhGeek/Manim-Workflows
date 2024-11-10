from manim import *
import math

# Constants
k_e = 8.99e9  # Coulomb constant in N·m²/C²
G = 6.674e-11  # Gravitational constant in N·m²/kg²
q_electron = -1.6e-19  # Charge of electron in Coulombs
q_proton = 1.6e-19  # Charge of proton in Coulombs
m_electron = 9.11e-31  # Mass of electron in kg
m_proton = 1.67e-27  # Mass of proton in kg
distance = 5.3e-11  # Distance between electron and proton in meters

# Calculate Electric Force
F_electric = (k_e * abs(q_electron * q_proton)) / (distance ** 2)

# Calculate Gravitational Force
F_gravitational = (G * m_electron * m_proton) / (distance ** 2)

class ElectricGravitationalForces(Scene):
    def construct(self):
        # Create Electron Sphere
        electron_sphere = Sphere(radius=0.2, color=BLUE).shift(LEFT * 2)
        electron_label = Tex(f"Mass = {m_electron:.2e} kg", color=WHITE).next_to(electron_sphere, DOWN)
        electron_charge = Tex(f"Charge = {q_electron:.2e} C", color=WHITE).next_to(electron_label, DOWN)
        
        # Show Electron
        self.play(Create(electron_sphere), Write(electron_label), Write(electron_charge))
        self.wait(1)
        
        # Shrink Electron to a Dot
        self.play(electron_sphere.animate.scale(0.1), electron_label.animate.scale(0.1), electron_charge.animate.scale(0.1))
        self.wait(1)
        
        # Create Proton Sphere
        proton_sphere = Sphere(radius=0.2, color=RED).shift(RIGHT * 2)
        proton_label = Tex(f"Mass = {m_proton:.2e} kg", color=WHITE).next_to(proton_sphere, DOWN)
        proton_charge = Tex(f"Charge = {q_proton:.2e} C", color=WHITE).next_to(proton_label, DOWN)
        
        # Show Proton
        self.play(Create(proton_sphere), Write(proton_label), Write(proton_charge))
        self.wait(1)
        
        # Shrink Proton to a Dot
        self.play(proton_sphere.animate.scale(0.1), proton_label.animate.scale(0.1), proton_charge.animate.scale(0.1))
        self.wait(1)

        # Show Electric Force Formula
        electric_force_formula = MathTex(r"F_{\text{elec}} = \frac{k_e |q_1 q_2|}{r^2}", color=WHITE).to_edge(UP)
        self.play(Write(electric_force_formula))
        self.wait(1)
        
        # Display Electric Force Value
        electric_force_value = MathTex(f"F_{{\\text{{elec}}}} = {F_electric:.2e} \, \\text{{N}}", color=WHITE).to_edge(UP).shift(RIGHT * 3)
        self.play(Write(electric_force_value))
        self.wait(2)

        # Show Gravitational Force Formula
        gravitational_force_formula = MathTex(r"F_{\text{grav}} = \frac{G m_1 m_2}{r^2}", color=WHITE).to_edge(UP)
        self.play(Write(gravitational_force_formula))
        self.wait(1)

        # Display Gravitational Force Value
        gravitational_force_value = MathTex(f"F_{{\\text{{grav}}}} = {F_gravitational:.2e} \, \\text{{N}}", color=WHITE).to_edge(UP).shift(LEFT * 3)
        self.play(Write(gravitational_force_value))
        self.wait(2)

        # Remove the spheres and show force values at the center
        self.play(FadeOut(electron_sphere), FadeOut(proton_sphere), FadeOut(electric_force_formula), FadeOut(gravitational_force_formula))
        self.play(
            electric_force_value.animate.move_to(ORIGIN + DOWN * 1),
            gravitational_force_value.animate.move_to(ORIGIN + UP * 1)
        )
        self.wait(2)
