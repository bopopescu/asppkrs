from collections import namedtuple # импорт кортежей
from flask_sqlalchemy import SQLAlchemy # РАССШИРЕННОЕ

from flask import Flask,render_template, redirect, url_for, request
import numpy as np

app=Flask(__name__) # __name__   -   имя текущего файла

Message = namedtuple('ustoychivost', 'znachenie') # КОРТЕЖ
messages = [] #коллекция, которая будет хранить все мессуджи

Message2 = namedtuple('ustoychivost', 'znachenie')
messages2 = [] #коллекция, которая будет хранить все мессуджи


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














# функция на возврат расширеного хтмл
@app.route('/expanded', methods=['GET', 'POST'])
def expanded():
    return render_template('expanded.html')
















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