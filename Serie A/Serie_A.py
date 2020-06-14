#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

'''
This Module is written to analyse the Data Set for the
past 10 season in the Italian Football League Serie A

'''

# Import modules, data wrangling and preparations


import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots as ms
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
    s.drop(labels=s.columns[22::], axis=1, inplace=True)
    s['Total Red Cards'] = s['HR'] + s['AR']
    s['Total Yellow Cards'] = s['HY'] + s['AY']
    s['Total Fouls'] = s['HF'] + s['AF']
    s['Total Shots'] = s['HS'] + s['AS']
    s['Total Shots on Target'] = s['HST'] + s['AST']
    s['Total Goals'] = s['FTHG'] + s['FTAG']
    s.dropna(how='all', inplace=True)
    return s

season_09_10 = aggregate_stats(season_09_10)
season_10_11 = aggregate_stats(season_10_11)
season_11_12 = aggregate_stats(season_11_12)
season_12_13 = aggregate_stats(season_12_13)
season_13_14 = aggregate_stats(season_13_14)
season_14_15 = aggregate_stats(season_14_15)
season_15_16 = aggregate_stats(season_15_16)
season_16_17 = aggregate_stats(season_16_17)
season_17_18 = aggregate_stats(season_17_18)
season_18_19 = aggregate_stats(season_18_19)



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
fig_top_home = go.Figure(data=go.Bar(x=x['Team'].head(5),y=x['Home Wins']),layout_title_text=
                        'Top 5 Teams for home wins')
