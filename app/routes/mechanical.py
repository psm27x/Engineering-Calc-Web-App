from flask import Blueprint, render_template, request, session
from app.calculations import mechanical as mech_calc

mechanical_bp = Blueprint('mechanical', __name__)

@mechanical_bp.route('/', methods=['GET', 'POST'])
def mechanical_page():
    result = None
    calc_type = request.form.get('calculation') if request.method == 'POST' else None

    if request.method == 'POST':
        try:
            if calc_type == 'force':
                mass = float(request.form['mass'])
                accel = float(request.form['acceleration'])
                result = mech_calc.force(mass, accel)

            elif calc_type == 'work':
                f = float(request.form['force_work'])
                d = float(request.form['distance'])
                result = mech_calc.work_done(f, d)

            elif calc_type == 'kinetic_energy':
                m = float(request.form['mass_ke'])
                v = float(request.form['velocity'])
                result = mech_calc.kinetic_energy(m, v)

            elif calc_type == 'power':
                w = float(request.form['work_done'])
                t = float(request.form['time'])
                result = mech_calc.power_formula(w, t)

            elif calc_type == 'potential_energy':
                m = float(request.form['mass_pe'])
                h = float(request.form['height_pe'])
                result = mech_calc.potential_energy(m, h)

            elif calc_type == 'pressure':
                f = float(request.form['force_press'])
                a = float(request.form['area_press'])
                result = mech_calc.pressure(f, a)

            elif calc_type == 'density':
                m = float(request.form['mass_den'])
                vol = float(request.form['volume_den'])
                result = mech_calc.density(m, vol)

            # ✅ Save to session history (correctly reassign)
            if result and calc_type:
                history = session.get('history', [])
                history.append({
                    'module': 'Mechanical',
                    'calculation': calc_type,
                    'result': result
                })
                session['history'] = history  # must reassign to trigger session save

        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template('mechanical.html', result=result, calc_type=calc_type)
