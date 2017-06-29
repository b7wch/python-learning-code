# -*- coding:utf-8 -*- 
# 2017/3/31

import random

Wa_Zhi = ['WZ'] * 100
Xie_Zi = ['XZ'] * 200
Tuo_Xie = ['TX'] * 300
Xiang_Lian = ['XL'] * 400

All_Before = Wa_Zhi + Xie_Zi + Tuo_Xie + Xiang_Lian
All_After = random.sample(All_Before, 100)  