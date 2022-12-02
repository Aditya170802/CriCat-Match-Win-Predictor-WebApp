from masterWinCal import Calc
from flask import Flask, redirect, url_for, render_template, request

gui_integrate = Flask(__name__)

@gui_integrate.route('/')
def welcome():
    return render_template('index.html')

@gui_integrate.route('/', methods=['POST'])
def getValue():
    game = request.form['matchtype']
    bat = request.form['bat_team']
    bowl = request.form['bowl_team']
    pl1 = request.form['team1']
    grnd = request.form['ground']
    tw = float(request.form['tw'])
    gw = float(request.form['gw'])
    pw = float(request.form['pw'])
    pl2 = request.form['team2']

    arr = [tw, gw, pw]
    lp1 = pl1.split(', ')
    lp2 = pl2.split(', ')
    # res = pw
    res, team = Calc.calc(game, bat, bowl, grnd, lp1, lp2, arr)
    if res=="Error":
        return render_template('errortemplate.html', result=res, team=team)
    return render_template('result_output.html', result=res, team=team)

if __name__=='__main__':
    gui_integrate.run(debug=True)