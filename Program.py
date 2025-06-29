# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:31:45 2024

@author: prana
"""

from Armor import HeadArmor, ChestArmor, HandArmor, LegArmor
from ArmorSet import ArmorSet
from SpiderPlotter import DRPlotter, ResPlotter
from ReadFiles import ReadArmorSets


def main():    
    # Read armor set stats from file
    armor_sets = ReadArmorSets()
    
    # Tomb Prospector set
    tombprosp_set = armor_sets['tombprosp_set']
    # Hunter set
    hunter_set = armor_sets['hunter_set']
    # Gascoigne set
    gascoigne_set = armor_sets['gascoigne_set']
    # Black Church set
    bl_church_set = armor_sets['bl_church_set']
    # White Church set
    wh_church_set = armor_sets['wh_church_set']
    # Crowfeather set
    crowfeather_set = armor_sets['crowfeather_set']
    # Henyk set
    henryk_set = armor_sets['henryk_set']
    # Yharnam Hunter set
    yh_hunter_set = armor_sets['yh_hunter_set']
    # Ashen Hunter set
    ashen_set = armor_sets['ashen_set']
    
    # Charred Hunter set with hunter hat
    ch_hunter_set = armor_sets['ch_hunter_set']
    hunter_hat = hunter_set.headArmor()
    ch_hunter_set.updateHead(hunter_hat)
    
    # Custom set 1    
    ch_hunter_garb = ch_hunter_set.chestArmor()
    gascoigne_gloves = gascoigne_set.handArmor()
    bl_church_trousers = bl_church_set.legArmor()    
    custom_set1 = ArmorSet(hunter_hat, ch_hunter_garb, gascoigne_gloves,
                           bl_church_trousers, "Custom Set 1")
    # Custom set 2
    tombprosp_garb = tombprosp_set.chestArmor()
    custom_set2 = ArmorSet(hunter_hat, tombprosp_garb, gascoigne_gloves,
                           bl_church_trousers, "Custom Set 2")
    # Custom set 3
    tombprosp_gloves = tombprosp_set.handArmor()
    custom_set3 = ArmorSet(hunter_hat, ch_hunter_garb, tombprosp_gloves,
                           bl_church_trousers, "Custom Set 3")
    # Custom set 4
    yh_hunter_garb = yh_hunter_set.chestArmor()
    custom_set4 = ArmorSet(hunter_hat, yh_hunter_garb, gascoigne_gloves,
                           bl_church_trousers, "Custom Set 4")
    
    # Display stats
    ashen_set.displayStats()
    
    # Plot armor stats
    spider = DRPlotter()
    # spider.plot_single(tombprosp_set)
    # spider.plot_single(yahargul_set)
    spider.plot_double(ashen_set, custom_set4)
    
    spider2 = ResPlotter()
    # spider2.plot_single(tombprosp_set)
    spider2.plot_double(ashen_set, custom_set4)
    
if __name__ == "__main__":
    main()