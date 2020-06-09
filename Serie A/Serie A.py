#!/usr/bin/env python
# coding: utf-8

'''
This Module is written to analyse the Data Set for the
past 10 season in the Italian Football League Serie A

'''

# Import modules, data wrangling and preparations


import pandas as pd
import plotly.graph_objects as go
season_09_10 = pd.read_csv('./italian-serie-a_zip/season-0910_csv.csv', parse_dates=['Date'],
                           dtype={'HomeTeam':'category',
                                  'AwayTeam':'category',
                                  'Div':'category'})


season_10_11 = pd.read_csv('./italian-serie-a_zip/season-1011_csv.csv', parse_dates=['Date'],
                           dtype={'HomeTeam':'category',
                                  'AwayTeam':'category',
                                  'Div':'category'})

season_11_12 = pd.read_csv('./italian-serie-a_zip/season-1112_csv.csv', parse_dates=['Date'],
                           dtype={'HomeTeam':'category',
                                  'AwayTeam':'category',
                                  'Div':'category'})

season_12_13 = pd.read_csv('./italian-serie-a_zip/season-1213_csv.csv', parse_dates=['Date'],
                           dtype={'HomeTeam':'category',
                                  'AwayTeam':'category',
                                  'Div':'category'})

season_13_14 = pd.read_csv('./italian-serie-a_zip/season-1314_csv.csv', parse_dates=['Date'],
                           dtype={'HomeTeam':'category',
                                  'AwayTeam':'category',
                                  'Div':'category'})

season_14_15 = pd.read_csv('./italian-serie-a_zip/season-1415_csv.csv', parse_dates=['Date'],
                           dtype={'HomeTeam':'category',
                                  'AwayTeam':'category',
                                  'Div':'category'})

season_15_16 = pd.read_csv('./italian-serie-a_zip/season-1516_csv.csv', parse_dates=['Date'],
                           dtype={'HomeTeam':'category',
                                  'AwayTeam':'category',
                                  'Div':'category'})

season_16_17 = pd.read_csv('./italian-serie-a_zip/season-1617_csv.csv', parse_dates=['Date'],
                           dtype={'HomeTeam':'category',
                                  'AwayTeam':'category',
                                  'Div':'category'})

season_17_18 = pd.read_csv('./italian-serie-a_zip/season-1718_csv.csv', parse_dates=['Date'],
                           dtype={'HomeTeam':'category',
                                  'AwayTeam':'category',
                                  'Div':'category'})

season_18_19 = pd.read_csv('./italian-serie-a_zip/season-1819_csv.csv', parse_dates=['Date'],
                           dtype={'HomeTeam':'category',
                                  'AwayTeam':'category',
                                  'Div':'category'})


# In[3]:


def aggregate_stats(s):
    '''
    This function yo wrangle the data, then it will be
    mapped to each Data Set
    '''
    s.drop(columns=s[22::], inplace=True)
    s['Total Red Cards'] = s['HR'] + s['AR']
    s['Total Yellow Cards'] = s['HY'] + s['AY']
    s['Total Fouls'] = s['HF'] + s['AF']
    s['Total Shots'] = s['HS'] + s['AS']
    s['Total Shots on Target'] = s['HST'] + s['AST']
    s['Total Goals'] = s['FTHG'] + s['FTAG']
    s.dropna(how='all', inplace=True)
    return s

season_09_10 = season_09_10.apply(aggregate_stats, axis='columns')
season_10_11 = season_10_11.apply(aggregate_stats, axis='columns')
season_11_12 = season_11_12.apply(aggregate_stats, axis='columns')
season_12_13 = season_12_13.apply(aggregate_stats, axis='columns')
season_13_14 = season_13_14.apply(aggregate_stats, axis='columns')
season_14_15 = season_14_15.apply(aggregate_stats, axis='columns')
season_15_16 = season_15_16.apply(aggregate_stats, axis='columns')
season_16_17 = season_16_17.apply(aggregate_stats, axis='columns')
season_17_18 = season_17_18.apply(aggregate_stats, axis='columns')
season_18_19 = season_18_19.apply(aggregate_stats, axis='columns')



# Concatenate all datasets into one.

decade = pd.concat([season_09_10, season_10_11, season_11_12, season_12_13, season_13_14,
                    season_14_15, season_15_16, season_16_17, season_17_18, season_18_19],
                   keys=['Season 09-10', 'Season 10-11', 'Season 11-12', 'Season 12-13',
                         'Season 13-14', 'Season 14-15', 'Season 15-16', 'Season 16-17',
                         'Season 17-18', 'Season 18-19'])
decade = decade.sort_values(by='HomeTeam')


