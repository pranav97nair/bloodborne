# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:42:46 2024

@author: prana
"""

class Character:
    def __init__(self, vit: int, end: int, strn: int, skl: int, blt: int, arc: int):
        self.__vit = vit
        self.__end = end
        self.__strn = strn
        self.__skl = skl
        self.__blt = blt
        self.__arc = arc
        
    def displayStats(self):
        print("Character Stats\n")
        print(f"Vitality: {self.__vit}")
        print(f"Endurance: {self.__end}")
        print(f"Strength: {self.__strn}")
        print(f"Skill: {self.__skl}")
        print(f"Bloodtinge: {self.__blt}")
        print(f"Arcane: {self.__arc}\n")
        
    # Define individual stat getters
    @property
    def vitality(self) -> int:
        return self.__vit
    
    @property
    def endurance(self) -> int:
        return self.__end
    
    @property
    def strength(self) -> int:
        return self.__strn
    
    @property
    def skill(self) -> int:
        return self.__skl
    
    @property
    def bloodtinge(self) -> int:
        return self.__blt
    
    @property
    def arcane(self) -> int:
        return self.__arc