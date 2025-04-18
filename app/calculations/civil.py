def beam_deflection(force, length, inertia, modulus):
    return round((force * length**3) / (3 * modulus * inertia), 4)

def bending_stress(moment, distance, section_modulus):
    return round((moment * distance) / section_modulus, 4)

def moment_of_inertia(base, height):
    return round((base * height**3) / 12, 4)

def slenderness_ratio(length, radius):
    return round(length / radius, 4)

def shear_stress(force, area):
    return round(force / area, 4)

def concrete_volume(length, width, depth):
    return round(length * width * depth, 4)
