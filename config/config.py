# -*- coding: utf-8 -*-

import os, sys, time,urllib.request

rarity = ['Mythic Rare', 'Rare', 'Uncommon', 'Common', 'Land']

language = ['en', 'tw']

star_city_set_number = {'isd' : 5215, 'dka' : 5221, 'avr' : 5228, 'm13': 5241, 'rtr' : 5243, 'gtc' : 5249}

card_set = ['isd', 'dka', 'avr', 'm13', 'rtr', 'gtc', 'dgm', 'm14', 'ths']

flip = {
    'isd' : [   8,  38,  47,  51,  64,  90, 114, 145, 149, 152, 159, 165, 168, 176, 181, 182, 185, 193, 208, 209],
    'dka' : [  13,  50,  55,  71,  81,  94,  98, 122, 125, 133, 140, 146, 147],
    'dgm' : [ 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]
}

card_num = {
    'isd' : {'Mythic Rare' : 17, 'Rare' : 65, 'Uncommon' : 74, 'Common' : 113, 'Land' : 15, 'Token' : 12},
    'dka' : {'Mythic Rare' : 14, 'Rare' : 41, 'Uncommon' : 48, 'Common' :  68, 'Land' :  0, 'Token' :  3},
    'avr' : {'Mythic Rare' : 15, 'Rare' : 53, 'Uncommon' : 60, 'Common' : 101, 'Land' : 15, 'Token' :  8},
    'm13' : {'Mythic Rare' : 15, 'Rare' : 53, 'Uncommon' : 60, 'Common' : 101, 'Land' : 20, 'Token' : 11},
    'rtr' : {'Mythic Rare' : 15, 'Rare' : 53, 'Uncommon' : 80, 'Common' : 101, 'Land' : 25, 'Token' : 12},
    'gtc' : {'Mythic Rare' : 15, 'Rare' : 53, 'Uncommon' : 80, 'Common' : 101, 'Land' :  0, 'Token' : 12} 

}

total_num = {
    'isd' : 264,
    'dka' : 158,
    'avr' : 244,
    'm13' : 249,
    'rtr' : 274,
    'gtc' : 249,
    'dgm' : 156,
    'm14' : 249,
    'ths' : 249
}

tcg_set_string = {
    'isd' : 'innistrad',
    'dka' : 'dark-ascension',
    'avr' : 'avacyn-restored',
    'm13' : 'Magic-2013-(M13)',
    'rtr' : 'return-to-ravnica',
    'gtc' : 'gatecrash'
    
}

date_string = time.strftime("%Y_%m_%d")

def get_table(set):
    f = open('../common/card_name_table/%s.txt'%set, 'r')
    table = []
    for line in f:
        table.append(line.strip('\n'))
        
    return table