elements = {'n'  : 0, 
            'H'  : 1, 'He' : 2, 'Li' : 3, 'Be' : 4, 'B'  : 5,
            'C'  : 6, 'N'  : 7, 'O'  : 8, 'F'  : 9, 'Ne' : 10,
            'Na' : 11,'Mg' : 12,'Al' : 13,'Si' : 14,'P'  : 15,
            'S'  : 16,'Cl' : 17,'Ar' : 18,'K'  : 19,'Ca' : 20,
            'Sc' : 21,'Ti' : 22,'V'  : 23,'Cr' : 24,'Mn' : 25,
            'Fe' : 26,'Co' : 27,'Ni' : 28,'Cu' : 29,'Zn' : 30,
            'Ga' : 31,'Ge' : 32,'As' : 33,'Se' : 34,'Br' : 35,
            'Kr' : 36,'Rb' : 37,'Sr' : 38,'Y'  : 39,'Zr' : 40,
            'Nb' : 41,'Mo' : 42,'Tc' : 43,'Ru' : 44,'Rh' : 45,
            'Pd' : 46,'Ag' : 47,'Cd' : 48,'In' : 49,'Sn' : 50,
            'Sb' : 51,'Te' : 52,'I'  : 53,'Xe' : 54,'Cs' : 55,
            'Ba' : 56,'La' : 57,'Ce' : 58,'Pr' : 59,'Nd' : 60,
            'Pm' : 61,'Sm' : 62,'Eu' : 63,'Gd' : 64,'Tb' : 65,
            'Dy' : 66,'Ho' : 67,'Er' : 68,'Tm' : 69,'Yb' : 70,
            'Lu' : 71,'Hf' : 72,'Ta' : 73,'W'  : 74,'Re' : 75,
            'Os' : 76,'Ir' : 77,'Pt' : 78,'Au' : 79,'Hg' : 80,
            'Tl' : 81,'Pb' : 82,'Bi' : 83,'Po' : 84,'At' : 85,
            'Rn' : 86,'Fr' : 87,'Ra' : 88,'Ac' : 89,'Th' : 90,
            'Pa' : 91,'U'  : 92,'Np' : 93,'Pu' : 94,'Am' : 95,
            'Cm' : 96,'Bk' : 97,'Cf' : 98,'Es' : 99,'Fm' :100,
            'Md' :101,'No' :102,'Lr' :103,'Rf' :104,'Db' :105,
            'Sg' :106,'Bh' :107,'Hs' :108,'Mt' :109,'Ds' :110,
            'Rg' :111,'Cn' :112,'Nh' :113,'Fl' :114,'Mc' :115,
            'Lv' :116,'Ts' :117,'Og' :118}

# данные обработанны из данныйх атомных масс с сайта http://cdfe.sinp.msu.ru/services/gsp.en.html   
ele_mass = {'0-n-1'     : 1.0,                  # нейтрон
            '2-a-4'     : 3.7273794066,         # ядро атома гелия (не используется в JENDL)
            '2-He-4'    : 3.968219,             # атом гелия 
            '3-Li-6'    : 5.96344956791536614,  # массы атома в массах нейтронов
            '3-Li-7'    : 6.955732786,
            '4-Be-9'    : 8.934761557,
            '5-B-7'     : 6.969528526,
            '5-B-8'     : 7.955670608,
            '5-B-9'     : 8.935898249,
            '5-B-10'    : 9.926919187,
            '5-B-11'    : 10.91472906,
            '6-C-10'    : 9.930801833,
            '6-C-10-m 3.354 МэВ'    : 9.934371568,
            '6-C-12'    : 11.89691293,
            '6-C-13'    : 12.89164835,
            '7-N-11-m 0.320 МэВ'    : 10.93170712,
            '7-N-11'                : 10.93136653,              # копия предыдущег значения за вычетом 0,32МэВ. Нужно чтобы файл мог считаться
            '7-N-12'    : 11.91536614,
            '7-N-14'    : 13.88277891,
            '7-N-14-m 8.490 МэВ'    : 13.891815,
            '7-N-14-m 8.964 МэВ'    : 13.89231949,
            '7-N-14-m 9.129 МэВ'    : 13.8924951,
            '7-N-15'    : 14.87124866,
            '8-O-13'    : 12.91292095,
            '8-O-14'    : 13.88825378,
            '8-O-15'    : 14.86982885,
            '8-O-16'    : 15.85750888,
            '8-O-17'    : 16.85309895,
            '8-O-18'    : 17.84453816,
            '9-F-15'    : 14.88900048,
            '9-F-16'    : 15.87391753,
            '9-F-19'    : 18.83519616,
            '9-F-19-m 4.683 МэВ'    : 18.84018038,
            '9-F-19-m 5.107 МэВ'    : 18.84063165,
            '9-F-19-m 5.337 МэВ'    : 18.84087644,
            '9-F-19-m 5.463 МэВ'    : 18.84101161,
            '9-F-19-m 5.621 МэВ'    : 18.84117871,
            '10-Ne-17'  : 16.87147872,
            '10-Ne-18'  : 17.85102839,
            '10-Ne-19'  : 18.83864243,
            '11-Na-20'  : 19.83547669,
            '11-Na-23'  : 22.79227346,
            '13-Al-24'  : 23.79376626,
            '13-Al-24-m 0.426 МэВ'  : 23.79421966,
            '13-Al-27'  : 26.74975201,
            '14-Si-28'  : 27.73658803,
            '14-Si-29'  : 28.72756959,
            '14-Si-30'  : 29.71627775,
            '14-Si-31'  : 30.70926661}

def getMass(ZA):
    Z = ZA // 1000 
    A = ZA % 1000
    name = getElement(Z)
    return float(ele_mass[ str(Z) + '-' + name + '-' + str(A)]) * 939565421 # в эВ

def getZ(ele):
    return int(elements[ele.capitalize()])

def getElement(z):
    for ele in elements:
        if elements[ele] == z:
            return ele
    return "None"

# Z = chemistry.getZ(ele)
# dau_ele = chemistry.getElement(dau_Z)