# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:19:24 2024

@author: prana
"""
from Armor import HeadArmor, ChestArmor, HandArmor, LegArmor
from ArmorSet import ArmorSet
import pandas as pd

def ReadArmorSets():
    # Read armor set stats into dataframe without 'totals'
    df = pd.read_csv('data/armor_sets_sheet.csv')
    df = df[df['Set pieces'] != 'Totals']

    armor_sets = {}

    # Read set name for each set(chunk) in dataframe and create an ArmorSet
    with open('data/armor_sets_list.txt', 'r') as file:
        for i in range(0, len(df), 4):
            chunk = df.iloc[i:i + 4] # armor set
            # isolate data for each component of the set
            head = chunk.iloc[0]
            chest = chunk.iloc[1]
            hand = chunk.iloc[2]
            leg = chunk.iloc[3]
            
            # read pre-defined armor set name and set variable name 
            line = file.readline()
            var_name, set_name = line.strip().split(',', 1)
            
            # create an ArmorSet by reading in the data
            hat = HeadArmor(head['Physical'], head['VS Blunt'], head['VS Thrust'], head['Blood'], head['Arcane'], head['Fire'], head['Bolt'], head['S. Poison'], head['R. Poison'], head['Frenzy'], head['Beast'])
            garb = ChestArmor(chest['Physical'], chest['VS Blunt'], chest['VS Thrust'], chest['Blood'], chest['Arcane'], chest['Fire'], chest['Bolt'], chest['S. Poison'], chest['R. Poison'], chest['Frenzy'], chest['Beast'])
            gloves = HandArmor(hand['Physical'], hand['VS Blunt'], hand['VS Thrust'], hand['Blood'], hand['Arcane'], hand['Fire'], hand['Bolt'], hand['S. Poison'], hand['R. Poison'], hand['Frenzy'], hand['Beast'])
            trousers = LegArmor(leg['Physical'], leg['VS Blunt'], leg['VS Thrust'], leg['Blood'], leg['Arcane'], leg['Fire'], leg['Bolt'], leg['S. Poison'], leg['R. Poison'], leg['Frenzy'], leg['Beast'])
            armor = ArmorSet(hat, garb, gloves, trousers, set_name)
            armor_sets[var_name] = armor
    
    return armor_sets