# Various statistical analysis


# Home Wins per team
# FTR stands for Final Time Record and "H" means that the home team won


condition2 = decade['FTR'] == 'H'
x = decade[condition2]['HomeTeam'].value_counts()
x = x.to_frame()
x.reset_index(inplace=True)
x.columns = ['Team', 'Home Wins']
fig_home_wins = go.Figure(data=go.Bar(x=x['Team'], y=x['Home Wins']),
                          layout_title_text="Home Wins per team since 2009-2010")


# Home Win percentage

total_home = decade['HomeTeam'].value_counts()
x['Total Home Games'] = total_home.values


x['Home win Percentage'] = (x['Home Wins'].values/total_home.values)*100


# Away win Percentage

away_win = decade[decade['FTR'] == 'A']['AwayTeam'].value_counts()

away_win.sort_values(ascending=False, inplace=True)

x['Away win'] = away_win.values


fig_away_wins = go.Figure(data=go.Bar(x=x['Team'], y=x['Away win']), layout_title_text=
                          'Away Wins per team since 2009-2010')


total_goals = decade['Total Goals'].sum()
total_yellows = decade['Total Yellow Cards'].sum()
total_reds = decade['Total Red Cards'].sum()
total_fouls = decade['Total Fouls'].sum()
total_shots = decade['Total Shots'].sum()
total_shots_on_target = decade['Total Shots on Target'].sum()
total_stats = {'Total Goals':total_goals, 'Total Yellow Cards': total_yellows,
               'Total Reds': total_reds,
               'Total Fouls': total_fouls, 'Total Shots': total_shots,
               'Total Shots on Target': total_shots_on_target}
total_stats = pd.Series(total_stats)

# Total per season


total_per_season = {
    'Season 09-10':{'Total Goals':season_09_10['Total Goals'].sum(),
                    'Total Yellow Cards': season_09_10['Total Yellow Cards'].sum(),
                    'Total Reds': season_09_10['Total Red Cards'].sum(),
                    'Total Fouls': season_09_10['Total Fouls'].sum(),
                    'Total Shots': season_09_10['Total Shots'].sum(),
                    'Total Shots on Target': season_09_10['Total Shots on Target'].sum(),
                    'Total Red Cards' : season_09_10['Total Red Cards'].sum()},
    'Season 10-11':{'Total Goals':season_10_11['Total Goals'].sum(),
                    'Total Yellow Cards': season_10_11['Total Yellow Cards'].sum(),
                    'Total Reds': season_10_11['Total Red Cards'].sum(),
                    'Total Fouls': season_10_11['Total Fouls'].sum(),
                    'Total Shots': season_10_11['Total Shots'].sum(),
                    'Total Shots on Target': season_10_11['Total Shots on Target'].sum(),
                    'Total Red Cards' : season_10_11['Total Red Cards'].sum()},
    'Season 11-12':{'Total Goals':season_11_12['Total Goals'].sum(),
                    'Total Yellow Cards': season_11_12['Total Yellow Cards'].sum(),
                    'Total Reds': season_11_12['Total Red Cards'].sum(),
                    'Total Fouls': season_11_12['Total Fouls'].sum(),
                    'Total Shots': season_11_12['Total Shots'].sum(),
                    'Total Shots on Target': season_11_12['Total Shots on Target'].sum(),
                    'Total Red Cards' : season_11_12['Total Red Cards'].sum()},
    'Season 12-13':{'Total Goals':season_12_13['Total Goals'].sum(),
                    'Total Yellow Cards': season_12_13['Total Yellow Cards'].sum(),
                    'Total Reds': season_12_13['Total Red Cards'].sum(),
                    'Total Fouls': season_12_13['Total Fouls'].sum(),
                    'Total Shots': season_12_13['Total Shots'].sum(),
                    'Total Shots on Target': season_12_13['Total Shots on Target'].sum(),
                    'Total Red Cards' : season_12_13['Total Red Cards'].sum()},
    'Season 13-14':{'Total Goals':season_13_14['Total Goals'].sum(),
                    'Total Yellow Cards': season_13_14['Total Yellow Cards'].sum(),
                    'Total Reds': season_13_14['Total Red Cards'].sum(),
                    'Total Fouls': season_13_14['Total Fouls'].sum(),
                    'Total Shots': season_13_14['Total Shots'].sum(),
                    'Total Shots on Target': season_13_14['Total Shots on Target'].sum(),
                    'Total Red Cards' : season_13_14['Total Red Cards'].sum()},
    'Season 14-15':{'Total Goals':season_14_15['Total Goals'].sum(),
                    'Total Yellow Cards': season_14_15['Total Yellow Cards'].sum(),
                    'Total Reds': season_14_15['Total Red Cards'].sum(),
                    'Total Fouls': season_14_15['Total Fouls'].sum(),
                    'Total Shots': season_14_15['Total Shots'].sum(),
                    'Total Shots on Target': season_14_15['Total Shots on Target'].sum(),
                    'Total Red Cards' : season_14_15['Total Red Cards'].sum()},
    'Season 15-16':{'Total Goals':season_15_16['Total Goals'].sum(),
                    'Total Yellow Cards': season_15_16['Total Yellow Cards'].sum(),
                    'Total Reds': season_15_16['Total Red Cards'].sum(),
                    'Total Fouls': season_15_16['Total Fouls'].sum(),
                    'Total Shots': season_15_16['Total Shots'].sum(),
                    'Total Shots on Target': season_15_16['Total Shots on Target'].sum(),
                    'Total Red Cards' : season_15_16['Total Red Cards'].sum()},
    'Season 16-17':{'Total Goals':season_16_17['Total Goals'].sum(),
                    'Total Yellow Cards': season_16_17['Total Yellow Cards'].sum(),
                    'Total Reds': season_16_17['Total Red Cards'].sum(),
                    'Total Fouls': season_16_17['Total Fouls'].sum(),
                    'Total Shots': season_16_17['Total Shots'].sum(),
                    'Total Shots on Target': season_16_17['Total Shots on Target'].sum(),
                    'Total Red Cards' : season_16_17['Total Red Cards'].sum()},
    'Season 17-18':{'Total Goals':season_17_18['Total Goals'].sum(),
                    'Total Yellow Cards': season_17_18['Total Yellow Cards'].sum(),
                    'Total Reds': season_17_18['Total Red Cards'].sum(),
                    'Total Fouls': season_17_18['Total Fouls'].sum(),
                    'Total Shots': season_17_18['Total Shots'].sum(),
                    'Total Shots on Target': season_17_18['Total Shots on Target'].sum(),
                    'Total Red Cards' : season_17_18['Total Red Cards'].sum()},
    'Season 18-19':{'Total Goals':season_18_19['Total Goals'].sum(),
                    'Total Yellow Cards': season_18_19['Total Yellow Cards'].sum(),
                    'Total Reds': season_18_19['Total Red Cards'].sum(),
                    'Total Fouls': season_18_19['Total Fouls'].sum(),
                    'Total Shots': season_18_19['Total Shots'].sum(),
                    'Total Shots on Target': season_18_19['Total Shots on Target'].sum(),
                    'Total Red Cards' : season_18_19['Total Red Cards'].sum()}
    }
