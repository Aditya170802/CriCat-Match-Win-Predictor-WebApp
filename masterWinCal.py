#this would be the master or the main place of all calculations for the win prediction.
import pandas as pd
import numpy as np

class Calc:
    def calc(format, teambatting, teambowling, ground,playerslistT1,playerslistT2, weightage):
        # reading all the necessary data files on the basis of format of the match
        
        if(format=="T20i"):
            players = pd.read_excel('./masterdatafiles/TestGuiT20.xlsx')
            versus = pd.read_excel("./masterdatafiles/t20_tvt.xlsx")
            ground_basis = pd.read_excel('./masterdatafiles/GroundEffect.xlsx')
        elif(format=="Test"):
            players = pd.read_excel('./masterdatafiles/TestGuiTest.xlsx')
            versus = pd.read_excel("./masterdatafiles/test_tvt.xlsx")
            ground_basis = pd.read_excel('./masterdatafiles/GroundEffectTest.xlsx')   
        elif(format=="odi"):

            players = pd.read_excel('./masterdatafiles/TestGuiodi.xlsx')
            versus = pd.read_excel("./masterdatafiles/odi_tvt.xlsx")
            ground_basis = pd.read_excel('./masterdatafiles/GroundEffectodi.xlsx')
        
        # all the necessary inputs taken from the user
        t1 = teambatting
        t2 = teambowling
        grnd = ground

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

        # winTeam = main_formula()

# y = ["J C Buttler","A D Hales","D J Malan","B A Stokes","H C Brook","M M Ali","S M Curran","A U Rashid","C R Woakes","R J W Topley","M A Wood"]
# x = ["D A Warner","A J Finch","M R Marsh","C Green","M P Stoinis","T H David","M S Wade","A Zampa","P J Cummins","M A Starc","J R Hazlewood"]
# # # # arr = ['t20',  'Pakistan','India', 'Sharjah']
# # # # val = Calc.calc(arr,x,y)
# India = ['R G Sharma','K L Rahul','V Kohli','S A Yadav','H H Pandya','K D Karthik','A R Patel','R Ashwin','B Kumar','Mohammed Shami','J J Bumrah']

# Pakistan = ['Babar Azam','Mohammad Rizwan','Shan Masood','Iftikhar Ahmed','Shadab Khan','Haider Ali','Mohammad Nawaz','Asif Ali','Shaheen Shah Afridi','Naseem Shah','Haris Rauf']


# nz = ['F H Allen','D P Conway','K S Williamson','G D Phillips','J D S Neesham','M J Santner','I S Sodhi','T G Southee','L H Ferguson','T A Boult']

# afg = ['Hazratullah Zazai','Rahmanullah Gurbaz','Usman Ghani','Ibrahim Zadran','Najibullah Zadran','Mohammad Nabi','Azmatullah Omarzai','Rashid Khan','Mujeeb Ur Rahman','Fareed Ahmad','Fazalhaq Farooqi']
# k = Calc.calc("T20i", "Pakistan", "England", "Melbourne", Pakistan, y, [0.2, 0.1, 0.7clear])
# print(str(k))
# k = Calc.calc("T20i", "India", "England", "Melbourne", India, y, [0.0, 0.0, 1])
# print(str(k))
#this would be the master or the main place of all calculations for the win prediction.

# class Calc:
#     def calc(array3,team1,team2):
#         players = pd.read_excel('TestGuiT20.xlsx')
#         ground_basis = pd.read_excel('GroundEffect.xlsx')
#         versus = pd.read_excel("t20_tvt.xlsx")
#         # array3 =['t20', 'India', 'Pakistan', 'Dubai']
#         ground_basis = pd.read_excel('GroundEffect.xlsx')
#         t1 = array3[1]
#         t2 = array3[2]
#         ground = array3[3]

#         gt1p = float(ground_basis.loc[ground_basis['Ground']==ground, [t1]].to_string()[-6::])/100
#         gt2p = float(ground_basis.loc[ground_basis['Ground']==ground, [t2]].to_string()[-6::])/100

#         teamp1 = 0
#         teamp2 = 0
#         for i in range(11):
#             p1 = float(players.loc[players['Name']==team1[i], ['Normal_Scores']].to_string()[-6::1])
#             p2 = float(players.loc[players['Name']==team2[i], ['Normal_Scores']].to_string()[-6::1])   
#             if(p1>p2):
#                 teamp1+=(p1-p2)
#             else:
#                 teamp2+=(p2-p1)
#         # if(teamp1>teamp2):
#         #     print("t1 has ", (teamp1)/(teamp1+teamp2), "probability to win")
#         # else:
#         #     print("t2 has ", (teamp2)/(teamp1+teamp2), "probability to win")

#         # if(gt1p>gt2p):
#         #     print("t1 has ", gt1p/(gt1p+gt2p), "probability to win acc to ground")
#         #     print("t2 has ", gt2p/(gt1p+gt2p), "probability to win acc to ground")

#         t1wt2 = float(versus.loc[versus['against']==t2, [t1]].to_string()[-6::])/100
#         t2wt1 = float(versus.loc[versus['against']==t1, [t2]].to_string()[-6::])/100
#         # if(t1wt2>t2wt1):
#         #     print(t1, "has", t1wt2, "chances to win against", t2)
#         # else:
#         #     print(t2, "has", t2wt1, "chances to win against", t1)


        
#         wint1 = (((teamp1)/(teamp1+teamp2))*0.5+gt1p*0.1+t1wt2*0.4)
#         wint2 = (((teamp2)/(teamp1+teamp2))*0.5+gt2p*0.1+t2wt1*0.4)
#         if(wint1>wint2):
#             result = ["{:.3f}".format(wint1), t1]
#             return result

#         else:
#             result = ["{:.3f}".format(wint2), t2]
#             return result

#         # winTeam = main_formula()

# # y = ["J J Bumrah",
# #         "Y S Chahal",
# #         "D L Chahar",
# #         "S Dhawan",
# #         "R D Gaikwad",
# #         "D J Hooda",
# #         "Ishan Kishan",
# #         "S S Iyer",
# #         "R A Jadeja",
# #         "K D Karthik",
# #         "V Kohli"
# #         ]
# # x = [
# #         "Asif Ali",
# #         "Babar Azam",
# #         "Danish Aziz",
# #         "Faheem Ashraf",
# #         "Fakhar Zaman",
# #         "Fawad Alam",
# #         "Haider Ali",
# #         "Haris Rauf",
# #         "Haris Sohail",
# #         "Hasan Ali",
# #         "Hussain Talat"
# #         ]
# # arr = ['t20',  'Pakistan','India', 'Sharjah']
# # val = Calc.calc(arr,x,y)

# # print(val)


