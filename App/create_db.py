import pandas as pd




def create_db():
    df = pd.read_csv('Data/data.csv')
    
    df = df.drop(columns={'Unnamed: 0'}, axis=1)
    df = df.drop(columns={'TeamPoints','OpponentPoints','Game','FieldGoals',
                      'FieldGoals.','X3PointShots','X3PointShots.','FreeThrows',
                      'Opp.FieldGoals','Opp.FieldGoals.','Opp.3PointShots',
                      'Opp.3PointShots.','Opp.FreeThrows'}, axis=1,)

    df.rename(columns={'WINorLOSS':'WINNER'}, inplace=True)
    df['WINNER'] = df['WINNER'] == 'W'
    df['Home'] = df['Home'] =='Home'

    east = ['TOR','IND','CHO','NYK','MIA','CLE','DET',
        'WAS','BOS','BRK','PHI','ORL','CHI','MIL','ATL']
    df['EastOpponent'] = df['Opponent'].isin(east)

    west = ['SAS','UTA','LAL','NOP','DEN','HOU','DAL',
        'LAC','POR','MEM','OKC','MIN','GSW','SAC','PHO']
    df['WestOpponent'] = df['Opponent'].isin(west)

    df['DefRebound'] = df['TotalRebounds'] - df['OffRebounds']
    df['Opp.DefRebound'] = df['Opp.TotalRebounds'] - df['Opp.OffRebounds']
    df['X2PointShotAttempted'] = df['FieldGoalsAttempted'] - df['X3PointShotsAttempted']
    df['Opp.2PointShotAttempted'] = df['Opp.FieldGoalsAttempted'] - df['Opp.3PointShotsAttempted']
    df['HighFreeThrow%'] = df['FreeThrows.'] > .800
    df['Opp.HighFreeThrow%'] = df['Opp.FreeThrows.'] >.800
    df['HighRebounds'] = df['TotalRebounds'] >= 60
    df['OppHighRebounds'] = df['Opp.TotalRebounds'] >=60
    df['AssistsTurnoverRatio'] = df['Assists'] / df['Turnovers']
    df['GameChangers'] = df['Steals'] + df['Blocks']
    df['Opp.AssistsTurnoverRatio'] = df['Opp.Assists'] / df['Opp.Turnovers']
    df['HighFoul%'] = df['TotalFouls'] >= 30
    df['Opp.HighFoul%'] = df['Opp.TotalFouls'] >= 30
    df['Opp.GameChangers'] = df['Opp.Steals'] + df['Opp.Blocks']

    print(df.head())

    
if __name__ == '__main__':
    create_db()