fig_top_away = go.Figure(data=go.Bar(x=x['Team'].head(5),y=x['Away win']),layout_title_text=
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


# In[ ]:


# More Categorization


# In[35]:


decade.head(1)


# In[5]:


away = pd.DataFrame(data=decade[['AwayTeam', 'FTAG', 'AS', 'AST', 'AF', 'AY', 'AR']])
home = pd.DataFrame(data=decade[['HomeTeam', 'FTHG', 'HS', 'HST', 'HF', 'HY', 'HR']])
away_defensive = pd.DataFrame(data=decade[['AwayTeam', 'FTHG', 'HS', 'HST']])
home_defensive = pd.DataFrame(data=decade[['HomeTeam', 'FTAG', 'AS', 'AST']])
away_fair_play = pd.DataFrame(data=decade[['AwayTeam', 'AF', 'AY', 'AR']])
home_fair_play = pd.DataFrame(data=decade[['HomeTeam', 'HF', 'HY', 'HR']])


# In[ ]:





# In[2]:


# Stats for the top 5 teams


# In[6]:


top_5_stats = {'Juventus F.C Turin':{
    
                          'Total Goals':away[away['AwayTeam']=='Juventus']['FTAG'].sum() + home[home['HomeTeam']=='Juventus']['FTHG'].sum(),
                          'Total Shots':away[away['AwayTeam']=='Juventus']['AS'].sum() + home[home['HomeTeam']=='Juventus']['HS'].sum(),
                          'Total Shots on Target':away[away['AwayTeam']=='Juventus']['AST'].sum() + home[home['HomeTeam']=='Juventus']['HST'].sum()
                          },
               'F.C Internazionale':{
    
                          'Total Goals':away[away['AwayTeam']=='Inter']['FTAG'].sum() + home[home['HomeTeam']=='Inter']['FTHG'].sum(),
                          'Total Shots':away[away['AwayTeam']=='Inter']['AS'].sum() + home[home['HomeTeam']=='Inter']['HS'].sum(),
                          'Total Shots on Target':away[away['AwayTeam']=='Inter']['AST'].sum() + home[home['HomeTeam']=='Inter']['HST'].sum()
                          },
                'A.S Roma':{
    
                          'Total Goals':away[away['AwayTeam']=='Roma']['FTAG'].sum() + home[home['HomeTeam']=='Roma']['FTHG'].sum(),
                          'Total Shots':away[away['AwayTeam']=='Roma']['AS'].sum() + home[home['HomeTeam']=='Roma']['HS'].sum(),
                          'Total Shots on Target':away[away['AwayTeam']=='Roma']['AST'].sum() + home[home['HomeTeam']=='Roma']['HST'].sum()
                          },
                 
               'A.C Milan':{
    
                          'Total Goals':away[away['AwayTeam']=='Milan']['FTAG'].sum() + home[home['HomeTeam']=='Milan']['FTHG'].sum(),
                          'Total Shots':away[away['AwayTeam']=='Milan']['AS'].sum() + home[home['HomeTeam']=='Milan']['HS'].sum(),
                          'Total Shots on Target':away[away['AwayTeam']=='Milan']['AST'].sum() + home[home['HomeTeam']=='Milan']['HST'].sum()
                          },
                'S.S.C. Napoli':{
    
                          'Total Goals':away[away['AwayTeam']=='Napoli']['FTAG'].sum() + home[home['HomeTeam']=='Napoli']['FTHG'].sum(),
                          'Total Shots':away[away['AwayTeam']=='Napoli']['AS'].sum() + home[home['HomeTeam']=='Napoli']['HS'].sum(),
                          'Total Shots on Target':away[away['AwayTeam']=='Napoli']['AST'].sum() + home[home['HomeTeam']=='Napoli']['HST'].sum()
                          }
              
              
              
              }

top_5_stats_defensive = {'Juventus F.C Turin':{
    
                          'Conceded Goals':away_defensive[away_defensive['AwayTeam']=='Juventus']['FTHG'].sum() + home_defensive[home_defensive['HomeTeam']=='Juventus']['FTAG'].sum(),
                          'Total Shots':away_defensive[away_defensive['AwayTeam']=='Juventus']['HS'].sum() + home_defensive[home_defensive['HomeTeam']=='Juventus']['AS'].sum(),
                          'Total Shots on Target':away_defensive[away_defensive['AwayTeam']=='Juventus']['HST'].sum() + home_defensive[home_defensive['HomeTeam']=='Juventus']['AST'].sum()
                          },
               'F.C Internazionale':{
    
                          'Conceded Goals':away_defensive[away_defensive['AwayTeam']=='Inter']['FTHG'].sum() + home_defensive[home_defensive['HomeTeam']=='Inter']['FTAG'].sum(),
                          'Total Shots':away_defensive[away_defensive['AwayTeam']=='Inter']['HS'].sum() + home_defensive[home_defensive['HomeTeam']=='Inter']['AS'].sum(),
                          'Total Shots on Target':away_defensive[away_defensive['AwayTeam']=='Inter']['HST'].sum() + home_defensive[home_defensive['HomeTeam']=='Inter']['AST'].sum()
                          },
                'A.S Roma':{
    
                          'Conceded Goals':away_defensive[away_defensive['AwayTeam']=='Roma']['FTHG'].sum() + home_defensive[home_defensive['HomeTeam']=='Roma']['FTAG'].sum(),
                          'Total Shots':away_defensive[away_defensive['AwayTeam']=='Roma']['HS'].sum() + home_defensive[home_defensive['HomeTeam']=='Roma']['AS'].sum(),
                          'Total Shots on Target':away_defensive[away_defensive['AwayTeam']=='Roma']['HST'].sum() + home_defensive[home_defensive['HomeTeam']=='Roma']['AST'].sum()
                          },
                 
               'A.C Milan':{
    
                          'Conceded Goals':away_defensive[away_defensive['AwayTeam']=='Milan']['FTHG'].sum() + home_defensive[home_defensive['HomeTeam']=='Milan']['FTAG'].sum(),
                          'Total Shots':away_defensive[away_defensive['AwayTeam']=='Milan']['HS'].sum() + home_defensive[home_defensive['HomeTeam']=='Milan']['AS'].sum(),
                          'Total Shots on Target':away_defensive[away_defensive['AwayTeam']=='Milan']['HST'].sum() + home_defensive[home_defensive['HomeTeam']=='Milan']['AST'].sum()
                          },
                'S.S.C. Napoli':{
    
                          'Conceded Goals':away_defensive[away_defensive['AwayTeam']=='Napoli']['FTHG'].sum() + home_defensive[home_defensive['HomeTeam']=='Napoli']['FTAG'].sum(),
                          'Total Shots':away_defensive[away_defensive['AwayTeam']=='Napoli']['HS'].sum() + home_defensive[home_defensive['HomeTeam']=='Napoli']['AS'].sum(),
                          'Total Shots on Target':away_defensive[away_defensive['AwayTeam']=='Napoli']['HST'].sum() + home_defensive[home_defensive['HomeTeam']=='Napoli']['AST'].sum()
                          }
              
              
              
              }

top_5_stats_fair_play = {'Juventus F.C Turin':{
    
                          'Fouls Committed':away_fair_play[away_fair_play['AwayTeam']=='Juventus']['AF'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Juventus']['HF'].sum(),
                          'Yellow Cards':away_fair_play[away_fair_play['AwayTeam']=='Juventus']['AY'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Juventus']['HY'].sum(),
                          'Red Cards':away_fair_play[away_fair_play['AwayTeam']=='Juventus']['AR'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Juventus']['HR'].sum()
                          },
               'F.C Internazionale':{
    
                          'Fouls Committed':away_fair_play[away_fair_play['AwayTeam']=='Inter']['AF'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Inter']['HF'].sum(),
                          'Yellow Cards':away_fair_play[away_fair_play['AwayTeam']=='Inter']['AY'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Inter']['HY'].sum(),
                          'Red Cards':away_fair_play[away_fair_play['AwayTeam']=='Inter']['AR'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Inter']['HR'].sum()
                          },
                'A.S Roma':{
    
                          'Fouls Committed':away_fair_play[away_fair_play['AwayTeam']=='Roma']['AF'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Roma']['HF'].sum(),
                          'Yellow Cards':away_fair_play[away_fair_play['AwayTeam']=='Roma']['AY'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Roma']['HY'].sum(),
                          'Red Cards':away_fair_play[away_fair_play['AwayTeam']=='Roma']['AR'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Roma']['HR'].sum()
                          },
                 
               'A.C Milan':{
    
                          'Fouls Committed':away_fair_play[away_fair_play['AwayTeam']=='Milan']['AF'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Milan']['HF'].sum(),
                          'Yellow Cards':away_fair_play[away_fair_play['AwayTeam']=='Milan']['AY'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Milan']['HY'].sum(),
                          'Red Cards':away_fair_play[away_fair_play['AwayTeam']=='Milan']['AR'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Milan']['HR'].sum()
                          },
                'S.S.C. Napoli':{
    
                          'Fouls Committed':away_fair_play[away_fair_play['AwayTeam']=='Napoli']['AF'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Napoli']['HF'].sum(),
                          'Yellow Cards':away_fair_play[away_fair_play['AwayTeam']=='Napoli']['AY'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Napoli']['HY'].sum(),
                          'Red Cards':away_fair_play[away_fair_play['AwayTeam']=='Napoli']['AR'].sum() + home_fair_play[home_fair_play['HomeTeam']=='Napoli']['HR'].sum()
                          }
              
              
              
              }


top_5_stats_fair_play = pd.DataFrame(top_5_stats_fair_play).T




top_5_stats_defensive = pd.DataFrame(top_5_stats_defensive).T

top_5_stats = pd.DataFrame(top_5_stats).T


# In[7]:


fig_top_5_stats = ms(rows=1, cols=1)
fig_top_5_stats.add_trace((go.Bar(y=top_5_stats.loc['Juventus F.C Turin'], x=['Goals', 'Shots', 'On Target'],
	                              name='Juventus')), row=1, col=1)
fig_top_5_stats.add_trace((go.Bar(y=top_5_stats.loc['F.C Internazionale'], x=['Goals', 'Shots', 'On Target'], 
	                              name='F.C Internazionale')), row=1, col=1)
fig_top_5_stats.add_trace((go.Bar(y=top_5_stats.loc['A.S Roma'], x=['Goals', 'Shots', 'On Target'],
	                              name='A.S Roma')), row=1, col=1)
fig_top_5_stats.add_trace((go.Bar(y=top_5_stats.loc['A.C Milan'], x=['Goals', 'Shots', 'On Target'],
	                              name='A.C Milan')), row=1, col=1)
fig_top_5_stats.add_trace((go.Bar(y=top_5_stats.loc['S.S.C. Napoli'], x=['Goals', 'Shots', 'On Target'],
	                              name='S.S.C. Napoli')), row=1, col=1)

fig_top_5_stats.update_layout(title_text="Top 5 Teams offensive stats")


# In[8]:


fig_top_5_stats_defensive = ms(rows=1, cols=1)
fig_top_5_stats_defensive.add_trace((go.Bar(y=top_5_stats_defensive.loc['Juventus F.C Turin'],
	                                    x=['Goals conceded', 'Shots', 'On Target'],
	                                    name='Juventus')), row=1, col=1)
fig_top_5_stats_defensive.add_trace((go.Bar(y=top_5_stats_defensive.loc['F.C Internazionale'],
	                                    x=['Goals conceded', 'Shots', 'On Target'],
	                                    name='F.C Internazionale')), row=1, col=1)
fig_top_5_stats_defensive.add_trace((go.Bar(y=top_5_stats_defensive.loc['A.S Roma'],
	                                    x=['Goals conceded', 'Shots', 'On Target'],
	                                    name='A.S Roma')), row=1, col=1)
fig_top_5_stats_defensive.add_trace((go.Bar(y=top_5_stats_defensive.loc['A.C Milan'],
	                                    x=['Goals conceded', 'Shots', 'On Target'],
	                                    name='A.C Milan')), row=1, col=1)
fig_top_5_stats_defensive.add_trace((go.Bar(y=top_5_stats_defensive.loc['S.S.C. Napoli'],
                                        x=['Goals conceded', 'Shots', 'On Target'],
                                        name='S.S.C. Napoli')), row=1, col=1)

fig_top_5_stats_defensive.update_layout(title_text="Top 5 Teams defensive stats")

fig_top_5_stats_defensive

#Total Goals comparison

f = ms(rows=1, cols=1)
f.add_bar(y=(top_5_stats.loc['Juventus F.C Turin']['Total Goals'],),
          x=('Goals Scored',), name='Juventus F.C', row=1, col=1)
f.add_bar(y=(top_5_stats.loc['F.C Internazionale']['Total Goals'],),
          x=('Goals Scored',), name='Internazionale', row=1, col=1)
f.add_bar(y=(top_5_stats.loc['S.S.C. Napoli']['Total Goals'],),
          x=('Goals Scored',), name='Napoli', row=1, col=1)
f.add_bar(y=(top_5_stats.loc['A.C Milan']['Total Goals'],),
          x=('Goals Scored',), name='A.C Milan', row=1, col=1)
f.add_bar(y=(top_5_stats.loc['A.S Roma']['Total Goals'],),
          x=('Goals Scored',), name='A.S Roma', row=1, col=1)

# top 5 teams total goals represented by a Piechart


pie = go.Figure(data=go.Pie(values=top_5_stats['Total Goals'].values,
	                        labels=top_5_stats['Total Goals'].index))
pie.update_layout(title_text='Top 5 teams goals since 2009-2010')

# Total goals for all teams participated in the Serie A from 2009-2010 till 2018-2019

grand_total_goals = {}

for x in home['HomeTeam'].unique():
    if (home.HomeTeam == x).any():
        grand_total_goals.update({x:(home[home['HomeTeam'] == x]['FTHG'].sum() +
                                     away[away['AwayTeam'] == x]['FTAG'].sum())})
grand_total_goals = pd.DataFrame(data=grand_total_goals, index=range(1)).T


grand_total_goals.columns = ['Total Goals',]
grand_total_goals.sort_values(by='Total Goals', ascending=False, inplace=True)

grand_total_goals_chart = go.Figure(data=go.Pie(values=grand_total_goals['Total Goals'],
	                                        labels=grand_total_goals.index), layout=
                                        {'title':{'text':'Total goals scored per team since 2009-2010'
                                    }})

grand_total_goals_chart


# In[181]:


grand_total_goals_bar = ms(rows=1, cols=1)
grand_total_goals_bar.add_bar(y=grand_total_goals['Total Goals'], x=grand_total_goals.index)
