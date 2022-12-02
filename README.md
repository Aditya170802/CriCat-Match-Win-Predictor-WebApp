# CriCat-Match-Win-Predictor-WebApp
This is a cricket match win predictor, uses tons of data, major statistical tools, and concepts of statistics to predict which team would have the highest probability of winning the game. Herein, the application would be taking data like team name, player 11, toss result, place of the match, etc. to predict the most probable result for the match.
Tools used: Python, HTML, CSS, Flask lib., Pandas lib., SciPy lib., NumPy lib., MS Excel
Understand the files and run the application:
The folder contains several folders and the folders are named accordingly:
like the 'masterdatafiles' folder contains all the data sets our team created and which we are using
for our estimation or prediction, likewise 'operations on data' folder contains all the python or text files
that we used for creating our datasets, cleaning original data and manipulating them.
The static, templates files are the files containing the web code, the frontend part.
'masterWinCal.py' is the main python file where all the data manipulation, and calculation is happening 
at the last stage, through which we are getting the result of the game.
To run the program:
1. you need to open the 'gui_integrate.py' file and run it (we have used VS Code to create and run these files)
2. Once the program runs, in the terminal you get a link to a local webpage which indeed is our webapp.
3. Fill in all values, and then click the predict button to predict the outcome.
4. to finish or close the site, just enter 'ctrl + C' in the terminalm and the program terminates.


CriCat is a cricket match win predictor application or tool built to predict the results of international cricket matches between two teams. As the outcome, it gives the probability in percentage to represent the chances of the winning team.
This is based on the user’s needs, as for every one of us, the criterion for a team to win a cricket match would be different. Someone might believe the records of a team matter the most when it comes to its winning, but some consider the teams’ players to play the most important role in deciding the result. So, the application is built with these factors in mind, to make it more flexible, reliable, and easier to use.
How does it work?
The application uses Python and its special libraries, to work with all the data extraction, and calculations to provide the desired results. It contains data of hundreds of international (capped) players, and thousands of international matches held till now, since 2010 across all formats. It creates datasets, based on the Effect of Grounds (or stadium) on teams’ games (their records), players’ stats, team vs team stats, tosses effect on the team, etc., and then goes through all these data, to predict with good accuracy. All the required inputs are made from the users’ end on the webpage, and then the backend comes into the picture, providing the most probable outcome. The application mostly uses statistical and descriptive analysis as its major chunk of calculations. The app not only is easy to use, but also fun to see with decent designs and graphics to please the eyes of the users.
How to use it?
To use the application, you just need to fill in all the relevant information the app asks for. Follow the following steps to get your desired output:
1.	Select the format of the match (Test, T20i, or ODI)
2.	Select the batting team
3.	Select the fielding team
4.	Enter the list of playing 11 players of the batting team.
5.	Enter the list of playing 11 players of the fielding team.
6.	Enter the name of the Stadium, where the match is being held.
7.	Enter the weightage (How much you think these factors weigh in teams’ win):
•	Players’ weightage (out of 1)
•	Ground weightage (out of 1)
•	Past (or record) weightage (out of 1)
*Note that the sum of the three factors should not exceed 1
8.	What now? Just hit the Predict button to view the result.

