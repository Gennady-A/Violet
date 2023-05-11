# Импорт необходимых библиотек.
import sys
import pandas as pd 
import matplotlib.pyplot as plt
import sqlite3
import os.path
import datetime
import stegano
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

# Визуал.
from Violet import Ui_MainWindow
from Help import Ui_HelpWindow
from Db_El import Ui_TextElementWidget
from Db import Ui_DbWindow

# Класс-шифратор.
from cypher import cryptographer


# Класс главного окна.
class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Связываем кнопки с функциями.
        self.ui.Encryption_btn.clicked.connect(self.encryption)
        self.ui.Decryption_btn.clicked.connect(self.decryption)
        self.ui.Break_btn.clicked.connect(self.breaking)
        self.ui.Add_btn.clicked.connect(self.add_key)
        self.ui.Del_btn.clicked.connect(self.del_key)
        self.ui.Take_btn.clicked.connect(self.take_key)
        self.ui.Histogram_btn.clicked.connect(self.get_histogram)
        self.ui.Help_btn.clicked.connect(self.show_info)
        self.ui.Save_btn.clicked.connect(self.save_text)
        self.ui.Bd_btn.clicked.connect(self.show_db)
        self.ui.FontSize_Value_sBox.valueChanged.connect(self.change_fontSize)
        self.ui.GetFromFile_btn.clicked.connect(self.choose_inputFile)
        self.ui.SetInFile_btn.clicked.connect(self.choose_outputFile)
        self.ui.Choose_img_btn.clicked.connect(self.choose_img)
        self.ui.Encription_to_file_btn.clicked.connect(self.encryption_to_img)
        self.ui.pushButton.clicked.connect(self.decryption_from_img)

        # Привязываем запуск функции к закрытию программы.
        app.aboutToQuit.connect(self.save_last_keys)

        # Выполняем функцию при запуске программы.
        self.load_keys()

    # Создаём экземпляр класса-шифратора.
    textToEncrypt = cryptographer()

    # Функция шифровки.
    def encryption(self):
        if len(str(self.ui.textEdit.toPlainText())) > 0:

            # Получаем метод и ключ.
            method = str(self.ui.Method_cBox.currentText())
            key = str(self.ui.Key_now_lEdit.text())

            # Устанавливаем текст в класс-шифратор, дальше с текстом будем работать через него.
            self.textToEncrypt.set_text(str(self.ui.textEdit.toPlainText()))
            
            # Определяем выбранный метод и действуем в соответсвии с ним. 
            # Взависимости от метода к ключу предъявляются разные тербования, 
            # из-за чего валидация ключа происходит при определении метода, а не 
            # перед этим.
            match method:
                case 'Одноалфавитный метод':
                    if key and key.isdigit() and key[0] != '0' and int(key) < self.textToEncrypt.maxChar :
                        self.textToEncrypt.encryption_text(method, key)
                        self.ui.Status_lab.setText('')
                    elif key == '':
                        self.ui.Status_lab.setText(f'Ошибка шифровки. Ключ не должен быть пустым.')
                    else:
                        self.ui.Status_lab.setText(f'Ошибка шифровки. Ключ должен быть числом не больше {self.textToEncrypt.maxChar-1}.')
                    
                case 'Перестановка символов':
                    valid_key = True
                    for i in key:
                        if int(i) > len(key):
                            valid_key = False
                            break 
                    if key and len(set(key)) == len(key) and key.isdigit() and len(key) > 1 and valid_key:
                        self.textToEncrypt.encryption_text(method, key)
                        self.ui.Status_lab.setText('')
                    elif len(key) < 2:
                        self.ui.Status_lab.setText('Ошибка шифровки. Длина ключа должна быть больше единицы.')
                    else:
                        self.ui.Status_lab.setText('Ошибка шифровки. Ключ должен состоять из разных символов, не превышающих по значению длинну ключа.')
                    
                case 'Инверсный метод':
                    if self.textToEncrypt.encryption_text(method, key):
                        self.ui.Status_lab.setText('')
                    else:
                        self.ui.Status_lab.setText('Ошибка шифровки. Проверьте введённого текста. Возможно, не все его символы поддерживаются программой.')

                case 'Гаммирование':
                    if key and key.isdigit() and len(key) >= 1:
                        self.textToEncrypt.encryption_text(method, key)
                        self.ui.Status_lab.setText('')
                    else:
                        self.ui.Status_lab.setText('Ошибка шифровки. Длина ключа должна быть больше или равна единице.') 

            self.ui.textEdit.setText(MainWindow.textToEncrypt.get_text())
        else: 
            self.ui.Status_lab.setText('Введите текст.')

    # Функция расшифровки.
    def decryption(self):
        if len(str(self.ui.textEdit.toPlainText())) > 0:
            
            # Получаем метод и ключ.
            method = self.ui.Method_cBox.currentText()
            key = self.ui.Key_now_lEdit.text()

            # Устанавливаем текст в класс-шифратор, дальше с текстом будем работать через него.
            self.textToEncrypt.set_text(self.ui.textEdit.toPlainText())

            # Определяем выбранный метод и действуем в соответсвии с ним. 
            # Взависимости от метода к ключу предъявляются разные тербования, 
            # из-за чего валидация ключа происходит при определении метода, а не 
            # перед этим.
            match method:
                case 'Одноалфавитный метод':
                    if key and key.isdigit() and int(key) < self.textToEncrypt.maxChar:
                        self.textToEncrypt.decryption_text(method, key)
                        self.ui.Status_lab.setText('')
                    elif key == '':
                        self.ui.Status_lab.setText(f'Ошибка расшифровки. Ключ не должен быть пустым.')
                    else:
                        self.ui.Status_lab.setText(f'Ошибка расшифровки. Ключ должен быть числом не больше {self.textToEncrypt.maxChar-1}.')
                    
                case 'Перестановка символов':
                    valid_key = True
                    for i in key:
                        if int(i) > len(key):
                            valid_key = False
                            break 
                    if key and len(set(key)) == len(key) and key.isdigit() and len(key) > 1 and valid_key:
                        self.textToEncrypt.decryption_text(method, key)
                        self.ui.Status_lab.setText('')
                    elif len(key) < 2:
                        self.ui.Status_lab.setText('Ошибка расшифровки. Длина ключа должна быть больше единицы.')
                    else:
                        self.ui.Status_lab.setText('Ошибка расшифровки. Ключ должен состоять из разных символов, не превышающих по значению длинну ключа.')
                    
                case 'Инверсный метод':
                    if self.textToEncrypt.decryption_text(method, key):
                        self.ui.Status_lab.setText('')
                    else:
                        self.ui.Status_lab.setText('Ошибка расшифровки. Проверьте введённого текста. Возможно, не все его символы поддерживаются программой.')

                case 'Гаммирование':
                    if key and key.isdigit() and len(key) >= 1:
                        self.textToEncrypt.decryption_text(method, key)
                        self.ui.Status_lab.setText('')
                    else:
                        self.ui.Status_lab.setText('Ошибка расшифровки. Длина ключа должна быть больше или равна единице.') 

            self.ui.textEdit.setText(self.textToEncrypt.get_text())

        else: 
            self.ui.Status_lab.setText('Введите текст.')
    
    # Функция взлома.
    def breaking(self):

        # Получаем необходимые для взлома параметры из полей.
        word = str(self.ui.Search_word_lEdit.text())
        keyPower = int(self.ui.Key_power_sBox.value())
        method = str(self.ui.Method_cBox.currentText())

        # Устанавливаем текст в класс-шифратор, дальше с текстом будем работать через него.
        self.textToEncrypt.set_text(self.ui.textEdit.toPlainText())

        if word and word != '':
            if len(word) <= len(self.textToEncrypt.get_text()):
                match method:
                    case 'Одноалфавитный метод':
                        keys = self.textToEncrypt.break_text(method, word)
                        if len(keys) > 0:
                            self.ui.Keys_lWidget.addItem('Подбор...')
                            for key in keys:
                                self.ui.Keys_lWidget.addItem(key)
                        
                    case 'Перестановка символов':
                        if keyPower <= 15:
                            if keyPower == 0:
                                self.ui.Status_lab.setText('Сила ключа не может быть равна нулю.')
                            else:
                                keys = self.textToEncrypt.break_text(method, word, keyPower)
                                if len(keys) > 0:
                                    self.ui.Keys_lWidget.addItem('Подбор...')
                                for key in keys:
                                    self.ui.Keys_lWidget.addItem(key)
                        else:
                            self.ui.Status_lab.setText('Слишком сильный ключ для этого метода.')
                     
                    case 'Инверсный метод':
                        self.ui.Status_lab.setText('Для этого типа шифра не требуется взлом, так как суть шифра в простом инвертировании символов.')

                    case 'Гаммирование':
                        if keyPower <= 6:
                            if keyPower == 0:
                                self.ui.Status_lab.setText('Сила ключа не может быть равна нулю.')
                            else:
                                keys = self.textToEncrypt.break_text(method, word, keyPower)
                                if len(keys) > 0:
                                    self.ui.Keys_lWidget.addItem('Подбор...')
                                for key in keys:
                                    self.ui.Keys_lWidget.addItem(key)
                        else:
                            self.ui.Status_lab.setText('Слишком сильный ключ для этого метода.')
            else:
                self.ui.Status_lab.setText('Искомое слово длиннее самого текста.')
        else:
            self.ui.Status_lab.setText('Введите искомое слово.')
  

    # Функция добавления ключа в список ключей.
    def add_key(self):
        key = self.ui.Key_now_lEdit.text()
        if key != '' and key.isdigit():
            self.ui.Keys_lWidget.addItem(key)

    # Функция удаления ключа из списка ключей.
    def del_key(self):
        if self.ui.Keys_lWidget.currentItem():
            self.ui.Keys_lWidget.takeItem(int(self.ui.Keys_lWidget.currentRow()))

    # Функция получения ключа из списка ключей.
    def take_key(self):
        if self.ui.Keys_lWidget.currentItem():
            self.ui.Key_now_lEdit.setText(self.ui.Keys_lWidget.currentItem().text())

    # Функция вывода гистограммы.
    def get_histogram(self):
        if len(self.ui.textEdit.toPlainText()) > 0:
            # После получения текста конвертируем его в Series, а затем выводим
            # через matplotlib.
            self.textToEncrypt.set_text(self.ui.textEdit.toPlainText())
            distribution = self.textToEncrypt.text_analysis()
            info = pd.Series(data = distribution, index = distribution.keys())
            info = info.sort_values(ascending = False)
            info.plot(kind="bar")
            plt.show()
        else: 
            # Если текст пуст - просим пользователя ввести текст.
            self.ui.Status_lab.setText('Введите текст.')

    # Функция вывода справки.
    def show_info(self):
        infoW = Help(self)
        infoW.show()

    # Функция сохранения текста в базу данных.
    def save_text(self):
        # Устанавливаем текст в наш шифратор.
        self.textToEncrypt.set_text(str(self.ui.textEdit.toPlainText()))
        # Если текст не пуст и его длинна не больше нуля - подключаемся к бд(Если бд есть) и сохраняем текст.
        if self.textToEncrypt.get_text() and len(self.textToEncrypt.get_text()) > 0:
            if os.path.exists("db\\texts.db"):
                try:
                    sqliteConnection = sqlite3.connect("db\\texts.db")
                    cur = sqliteConnection.cursor()
                    sqlReq = f"INSERT INTO Texts (text, key, date) VALUES ('{self.textToEncrypt.get_text()}', '{self.textToEncrypt.get_key()}', '{str(datetime.datetime.now())}')"
                    cur.execute(sqlReq)
                    sqliteConnection.commit()
                    cur.close()
                    sqliteConnection.close()
                except:
                    self.ui.Status_lab.setText('Непредвиденная ошибка. Возможно, есть неподдерживаемые символы.')
            else:
                self.ui.Status_lab.setText('База данных не найдена.')
        else:
            self.ui.Status_lab.setText('Нечего сохранять.')

    # Функция вывода окна базы данных.
    def show_db(self):
        dbW = DbWindow(self)
        dbW.show()

    # Функция изменения размера шрифта.
    def change_fontSize(self):
        # При изменении размера шрифта меняются только символы, которые будут введены дальше, 
        # а прежние символы остаются прежними. Чтобы это исправить мы перезаписываем текст 
        # по-новой. Получаем текст, стираем его из поля, изменяем размер шрифта и записываем 
        # текст снова.  
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit.setText('')
        self.ui.textEdit.setFontPointSize(self.ui.FontSize_Value_sBox.value())
        self.ui.textEdit.setText(text)

    # Функция сохранения списка ключей. Привязана к событию закрытия приложения.
    def save_last_keys(self):
        # Если база данных найдена, то при сохранении ключей мы сначала 
        # удаляем все прежние, а потом добавляем нынешние.
        if os.path.exists('db\\texts.db'):
            sqliteConnection = sqlite3.connect('db\\texts.db')
            cur = sqliteConnection.cursor()
            sqlReq = "DELETE FROM Keys"
            cur.execute(sqlReq)
            sqliteConnection.commit()
            count = self.ui.Keys_lWidget.count()
            for i in range(count):
                itemText = self.ui.Keys_lWidget.item(i).text()
                sqlReq = f"INSERT INTO Keys (key) VALUES ('{itemText}')"
                cur.execute(sqlReq)
                sqliteConnection.commit()
            cur.close()
            sqliteConnection.close()

    # Функция загрузки списка ключей. Привязана к событию запуска приложения.
    def load_keys(self):
        if os.path.exists('db\\texts.db'):
            sqliteConnection = sqlite3.connect('db\\texts.db')
            cur = sqliteConnection.cursor()
            count = self.ui.Keys_lWidget.count()
            sqlReq = f"SELECT * FROM Keys"
            keys = cur.execute(sqlReq).fetchall()
            for key in keys:
                self.ui.Keys_lWidget.addItem(key[1])
            cur.close()
            sqliteConnection.close()

    # Функция для выбора загружаемого текстового файла.
    def choose_inputFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","Текстовые файлы (*.txt);;Все файлы (*)", options=options)
        if file:
            if os.path.exists(file):
                with open(file, 'r', encoding='utf-8') as f:
                    self.ui.textEdit.setText(f.read())

    # Функция для выбора выгружаемого текстового файла.
    def choose_outputFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Текстовые файлы (*.txt);;Все файлы (*)", options=options)
        if file:
            if os.path.exists(file):
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(self.ui.textEdit.toPlainText())

    # Функция для выбора целевого изображения.
    def choose_img(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Png (*.png);;Jpg (*.jpg);;Jpeg (*.jpeg)", options=options)
        if file:
            if os.path.exists(file):
                self.ui.Img_adres_lab.setText(file)

    # Функция шифровки текста в изображение.
    def encryption_to_img(self):
        file = self.ui.Img_adres_lab.text()
        if os.path.exists(file):
            format = file.split('.')[-1]
            message = self.ui.textEdit.toPlainText()
            if len(message) > 0:
                if os.path.exists('imgs'):
                    imgsList = os.listdir('imgs')
                    i = 0
                    while f'{i}.{format}' in imgsList:
                        i += 1
                        if i > 1000:
                            self.ui.Status_lab.setText('Почисти папку с картинками.')
                            break
                    if self.ui.Status_lab.text() == 'Почисти папку с картинками.':
                        pass
                    else:
                        if len(message) <= 100:
                            secret = stegano.lsb.hide(file, message)
                            secret.save(f'imgs\\{i}.{format}')
                        else:
                            self.ui.Status_lab.setText('Сообщение слишком длинное для записи в изображение.')
            else:
                self.ui.Status_lab.setText('Сообщение пустое.')

    # Функция для расшифровки текста из изображения.
    def decryption_from_img(self):
        file = self.ui.Img_adres_lab.text()
        if os.path.exists(file):
            try:
                message = stegano.lsb.reveal(file)
                self.ui.textEdit.setText(message)
            except:
                self.ui.Status_lab.setText('Сообщение не обнаружено.')


# Класс окна справки.
class Help(QMainWindow):
    def __init__(self, parent=None):
        super(Help, self).__init__(parent)
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self)


