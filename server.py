from collections import namedtuple # импорт кортежей
from flask_sqlalchemy import SQLAlchemy # РАССШИРЕННОЕ

from flask import Flask,render_template, redirect, url_for, request
import numpy as np

app=Flask(__name__) # __name__   -   имя текущего файла

Message = namedtuple('ustoychivost', 'znachenie') # КОРТЕЖ
messages = [] #коллекция, которая будет хранить все мессуджи

Message2 = namedtuple('ustoychivost', 'znachenie')
messages2 = [] #коллекция, которая будет хранить все мессуджи

Message3 = namedtuple('ustoychivost', 'znachenie')
messages3 = []



@app.route ('/', methods=['GET'])
def index ():
    return render_template('index.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.html', messages=messages, messages2=messages2) # возврат кортежей и шаблона

#в форме прописать путь до маршрута action . принять объект запроса. данные вероятно не долетают
@app.route('/add_message', methods=['POST'])
def variaciya():

    perviy_god = float(request.form['perviy_god'])
    vtoroy_god = float(request.form['vtoroy_god'])
    tretiy_god = float(request.form['tretiy_god'])
    chetvertiy_god = float(request.form['chetvertiy_god'])
    pyatiy_god = float(request.form['pyatiy_god'])
    izmereniya_nadoya = (perviy_god, vtoroy_god, tretiy_god, chetvertiy_god, pyatiy_god)
    
    dot_perviy_god=float(request.form[ "dot_perviy_god"])
    dot_vtoroy_god=float(request.form[ "dot_vtoroy_god"])
    dot_tretiy_god=float(request.form[ "dot_tretiy_god"])
    dot_chetvertiy_god=float(request.form[ "dot_chetvertiy_god"])
    dot_pyatiy_god=float(request.form[ "dot_pyatiy_god"])
    dot_po_godam = (dot_perviy_god, dot_vtoroy_god, dot_tretiy_god, dot_chetvertiy_god, dot_pyatiy_god)

    #ВАРИАЦИЯ ВАРИАЦИЯ ВАРИАЦИЯ
    kolichestvo_izmereniy = len(izmereniya_nadoya)
    summa_izmereniy=0  #этот цикл для рассчета среднего значения измерений
    for i in izmereniya_nadoya:
        summa_izmereniy = summa_izmereniy + i
    srednee_izmereniy=summa_izmereniy/kolichestvo_izmereniy
    kvadrat_raznosti=0
    for i in izmereniya_nadoya:
        kvadrat_raznosti = (np.square(i - srednee_izmereniy) + kvadrat_raznosti)
    variaciya = round(((np.sqrt(kvadrat_raznosti/(kolichestvo_izmereniy-1)))/srednee_izmereniy)*100, 4)

    #КОРРЕЛЯЦИЯ КОРРЕЛЯЦИЯ КОРРЕЛЯЦИЯ

    sr_nadoi = sum(izmereniya_nadoya)/len(izmereniya_nadoya)
    sr_dotacii = sum(dot_po_godam)/len(dot_po_godam)
    summa_po_godam = 0
    for i, j  in zip(dot_po_godam, izmereniya_nadoya):
        summa_po_godam = (i - sr_dotacii)*(j - sr_dotacii) + summa_po_godam
    summa_srednih_dotacii = 0 # vso soshlos s kompoma
    for i in dot_po_godam :
          summa_srednih_dotacii  =  np.square(i - sr_dotacii) + summa_srednih_dotacii
    summa_srednego_nadoya = 0 # vso soshlos s kompom
    for i in izmereniya_nadoya:
          summa_srednego_nadoya   =  np.square(i - sr_nadoi) + summa_srednego_nadoya
    znamenatel_korrel = np.sqrt(summa_srednih_dotacii * summa_srednego_nadoya)
    koefficient_korrelyacii = summa_po_godam/znamenatel_korrel
    korrelyaciya = round(koefficient_korrelyacii,4)

    #НАИМЕНЬШИЕ КВАДРАТЫ НАИМЕНЬШИЕ КВАДРАТЫ НАИМЕНЬШИЕ КВАДРАТЫ НАИМЕНЬШИЕ КВАДРАТЫ НАИМЕНЬШИЕ КВАДРАТЫ 

    id1 = (1,2,3,4,5)
    chislitel_vichitaemoe_summa = 0
    for i,j in zip (dot_po_godam, id1):
        chislitel_vichitaemoe_summa  = i * j + chislitel_vichitaemoe_summa
    chislitel_vychetaemoe = chislitel_vichitaemoe_summa # потом домножить на 5ю посмотрим что будет
    summa_dotacii = 0
    for i in dot_po_godam:
        summa_dotacii = i + summa_dotacii
    summa_goda = 0
    for i in id1:
        summa_goda = i + summa_goda
    chislitel = chislitel_vychetaemoe * 5 - (summa_goda * summa_dotacii)
    znamenatel_vichitaemoe1 = 0
    for i in id1:
        znamenatel_vichitaemoe1 = (np.square (i)) + znamenatel_vichitaemoe1
    znamenatel_vichitaemoe = znamenatel_vichitaemoe1 * len(id1)
    znamenatal_vichitatel1 = 0
    for i in id1:
        znamenatal_vichitatel1  = i + znamenatal_vichitatel1
    znamenatal_vichitatel = np.square (znamenatal_vichitatel1)
    znamenatel = znamenatel_vichitaemoe - znamenatal_vichitatel
    koef = chislitel/znamenatel

    prog0 = dot_pyatiy_god
    prog1 = round (prog0+koef,2)
    prog2 = round(prog1+koef, 2)
    prog3 = round(prog2+koef,2)
    prog4 = round(prog3+koef,2)
    prog5 = round(prog4+koef, 2)

    messages.append(Message([ #скобка открывающая кортеж
        #summ # возврат значения, указанного в функции, summ и есть это значение   
        variaciya , korrelyaciya, prog0, prog1, prog2, prog3, prog4, prog5
        ]), ) #скобка закрывающая кортеж и его результат
    return redirect(url_for('main'))

