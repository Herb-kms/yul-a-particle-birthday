"""Python/Pygame source design for the particle birthday scene.
The hosted page mirrors this projection loop in Canvas because static hosting cannot run Python."""
from math import sin, cos, pi
from random import uniform

FOCAL = 240

def project(x, y, z, center):
    scale = FOCAL / (FOCAL + z)
    return center[0] + x * scale, center[1] + y * scale, scale

def rose_points(center, radius=26, count=115):
    cx, cy, cz = center
    for _ in range(count):
        angle = uniform(0, 2 * pi)
        radial = uniform(0, 1) ** .5
        petal = sin(angle * 3) * 10
        yield (cx + cos(angle) * (radial * radius + petal),
               cy + sin(angle) * (radial * radius * .8 + petal * .35),
               cz + uniform(-18, 18), (241, 63, 100))

