# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:18:57 2024

@author: prana
"""

from Weapon import LudwigHolyBlade
from Character import Character
from ARCalculator import ARCalculator

def main():
    ludwig10 = LudwigHolyBlade(10)
    # ludwig10.displayStats()
    
    mymain = Character(31, 25, 23, 25, 13, 25)
    # goodboy.displayStats()
    
    ar1 = ARCalculator(ludwig10, mymain)
    ar1.calcAR()
    

if __name__ == "__main__":
    main()
        