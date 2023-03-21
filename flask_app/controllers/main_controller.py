from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.loadout_model import Loadout
from flask_app.models.gun_model import Gun
from weapon_data.weapons import weapons, attachments


@app.route("/")
def home():
    form_progress = {}
    if "data" in session:
        form_progress = {
            **session['data']
        }
        del session['data']
    return render_template("form.html", weapons=weapons, attachments=attachments, form_progress=form_progress)


@app.route("/add_loadout", methods=['POST'])
def create_loadout():
    gun_data = {
        'muzzle': request.form['muzzle'],
        'barrel': request.form['barrel'],
        'underbarrel': request.form['underbarrel'],
        'rear_grip': request.form['rear_grip'],
        'optic': request.form['optic'],
        'laser': request.form['laser'],
        'ammo': request.form['ammo'],
        'magazine': request.form['magazine'],
        'stock': request.form['stock'],
        'gun_name': request.form['gun_name'],
        'gun_type': request.form['gun_type']
    }

    if not Gun.validate_info(gun_data) or not Loadout.validate_info(request.form):
        session['data'] = request.form
        return redirect('/')

    if 'data' in session:
        del session['data']
    gun = Gun.add_gun(gun_data)

    loadout_data = {
        'gun_id': gun,
        'creator': request.form['creator'],
        'game_mode': request.form['game_mode']
    }

    Loadout.add_loadout(loadout_data)

    return redirect("/")
