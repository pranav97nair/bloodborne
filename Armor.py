# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:02:43 2024

@author: prana
"""

from ArmorComponent import ArmorComponent

class HeadArmor(ArmorComponent):
    def __init__(self, phys, blunt, thrust, blood, arcane, fire, bolt, 
                slowp, rapidp, frenzy, beast):
        super().__init__(phys, blunt, thrust, blood, arcane, fire, bolt, 
                    slowp, rapidp, frenzy, beast)
     
    @property
    def armor_type(self):
        return "Head Armor"
    
    @property
    def physical_def(self):
        return self.phys
    
    @property
    def blunt_def(self):
        return self.blunt
    
    @property
    def thrust_def(self):
        return self.thrust
    
    @property
    def blood_def(self):
        return self.blood
    
    @property
    def arcane_def(self):
        return self.arcane
    
    @property
    def fire_def(self):
        return self.fire
    
    @property
    def bolt_def(self):
        return self.bolt
    
    @property
    def slow_poison_res(self):
        return self.slowp
    
    @property
    def rapid_poison_res(self):
        return self.rapidp
    
    @property
    def frenzy_res(self):
        return self.frenzy
    
    @property
    def beasthood(self):
        return self.beast
    
class ChestArmor(ArmorComponent):
    def __init__(self, phys, blunt, thrust, blood, arcane, fire, bolt, 
                slowp, rapidp, frenzy, beast):
        super().__init__(phys, blunt, thrust, blood, arcane, fire, bolt, 
                    slowp, rapidp, frenzy, beast)
     
    @property
    def armor_type(self):
        return "Chest Armor"
    
    @property
    def physical_def(self):
        return self.phys
    
    @property
    def blunt_def(self):
        return self.blunt
    
    @property
    def thrust_def(self):
        return self.thrust
    
    @property
    def blood_def(self):
        return self.blood
    
    @property
    def arcane_def(self):
        return self.arcane
    
    @property
    def fire_def(self):
        return self.fire
    
    @property
    def bolt_def(self):
        return self.bolt
    
    @property
    def slow_poison_res(self):
        return self.slowp
    
    @property
    def rapid_poison_res(self):
        return self.rapidp
    
    @property
    def frenzy_res(self):
        return self.frenzy
    
    @property
    def beasthood(self):
        return self.beast
    
class HandArmor(ArmorComponent):
    def __init__(self, phys, blunt, thrust, blood, arcane, fire, bolt, 
                slowp, rapidp, frenzy, beast):
        super().__init__(phys, blunt, thrust, blood, arcane, fire, bolt, 
                    slowp, rapidp, frenzy, beast)
     
    @property
    def armor_type(self):
        return "Hand Armor"
    
    @property
    def physical_def(self):
        return self.phys
    
    @property
    def blunt_def(self):
        return self.blunt
    
    @property
    def thrust_def(self):
        return self.thrust
    
    @property
    def blood_def(self):
        return self.blood
    
    @property
    def arcane_def(self):
        return self.arcane
    
    @property
    def fire_def(self):
        return self.fire
    
    @property
    def bolt_def(self):
        return self.bolt
    
    @property
    def slow_poison_res(self):
        return self.slowp
    
    @property
    def rapid_poison_res(self):
        return self.rapidp
    
    @property
    def frenzy_res(self):
        return self.frenzy
    
    @property
    def beasthood(self):
        return self.beast
    
class LegArmor(ArmorComponent):
    def __init__(self, phys, blunt, thrust, blood, arcane, fire, bolt, 
                slowp, rapidp, frenzy, beast):
        super().__init__(phys, blunt, thrust, blood, arcane, fire, bolt, 
                    slowp, rapidp, frenzy, beast)
     
    @property
    def armor_type(self):
        return "Leg Armor"
    
    @property
    def physical_def(self):
        return self.phys
    
    @property
    def blunt_def(self):
        return self.blunt
    
    @property
    def thrust_def(self):
        return self.thrust
    
    @property
    def blood_def(self):
        return self.blood
    
    @property
    def arcane_def(self):
        return self.arcane
    
    @property
    def fire_def(self):
        return self.fire
    
    @property
    def bolt_def(self):
        return self.bolt
    
    @property
    def slow_poison_res(self):
        return self.slowp
    
    @property
    def rapid_poison_res(self):
        return self.rapidp
    
    @property
    def frenzy_res(self):
        return self.frenzy
    
    @property
    def beasthood(self):
        return self.beast
    
