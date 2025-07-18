# mytools

Library of my useful functions in Python
- temperature: conversion Celsius <-> Fahrenheit
    - c2f(c) - Celsius -> Fahrenheit
    - f2c(f) - Fahrenheit - Celsius
- math_extra:
    - sincos_fraction(fraction) - Calculating sine and cosine based on the size of an angle given as a circle fraction. Return as complex number (cos + i sin).
    - split_complex(z) - Give complex number as tuple. Useful for `a,b = split_comlex(z)`
    - rotate_complex_point(point: complex, fraction: float) -> comple - rotate 2D point give as a complex number around the center of reference (0,0)
    - rotate_around(point: complex, center: complex, fraction: float) -> complex - rotate not around centre of reference but a given point (as a complex number too).
    - koch_segment(a: complex, b: complex, depth: int) -> list[complex] - return list of points (as complex numbers) for a koch curve of given depth betwen two points a and b (as complex nu too)
    - koch_snowflake(n: int) -> list[complex] - create points for koch snowflake - can be chaned
    - koch_snowflake2(n: int) -> list[complex] - create points for koch snowflake - can be chaned