# Класс окна базы данных.
class DbWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DbWindow, self).__init__(parent)
        self.ui = Ui_DbWindow()
        self.ui.setupUi(self)

        # Привязываем функции.
        self.ui.Db_Update_btn.clicked.connect(self.updateDb)

    # Функция для запроса к базе данных.
    def updateDb(self):

        # Прежде чем загрузить записи из базы данных, нужно очистить список.
        for i in range(self.ui.Db_Elems_vLayout.count()):
            widget = self.ui.Db_Elems_vLayout.itemAt(0).widget()
            self.ui.Db_Elems_vLayout.removeWidget(widget)

        # Если бд существует, то обратимся к ней и получим записи.
        if os.path.exists('db\\texts.db'):
            sqliteConnection = sqlite3.connect("db\\texts.db")
            cur = sqliteConnection.cursor()
            sqlReq = f"SELECT * FROM Texts"
            cur.execute(sqlReq)
            res = cur.fetchall()
            sqliteConnection.commit()
            cur.close()
            sqliteConnection.close()

            # Проходимся в цикле по полученным элементам, устанавливаем виджеты и наполняем их соответствующей информацией.
            for el in res:
                dataList = list(el)
                index = str(dataList[0])
                text = dataList[1]
                key = dataList[2]
                date = dataList[3]
                newEl = DbElement('Element', text, key, date, self)
                self.ui.Db_Elems_vLayout.addWidget(newEl)

