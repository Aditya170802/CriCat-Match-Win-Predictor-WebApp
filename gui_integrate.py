from masterWinCal import Calc
from flask import Flask, redirect, url_for, render_template, request
from create_normdata import who_wins

gui_integrate = Flask(__name__)

@gui_integrate.route('/')
def welcome():
    return render_template('opening.html')

@gui_integrate.route('/whowins', methods=['GET', 'POST'])
def getValue():
    if request.method =='POST':
        submit_button = request.form.get('submit_button')
        if submit_button == 'PREDICT':
            game = request.form['matchtype']
            bat = request.form['bat_team']
            bowl = request.form['bowl_team']
            pl1 = request.form.getlist('team1')
            grnd = request.form['ground']
            tw = float(request.form['tw'])
            gw = float(request.form['gw'])
            pw = float(request.form['pw'])
            pl2 = request.form.getlist('team2')
            # print(pl1, pl2)
            arr = [tw, gw, pw]
            # lp1 = pl1.split(', ')
            # lp2 = pl2.split(', ')
            # res = pw
            res, team = Calc.calc(game, bat, bowl, grnd, pl1, pl2, arr)
            if res=="Error":
                return render_template('errortemplate.html', result=res, team=team)
            return render_template('result_output.html', result=res, team=team)
        elif submit_button == 'LATEST':
            game = request.form['matchtype']
            bat = request.form['bat_team']
            bowl = request.form['bowl_team']
            latestdataset = who_wins()
            pl1, pl2 = latestdataset.createdataset(team1=bat.lower(), team2=bowl.lower(), match=game.lower()) 
            print(pl1, pl2)
            return render_template('index.html', pl1=pl1, pl2=pl2, format = game, bat= bat, bowl = bowl)
    else:
        return render_template('index.html', pl1="", pl2="", format = "", bat= "", bowl = "")

if __name__=='__main__':
    gui_integrate.run(debug=True)