# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:04:44 2024

@author: prana
"""

from abc import ABC, abstractproperty, abstractmethod
import pandas as pd

class Weapon(ABC):    
    @abstractproperty
    def base_phys_dmg(self) -> int:
        pass
    
    @abstractproperty
    def base_bld_dmg(self) -> int:
        pass
    
    @abstractproperty
    def base_arc_dmg(self) -> int:
        pass
    
    @abstractproperty
    def base_fire_dmg(self) -> int:
        pass
    
    @abstractproperty
    def base_bolt_dmg(self) -> int:
        pass
    
    @abstractproperty
    def upgrade_level(self) -> int:
        pass
    
    @abstractproperty
    def str_scaling(self) -> float:
        pass
    
    @abstractproperty
    def skl_scaling(self) -> float:
        pass
    
    @abstractproperty
    def blt_scaling(self) -> float:
        pass
    
    @abstractproperty
    def arc_scaling(self) -> float:
        pass
    
    @abstractmethod
    def displayStats():
        pass
    

class LudwigHolyBlade(Weapon):
    def __init__(self, level: int):
        self.__dmg_dict = {}
        for i in range(11):
            self.__dmg_dict[i] = [100 + 10*i, 0, 0, 0, 0]
        
        self.__scale_dict = {}
        with open('data/ludwig_hb_scaling.txt', 'r') as file:
            for i in range(11):
                line = file.readline()
                index, str_scl, skl_scl, blt_scl, arc_scl = line.strip().split(',')
                self.__scale_dict[i] = [str_scl, skl_scl, blt_scl, arc_scl]
                
        self.__level = level
        dmg_row = self.__dmg_dict[level]
        self.__phys = dmg_row[0]
        self.__bld = dmg_row[1]  
        self.__arc = dmg_row[2]
        self.__fire = dmg_row[3]   
        self.__bolt = dmg_row[4]
        
        scl_row = self.__scale_dict[level]
        self.__str_scale = float(scl_row[0])
        self.__skl_scale = float(scl_row[1])
        self.__blt_scale = float(scl_row[2])
        self.__arc_scale = float(scl_row[3])      
    
    @property
    def base_phys_dmg(self) -> int:
        return self.__phys
    
    @property
    def base_bld_dmg(self) -> int:
        return self.__bld
    
    @property
    def base_arc_dmg(self) -> int:
        return self.__arc
    
    @property
    def base_fire_dmg(self) -> int:
        return self.__fire
    
    @property
    def base_bolt_dmg(self) -> int:
        return self.__bolt
    
    @property
    def upgrade_level(self) -> int:
        return self.__level
    
    @property
    def str_scaling(self) -> float:
        return self.__str_scale
    
    @property
    def skl_scaling(self) -> float:
        return self.__skl_scale
    
    @property
    def blt_scaling(self) -> float:
        return self.__blt_scale
    
    @property
    def arc_scaling(self) -> float:
        return self.__arc_scale
            
    def getScalingGrade(self, value: float) -> str:
        if value == 0.0:
            return '-'
        elif value < 0.55:
            return 'D'
        elif value < 0.65:
            return 'C'
        elif value < 0.85:
            return 'B'
        elif value < 1.10:
            return 'A'
        else:
            return 'S'
    
    def displayStats(self):
        print("Weapon: Ludwig's Holy Blade")
        print(f"Level: +{self.__level}\n")
        str_scale_grade = self.getScalingGrade(self.__str_scale)
        skl_scale_grade = self.getScalingGrade(self.__skl_scale)
        blt_scale_grade = self.getScalingGrade(self.__blt_scale)
        arc_scale_grade = self.getScalingGrade(self.__arc_scale)
        print("Scaling")
        print(f"Strength: {str_scale_grade}\t\tSkill: {skl_scale_grade}\tBloodtinge: {blt_scale_grade}\tArcane: {arc_scale_grade}")
        print()
        print("Base Damage")
        print(f"Physical: {self.__phys}")
        print(f"Blood: {self.__bld}")
        print(f"Arcane: {self.__arc}")
        print(f"Fire: {self.__fire}")
        print(f"Bolt: {self.__bolt}\n")
        
    










    
