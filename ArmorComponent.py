# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:29:56 2024

@author: prana
"""
from abc import ABC, abstractproperty

class ArmorComponent(ABC):
    def __init__(self, phys, blunt, thrust, blood, arcane, fire, bolt, 
                slowp, rapidp, frenzy, beast):
        self.phys = phys
        self.blunt = blunt
        self.thrust = thrust
        self.blood = blood
        self.arcane = arcane
        self.fire = fire
        self.bolt = bolt
        self.slowp = slowp
        self.rapidp = rapidp
        self.frenzy = frenzy
        self.beast = beast
    
    @abstractproperty
    def armor_type(self) -> str:
        pass
    
    @abstractproperty
    def physical_def(self) -> int:
        pass
    
    @abstractproperty
    def blunt_def(self) -> int:
        pass
    
    @abstractproperty
    def thrust_def(self) -> int:
        pass
    
    @abstractproperty
    def blood_def(self) -> int:
        pass
    
    @abstractproperty
    def arcane_def(self) -> int:
        pass
    
    @abstractproperty
    def fire_def(self) -> int:
        pass
    
    @abstractproperty
    def bolt_def(self) -> int:
        pass
    
    @abstractproperty
    def slow_poison_res(self) -> int:
        pass
    
    @abstractproperty
    def rapid_poison_res(self) -> int:
        pass
    
    @abstractproperty
    def frenzy_res(self) -> int:
        pass
    
    @abstractproperty
    def beasthood(self) -> int:
        pass
    
    def displayStats(self):
        print(f"Type: {self.armor_type}\n")
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    