#!/usr/bin/env python
# coding: utf-8

'''
This Module is written to analyse the Data Set for the
past 10 season in the Italian Football League Serie A

'''

# Import modules, data wrangling and preparations


import pandas as pd

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
    s.drop(columns=x[22::], inplace=True)
    s['Total Red Cards'] = x['HR'] + x['AR']
    s['Total Yellow Cards'] = x['HY'] + x['AY']
    s['Total Fouls'] = x['HF'] + x['AF']
    s['Total Shots'] = x['HS'] + x['AS']
    s['Total Shots on Target'] = x['HST'] + x['AST']
    s['Total Goals'] = x['FTHG'] + x['FTAG']
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
                    season_14_15, season_15_16, season_16_17, season_17_18, season_18_19])
decade = decade.sort_values(by='HomeTeam')


# Various statistical analysis


# Home Wins per team
# FTR stands for Final Time Record and "H" means that the home team won


condition2 = decade['FTR'] == 'H'
x = decade[condition2]['HomeTeam'].value_counts()
x = x.to_frame()
x.reset_index(inplace=True)
x.columns = ['Team', 'Home Wins']
x.set_index('Team', inplace=True)
x.head(1)
x.head(5)[::-1].plot(y='Home Wins', figsize=(8, 6), kind='barh', title="Top 5 Home win")


# Home Win percentage



total_home = decade['HomeTeam'].value_counts()
x['Total Home Games'] = total_home.values


x['Home win Percentage'] = (x['Home Wins'].values/total_home.values)*100


x.head(5)[::-1].plot(figsize=(8, 6), y='Home win Percentage', title='Top 5 Home win %', kind='barh')

# Away win Percentage

away_win = decade[decade['FTR'] == 'A']['AwayTeam'].value_counts()/decade['AwayTeam'].value_counts()

away_win.sort_values(ascending=False, inplace=True)

x['Away win Percentage'] = away_win.values*100


x.head(5)[::-1].plot(y='Away win Percentage', figsize=(8, 6), kind='barh',
                     title=' Top 5 Away win %')

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

total_per_season['Total Yellow Cards'][::-1].plot(title='Total Yellow Cards per Season',
                                                  y='Total Yellow Cards', figsize=(8, 6),
                                                  kind='barh', color='yellow')


total_per_season['Total Goals'].plot(y='Total Goals', figsize=(8, 6), kind='barh',
                                     title='Total Goals per Season')


total_per_season['Total Red Cards'].plot(y='Total Red Cards', figsize=(8, 6), kind='barh',
                                         title='Total Red Cards per Season', color='red')


total_per_season['Total Fouls'].plot(y='Total Fouls', figsize=(8, 6), kind='barh',
                                     title='Total Fouls per Season', color='blue')
