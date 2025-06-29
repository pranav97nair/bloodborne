# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:57:20 2024

@author: prana
"""

from Weapon import Weapon
from Character import Character

class ARCalculator():
    def __init__(self, weapon: Weapon, character: Character):
        self.__weapon = weapon
        self.__character = character
        self.__attr_sat = self.__init_attr_sat()
        self.__init_stats()
        
        # self.__weapon.displayStats()
        # self.__character.displayStats()
        
        return
        
    
    def __init_attr_sat(self):
        attr_sat = {}
        with open('data/attr_saturation.txt', 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                level, sat_value = line.strip().split(',', 1)
                attr_sat[int(level)] = float(sat_value)
                
        return attr_sat
    
    def calcAR(self):
        # Physical
        base_phys = self.__weapon.base_phys_dmg
        if base_phys > 0:
            self.__scaled_phys = self.__scaleDamage(base_phys, 'phys')
        
        # Blood
        base_bld = self.__weapon.base_bld_dmg
        if base_bld > 0:
            self.__scaled_bld = self.__scaleDamage(base_bld, 'bld')
        
        # Arcane
        base_arc = self.__weapon.base_arc_dmg
        if base_arc > 0:
            self.__scaled_arc = self.__scaleDamage(base_arc, 'arc')
            
        # Fire
        base_fire = self.__weapon.base_fire_dmg
        if base_fire > 0:
            self.__scaled_fire = self.__scaleDamage(base_fire, 'arc')
        
        # Bolt
        base_bolt = self.__weapon.base_bolt_dmg
        if base_bolt > 0:
            self.__scaled_bolt = self.__scaleDamage(base_bolt, 'arc')
        
        total_dmg = round(self.__scaled_phys + self.__scaled_bld + self.__scaled_arc + 
                          self.__scaled_fire + self.__scaled_bolt)
        
        print(f"Attack Rating: {total_dmg}")
        
        
        
        return
    
    def __scaleDamage(self, base_dmg: int, dmg_type: str):
        # We start with the base damage number
        dmg_output = base_dmg

        if dmg_type.__eq__('phys'):
            # Physical damage scales with both strength and skill
            str_bonus = base_dmg * self.__str_scale * self.__str_satur
            skl_bonus = base_dmg * self.__skl_scale * self.__skl_satur
            dmg_output += str_bonus + skl_bonus
            
        elif dmg_type.__eq__('bld'):
            # Blood damage scales only with bloodtinge
            bld_bonus = base_dmg * self.__blt_scale * self.__blt_satur
            dmg_output += bld_bonus
            
        elif dmg_type.__eq__('arc'):
            # Arcane, fire and bolt damage scales only with arcane
            arc_bonus = base_dmg * self.__arc_scale * self.__arc_satur
            dmg_output += arc_bonus
            
        return dmg_output
    
    def __init_stats(self):
        str_stat = self.__character.strength
        skl_stat = self.__character.skill
        blt_stat = self.__character.bloodtinge
        arc_stat = self.__character.arcane
        
        self.__str_satur = self.__attr_sat[str_stat]
        self.__skl_satur = self.__attr_sat[skl_stat]
        self.__blt_satur = self.__attr_sat[blt_stat]
        self.__arc_satur = self.__attr_sat[arc_stat]
        
        self.__str_scale = self.__weapon.str_scaling
        self.__skl_scale = self.__weapon.skl_scaling
        self.__blt_scale = self.__weapon.blt_scaling
        self.__arc_scale = self.__weapon.arc_scaling
        
        self.__scaled_phys = 0
        self.__scaled_bld = 0
        self.__scaled_arc = 0
        self.__scaled_fire = 0
        self.__scaled_bolt = 0
        
        return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
