# import of required packages

import pandas as pd
import numpy as np
from copy import deepcopy
import io, os.path
from lxml import etree as et
import csv

# define a function that creates a dictionary for loaded tables

def dict_fun(root):
    root_attrib = root.attrib
    for tab in root:
        tab_dict = deepcopy(root_attrib)
        attrib_dict = {}
        attrib_dict.update(tab.attrib)
        for key, value in attrib_dict.items():
            attrib_dict.update({key:value})
        tab_dict.update(attrib_dict)
        yield tab_dict
        
# load the XML files, convert to pandas data frames using the dict_fun function and save in the form of CSV

for frame in ['Badges','Comments','PostHistory','PostLinks','Posts','Tags','Users','Votes']:
    link = os.path.join(r'.\Travel_stack_exchange',frame)  
    tree = et.parse(link + '.xml')
    root = tree.getroot()
    tab_list = list(dict_fun(root))
    df = pd.DataFrame(tab_list)
    df = df.replace(r'\\n', ' ', regex=True)
    df = df.replace(r'\\r', ' ', regex=True)
    df.to_csv(link + ".csv", sep=';', index=False)
    df = pd.read_csv(link + ".csv", sep=';')
	
# load data frames from CSV files

Badges_df = pd.read_csv(r'.\Travel_stack_exchange\Badges.csv', sep=';')
Comments_df = pd.read_csv(r'.\Travel_stack_exchange\Comments.csv', sep=';')
PostHistory_df = pd.read_csv(r'.\Travel_stack_exchange\PostHistory.csv', sep=';')
PostLinks_df = pd.read_csv(r'.\Travel_stack_exchange\PostLinks.csv', sep=';')
Posts_df = pd.read_csv(r'.\Travel_stack_exchange\Posts.csv', sep=';')
Tags_df = pd.read_csv(r'.\Travel_stack_exchange\Tags.csv', sep=';')
Users_df = pd.read_csv(r'.\Travel_stack_exchange\Users.csv', sep=';')
Votes_df = pd.read_csv(r'.\Travel_stack_exchange\Votes.csv', sep=';')

# displaying dates in the datetime type

Badges_df.Date = pd.to_datetime(Badges_df.Date)
Comments_df.CreationDate = pd.to_datetime(Comments_df.CreationDate)
PostHistory_df.CreationDate = pd.to_datetime(PostHistory_df.CreationDate)
PostLinks_df.CreationDate = pd.to_datetime(PostLinks_df.CreationDate)
Posts_df.ClosedDate = pd.to_datetime(Posts_df.ClosedDate)
Posts_df.CommunityOwnedDate = pd.to_datetime(Posts_df.CommunityOwnedDate)
Posts_df.CreationDate = pd.to_datetime(Posts_df.CreationDate)
Posts_df.LastActivityDate = pd.to_datetime(Posts_df.LastActivityDate)
Posts_df.LastEditDate = pd.to_datetime(Posts_df.LastEditDate)
Users_df.CreationDate = pd.to_datetime(Users_df.CreationDate)
Users_df.LastAccessDate = pd.to_datetime(Users_df.LastAccessDate)
Votes_df.CreationDate = pd.to_datetime(Votes_df.CreationDate)
