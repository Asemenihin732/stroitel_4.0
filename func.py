import pandas as pd
import random
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit
import tkinter as tk
from tkinter import ttk

def submit_dates():
    month = entry1.get()
    year = entry2.get()
    data = pd.read_excel('graphs.xlsx')
    kolv_in1 = float(entry3.get())
    kolv_in2 = float(entry4.get())
    kolv_in3 = float(entry5.get())
    kolv_in4 = float(entry6.get())
    kolv_in5 = float(entry7.get())
    kolv_in6 = float(entry8.get())
    # ____________________________Работает__________________________________________________________________________
    X = data[["Месяц строительства ", "year "]]
    Y = data[["Общестроительные работы", "Тепломонтажнные работы ", "Электромонтажные работы ",
              "Общестроительные работы1", "Тепломонтажнные работы1", "Электромонтажные работы1",
              "Общестроительные работы12", "Тепломонтажнные работы12", "Электромонтажные работы12",
              "Итого", "Итого 1", "Итого 12"]]
    tscv = TimeSeriesSplit(n_splits=10)
    for train_index, test_index in tscv.split(X):
        x_train, x_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = Y.iloc[train_index], Y.iloc[test_index]
        model = RandomForestRegressor()
        model.fit(x_train, y_train)
        ypred = model.predict(X)

    plt.plot(X["Месяц строительства "], Y["Общестроительные работы"],
            label="Фактические значения Общестроительные работы Б1")
    # plt.plot(X["Месяц строительства "], Y["Тепломонтажнные работы "],
    #          label="Фактические значения Тепломонтажнные работы Б1")
    # plt.plot(X["Месяц строительства "], Y["Электромонтажные работы "],
    #          label="Фактические значения Электромонтажные работы Б1")
    # plt.plot(X["Месяц строительства "], Y["Общестроительные работы1"],
    #         label="Фактические значения Общестроительные работы  Б2")
    # plt.plot(X["Месяц строительства "], Y["Тепломонтажнные работы1"],
    #          label="Фактические значения Тепломонтажнные работы Б2")
    # plt.plot(X["Месяц строительства "], Y["Электромонтажные работы1"],
    #          label="Фактические значения Электромонтажные работы Б2")
    # plt.plot(X["Месяц строительства "], Y["Итого"],
    #          label="Фактические значения Итого")
    # plt.plot(X["Месяц строительства "], Y["Итого 1"],
    #          label="Фактические значения Итого 1 ")
    # plt.plot(X["Месяц строительства "], Y["Итого 12"],
    #          label="Фактические значения Итого 12 ")
    # plt.plot(X["Месяц строительства "], Y["Общестроительные работы1"],
    #          label="Фактические значения Общестроительные работы1")
    # plt.plot(X["Месяц строительства "], Y["Общестроительные работы12"],
    #          label="Фактические значения Общестроительные работы12")
    #
    # plt.plot(X["Месяц строительства "][:13], (kolv_in1*1.5+(100-kolv_in1)*1.2) * ypred[:13, 0], label="Прогноз общего количества рабочих для общестроительных работ 1 год")
    # plt.plot(X["Месяц строительства "][12:], (kolv_in4*1.5+(100-kolv_in4)*1.2) * ypred[12:, 0], label="Прогноз общего количества рабочих для общестроительных работ 2 год")
    # plt.plot(X["Месяц строительства "][:13], (kolv_in2*1.5+(100-kolv_in2)*1.2) * ypred[:13, 1], label="Прогноз общего количества рабочих для тепломонтажных работ 1 год")
    # plt.plot(X["Месяц строительства "][12:], (kolv_in5*1.5+(100-kolv_in5)*1.2) * ypred[12:, 1], label="Прогноз общего количества рабочих для тепломонтажных работ 2 год")
    # plt.plot(X["Месяц строительства "][:13], (kolv_in3*1.5+(100-kolv_in3)*1.2) * ypred[:13, 2], label="Прогноз общего количества рабочих для электромонтажных работ 1 год")
    # plt.plot(X["Месяц строительства "][12:], (kolv_in6*1.5+(100-kolv_in6)*1.2) * ypred[12:, 2], label="Прогноз общего количества рабочих для электромонтажных работ 2 год")
    # plt.plot(X["Месяц строительства "][:13], (kolv_in1*1.5+(100-kolv_in1)*1.2) * ypred[:13, 3], label="Прогноз общего количества рабочих для общестроительных работ 1 год Б2")
    # plt.plot(X["Месяц строительства "][12:], (kolv_in4*1.5+(100-kolv_in4)*1.2) * ypred[12:, 3], label="Прогноз общего количества рабочих для общестроительных работ 2 год Б2")
    # plt.plot(X["Месяц строительства "][:13], (kolv_in2*1.5+(100-kolv_in2)*1.2) * ypred[:13, 4], label="Прогноз общего количества рабочих для тепломонтажных работ 1 год Б2")
    # plt.plot(X["Месяц строительства "][12:], (kolv_in5*1.5+(100-kolv_in5)*1.2) * ypred[12:, 4], label="Прогноз общего количества рабочих для тепломонтажных работ 2 год Б2")
    # plt.plot(X["Месяц строительства "][:13], (kolv_in3*1.5+(100-kolv_in3)*1.2) * ypred[:13, 5], label="Прогноз общего количества рабочих для электромонтажных работ 1 год Б2")
    # plt.plot(X["Месяц строительства "][12:], (kolv_in6*1.5+(100-kolv_in6)*1.2) * ypred[12:, 5], label="Прогноз общего количества рабочих для электромонтажных работ 2 год Б2")
