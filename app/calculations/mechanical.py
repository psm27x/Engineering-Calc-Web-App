def force(mass, acceleration):
    return round(mass * acceleration, 4)

def work_done(force, distance):
    return round(force * distance, 4)

def kinetic_energy(mass, velocity):
    return round(0.5 * mass * velocity**2, 4)

def power_formula(work, time):
    if time == 0:
        return "Time cannot be zero"
    return round(work / time, 4)

def potential_energy(mass, height, g=9.81):
    return round(mass * g * height, 4)

def pressure(force, area):
    if area == 0:
        return "Area cannot be zero"
    return round(force / area, 4)

def density(mass, volume):
    if volume == 0:
        return "Volume cannot be zero"
    return round(mass / volume, 4)
