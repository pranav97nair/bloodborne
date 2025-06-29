# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:28:12 2024

@author: prana
"""

from Armor import HeadArmor, ChestArmor, HandArmor, LegArmor

class ArmorSet():
    def __init__(self, hat: HeadArmor, garb: ChestArmor, gloves: HandArmor, 
                 trousers: LegArmor, name: str):
        self.hat = hat
        self.garb = garb
        self.gloves = gloves
        self.trousers = trousers
        self.name = name
        
        self.phys = self.calcPhys()
        self.blunt = self.calcBlunt()
        self.thrust = self.calcThrust()
        self.blood = self.calcBlood()
        self.arcane = self.calcArcane()
        self.fire = self.calcFire()
        self.bolt = self.calcBolt()
        self.slowp = self.calcSlowP()
        self.rapidp = self.calcRapidP()
        self.frenzy = self.calcFrenzy()
        self.beast = self.calcBeast()
        
    
    def getName(self):
        return self.name
    
    def calcPhys(self):
        return (self.hat.physical_def + self.garb.physical_def + self.gloves.physical_def
                + self.trousers.physical_def)
    
    def calcBlunt(self):
        return (self.hat.blunt_def + self.garb.blunt_def + self.gloves.blunt_def
                + self.trousers.blunt_def)
    
    def calcThrust(self):
        return (self.hat.thrust_def + self.garb.thrust_def + self.gloves.thrust_def
                + self.trousers.thrust_def)
    
    def calcBlood(self):
        return (self.hat.blood_def + self.garb.blood_def + self.gloves.blood_def
                + self.trousers.blood_def)
    
    def calcArcane(self):
        return (self.hat.arcane_def + self.garb.arcane_def + self.gloves.arcane_def
                + self.trousers.arcane_def)
    
    def calcFire(self):
        return (self.hat.fire_def + self.garb.fire_def + self.gloves.fire_def
                + self.trousers.fire_def)
    
    def calcBolt(self):
        return (self.hat.bolt_def + self.garb.bolt_def + self.gloves.bolt_def
                + self.trousers.bolt_def)
    
    def calcSlowP(self):
        return (self.hat.slow_poison_res + self.garb.slow_poison_res + self.gloves.slow_poison_res
                + self.trousers.slow_poison_res)
    
    def calcRapidP(self):
        return (self.hat.rapid_poison_res + self.garb.rapid_poison_res + self.gloves.rapid_poison_res
                + self.trousers.rapid_poison_res)
    
    def calcFrenzy(self):
        return (self.hat.frenzy_res + self.garb.frenzy_res + self.gloves.frenzy_res
                + self.trousers.frenzy_res)
    
    def calcBeast(self):
        return (self.hat.beasthood + self.garb.beasthood + self.gloves.beasthood
                + self.trousers.beasthood)
    
    def displayStats(self):
        print(f"Name: {self.name}\n")
        print("Defenses")
        print(f"Physical: {self.phys}")        
        print(f"Blunt: {self.blunt}")       
        print(f"Thurst: {self.thrust}")       
        print(f"Blood: {self.blood}")       
        print(f"Arcane: {self.arcane}")       
        print(f"Fire: {self.fire}")       
        print(f"Bolt: {self.bolt}\n")
        print("Resistances")
        print(f"Slow Poison: {self.slowp}")
        print(f"Rapid Poison: {self.rapidp}")
        print(f"Frenzy: {self.frenzy}\n")
        print(f"Beasthood: {self.beast}\n")
        
    #define stat getters
    def physical_def(self):
        return self.phys
    
    def blunt_def(self):
        return self.blunt
    
    def thrust_def(self):
        return self.thrust
    
    def blood_def(self):
        return self.blood
    
    def arcane_def(self):
        return self.arcane
    
    def fire_def(self):
        return self.fire
    
    def bolt_def(self):
        return self.bolt
    
    def slow_poison_def(self):
        return self.slowp
    
    def rapid_poison_def(self):
        return self.rapidp
    
    def frenzy_def(self):
        return self.frenzy
    
    def beasthood(self):
        return self.beast
    
    #define component getters
    def headArmor(self):
        return self.hat
    
    def chestArmor(self):
        return self.garb
    
    def handArmor(self):
        return self.gloves
    
    def legArmor(self):
        return self.trousers
    
    #define component setters
    def updateHead(self, hat: HeadArmor):
        self.hat = hat
        self.recalcAll()
        
    def updateChest(self, garb: ChestArmor):
        self.garb = garb
        self.recalcAll()
        
    def updateHand(self, gloves: HandArmor):
        self.gloves = gloves
        self.recalcAll()
        
    def updateLeg(self, trousers: LegArmor):
        self.trousers = trousers
        self.recalcAll()
    
    # function to recalculate all stats
    def recalcAll(self):
        self.phys = self.calcPhys()
        self.blunt = self.calcBlunt()
        self.thrust = self.calcThrust()
        self.blood = self.calcBlood()
        self.arcane = self.calcArcane()
        self.fire = self.calcFire()
        self.bolt = self.calcBolt()
        self.slowp = self.calcSlowP()
        self.rapidp = self.calcRapidP()
        self.frenzy = self.calcFrenzy()
        self.beast = self.calcBeast()
    
    
    
    
    
    
    
    
    
    
    
    
    
    