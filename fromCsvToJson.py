# -*- coding: utf-8 -*-
# python v = 2.7
# author: Pavel Lukyanov
import csv
import json


def main():
    '''
    открытие всего, парсинг, заполнение, возврат заполненного Json
    '''
    def getJsonParam(name, data, comandsList):
        '''
        заполнение словаря для json
        :args name -> list; users
              data -> dict; команды
              comandList -> list; список на выход для Json
        :return comandList -> list
        '''
        if isinstance(name, list):
            # для того, чтобы убрать повторы ключей, когда они в разном порядке
            paramList = {'param': sorted(name)}
        else:
            paramList = {'param': name}
        paramList.update(data)
        if paramList not in comandsList:
            paramList.update(data)
            comandsList.append(paramList)
            return comandsList

    def checkData(data, file1, file2, names, comandsList, i, namesToUse):
        '''
        проверка данных на повтор для разных user
        :args data -> dict; словарь для проверки
              file1 -> list; данные с файла
              file2 -> list; данные с файла
              names -> list; для getJsonParam
              comandList -> list; для getJsonParam
              i -> int; номер юзера
              namesToUse -> list; список доп юзеров
        :return list
        '''
        if data in file1 and data in file2:
            return getJsonParam(names, data, comandsList)
        elif data not in file1 and data not in file2:
            return getJsonParam(names[i], data, comandsList)
        elif data not in file1 and data in file2:
            namesL = [names[i], namesToUse[1]]
            return getJsonParam(namesL, data, comandsList)
        elif data in file1 and data not in file2:
            namesL = [names[i], namesToUse[0]]
            return getJsonParam(namesL, data, comandsList)
    try:
        fileUser1 = open('user1.csv', 'r')
        fileUser2 = open('user2.csv', 'r')
        fileUser3 = open('user3.csv', 'r')
        jsonFile = open('file.json', 'w')
        readerUser1 = csv.DictReader(fileUser1, delimiter=';')
        readerUser2 = csv.DictReader(fileUser2, delimiter=';')
        readerUser3 = csv.DictReader(fileUser3, delimiter=';')
        user1 = []
        user2 = []
        user3 = []
        names = [{'user': fileUser1.name.split(
            '.')[0]}, {'user': fileUser2.name.split('.')[0]}, {'user': fileUser3.name.split('.')[0]}]
        for row in readerUser1:
            user1.append(row)
        for row in readerUser2:
            user2.append(row)
        for row in readerUser3:
            user3.append(row)
        comandsList = []
        for data in user2:
            checkData(data, user1, user3, names,
                    comandsList, 1, [names[0], names[2]])
        for data in user1:
            checkData(data, user2, user3, names,
                    comandsList, 0, [names[1], names[2]])
        for data in user3:
            checkData(data, user1, user2, names,
                    comandsList, 2, [names[0], names[1]])
        dictOut = {'commands': comandsList}
        json.dump(dictOut, jsonFile, indent=4)
    finally:
        fileUser1.close()
        fileUser2.close()
        fileUser3.close()
        jsonFile.close()

if __name__ == '__main__':
    main()
