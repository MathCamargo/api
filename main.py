import flask
from os import environ

app = flask.Flask('enpeufscarbot')


@app.route('/', methods=['GET'])
def index():
    a = open('mainpage.txt', 'r')
    b = a.read()
    a.close()
    return b
    
def main():
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

@app.route('/docs', methods=['GET'])
def docs():
    a = open('docs.txt', 'r')
    b = a.read()
    a.close()
    return b

@app.route('/days/17-7-2021', methods=['GET'])
def days_0():
    return {'ferias': 29, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/18-7-2021', methods=['GET'])
def days_1():
    return {'ferias': 28, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/19-7-2021', methods=['GET'])
def days_2():
    return {'ferias': 27, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/20-7-2021', methods=['GET'])
def days_3():
    return {'ferias': 26, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/21-7-2021', methods=['GET'])
def days_4():
    return {'ferias': 25, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/22-7-2021', methods=['GET'])
def days_5():
    return {'ferias': 24, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/23-7-2021', methods=['GET'])
def days_6():
    return {'ferias': 23, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/24-7-2021', methods=['GET'])
def days_7():
    return {'ferias': 22, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/25-7-2021', methods=['GET'])
def days_8():
    return {'ferias': 21, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/26-7-2021', methods=['GET'])
def days_9():
    return {'ferias': 20, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/27-7-2021', methods=['GET'])
def days_10():
    return {'ferias': 19, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/28-7-2021', methods=['GET'])
def days_11():
    return {'ferias': 18, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/29-7-2021', methods=['GET'])
def days_12():
    return {'ferias': 17, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/30-7-2021', methods=['GET'])
def days_13():
    return {'ferias': 16, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/31-7-2021', methods=['GET'])
def days_14():
    return {'ferias': 15, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/1-8-2021', methods=['GET'])
def days_15():
    return {'ferias': 14, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/2-8-2021', methods=['GET'])
def days_16():
    return {'ferias': 13, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/3-8-2021', methods=['GET'])
def days_17():
    return {'ferias': 12, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/4-8-2021', methods=['GET'])
def days_19():
    return {'ferias': 11, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/5-8-2021', methods=['GET'])
def days_20():
    return {'ferias': 10, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/6-8-2021', methods=['GET'])
def days_21():
    return {'ferias': 9, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/7-8-2021', methods=['GET'])
def days_22():
    return {'ferias': 8, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/8-8-2021', methods=['GET'])
def days_23():
    return {'ferias': 7, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/9-8-2021', methods=['GET'])
def days_24():
    return {'ferias': 6, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/10-8-2021', methods=['GET'])
def days_25():
    return {'ferias': 5, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/11-8-2021', methods=['GET'])
def days_26():
    return {'ferias': 4, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/12-8-2021', methods=['GET'])
def days_27():
    return {'ferias': 3, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/13-8-2021', methods=['GET'])
def days_28():
    return {'ferias': 2, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/14-8-2021', methods=['GET'])
def days_29():
    return {'ferias': 1, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/15-8-2021', methods=['GET'])
def days_30():
    return {'ferias': 0, 
    'daulas': 0, 
    'total': 104, 
    'porcentagem': 0.000
    }

@app.route('/days/16-8-2021', methods=['GET'])
def days_31():
    return {'ferias': 0, 
    'daulas': 1, 
    'total': 104, 
    'porcentagem': 0.97
    }

@app.route('/days/17-8-2021', methods=['GET'])
def days_32():
    return {'ferias': 0, 
    'daulas': 2, 
    'total': 104, 
    'porcentagem': 1.94
    }

@app.route('/days/18-8-2021', methods=['GET'])
def days_33():
    return {'ferias': 0, 
    'daulas': 3, 
    'total': 104, 
    'porcentagem': 2.91
    }

@app.route('/days/19-8-2021', methods=['GET'])
def days_34():
    return {'ferias': 0, 
    'daulas': 4, 
    'total': 104, 
    'porcentagem': 3.88
    }

@app.route('/days/20-8-2021', methods=['GET'])
def days_35():
    return {'ferias': 0, 
    'daulas': 5, 
    'total': 104, 
    'porcentagem': 4.85
    }

@app.route('/days/21-8-2021', methods=['GET'])
def days_36():
    return {'ferias': 0, 
    'daulas': 6, 
    'total': 104, 
    'porcentagem': 5.83
    }

@app.route('/days/22-8-2021', methods=['GET'])
def days_37():
    return {'ferias': 0, 
    'daulas': 7, 
    'total': 104, 
    'porcentagem': 6.80
    }

@app.route('/days/23-8-2021', methods=['GET'])
def days_38():
    return {'ferias': 0, 
    'daulas': 8, 
    'total': 104, 
    'porcentagem': 7.77
    }

@app.route('/days/24-8-2021', methods=['GET'])
def days_39():
    return {'ferias': 0, 
    'daulas': 9, 
    'total': 104, 
    'porcentagem': 8.74
    }

@app.route('/days/25-8-2021', methods=['GET'])
def days_40():
    return {'ferias': 0, 
    'daulas': 10, 
    'total': 104, 
    'porcentagem': 9.71
    }

@app.route('/days/26-8-2021', methods=['GET'])
def days_41():
    return {'ferias': 0, 
    'daulas': 11, 
    'total': 104, 
    'porcentagem': 10.68
    }

@app.route('/days/27-8-2021', methods=['GET'])
def days_42():
    return {'ferias': 0, 
    'daulas': 12, 
    'total': 104, 
    'porcentagem': 11.65
    }

@app.route('/days/28-8-2021', methods=['GET'])
def days_43():
    return {'ferias': 0, 
    'daulas': 13, 
    'total': 104, 
    'porcentagem': 12.62
    }

@app.route('/days/29-8-2021', methods=['GET'])
def days_44():
    return {'ferias': 0, 
    'daulas': 14, 
    'total': 104, 
    'porcentagem': 13.59
    }

@app.route('/days/30-8-2021', methods=['GET'])
def days_45():
    return {'ferias': 0, 
    'daulas': 15, 
    'total': 104, 
    'porcentagem': 14.56
    }

@app.route('/days/31-8-2021', methods=['GET'])
def days_46():
    return {'ferias': 0, 
    'daulas': 16, 
    'total': 104, 
    'porcentagem': 15.53
    }

@app.route('/days/1-9-2021', methods=['GET'])
def days_47():
    return {'ferias': 0, 
    'daulas': 17, 
    'total': 104, 
    'porcentagem': 16.50
    }

@app.route('/days/2-9-2021', methods=['GET'])
def days_48():
    return {'ferias': 0, 
    'daulas': 18, 
    'total': 104, 
    'porcentagem': 17.48
    }

@app.route('/days/3-9-2021', methods=['GET'])
def days_49():
    return {'ferias': 0, 
    'daulas': 19, 
    'total': 104, 
    'porcentagem': 18.45
    }

@app.route('/days/4-9-2021', methods=['GET'])
def days_50():
    return {'ferias': 0, 
    'daulas': 20, 
    'total': 104, 
    'porcentagem': 19.42
    }

@app.route('/days/5-9-2021', methods=['GET'])
def days_51():
    return {'ferias': 0, 
    'daulas': 21, 
    'total': 104, 
    'porcentagem': 20.39
    }

@app.route('/days/6-9-2021', methods=['GET'])
def days_52():
    return {'ferias': 0, 
    'daulas': 22, 
    'total': 104, 
    'porcentagem': 21.36
    }

@app.route('/days/7-9-2021', methods=['GET'])
def days_53():
    return {'ferias': 0, 
    'daulas': 23, 
    'total': 104, 
    'porcentagem': 22.33
    }

@app.route('/days/8-9-2021', methods=['GET'])
def days_54():
    return {'ferias': 0, 
    'daulas': 24, 
    'total': 104, 
    'porcentagem': 23.30
    }

@app.route('/days/9-9-2021', methods=['GET'])
def days_55():
    return {'ferias': 0, 
    'daulas': 25, 
    'total': 104, 
    'porcentagem': 24.27
    }

@app.route('/days/10-9-2021', methods=['GET'])
def days_56():
    return {'ferias': 0, 
    'daulas': 26, 
    'total': 104, 
    'porcentagem': 25.24
    }

@app.route('/days/11-9-2021', methods=['GET'])
def days_57():
    return {'ferias': 0, 
    'daulas': 27, 
    'total': 104, 
    'porcentagem': 26.21
    }

@app.route('/days/12-9-2021', methods=['GET'])
def days_58():
    return {'ferias': 0, 
    'daulas': 28, 
    'total': 104, 
    'porcentagem': 27.18
    }

@app.route('/days/13-9-2021', methods=['GET'])
def days_59():
    return {'ferias': 0, 
    'daulas': 29, 
    'total': 104, 
    'porcentagem': 28.16
    }

@app.route('/days/14-9-2021', methods=['GET'])
def days_60():
    return {'ferias': 0, 
    'daulas': 30, 
    'total': 104, 
    'porcentagem': 29.13
    }

@app.route('/days/15-9-2021', methods=['GET'])
def days_61():
    return {'ferias': 0, 
    'daulas': 31, 
    'total': 104, 
    'porcentagem': 30.10
    }

@app.route('/days/16-9-2021', methods=['GET'])
def days_62():
    return {'ferias': 0, 
    'daulas': 32, 
    'total': 104, 
    'porcentagem': 31.07
    }

@app.route('/days/17-9-2021', methods=['GET'])
def days_63():
    return {'ferias': 0, 
    'daulas': 33, 
    'total': 104, 
    'porcentagem': 32.04
    }

@app.route('/days/18-9-2021', methods=['GET'])
def days_64():
    return {'ferias': 0, 
    'daulas': 34, 
    'total': 104, 
    'porcentagem': 33.01
    }

@app.route('/days/19-9-2021', methods=['GET'])
def days_65():
    return {'ferias': 0, 
    'daulas': 35, 
    'total': 104, 
    'porcentagem': 33.98
    }

@app.route('/days/20-9-2021', methods=['GET'])
def days_66():
    return {'ferias': 0, 
    'daulas': 36, 
    'total': 104, 
    'porcentagem': 34.95
    }

@app.route('/days/21-9-2021', methods=['GET'])
def days_67():
    return {'ferias': 0, 
    'daulas': 37, 
    'total': 104, 
    'porcentagem': 35.92
    }

@app.route('/days/22-9-2021', methods=['GET'])
def days_68():
    return {'ferias': 0, 
    'daulas': 38, 
    'total': 104, 
    'porcentagem': 36.89
    }

@app.route('/days/23-9-2021', methods=['GET'])
def days_69():
    return {'ferias': 0, 
    'daulas': 39, 
    'total': 104, 
    'porcentagem': 37.86
    }

@app.route('/days/24-9-2021', methods=['GET'])
def days_70():
    return {'ferias': 0, 
    'daulas': 40, 
    'total': 104, 
    'porcentagem': 38.83
    }

@app.route('/days/25-9-2021', methods=['GET'])
def days_71():
    return {'ferias': 0, 
    'daulas': 41, 
    'total': 104, 
    'porcentagem': 39.81
    }

@app.route('/days/26-9-2021', methods=['GET'])
def days_72():
    return {'ferias': 0, 
    'daulas': 42, 
    'total': 104, 
    'porcentagem': 40.78
    }

@app.route('/days/27-9-2021', methods=['GET'])
def days_73():
    return {'ferias': 0, 
    'daulas': 43, 
    'total': 104, 
    'porcentagem': 41.75
    }

@app.route('/days/28-9-2021', methods=['GET'])
def days_74():
    return {'ferias': 0, 
    'daulas': 44, 
    'total': 104, 
    'porcentagem': 42.72
    }

@app.route('/days/29-9-2021', methods=['GET'])
def days_75():
    return {'ferias': 0, 
    'daulas': 45, 
    'total': 104, 
    'porcentagem': 43.69
    }

@app.route('/days/30-9-2021', methods=['GET'])
def days_76():
    return {'ferias': 0, 
    'daulas': 46, 
    'total': 104, 
    'porcentagem': 44.66
    }

@app.route('/days/1-10-2021', methods=['GET'])
def days_77():
    return {'ferias': 0, 
    'daulas': 47, 
    'total': 104, 
    'porcentagem': 45.63
    }

@app.route('/days/2-10-2021', methods=['GET'])
def days_78():
    return {'ferias': 0, 
    'daulas': 48, 
    'total': 104, 
    'porcentagem': 46.60
    }

@app.route('/days/3-10-2021', methods=['GET'])
def days_79():
    return {'ferias': 0, 
    'daulas': 49, 
    'total': 104, 
    'porcentagem': 47.57
    }

@app.route('/days/4-10-2021', methods=['GET'])
def days_80():
    return {'ferias': 0, 
    'daulas': 50, 
    'total': 104, 
    'porcentagem': 48.54
    }

@app.route('/days/5-10-2021', methods=['GET'])
def days_81():
    return {'ferias': 0, 
    'daulas': 51, 
    'total': 104, 
    'porcentagem': 49.51
    }

@app.route('/days/6-10-2021', methods=['GET'])
def days_82():
    return {'ferias': 0, 
    'daulas': 52, 
    'total': 104, 
    'porcentagem': 50.49
    }

@app.route('/days/7-10-2021', methods=['GET'])
def days_83():
    return {'ferias': 0, 
    'daulas': 53, 
    'total': 104, 
    'porcentagem': 51.46
    }

@app.route('/days/8-10-2021', methods=['GET'])
def days_84():
    return {'ferias': 0, 
    'daulas': 54, 
    'total': 104, 
    'porcentagem': 52.43
    }

@app.route('/days/9-10-2021', methods=['GET'])
def days_85():
    return {'ferias': 0, 
    'daulas': 55, 
    'total': 104, 
    'porcentagem': 53.40
    }

@app.route('/days/10-10-2021', methods=['GET'])
def days_86():
    return {'ferias': 0, 
    'daulas': 56, 
    'total': 104, 
    'porcentagem': 54.37
    }

@app.route('/days/11-10-2021', methods=['GET'])
def days_87():
    return {'ferias': 0, 
    'daulas': 57, 
    'total': 104, 
    'porcentagem': 55.34
    }

@app.route('/days/12-10-2021', methods=['GET'])
def days_88():
    return {'ferias': 0, 
    'daulas': 58, 
    'total': 104, 
    'porcentagem': 56.31
    }

@app.route('/days/13-10-2021', methods=['GET'])
def days_89():
    return {'ferias': 0, 
    'daulas': 59, 
    'total': 104, 
    'porcentagem': 57.28
    }

@app.route('/days/14-10-2021', methods=['GET'])
def days_90():
    return {'ferias': 0, 
    'daulas': 60, 
    'total': 104, 
    'porcentagem': 58.25
    }

@app.route('/days/15-10-2021', methods=['GET'])
def days_91():
    return {'ferias': 0, 
    'daulas': 61, 
    'total': 104, 
    'porcentagem': 59.22
    }

@app.route('/days/16-10-2021', methods=['GET'])
def days_92():
    return {'ferias': 0, 
    'daulas': 62, 
    'total': 104, 
    'porcentagem': 60.19
    }

@app.route('/days/17-10-2021', methods=['GET'])
def days_93():
    return {'ferias': 0, 
    'daulas': 63, 
    'total': 104, 
    'porcentagem': 61.17
    }

@app.route('/days/18-10-2021', methods=['GET'])
def days_94():
    return {'ferias': 0, 
    'daulas': 64, 
    'total': 104, 
    'porcentagem': 62.14
    }

@app.route('/days/19-10-2021', methods=['GET'])
def days_95():
    return {'ferias': 0, 
    'daulas': 65, 
    'total': 104, 
    'porcentagem': 63.11
    }

@app.route('/days/20-10-2021', methods=['GET'])
def days_96():
    return {'ferias': 0, 
    'daulas': 66, 
    'total': 104, 
    'porcentagem': 64.08
    }

@app.route('/days/21-10-2021', methods=['GET'])
def days_97():
    return {'ferias': 0, 
    'daulas': 67, 
    'total': 104, 
    'porcentagem': 65.05
    }

@app.route('/days/22-10-2021', methods=['GET'])
def days_98():
    return {'ferias': 0, 
    'daulas': 68, 
    'total': 104, 
    'porcentagem': 66.02
    }

@app.route('/days/23-10-2021', methods=['GET'])
def days_99():
    return {'ferias': 0, 
    'daulas': 69, 
    'total': 104, 
    'porcentagem': 66.99
    }

@app.route('/days/24-10-2021', methods=['GET'])
def days_101():
    return {'ferias': 0, 
    'daulas': 70, 
    'total': 104, 
    'porcentagem': 67.96
    }

@app.route('/days/25-10-2021', methods=['GET'])
def days_102():
    return {'ferias': 0, 
    'daulas': 71, 
    'total': 104, 
    'porcentagem': 68.93
    }

@app.route('/days/26-10-2021', methods=['GET'])
def days_103():
    return {'ferias': 0, 
    'daulas': 72, 
    'total': 104, 
    'porcentagem': 69.90
    }

@app.route('/days/27-10-2021', methods=['GET'])
def days_104():
    return {'ferias': 0, 
    'daulas': 73, 
    'total': 104, 
    'porcentagem': 70.87
    }

@app.route('/days/28-10-2021', methods=['GET'])
def days_105():
    return {'ferias': 0, 
    'daulas': 74, 
    'total': 104, 
    'porcentagem': 71.84
    }

@app.route('/days/29-10-2021', methods=['GET'])
def days_106():
    return {'ferias': 0, 
    'daulas': 75, 
    'total': 104, 
    'porcentagem': 72.82
    }

@app.route('/days/30-10-2021', methods=['GET'])
def days_107():
    return {'ferias': 0, 
    'daulas': 76, 
    'total': 104, 
    'porcentagem': 73.79
    }

@app.route('/days/31-10-2021', methods=['GET'])
def days_108():
    return {'ferias': 0, 
    'daulas': 77, 
    'total': 104, 
    'porcentagem': 74.76
    }

@app.route('/days/1-11-2021', methods=['GET'])
def days_109():
    return {'ferias': 0, 
    'daulas': 78, 
    'total': 104, 
    'porcentagem': 75.73
    }

@app.route('/days/2-11-2021', methods=['GET'])
def days_110():
    return {'ferias': 0, 
    'daulas': 79, 
    'total': 104, 
    'porcentagem': 76.70
    }

@app.route('/days/3-11-2021', methods=['GET'])
def days_111():
    return {'ferias': 0, 
    'daulas': 80, 
    'total': 104, 
    'porcentagem': 77.67
    }

@app.route('/days/4-11-2021', methods=['GET'])
def days_112():
    return {'ferias': 0, 
    'daulas': 81, 
    'total': 104, 
    'porcentagem': 78.64
    }

@app.route('/days/5-11-2021', methods=['GET'])
def days_113():
    return {'ferias': 0, 
    'daulas': 82, 
    'total': 104, 
    'porcentagem': 79.61
    }

@app.route('/days/6-11-2021', methods=['GET'])
def days_114():
    return {'ferias': 0, 
    'daulas': 83, 
    'total': 104, 
    'porcentagem': 80.58
    }

@app.route('/days/7-11-2021', methods=['GET'])
def days_115():
    return {'ferias': 0, 
    'daulas': 84, 
    'total': 104, 
    'porcentagem': 81.55
    }

@app.route('/days/8-11-2021', methods=['GET'])
def days_116():
    return {'ferias': 0, 
    'daulas': 85, 
    'total': 104, 
    'porcentagem': 82.52
    }

@app.route('/days/9-11-2021', methods=['GET'])
def days_117():
    return {'ferias': 0, 
    'daulas': 86, 
    'total': 104, 
    'porcentagem': 83.50
    }

@app.route('/days/10-11-2021', methods=['GET'])
def days_118():
    return {'ferias': 0, 
    'daulas': 87, 
    'total': 104, 
    'porcentagem': 84.47
    }

@app.route('/days/11-11-2021', methods=['GET'])
def days_119():
    return {'ferias': 0, 
    'daulas': 88, 
    'total': 104, 
    'porcentagem': 85.44
    }

@app.route('/days/12-11-2021', methods=['GET'])
def days_120():
    return {'ferias': 0, 
    'daulas': 89, 
    'total': 104, 
    'porcentagem': 86.41
    }

@app.route('/days/13-11-2021', methods=['GET'])
def days_121():
    return {'ferias': 0, 
    'daulas': 90, 
    'total': 104, 
    'porcentagem': 87.38
    }

@app.route('/days/14-11-2021', methods=['GET'])
def days_122():
    return {'ferias': 0, 
    'daulas': 91, 
    'total': 104, 
    'porcentagem': 88.35
    }

@app.route('/days/15-11-2021', methods=['GET'])
def days_123():
    return {'ferias': 0, 
    'daulas': 92, 
    'total': 104, 
    'porcentagem': 89.32
    }

@app.route('/days/16-11-2021', methods=['GET'])
def days_124():
    return {'ferias': 0, 
    'daulas': 93, 
    'total': 104, 
    'porcentagem': 90.29
    }

@app.route('/days/17-11-2021', methods=['GET'])
def days_125():
    return {'ferias': 0, 
    'daulas': 94, 
    'total': 104, 
    'porcentagem': 91.26
    }

@app.route('/days/18-11-2021', methods=['GET'])
def days_126():
    return {'ferias': 0, 
    'daulas': 95, 
    'total': 104, 
    'porcentagem': 92.23
    }

@app.route('/days/19-11-2021', methods=['GET'])
def days_127():
    return {'ferias': 0, 
    'daulas': 96, 
    'total': 104, 
    'porcentagem': 93.20
    }

@app.route('/days/20-11-2021', methods=['GET'])
def days_128():
    return {'ferias': 0, 
    'daulas': 97, 
    'total': 104, 
    'porcentagem': 94.17
    }

@app.route('/days/21-11-2021', methods=['GET'])
def days_129():
    return {'ferias': 0, 
    'daulas': 98, 
    'total': 104, 
    'porcentagem': 95.15
    }

@app.route('/days/22-11-2021', methods=['GET'])
def days_130():
    return {'ferias': 0, 
    'daulas': 99, 
    'total': 104, 
    'porcentagem': 96.12
    }

@app.route('/days/23-11-2021', methods=['GET'])
def days_131():
    return {'ferias': 0, 
    'daulas': 100, 
    'total': 104, 
    'porcentagem': 97.09
    }

@app.route('/days/24-11-2021', methods=['GET'])
def days_132():
    return {'ferias': 0, 
    'daulas': 101, 
    'total': 104, 
    'porcentagem': 98.06
    }

@app.route('/days/25-11-2021', methods=['GET'])
def days_133():
    return {'ferias': 0, 
    'daulas': 102, 
    'total': 104, 
    'porcentagem': 99.03
    }

@app.route('/days/26-11-2021', methods=['GET'])
def days_134():
    return {'ferias': 0, 
    'daulas': 103, 
    'total': 104, 
    'porcentagem': 99.90
    }

@app.route('/days/27-11-2021', methods=['GET'])
def days_135():
    return {'ferias': 0, 
    'daulas': 104, 
    'total': 104, 
    'porcentagem': 100
    }

if __name__ == '__main__':
    main()
