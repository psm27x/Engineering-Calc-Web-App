from flask import Blueprint, render_template, request, session
from app.calculations import electrical as electrical_calc

electrical_bp = Blueprint('electrical', __name__)

@electrical_bp.route('/', methods=['GET', 'POST'])
def electrical_page():
    result = None
    calc_type = request.form.get('calculation') if request.method == 'POST' else None

    if request.method == 'POST':
        try:
            if calc_type == 'voltage':
                current = float(request.form['current_v'])
                resistance = float(request.form['resistance_v'])
                result = electrical_calc.calculate_voltage(current, resistance)

            elif calc_type == 'current':
                voltage = float(request.form['voltage_i'])
                resistance = float(request.form['resistance_i'])
                result = electrical_calc.calculate_current(voltage, resistance)

            elif calc_type == 'power':
                voltage = float(request.form['voltage_p'])
                current = float(request.form['current_p'])
                result = electrical_calc.calculate_power(voltage, current)

            elif calc_type == 'resistance':
                voltage = float(request.form['voltage_r'])
                current = float(request.form['current_r'])
                result = electrical_calc.calculate_resistance(voltage, current)

            elif calc_type == 'energy':
                power = float(request.form['power_e'])
                time = float(request.form['time_e'])
                result = electrical_calc.calculate_energy(power, time)

            elif calc_type == 'capacitor_energy':
                capacitance = float(request.form['capacitance'])
                voltage = float(request.form['voltage_c'])
                result = electrical_calc.calculate_capacitor_energy(capacitance, voltage)

            # ✅ Save to session-based history (correctly reassign)
            if result and calc_type:
                history = session.get('history', [])
                history.append({
                    'module': 'Electrical',
                    'calculation': calc_type,
                    'result': result
                })
                session['history'] = history

        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template('electrical.html', result=result, calc_type=calc_type)