total_per_season = pd.DataFrame(total_per_season).T
total_per_season.columns = ['Total Goals', 'Total Yellow Cards', 'Total Reds', 'Total Fouls',
                            'Total Shots', 'Total Shots on Target', 'Total Red Cards']


# Graphs for different stats

fig_yellow = go.Figure(data=go.Bar(y=total_per_season['Total Yellow Cards'], x=total_per_season.index),
                       layout_title_text="Total Yellow Cards per season since 2009-2010")



fig_goals = go.Figure(data=go.Bar(y=total_per_season['Total Goals'], x=total_per_season.index),
                      layout_title_text="Total Goals per season since 2009-2010")


fig_red = go.Figure(data=go.Bar(y=total_per_season['Total Red Cards'], x=total_per_season.index),
                    layout_title_text="Total Red Cards per season since 2009-2010")



fig_fouls = go.Figure(data=go.Bar(y=total_per_season['Total Fouls'], x=total_per_season.index),
                      layout_title_text="Total Fouls per season since 2009-2010")
# TOP 5 collection
fig_top_home = go.Figure(data=go.Bar(x=x['Team'].head(5), y=x['Home Wins']), layout_title_text=
                         'Top 5 Teams for home wins')
fig_top_away = go.Figure(data=go.Bar(x=x['Team'].head(5), y=x['Away win']), layout_title_text=
                         'Top 5 Teams for away wins')
#writing graphs to images, can be found under the Graph subfolder in the Github
fig_yellow.write_image(r'./Graphs\Yellow_Cards.png')
fig_goals.write_image(r'./Graphs\Goals.png')
fig_red.write_image(r'./Graphs\Red_Cards.png')
fig_fouls.write_image(r'./Graphs\Fouls.png')
fig_home_wins.write_image(r'./Graphs\Home_Wins.png')
fig_away_wins.write_image(r'./Graphs\Away_Wins.png')
fig_top_home.write_image(r'./Graphs/Top_5_Home.png')
fig_top_away.write_image(r'./Graphs/Top_5_Away.png')