@app.route('/add', methods=['POST'])
def variaciya2():
    perviy_god2 = float(request.form['perviy_god2'])
    vtoroy_god2 = float(request.form['vtoroy_god2'])
    tretiy_god2 = float(request.form['tretiy_god2'])
    chetvertiy_god2 = float(request.form['chetvertiy_god2'])
    pyatiy_god2 = float(request.form['pyatiy_god2'])
    izmereniya_nadoya2 = (perviy_god2, vtoroy_god2, tretiy_god2, chetvertiy_god2, pyatiy_god2)
    
    dot_perviy_god2=float(request.form[ "dot_perviy_god2"])
    dot_vtoroy_god2=float(request.form[ "dot_vtoroy_god2"])
    dot_tretiy_god2=float(request.form[ "dot_tretiy_god2"])
    dot_chetvertiy_god2=float(request.form[ "dot_chetvertiy_god2"])
    dot_pyatiy_god2=float(request.form[ "dot_pyatiy_god2"])
    dot_po_godam2 = (dot_perviy_god2, dot_vtoroy_god2, dot_tretiy_god2, dot_chetvertiy_god2, dot_pyatiy_god2)

    #ВАРИАЦИЯ ВАРИАЦИЯ ВАРИАЦИЯ
    kolichestvo_izmereniy2 = len(izmereniya_nadoya2)
    summa_izmereniy2=0  #этот цикл для рассчета среднего значения измерений
    for i in izmereniya_nadoya2:
        summa_izmereniy2 = summa_izmereniy2 + i
    srednee_izmereniy2=summa_izmereniy2/kolichestvo_izmereniy2

    kvadrat_raznosti2=0
    for i in izmereniya_nadoya2:
        kvadrat_raznosti2 = (np.square(i - srednee_izmereniy2) + kvadrat_raznosti2)
    variaciya2 = round(((np.sqrt(kvadrat_raznosti2/(kolichestvo_izmereniy2-1)))/srednee_izmereniy2)*100,3)

    #КОРРЕЛЯЦИЯ КОРРЕЛЯЦИЯ КОРРЕЛЯЦИЯ

    sr_nadoi2 = sum(izmereniya_nadoya2)/len(izmereniya_nadoya2)
    sr_dotacii2 = sum(dot_po_godam2)/len(dot_po_godam2)

    summa_po_godam2 = 0
    for i, j  in zip(dot_po_godam2, izmereniya_nadoya2):
        summa_po_godam2 = (i - sr_dotacii2)*(j - sr_dotacii2) + summa_po_godam2

    summa_srednih_dotacii2 = 0 # vso soshlos s kompoma
    for i in dot_po_godam2:
          summa_srednih_dotacii2  =  np.square(i - sr_dotacii2) + summa_srednih_dotacii2

    summa_srednego_nadoya2 = 0 # vso soshlos s kompom
    for i in izmereniya_nadoya2:
          summa_srednego_nadoya2   =  np.square(i - sr_nadoi2) + summa_srednego_nadoya2

    znamenatel_korrel2 = np.sqrt(summa_srednih_dotacii2 * summa_srednego_nadoya2)
    koefficient_korrelyacii2 = round(summa_po_godam2/znamenatel_korrel2,4)



    korrelyaciya2 = koefficient_korrelyacii2

    #НАИМЕНЬШИЕ КВАДРАТЫ НАИМЕНЬШИЕ КВАДРАТЫ НАИМЕНЬШИЕ КВАДРАТЫ НАИМЕНЬШИЕ КВАДРАТЫ НАИМЕНЬШИЕ КВАДРАТЫ 

    id2 = (1,2,3,4,5)
    chislitel_vichitaemoe_summa2 = 0
    for i,j in zip (dot_po_godam2, id2):
        chislitel_vichitaemoe_summa2  = i * j + chislitel_vichitaemoe_summa2
    chislitel_vychetaemoe2 = chislitel_vichitaemoe_summa2 # потом домножить на 5ю посмотрим что будет
    summa_dotacii2 = 0
    for i in dot_po_godam2:
        summa_dotacii2 = i + summa_dotacii2
    summa_goda2 = 0
    for i in id2:
        summa_goda2 = i + summa_goda2
    chislitel2 = chislitel_vychetaemoe2 * 5 - (summa_goda2 * summa_dotacii2)
    znamenatel_vichitaemoe2 = 0
    for i in id2:
        znamenatel_vichitaemoe2 = (np.square (i)) + znamenatel_vichitaemoe2
    znamenatel_vichitaemoe2 = znamenatel_vichitaemoe2 * len(id2)
    znamenatal_vichitatel2 = 0
    for i in id2:
        znamenatal_vichitatel2  = i + znamenatal_vichitatel2
    znamenatal_vichitatel2 = np.square (znamenatal_vichitatel2)
    znamenatel2 = znamenatel_vichitaemoe2 - znamenatal_vichitatel2
    koef2 = chislitel2/znamenatel2

    prog0 = dot_pyatiy_god2
    prog1 = round (prog0+koef2,2)
    prog2 = round(prog1+koef2, 2)
    prog3 = round(prog2+koef2,2)
    prog4 = round(prog3+koef2,2)
    prog5 = round(prog4+koef2, 2)

    messages2.append(Message2([ #скобка открывающая кортеж
        #summ # возврат значения, указанного в функции, summ и есть это значение   
        variaciya2 , korrelyaciya2, prog0, prog1, prog2, prog3, prog4, prog5
        ]), ) #скобка закрывающая кортеж и его результат

    return redirect(url_for('main'))