#_________________________Количество рабочих по странам от этапов 1 блок____________________________________________
    # plt.plot(X["Месяц строительства "][:13], kolv_in1 * 1.5 * ypred[:13, 0],
    #          label="Кол-во иностранцев 1 1 Б1")
    # plt.plot(X["Месяц строительства "][:13], kolv_in2 * 1.5 * ypred[:13, 1],
    #          label="Кол-во иностранцев 2 1 Б1")
    # plt.plot(X["Месяц строительства "][:13], kolv_in3 * 1.5 * ypred[:13, 2],
    #          label="Кол-во иностранцев 3 1 Б1")
    # #________________________________________________________________\/
    # plt.plot(X["Месяц строительства "][12:], kolv_in4*1.5 * ypred[12:, 0],
    #          label="Кол-во иностранцев 1 2 Б1")
    # plt.plot(X["Месяц строительства "][12:], kolv_in5*1.5 * ypred[12:, 1],
    #          label="Кол-во иностранцев 2 2 Б1")
    # plt.plot(X["Месяц строительства "][12:], kolv_in6*1.5 * ypred[12:, 2],
    #          label="Кол-во иностранцев 3 2 Б1")
    # #____________________________________________________________________
    # plt.plot(X["Месяц строительства "][:13], (1-kolv_in1)*1.2 * ypred[:13, 0],
    #          label="Кол-во местных 1 1 Б1")

    # plt.plot(X["Месяц строительства "][:13], (100-kolv_in2)*1.2 * ypred[:13, 1],
    #          label="Кол-во местных 2 1 Б1")
    # plt.plot(X["Месяц строительства "][:13], (100-kolv_in3)*1.2 * ypred[:13, 2],
    #          label="Кол-во местных 3 1 Б1")
    # #__________________________________________________________________
    # plt.plot(X["Месяц строительства "][12:], (100-kolv_in4)*1.2 * ypred[12:, 0],
    #          label="Кол-во местных 1 2 Б1")
    # plt.plot(X["Месяц строительства "][12:], (100-kolv_in5)*1.2 * ypred[12:, 1],
    #          label="Кол-во местных 2 2 Б1")
    # plt.plot(X["Месяц строительства "][12:], (100-kolv_in6)*1.2 * ypred[12:, 2],
    #          label="Кол-во местных 3 2 Б1")

    #

    # # _________________________Количество рабочих по странам от этапов 2 блок____________________________________________
    # plt.plot(X["Месяц строительства "][:13], kolv_in1*1.5 * ypred[:13, 3],
    #          label="Кол-во иностранцев 1 1 Б2")
    # plt.plot(X["Месяц строительства "][:13], kolv_in2*1.5 * ypred[:13, 4],
    #          label="Кол-во иностранцев 2 1 Б2")
    # plt.plot(X["Месяц строительства "][:13], kolv_in3*1.5 * ypred[:13, 5],
    #          label="Кол-во иностранцев 3 1 Б2")
    # # # ________________________________________________________________\/
    # plt.plot(X["Месяц строительства "][12:], kolv_in4*1.5 * ypred[12:, 3],
    #          label="Кол-во иностранцев 1 2 Б2")
    # plt.plot(X["Месяц строительства "][12:], kolv_in5*1.5 * ypred[12:, 4],
    #          label="Кол-во иностранцев 2 2 Б2")
    # plt.plot(X["Месяц строительства "][12:], kolv_in6*1.5 * ypred[12:, 5],
    #          label="Кол-во иностранцев 3 2 Б2")
    #
    # # # ____________________________________________________________________
    # plt.plot(X["Месяц строительства "][:13], (100-kolv_in1)*1.2 * ypred[:13, 3],
    #          label="Кол-во местных 1 1 Б2")
    # plt.plot(X["Месяц строительства "][:13], (100-kolv_in2)*1.2 * ypred[:13, 4],
    #          label="Кол-во местных 2 1 Б2")
    # plt.plot(X["Месяц строительства "][:13], (100-kolv_in3)*1.2 * ypred[:13, 5],
    #          label="Кол-во местных 3 1 Б2")
    # # __________________________________________________________________
    # plt.plot(X["Месяц строительства "][12:], (100-kolv_in4)*1.2 * ypred[12:, 3],
    #          label="Кол-во местных 1 2 Б2")
    # plt.plot(X["Месяц строительства "][12:], (100-kolv_in5)*1.2 * ypred[12:, 4],
    #          label="Кол-во местных 2 2 Б2")
    # plt.plot(X["Месяц строительства "][12:], (100-kolv_in6)*1.2 * ypred[12:, 5],
    #          label="Кол-во местных 3 2 Б2")
    #

    # #_________________Kol-vo sobesedovaniy___________________________________________________
    plt.plot(X["Месяц строительства "][:13], 10*kolv_in1 * 1.5 * ypred[:13, 0],
             label="Кол-во иностранцев 1 1 Б1")
    plt.plot(X["Месяц строительства "][:13], 10*kolv_in2 * 1.5 * ypred[:13, 1],
             label="Кол-во иностранцев 2 1 Б1")
    plt.plot(X["Месяц строительства "][:13], 10*kolv_in3 * 1.5 * ypred[:13, 2],
             label="Кол-во иностранцев 3 1 Б1")
    # # ________________________________________________________________\/
    # plt.plot(X["Месяц строительства "][12:], 10*kolv_in4 * 1.5 * ypred[12:, 0],
    #          label="Кол-во иностранцев 1 2 Б1")
    # plt.plot(X["Месяц строительства "][12:], 10*kolv_in5 * 1.5 * ypred[12:, 1],
    #          label="Кол-во иностранцев 2 2 Б1")
    # plt.plot(X["Месяц строительства "][12:], 10*kolv_in6 * 1.5 * ypred[12:, 2],
    #          label="Кол-во иностранцев 3 2 Б1")
    # # ____________________________________________________________________
    # plt.plot(X["Месяц строительства "][:13], random.randint(15, 20) *(100 - kolv_in1) * 1.2 * ypred[:13, 0],
    #          label="Кол-во местных 1 1 Б1")
    # plt.plot(X["Месяц строительства "][:13], random.randint(15, 20) *(100 - kolv_in2) * 1.2 * ypred[:13, 1],
    #          label="Кол-во местных 2 1 Б1")
    # plt.plot(X["Месяц строительства "][:13], random.randint(15, 20) *(100 - kolv_in3) * 1.2 * ypred[:13, 2],
    #          label="Кол-во местных 3 1 Б1")
    # # __________________________________________________________________
    # plt.plot(X["Месяц строительства "][12:], random.randint(15, 20) *(100 - kolv_in4) * 1.2 * ypred[12:, 0],
    #          label="Кол-во местных 1 2 Б1")
    # plt.plot(X["Месяц строительства "][12:], random.randint(15, 20) *(100 - kolv_in5) * 1.2 * ypred[12:, 1],
    #          label="Кол-во местных 2 2 Б1")
    # plt.plot(X["Месяц строительства "][12:], random.randint(15, 20) *(100 - kolv_in6) * 1.2 * ypred[12:, 2],
    #          label="Кол-во местных 3 2 Б1")
    #
    # #__________________________________BLOCK2________________________________________
    # plt.plot(X["Месяц строительства "][:13], 10*kolv_in1 * 1.5 * ypred[:13, 3],
    #          label="Кол-во иностранцев 1 1 Б2")
    # plt.plot(X["Месяц строительства "][:13], 10*kolv_in2 * 1.5 * ypred[:13, 4],
    #          label="Кол-во иностранцев 2 1 Б2")
    # plt.plot(X["Месяц строительства "][:13], 10*kolv_in3 * 1.5 * ypred[:13, 5],
    #          label="Кол-во иностранцев 3 1 Б2")
    # # # ________________________________________________________________\/
    # plt.plot(X["Месяц строительства "][12:], 10*kolv_in4 * 1.5 * ypred[12:, 3],
    #          label="Кол-во иностранцев 1 2 Б2")
    # plt.plot(X["Месяц строительства "][12:], 10*kolv_in5 * 1.5 * ypred[12:, 4],
    #          label="Кол-во иностранцев 2 2 Б2")
    # plt.plot(X["Месяц строительства "][12:], 10*kolv_in6 * 1.5 * ypred[12:, 5],
    #          label="Кол-во иностранцев 3 2 Б2")
    #
    # # # ____________________________________________________________________
    # plt.plot(X["Месяц строительства "][:13], random.randint(15, 20) *(100 - kolv_in1) * 1.2 * ypred[:13, 3],
    #          label="Кол-во местных 1 1 Б2")
    # plt.plot(X["Месяц строительства "][:13], random.randint(15, 20) *(100 - kolv_in2) * 1.2 * ypred[:13, 4],
    #          label="Кол-во местных 2 1 Б2")
    # plt.plot(X["Месяц строительства "][:13], random.randint(15, 20) *(100 - kolv_in3) * 1.2 * ypred[:13, 5],
    #          label="Кол-во местных 3 1 Б2")
    # # __________________________________________________________________
    # plt.plot(X["Месяц строительства "][12:], random.randint(15, 20) *(100 - kolv_in4) * 1.2 * ypred[12:, 3],
    #          label="Кол-во местных 1 2 Б2")
    # plt.plot(X["Месяц строительства "][12:], random.randint(15, 20) *(100 - kolv_in5) * 1.2 * ypred[12:, 4],
    #          label="Кол-во местных 2 2 Б2")
    # plt.plot(X["Месяц строительства "][12:], random.randint(15, 20) *(100 - kolv_in6) * 1.2 * ypred[12:, 5],
    #          label="Кол-во местных 3 2 Б2")



    plt.xlabel('Длительность стройки (мес.)')
    plt.ylabel('Количество рабочих (чел.)')
    #plt.legend(loc="upper right")

    plt.figtext(0.5, 0.95, f"Дата начала стройки: {month}.{year}", ha='center', va='bottom')
    plt.show()
    # ________________________________________________________________________________________________


