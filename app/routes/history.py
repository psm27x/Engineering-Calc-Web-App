from flask import Blueprint, render_template, session

history_bp = Blueprint('history', __name__)

@history_bp.route('/history')
def show_history():
    history = session.get('history', [])
    return render_template('history.html', history=history)
