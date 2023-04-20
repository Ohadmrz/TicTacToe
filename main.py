import sys
sys.path.append("./OH_AD_HD")
import to_prac.py


my_citie = {
   2008:{'Germany':['Berlin', 'Munich'],
           'France' :['Paris','Leon','Bordeaux']},
   2009: {'China':['Hong Kong', 'Shanghai','Beijing'],
            'Japan':['Nagoya','Toyokawa','Yatomi'],
            'Mexico':['Tijuana','Ecatepec']},
   2010: {'Germany': ['Berlin', 'Dusseldorf'],
            'France': ['Paris', 'Nice', 'Bordeaux'],
            'Japan':['Tokyo','Toyokawa','Yatomi']}}

result = keif(my_citie)
print(result)