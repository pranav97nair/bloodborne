# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:13:42 2024

@author: prana
"""

import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np
from ArmorSet import ArmorSet

class DRPlotter:
    def __init__(self):
        images = ['images/physical_DEF.jpg','images/VS_blunt.jpg','images/VS_thrust.jpg','images/blood_DEF.jpg','images/arcane_DEF.jpg','images/fire_DEF.jpg','images/bolt_DEF.jpg']
        self.loaded_images = [image.imread(file) for file in images]
    
    def plot_single(self, armor_set: ArmorSet):
        # Initialize armor stats
        r = self.get_armor_stats(armor_set)
        
        # Initialize angular positions
        theta = np.linspace(0.0, 2 * np.pi, len(r))
        
        # Plot data
        plt.style.use('dark_background')
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.set_title("Damage Reduction", pad=10)
        ax.plot(theta, r, color='blue', label=armor_set.getName())
        ax.fill(theta, r, color='blue', alpha=0.4)
        ax.grid(alpha=0.5)
        
        rmax = 300 if max(r) < 300 else 350
        ax.set_rticks([100, 200, rmax])
        
        self.setup_theta_ticks(ax, r)
        self.setup_img_labels(ax)
        self.setup_legend(ax)
        
        plt.show()
        
    def plot_double(self, armor_set1: ArmorSet, armor_set2: ArmorSet):
        # Initialize armor set stats
        r1 = self.get_armor_stats(armor_set1)        
        r2 = self.get_armor_stats(armor_set2)
    
        # Initialize angular poistions
        theta = np.linspace(0.0, 2 * np.pi, len(r1))

        # Plot data
        plt.style.use('dark_background')
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})        
        ax.set_title("Damage Reduction", pad=10)
        ax.plot(theta, r1, color='blue', label=armor_set1.getName())
        ax.fill(theta, r1, color='blue', alpha=0.6)
        ax.plot(theta, r2, color='red', label=armor_set2.getName())
        ax.fill(theta, r2, color='red', alpha=0.4)
        ax.grid(alpha=0.5)
        
        rmax = 300 if max(max(r1),max(r2)) < 300 else 350
        ax.set_rticks([100, 200, rmax])

        self.setup_theta_ticks(ax, r1)
        self.setup_img_labels(ax)
        self.setup_legend(ax)
        
        plt.show()

    # Extract damage reduction stats from armor set
    def get_armor_stats(self, armor_set: ArmorSet):
        r = []
        r.append(armor_set.physical_def())
        r.append(armor_set.blunt_def())
        r.append(armor_set.thrust_def())
        r.append(armor_set.blood_def())
        r.append(armor_set.arcane_def())
        r.append(armor_set.fire_def())
        r.append(armor_set.bolt_def())
        # append slow poison def again at the end to neatly self-connect the spider plot
        r.append(armor_set.physical_def())
        return r

    # Configure labels for each stat using symbol images loaded by constructor
    def setup_img_labels(self, ax):
        # physical
        img = self.loaded_images[0]
        img_imgbox = ax.inset_axes([1.03, 0.45, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        # blunt
        img = self.loaded_images[1]
        img_imgbox = ax.inset_axes([0.82, 0.91, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        # thrust
        img = self.loaded_images[2]
        img_imgbox = ax.inset_axes([0.32, 1.01, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        # blood
        img = self.loaded_images[3]
        img_imgbox = ax.inset_axes([-0.08, 0.7, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        # arcane
        img = self.loaded_images[4]
        img_imgbox = ax.inset_axes([-0.08, 0.2, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        # fire
        img = self.loaded_images[5]
        img_imgbox = ax.inset_axes([0.32, -0.11, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        # bolt
        img = self.loaded_images[6]
        img_imgbox = ax.inset_axes([0.82, -0.01, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        
    # Configure angular ticks and labels
    def setup_theta_ticks(self, ax, r):
        theta_ticks = np.linspace(0.0, 2 * np.pi, len(r)-1, endpoint=False)
        ax.set_xticks(theta_ticks)
        ax.set_xticklabels([''] * len(theta_ticks)) # remove default labels

    # Configure legend
    def setup_legend(self, ax):
        angle = np.deg2rad(240)
        ax.legend(loc="lower left",
                  bbox_to_anchor=(0.1 + np.cos(angle)/2, 0.1 + np.sin(angle)/2))


class ResPlotter():
    def __init__(self):
        images = ['images/beasthood.jpg','images/slow_poison_RES.jpg','images/frenzy_RES.jpg','images/rapid_poison_RES.jpg']
        self.loaded_images = [image.imread(file) for file in images]
    
    def plot_single(self, armor_set: ArmorSet):
        # Initialize armor stats
        r = self.get_armor_stats(armor_set)
        
        # Initialize angular positions
        theta = [np.pi/2, 9*np.pi/8, 3*np.pi/2, 15*np.pi/8, np.pi/2]

        # Plot data
        plt.style.use('dark_background')
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.set_title("Beasthood and Resistances", pad=10)
        ax.plot(theta, r, color='blue', label=armor_set.getName())
        ax.fill(theta, r, color='blue', alpha=0.4)
        ax.grid(alpha=0.5)
        ax.set_rticks([50, 100, 150])
        
        self.setup_theta_ticks(ax, r)
        self.setup_img_labels(ax)
        self.setup_legend(ax)
        
        plt.show()
        
    def plot_double(self, armor_set1: ArmorSet, armor_set2: ArmorSet):
        # Initialize armor stats
        r1 = self.get_armor_stats(armor_set1)        
        r2 = self.get_armor_stats(armor_set2)
        
        # Initialize angular positions
        theta = [np.pi/2, 9*np.pi/8, 3*np.pi/2, 15*np.pi/8, np.pi/2]

        # Plot data
        plt.style.use('dark_background')
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.set_title("Beasthood and Resistances", pad=10)
        ax.plot(theta, r1, color='blue', label=armor_set1.getName())
        ax.fill(theta, r1, color='blue', alpha=0.6)
        ax.plot(theta, r2, color='red', label=armor_set2.getName())
        ax.fill(theta, r2, color='red', alpha=0.4)
        ax.grid(alpha=0.5)
        ax.set_rticks([50, 100, 150])
        
        self.setup_theta_ticks(ax, r1)
        self.setup_img_labels(ax)
        self.setup_legend(ax)
        
        plt.show()
    
    # Extract resistance and beasthood stats from armor set
    def get_armor_stats(self, armor_set: ArmorSet):
        r = []
        r.append(armor_set.beasthood())
        r.append(armor_set.slow_poison_def())
        r.append(armor_set.frenzy_def())
        r.append(armor_set.rapid_poison_def())       
        # append beasthood again at the end to neatly self-connect the spider plot
        r.append(armor_set.beasthood())
        return r
    
    # Configure labels for each stat using symbol images loaded by constructor
    def setup_img_labels(self, ax):
        # physical
        img = self.loaded_images[0]
        img_imgbox = ax.inset_axes([0.45, 1.02, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        # blunt
        img = self.loaded_images[1]
        img_imgbox = ax.inset_axes([-0.1, 0.24, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        # thrust
        img = self.loaded_images[2]
        img_imgbox = ax.inset_axes([0.45, -0.12, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        # blood
        img = self.loaded_images[3]
        img_imgbox = ax.inset_axes([1.0, 0.24, 0.1, 0.1])
        img_imgbox.imshow(img)
        img_imgbox.axis('off')
        
    # Configure angular ticks and labels
    def setup_theta_ticks(self, ax, r):
        theta_ticks = [np.pi/2, 9*np.pi/8, 3*np.pi/2, 15*np.pi/8]
        ax.set_xticks(theta_ticks)
        ax.set_xticklabels([''] * len(theta_ticks))
        
    # Configure legend
    def setup_legend(self, ax):
        angle = np.deg2rad(240)
        ax.legend(loc="lower left",
                  bbox_to_anchor=(0.1 + np.cos(angle)/2, 0.1 + np.sin(angle)/2))    
        
        
        
        
        
        
        
        
        
        
        
