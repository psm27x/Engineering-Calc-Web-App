def calculate_voltage(current, resistance):
    return round(current * resistance, 4)

def calculate_current(voltage, resistance):
    if resistance == 0:
        return "Resistance cannot be zero"
    return round(voltage / resistance, 4)

def calculate_power(voltage, current):
    return round(voltage * current, 4)

def calculate_resistance(voltage, current):
    if current == 0:
        return "Current cannot be zero"
    return round(voltage / current, 4)

def calculate_energy(power, time):
    return round(power * time, 4)

def calculate_capacitor_energy(capacitance, voltage):
    return round(0.5 * capacitance * voltage**2, 4)
