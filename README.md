---

# CriCat: Cricket Match Win Predictor Web Application

CriCat is a sophisticated cricket match win predictor designed to forecast the outcomes of international cricket matches. Leveraging extensive data, advanced statistical tools, and key statistical concepts, the application calculates the team with the highest probability of winning the game. By considering factors such as team names, player lineups, toss results, and match locations, CriCat provides a reliable estimate for match results.

## Technologies Used
- Python
- HTML
- CSS
- Flask library
- Pandas library
- SciPy library
- NumPy library
- Microsoft Excel

## Project Structure
The project directory includes several folders with descriptive names:
- **masterdatafiles:** Contains datasets created by our team for estimation and prediction.
- **operations on data:** Houses Python and text files utilized for dataset creation, original data cleaning, and manipulation.
- **static, templates:** Contain frontend files with web code for the application.

The main Python file, **masterWinCal.py**, handles data manipulation and calculations in the final stages, producing the game result.

## Running the Application
To run the CriCat application:

1. Open the **gui_integrate.py** file and run it using your preferred code editor (VS Code is recommended).
2. Upon running the program, the terminal will display a link to a local webpage, which is our web app.
3. Fill in all the required values on the webpage.
4. Click the "Predict" button to obtain the predicted outcome.
5. To close the site, use 'Ctrl + C' in the terminal, terminating the program.

## About CriCat
CriCat is more than just a cricket match win predictor; it's a tool tailored to individual preferences. Whether you prioritize team records or player performance, CriCat adapts to your criteria, offering flexibility, reliability, and ease of use.

## How It Works
CriCat utilizes Python and specialized libraries for data extraction and calculations. With data spanning hundreds of international players and thousands of matches since 2010, the application creates datasets incorporating various factors like stadium effects, player stats, team vs. team performance, and toss outcomes. Statistical and descriptive analyses form the core of the calculations, ensuring accurate predictions. The user provides inputs on the web interface, and CriCat's backend delivers the most probable outcome, enhanced by appealing designs and graphics.

## Usage Instructions
Using CriCat is a straightforward process. Follow these steps to get your desired output:

1. Select the match format (Test, T20i, or ODI).
2. Choose the batting team.
3. Select the fielding team.
4. Enter the playing 11 for both teams.
5. Specify the match stadium.
6. Set weightages for factors influencing the match outcome:
   - Players' weightage (out of 1)
   - Ground weightage (out of 1)
   - Past (or record) weightage (out of 1)
   *Ensure the sum of the three factors does not exceed 1.
7. Click the "Predict" button to view the result.

---

Enjoy using CriCat, where predictions meet precision in the world of cricket!

---
