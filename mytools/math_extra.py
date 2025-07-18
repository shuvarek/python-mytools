
def sincos_fraction(fraction):
    """
    Oblicza sin i cos liczby i podaje jako liczbę zespoloną sin+i*cos
    """
    j = 0+1j
    return( j** ( 4*fraction ) )


def split_complex(z):
    """
    Zwraca część rzeczywistą i urojoną liczby zespolonej jako krotkę (re, im).
    
    Parametr:
        z (complex): liczba zespolona

    Zwraca:
        tuple: (float, float) — część rzeczywista i urojona
    """
    return z.real, z.imag


def rotate_complex_point(point: complex, fraction: float) -> complex:
    from .math_extra import sincos_fraction

    rotation = sincos_fraction(fraction)
    return point * rotation


def rotate_around(point: complex, center: complex, fraction: float) -> complex:
    """
    Obraca punkt wokół innego punktu (centru) o zadany ułamek pełnego obrotu.
    
    Parametry:
        point (complex): Punkt do obrócenia
        center (complex): Środek obrotu
        fraction (float): Ułamek pełnego obrotu (np. 0.25 to 90 stopni)

    Zwraca:
        complex: Punkt po obrocie
    """
    rotation = sincos_fraction(fraction)
    return (point - center) * rotation + center


def koch_segment(a: complex, b: complex, depth: int) -> list[complex]:
    """
    Rekurencyjnie wyznacza punkty na krzywej Kocha między punktami a i b.
    Zwraca listę punktów jako liczby zespolone.

    depth: poziom rekurencji (0 to tylko [a, b])
    """
    if depth == 0:
        return [a, b]

    # Podział odcinka na trzy części
    c = a + (b - a) / 3
    d = a + 2 * (b - a) / 3

    # Wierzchołek trójkąta równobocznego
    e = c + (d - c) * rotate_complex_point(1, 1/6)  # obrót o 60° = 1/6 obrotu

    # Rekurencyjne pododcinki
    part1 = koch_segment(a, c, depth - 1)
    part2 = koch_segment(c, e, depth - 1)
    part3 = koch_segment(e, d, depth - 1)
    part4 = koch_segment(d, b, depth - 1)

    # Sklejanie wyników — pomijamy ostatni punkt każdego fragmentu, poza ostatnim
    return part1[:-1] + part2[:-1] + part3[:-1] + part4


def koch_snowflake(depth: int) -> list[complex]:
    from mytools.math_extra import rotate_complex_point

    a = 0 + 0j
    b = 1 + 0j
    c = rotate_complex_point(b - a, 1/3) + a
    d = rotate_complex_point(b - a, 2/3) + a

    side1 = koch_segment(a, b, depth)
    side2 = koch_segment(b, c, depth)[1:]  # unikaj duplikatów
    side3 = koch_segment(c, a, depth)[1:]

    return side1 + side2 + side3


from mytools.math_extra import rotate_complex_point

def koch_snowflake2(n: int) -> list[complex]:
    def koch(p1, p2, depth):
        if depth == 0:
            return [p1]
        else:
            delta = (p2 - p1) / 3
            a = p1 + delta
            b = a + rotate_complex_point(delta, 1/6)  # obrót o 60°
            c = p1 + 2 * delta
            return (
                koch(p1, a, depth - 1)
                + koch(a, b, depth - 1)
                + koch(b, c, depth - 1)
                + koch(c, p2, depth - 1)
            )

    # Startowe punkty trójkąta równobocznego na okręgu jednostkowym
    p1 = 0 + 1j
    p2 = rotate_complex_point(p1, 1/3)  # obrót o 120°
    p3 = rotate_complex_point(p1, 2/3)  # obrót o 240°

    # Złożenie całego płatka
    points = koch(p1, p2, n) + koch(p2, p3, n) + koch(p3, p1, n)
    points.append(points[0])  # zamknięcie pętli

    return points

