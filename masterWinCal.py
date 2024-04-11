#this would be the master or the main place of all calculations for the win prediction.
import pandas as pd
import numpy as np


class Calc:
    def calc(format, teambatting, teambowling, ground,playerslistT1,playerslistT2, weightage):
        # reading all the necessary data files on the basis of format of the match
        if(format=="T20i"):
            players = pd.read_excel('./masterdatafiles/norm_players.xlsx')
            versus = pd.read_excel("./masterdatafiles/t20_tvt.xlsx")
            ground_basis = pd.read_excel('./masterdatafiles/GroundEffect.xlsx')
            default = pd.read_excel('./masterdatafiles/T20_PlayingXI.xlsx')
        elif(format=="Test"):
            players = pd.read_excel('./masterdatafiles/norm_players.xlsx')
            versus = pd.read_excel("./masterdatafiles/test_tvt.xlsx")
            default = pd.read_excel('./masterdatafiles/Test_PlayingXI.xlsx')
            ground_basis = pd.read_excel('./masterdatafiles/GroundEffectTest.xlsx')   
        elif(format=="odi"):
            players = pd.read_excel('./masterdatafiles/norm_players.xlsx')
            versus = pd.read_excel("./masterdatafiles/odi_tvt.xlsx")
            ground_basis = pd.read_excel('./masterdatafiles/GroundEffectodi.xlsx')
            default = pd.read_excel('./masterdatafiles/Odi_PlayingXI.xlsx')
        
        # all the necessary inputs taken from the user
        t1 = teambatting
        t2 = teambowling
        grnd = ground

        if(playerslistT1[0]=="default"):
            playerslistT1 = default[t1].to_list()
        if(playerslistT2[0]=="default"):
            playerslistT2 = default[t2].to_list()
        try:
            gt1p = 0
            gt2p = 0
            if(grnd in list(ground_basis['Ground'])):
                gt1p = float(ground_basis.loc[ground_basis['Ground']==grnd, [t1]].to_string()[-6::])/100
                gt2p = float(ground_basis.loc[ground_basis['Ground']==grnd, [t2]].to_string()[-6::])/100

            teamp1 = 0
            teamp2 = 0
            for i in range(11):
                p1 = float(players.loc[players['Name']==playerslistT1[i], ['Normal_Scores']].to_string()[-6::1])
                p2 = float(players.loc[players['Name']==playerslistT2[i], ['Normal_Scores']].to_string()[-6::1])   
                if(p1>p2):
                    teamp1+=(p1-p2)
                else:
                    teamp2+=(p2-p1)
            # if(teamp1>teamp2):
            #     print("t1 has ", (teamp1)/(teamp1+teamp2), "probability to win")
            # else:
            #     print("t2 has ", (teamp2)/(teamp1+teamp2), "probability to win")

            # if(gt1p>gt2p):
            #     print("t1 has ", gt1p/(gt1p+gt2p), "probability to win acc to grnd")
            #     print("t2 has ", gt2p/(gt1p+gt2p), "probability to win acc to grnd")

            t1wt2 = float(versus.loc[versus['against']==t2, [t1]].to_string()[-6::])/100
            t2wt1 = float(versus.loc[versus['against']==t1, [t2]].to_string()[-6::])/100
            # if(t1wt2>t2wt1):
            #     print(t1, "has", t1wt2, "chances to win against", t2)
            # else:
            #     print(t2, "has", t2wt1, "chances to win against", t1)

    # weightage[0, 1, 2]  = [players, ground, past]
            constx = weightage[0]
            consty = weightage[1]
            constz = weightage[2] 
            wint1 = (((teamp1)/(teamp1+teamp2))*constx+gt1p*consty+t1wt2*constz)*1.02 #(1.2 is  no. representing the probability 0.51 times the batting team winning the game)
            wint2 = (((teamp2)/(teamp1+teamp2))*constx+gt2p*consty+t2wt1*constz)*0.98

            if(wint1>wint2):
                result = "{} has {:.2f}% chances of winning the game".format(t1,(wint1*100)/(wint1+wint2))
                return result, t1
            else:
                result = "{} has {:.2f}% chances of winning the game".format(t2,(wint2*100)/(wint1+wint2))
                return result, t2
        except:
            return "Error", "Occured"
        # winTeam = main_formula()



