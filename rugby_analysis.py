#Here we are importing modules to the program, pandas is used for data analysis and numpy is used for working with arrays
import pandas as pd
import numpy as np

DATA_PATH = "C:\\Users\\jolly\\PycharmProjects\\VexCodingProject\\data_rugby_u13b\\QE_U13B_Rugby.xlsx"

#This is getting the data from the excel sheet of the rugby scores for the U13B QE rugby team
def get_data_from_excel():
    stats_df = pd.read_excel(DATA_PATH, sheet_name= "SummaryStats")
    sort_by_max_points = stats_df.sort_values('points difference',
                                         ascending=False)
    
    #Finding which schools have beaten QE
    print (sort_by_max_points)
    value = \
    sort_by_max_points[sort_by_max_points['School'] == 'Queen Elizabeth boys School']['points difference'].values[0]
    df2 = sort_by_max_points.loc[sort_by_max_points['points difference'] >= value]
    return(df2)

#Extracting the scores from each game
def calculate_qe_win_rate():
    win_df = pd.read_excel(DATA_PATH, sheet_name="QE")
    win_df[['res', 'score']] = win_df['Result'].str.split('\n', expand=True)

    win_df[['score1', 'score2']] = win_df['score'].str.split('-', expand=True)
    win_df[["score1", "score2"]] = win_df[["score1", "score2"]].apply(pd.to_numeric)

#Calculating the percentage difference in each game played
    win_df['percent_result'] = (win_df['score1'] / win_df['score2']) * 100
    win_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    win_df.dropna(subset=["percent_result"], how="all", inplace=True)
    win_df['percent_result'] = win_df['percent_result'].astype(int)
    
#Making the teams go in order from hardest to easiest so it is easier to understand
    win_df = win_df.sort_values('percent_result', ascending=True)
    
#Arranging each team a difficulty level based on the percentage won by
    classify_opp = ['challenging', 'moderate', 'easy']
   
    conditions = [
        (win_df['percent_result'] < 100 ),
        (win_df['percent_result'] < 200),
        (win_df['percent_result'] >= 200)
    ]
    
#Saving the result as an excel sheet so it is easier to understand
    win_df['win_type'] = np.select(conditions, classify_opp, default = '')
    win_df.drop(win_df.columns.difference(['Opponent', 'percent_result', 'win_type']), 1, inplace=True)
    print(win_df)
    win_df.to_excel("data_rugby_u13b\\U13B_Rugby_stats.xlsx")



if __name__ == "__main__":
    calculate_qe_win_rate()
