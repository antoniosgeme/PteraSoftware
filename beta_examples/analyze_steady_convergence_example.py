# ToDo: Document this script.

import logging

import pterasoftware as ps

# Configure a logger for this example.
example_logger = logging.getLogger("example")
example_logger.setLevel(logging.DEBUG)

# Create an airplane object. Read through the solver examples for more details on
# creating this object.
leading_airplane = ps.geometry.Airplane(
    weight=250,
    wings=[
        ps.geometry.Wing(
            symmetric=True,
            chordwise_spacing="uniform",
            wing_cross_sections=[
                ps.geometry.WingCrossSection(
                    airfoil=ps.geometry.Airfoil(
                        name="naca2412",
                    ),
                    spanwise_spacing="cosine",
                ),
                ps.geometry.WingCrossSection(
                    x_le=0.0,
                    y_le=5.0,
                    z_le=0.0,
                    chord=1.0,
                    airfoil=ps.geometry.Airfoil(
                        name="naca2412",
                    ),
                ),
                ps.geometry.WingCrossSection(
                    x_le=0.25,
                    y_le=10.0,
                    z_le=0.0,
                    chord=1.0,
                    airfoil=ps.geometry.Airfoil(
                        name="naca2412",
                    ),
                ),
            ],
        ),
        ps.geometry.Wing(
            x_le=5.0,
            symmetric=True,
            chordwise_spacing="uniform",
            wing_cross_sections=[
                ps.geometry.WingCrossSection(
                    airfoil=ps.geometry.Airfoil(
                        name="naca0012",
                    ),
                    spanwise_spacing="cosine",
                ),
                ps.geometry.WingCrossSection(
                    x_le=0.0,
                    y_le=5.0,
                    z_le=0.0,
                    chord=1.0,
                    airfoil=ps.geometry.Airfoil(
                        name="naca0012",
                    ),
                ),
            ],
        ),
    ],
)

trailing_airplane = ps.geometry.Airplane(
    weight=250,
    x_ref=10,
    y_ref=-5,
    wings=[
        ps.geometry.Wing(
            x_le=10,
            y_le=-5,
            symmetric=True,
            chordwise_spacing="uniform",
            wing_cross_sections=[
                ps.geometry.WingCrossSection(
                    airfoil=ps.geometry.Airfoil(
                        name="naca2412",
                    ),
                    spanwise_spacing="cosine",
                ),
                ps.geometry.WingCrossSection(
                    x_le=0.0,
                    y_le=5.0,
                    z_le=0.0,
                    chord=1.0,
                    airfoil=ps.geometry.Airfoil(
                        name="naca2412",
                    ),
                ),
                ps.geometry.WingCrossSection(
                    x_le=0.25,
                    y_le=10.0,
                    z_le=0.0,
                    chord=1.0,
                    airfoil=ps.geometry.Airfoil(
                        name="naca2412",
                    ),
                ),
            ],
        ),
        ps.geometry.Wing(
            x_le=15.0,
            y_le=-5,
            symmetric=True,
            chordwise_spacing="uniform",
            wing_cross_sections=[
                ps.geometry.WingCrossSection(
                    airfoil=ps.geometry.Airfoil(
                        name="naca0012",
                    ),
                    spanwise_spacing="cosine",
                ),
                ps.geometry.WingCrossSection(
                    x_le=0.0,
                    y_le=5.0,
                    z_le=0.0,
                    chord=1.0,
                    airfoil=ps.geometry.Airfoil(
                        name="naca0012",
                    ),
                ),
            ],
        ),
    ],
)


default_operating_point = ps.operating_point.OperatingPoint()

# Construct this example's problem object.
default_problem = ps.problems.SteadyProblem(
    airplanes=[leading_airplane, trailing_airplane],
    operating_point=default_operating_point,
)

converged_attributes = ps.convergence.analyze_steady_convergence(
    base_problem=default_problem, solver_type="steady ring vortex lattice method"
)