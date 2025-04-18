from flask import Blueprint, render_template, request, session
from app.calculations import civil
import matplotlib.pyplot as plt
import numpy as np
import os

civil_bp = Blueprint('civil', __name__)

@civil_bp.route('/', methods=['GET', 'POST'])
def civil_page():
    result = None
    plot_url = None
    calc_type = request.form.get('calculation') if request.method == 'POST' else None

    if request.method == 'POST':
        try:
            if calc_type == 'beam_deflection':
                force = float(request.form['force'])
                length = float(request.form['length'])
                inertia = float(request.form['inertia'])
                modulus = float(request.form['modulus'])
                result = civil.beam_deflection(force, length, inertia, modulus)

                # Plot
                x = np.linspace(0, length, 100)
                y = -(force * x**2) * (3 * length - x) / (6 * modulus * inertia)
                plot_path = os.path.join('app', 'static', 'beam_plot.png')
                plt.figure()
                plt.plot(x, y)
                plt.title('Beam Deflection Curve')
                plt.xlabel('Length (m)')
                plt.ylabel('Deflection (m)')
                plt.grid(True)
                plt.savefig(plot_path)
                plt.close()
                plot_url = '/static/beam_plot.png'

            elif calc_type == 'bending_stress':
                moment = float(request.form['moment'])
                distance = float(request.form['distance'])
                section_modulus = float(request.form['section_modulus'])
                result = civil.bending_stress(moment, distance, section_modulus)

            elif calc_type == 'moment_inertia':
                base = float(request.form['base'])
                height = float(request.form['height'])
                result = civil.moment_of_inertia(base, height)

            elif calc_type == 'slenderness_ratio':
                length = float(request.form['length_sr'])
                radius = float(request.form['radius_sr'])
                result = civil.slenderness_ratio(length, radius)

            elif calc_type == 'shear_stress':
                force = float(request.form['force_ss'])
                area = float(request.form['area_ss'])
                result = civil.shear_stress(force, area)

            elif calc_type == 'concrete_volume':
                length = float(request.form['length_cv'])
                width = float(request.form['width_cv'])
                depth = float(request.form['depth_cv'])
                result = civil.concrete_volume(length, width, depth)

            # ✅ Save to session-based history (correctly reassign)
            if result and calc_type:
                history = session.get('history', [])
                history.append({
                    'module': 'Civil',
                    'calculation': calc_type,
                    'result': result
                })
                session['history'] = history

        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template('civil.html', result=result, plot_url=plot_url, calc_type=calc_type)