root = tk.Tk()
root.title("Ввод дат")

label1 = ttk.Label(root, text="Введите месяц:")
label1.grid(column=0, row=0)
entry1 = ttk.Entry(root)
entry1.grid(column=1, row=0)

label2 = ttk.Label(root, text="Введите год:")
label2.grid(column=0, row=1)
entry2 = ttk.Entry(root)
entry2.grid(column=1, row=1)

label3 = ttk.Label(root, text="Введите количество иностранцев общ 1 год:")
label3.grid(column=0, row=2)
entry3 = ttk.Entry(root)
entry3.grid(column=1, row=2)

label4 = ttk.Label(root, text="Введите количество иностранцев тепл 1 год:")
label4.grid(column=0, row=3)
entry4 = ttk.Entry(root)
entry4.grid(column=1, row=3)

label5 = ttk.Label(root, text="Введите количество иностранцев элек 1 год:")
label5.grid(column=0, row=4)
entry5 = ttk.Entry(root)
entry5.grid(column=1, row=4)

label6 = ttk.Label(root, text="Введите количество иностранцев общ 2 год:")
label6.grid(column=0, row=5)
entry6 = ttk.Entry(root)
entry6.grid(column=1, row=5)

label7 = ttk.Label(root, text="Введите количество иностранцев тепл 2 год:")
label7.grid(column=0, row=6)
entry7 = ttk.Entry(root)
entry7.grid(column=1, row=6)

label8 = ttk.Label(root, text="Введите количество иностранцев элек 2 год:")
label8.grid(column=0, row=7)
entry8 = ttk.Entry(root)
entry8.grid(column=1, row=7)

submit_button = ttk.Button(root, text="Отправить", command=submit_dates)
submit_button.grid(column=1, row=8)

root.mainloop()