@app.route('/expanded', methods=['GET', 'POST'])
def expanded():
    return render_template('expanded.html', messages3=messages3)

@app.route('/deeper' , methods=['POST'])
def deeper():
    total_count = (1,2,3,4,5)

    selfprice1 = float(request.form['selfprice1'])
    selfprice2 = float(request.form['selfprice2'])
    selfprice3 = float(request.form['selfprice3'])
    selfprice4 = float(request.form['selfprice4'])
    selfprice5 = float(request.form['selfprice5'])
    total_selfprice = (selfprice1, selfprice2, selfprice3, selfprice4, selfprice5)
    var_total_selfprice = round(np.std(total_selfprice, ddof=1)/np.average(total_selfprice)*100,3)
    
    subsidies1 = float(request.form['subsidies1'])
    subsidies2 = float(request.form['subsidies2'])
    subsidies3 = float(request.form['subsidies3'])
    subsidies4 = float(request.form['subsidies4'])
    subsidies5 = float(request.form['subsidies5'])
    total_subsidies = (subsidies1, subsidies2, subsidies3, subsidies4, subsidies5)
    var_total_subsidies = round(np.std(total_subsidies, ddof=1)/np.average(total_subsidies)*100,3)

    #tradeprice1 = float(request.form['tradeprice1'])
    #tradeprice2 = float(request.form['tradeprice2'])
    #tradeprice3 = float(request.form['tradeprice3'])
    #tradeprice4 = float(request.form['tradeprice4'])
    #tradeprice5 = float(request.form['tradeprice5'])
    #total_tradeprice = (tradeprice1, tradeprice2, tradeprice3, tradeprice4, tradeprice5)
    #var_total_tradeprice = round(np.std(total_tradeprice, ddof=1)/np.average(total_tradeprice)*100,3)

    #rent_with_sub1 = float(request.form['rent_with_sub1'])
    #rent_with_sub2 = float(request.form['rent_with_sub2'])
    #rent_with_sub3 = float(request.form['rent_with_sub3'])
    #rent_with_sub4 = float(request.form['rent_with_sub4'])
    #rent_with_sub5 = float(request.form['rent_with_sub5'])
    #total_rent_with_sub = (rent_with_sub1, rent_with_sub2, rent_with_sub3, rent_with_sub4, rent_with_sub5)
    #var_total_rent_with_sub = round(np.std(total_rent_with_sub, ddof=1)/np.average(total_rent_with_sub)*100, 3)

    #rent_without_sub1 = float(request.form['rent_without_sub1'])
    #rent_without_sub2 = float(request.form['rent_without_sub2'])
    #rent_without_sub3 = float(request.form['rent_without_sub3'])
    #rent_without_sub4 = float(request.form['rent_without_sub4'])
    #rent_without_sub5 = float(request.form['rent_without_sub5'])
    #total_rent_without_sub = (rent_without_sub1, rent_without_sub2, rent_without_sub3, rent_without_sub4, rent_without_sub5)
    #var_total_rent_without_sub= round(np.std(total_rent_without_sub, ddof=1)/np.average(total_rent_without_sub)*100 ,3)

    #lifetime1 = float(request.form['lifetime1'])
    #lifetime2 = float(request.form['lifetime2'])
    #lifetime3 = float(request.form['lifetime3'])
    #lifetime4 = float(request.form['lifetime4'])
    #lifetime5 = float(request.form['lifetime5'])
    #total_lifetime = (lifetime1, lifetime2, lifetime3, lifetime4, lifetime5)
    #var_total_lifetime= round(np.std(total_lifetime, ddof=1)/np.average(total_lifetime)*100, 3)


    #offspring1= float(request.form['offspring1'])
    #offspring2= float(request.form['offspring2'])
    #offspring3= float(request.form['offspring3'])
    #offspring4= float(request.form['offspring4'])
    #offspring5= float(request.form['offspring5'])
    #total_offspring = (offspring1, offspring2, offspring3, offspring4, offspring5)
    #var_total_offspring= round(np.std(total_offspring, ddof=1)/np.average(total_offspring)*100, 3)

    #mortality1 = float(request.form['mortality1'])
    #mortality2 = float(request.form['mortality2'])
    #mortality3 = float(request.form['mortality3'])
    #mortality4 = float(request.form['mortality4'])
    #mortality5 = float(request.form['mortality5'])
    #total_mortality = (mortality1, mortality2, mortality3, mortality4, mortality5)
    #var_total_mortality= round (np.std(total_mortality, ddof=1)/np.average(total_mortality)*100, 3)

    #yeild1 = float(request.form['yeild1'])
    #yeild2 = float(request.form['yeild2'])
    #yeild3 = float(request.form['yeild3'])
    #yeild4 = float(request.form['yeild4'])
    #yeild5 = float(request.form['yeild5'])
    #total_yeild = (yeild1, yeild2, yeild3, yeild4, yeild5)
    #var_total_yeild= round (np.std(total_yeild, ddof=1)/np.average(total_yeild)*100, 3)

    #fat_content1 = float(request.form['fat_content1'])
    #fat_content2 = float(request.form['fat_content2'])
    #fat_content3 = float(request.form['fat_content3'])
    #fat_content4 = float(request.form['fat_content4'])
    #fat_content5 = float(request.form['fat_content5'])
    #total_fat_content = (fat_content1, fat_content2, fat_content3, fat_content4, fat_content5)
    #var_fat_content= round (np.std(total_fat_content, ddof=1)/np.average(total_fat_content)*100, 3)

    #protein_content1 = float(request.form['protein_content1'])
    #protein_content2 = float(request.form['protein_content2'])
    #protein_content3 = float(request.form['protein_content3'])
    #protein_content4 = float(request.form['protein_content4'])
    #protein_content5 = float(request.form['protein_content5'])
    #total_protein_content = (protein_content1, protein_content2, protein_content3, protein_content4, protein_content5)
    #var_total_protein_content= round (np.std(total_protein_content, ddof=1)/np.average(total_protein_content)*100, 3)


    #Корреляция себестоимости и дотаций, но это пример, пусть пока считает
    #corr_total_selfprice_total_subsidies = np.corrcoef (total_selfprice, total_subsidies)

    
    #corr_total_selfprice_total_offspring = round(np.corrcoef (total_selfprice, total_offspring) ,3)
    #corr_total_selfprice_total_mortality = round(np.corrcoef (total_selfprice, total_mortality), 3)
    #corr_total_selfprice_total_lifetime = round(np.corrcoef (total_selfprice, total_lifetime), 3)
    #corr_total_selfprice_total_yeild = round(np.corrcoef (total_selfprice, total_yeild), 3)

    #corr_total_subsidies_total_offspring = round (np.corrcoef (total_subsidies, total_offspring),3)
    #corr_total_subsidies_total_mortality = round(np.corrcoef (total_subsidies, total_mortality),3)
    #corr_total_subsidies_total_lifetime = round(np.corrcoef (total_subsidies, total_lifetime),3)
    #corr_total_subsidies_total_yeild = round(np.corrcoef (total_subsidies, total_yeild), 3)

    #corr_total_tradeprice_total_rent_with_sub= round (np.corrcoef (total_tradeprice, total_rent_with_sub), 3)
    #corr_total_tradeprice_total_offspring= round (np.corrcoef (total_tradeprice, total_offspring), 3)
    #corr_total_tradeprice_total_mortality= round (np.corrcoef (total_tradeprice, total_mortality), 3)

    #corr_total_rent_without_sub_total_yeild= round(np.corrcoef (total_rent_without_sub, total_yeild),3)

    #corr_total_offspring_total_yeild= round(np.corrcoef (total_offspring, total_yeild), 3)
    #corr_total_offspring_total_mortality= round (np.corrcoef (total_offspring, total_mortality), 3)

    #corr_total_yeild_total_fat_content= round(np.corrcoef (total_yeild, total_fat_content), 3)
    #corr_total_protein_content= round(np.corrcoef (total_yeild, total_protein_content), 3)


    messages3.append(Message3([ #скобка открывающая кортеж
        #summ # возврат значения, указанного в функции, summ и есть это значение   

        var_total_selfprice, var_total_subsidies #, var_total_tradeprice, var_total_rent_with_sub, var_total_rent_without_sub
        #var_total_lifetime, var_total_offspring, var_total_mortality, var_total_yeild,
        #var_fat_content, var_total_protein_content,
        
        #corr_total_selfprice_total_offspring [0,1], corr_total_selfprice_total_mortality [0,1],
        #corr_total_selfprice_total_lifetime [0,1], corr_total_selfprice_total_yeild  [0,1],
        #corr_total_subsidies_total_offspring [0,1], corr_total_subsidies_total_mortality [0,1], 
        #corr_total_subsidies_total_lifetime [0,1], corr_total_subsidies_total_yeild [0,1],
        #corr_total_tradeprice_total_rent_with_sub [0,1], corr_total_tradeprice_total_offspring [0,1],
        #corr_total_tradeprice_total_mortality [0,1], corr_total_rent_without_sub_total_yeild [0,1],
        #corr_total_offspring_total_yeild [0,1], corr_total_offspring_total_mortality [0,1],
        #corr_total_yeild_total_fat_content [0,1], corr_total_protein_content [0,1],



        

        ]), ) #скобка закрывающая кортеж и его результат

    return redirect(url_for('expanded'))