# Класс виджета элемента базы данных.
class DbElement(QWidget):
    def __init__(self, index='', text='', key='', date='', parent=None):
        super(DbElement, self).__init__(parent)
        self.ui = Ui_TextElementWidget()
        self.ui.setupUi(self)
        # При создании виджета получаем данные и разделяем их.
        time = (date.split(' ')[1])
        date = date.split(' ')[0]
        
        # Заполняем виджет
        self.ui.Db_Element_gBox.setTitle(date)
        self.ui.El_Text_tEdit.setText(text)
        self.ui.El_Key_lEdit.setText(key)
        self.ui.El_Date_lEdit.setText(time)

        # Привязываем функции.
        self.ui.pushButton.clicked.connect(self.del_el_from_db)

    # Функция удаления виджета и соответствующей записи из бд.
    def del_el_from_db(self):
        index = self.ui.Db_Element_gBox.title()
        date = f'{self.ui.Db_Element_gBox.title()} {self.ui.El_Date_lEdit.text()}'
        sqliteConnection = sqlite3.connect("db\\texts.db")
        cur = sqliteConnection.cursor()
        sqlReq = f"DELETE FROM Texts WHERE date = '{date}'"
        cur.execute(sqlReq)
        res = cur.fetchall()
        sqliteConnection.commit()
        cur.close()
        sqliteConnection.close()
        self.deleteLater()

# Если запускается как файл, а не как модуль - запускаем приложение.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())