#ДЛЯ РАССШИРЕННОГО ПРИЛОЖЕНИЯ
db = SQLAlchemy() # РАССШИРЕННОЕ
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    return app

class CowsBreeds (db.Model):
    id = db.Column(db.Integer, primary_key=True) #создаем столбец, назначаем содержимое
    breed = db.Column(db.String, nullable=False) #создаем столбец, назначаем содержимое, обязательное к заполнению
    latitude = db.Column(db.String, nullable = False)
    longitude = db.Column(db.String, nullable = False)
    self_cost = db.Column(db.Float, nullable = False)
    trade_cost = db.Column(db.Float, nullable = False)
    subsidies = db.Column(db.Float, nullable = False)
    pr_with_sub = db.Column(db.Float, nullable = False)
    pr_without_sub = db.Column(db.Float, nullable = False)
    lifetime = db.Column(db.Float, nullable = False)
    offspring = db.Column(db.Float, nullable = False)
    mortality = db.Column(db.Float, nullable = False)
    yeild = db.Column(db.Float, nullable = False)
    fat_content = db.Column(db.Float, nullable = True)#создаем столбец, назначаем содержимое, НЕ обязательное к заполнению
    protein_content = db.Column(db.Float, nullable = True)

    def __repr__(self):
        return '<CowsBreeds {} {}>'.format(self.breed, self.yeild)








# Попытка построить график. Но это немного попозже
@app.route('/line')
def line():
    labels = ['1-st', '2-nd', '3-d','4-th' ,'5-th' ,'6-th' ,'7-th' ,'8-th' ,'9-th' ,'10-th' ]
    values = [230,456]

    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Тут будет прогноз методом наименьших квадратов', min=0, max=500, labels=line_labels, values=line_values)






if __name__ == '__main__':  #файл запускается напрямую
    app.run(debug=True)