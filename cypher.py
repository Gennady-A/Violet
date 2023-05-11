import itertools


class cryptographer:
    def __init__(self):
        self.text = False
        self.key = False
        self.len = 0
        self.maxChar = 2048

    # Функция установки текста.
    def set_text(self, text):
        if text != self.text:
            self.key = False
            self.text = text
            self.len = len(text)

    # Функция получения текста.
    def get_text(self):
        return self.text
    
    # Функция установки ключа.
    def set_key(self, key):
        self.key = key
    
    # Функция получения ключа.
    def get_key(self):
        return self.key

    # Функция шифровки.
    def encryption_text(self, method, key = False):
        new_text = ''
        match method:
            # Суть метода в увеличении кода каждого символа на фиксированное значение.
            case 'Одноалфавитный метод':
                for c in self.text:
                    new_text += chr((ord(c) + int(key)) % self.maxChar)
                self.text = new_text
                self.key = key
                return self.text 
            

            # Суть метода в проходе по "секторам" текста длинной в 
            # длинну ключа и перестановке символов в соответствии с ключём. 
            # Пример: 
            # абв -> 312 = ваб 
            # абв -> 321 = вба 
            # абвгде -> 321 = вбаедг: абв(123) -> вба(321) + где(123) -> едг(321) = вбаедг(321321)
            case 'Перестановка символов':
                segments = self.len // len(key)
                segment_number = 0
                while (segment_number + 1) * len(key) < self.len:
                    segment = self.text[(segment_number) * len(key): len(key) * (segment_number + 1)]
                    new_segment = ['-' for i in range(len(segment))]
                    for i in range(len(key)):
                        new_segment[i] = segment[int(key[i])-1]
                    new_segment = ''.join(new_segment)
                    new_text += new_segment
                    segment_number += 1
                if len(self.text[(segment_number * len(key)):]) == len(key):
                    segment = self.text[(segment_number)*len(key):]
                    new_segment = ['-' for i in range(len(segment))]
                    for i in range(len(key)):
                        new_segment[i] = segment[int(key[i])-1]
                    new_segment = ''.join(new_segment)
                    new_text += new_segment
                else:
                    new_text += self.text[(segment_number)*len(key):]
                self.text = new_text
                self.key = key
                return self.text 
                        
            # Суть метода в инверсии каждого символа - 
            # смене символа на противоположный в заданном диапазоне.
            case 'Инверсный метод':
                for c in self.text:
                    if ord(c) > self.maxChar - 1:
                        return False
                    new_text += chr(self.maxChar - 1 - ord(c))
                self.text = new_text
                self.key = False
                return self.text 

            # Один из многоалфавитных шифров. 
            # Суть таже, что и в одноалфавитном, 
            # но применяется не одинаковое смещение 
            # для каждого символа, а гамма.
            case 'Гаммирование':
                gamma = key * (self.len // len(key) + 2)
                for i in range(len(self.text)):
                    new_text += chr(ord(self.text[i]) + int(gamma[i]))
                self.text = new_text
                self.key = key
                return self.text
            
            # Отлавливаем все неподходящие значения.
            case _:
                return False

    # Функция дешифровки.
    def decryption_text(self, method, key = False):
        new_text = ''
        match method:
            # Суть метода в увеличении кода каждого символа на фиксированное значение.
            case 'Одноалфавитный метод':
                for c in self.text:
                    new_char_code = (ord(c) - int(key)) 
                    if new_char_code < 0:
                        new_char_code = self.maxChar + new_char_code
                    new_text += chr(new_char_code)
                self.text = new_text
                self.key = False
                return self.text 
            
            # Суть метода в проходе по "секторам" текста длинной в 
            # длинну ключа и перестановке символов в соответствии с ключём. 
            # Пример: 
            # абв -> 312 = ваб 
            # абв -> 321 = вба 
            # абвгде -> 321 = вбаедг: абв(123) -> вба(321) + где(123) -> едг(321) = вбаедг(321321)    
            case 'Перестановка символов':
                segments = self.len // len(key)
                segment_number = 0
                while (segment_number + 1) * len(key) < self.len:
                    segment = self.text[(segment_number) * len(key): len(key) * (segment_number + 1)]
                    new_segment = ['-' for i in range(len(segment))]
                    for i in range(len(key)):
                        new_segment[int(key[i])-1] = segment[i]
                    new_segment = ''.join(new_segment)
                    new_text += new_segment
                    segment_number += 1
                if len(self.text[(segment_number * len(key)):]) == len(key):
                    segment = self.text[(segment_number)*len(key):]
                    new_segment = ['-' for i in range(len(segment))]
                    for i in range(len(key)):
                        new_segment[int(key[i])-1] = segment[i]
                    new_segment = ''.join(new_segment)
                    new_text += new_segment
                else:
                    new_text += self.text[(segment_number)*len(key):]
                self.text = new_text
                self.key = False
                return self.text 
                
            # Суть метода в инверсии каждого символа - 
            # смене символа на противоположный в заданном диапазоне.
            case 'Инверсный метод':
                for c in self.text:
                    if ord(c) > self.maxChar - 1:
                        return False
                    new_text += chr(self.maxChar - 1 - ord(c))
                self.text = new_text
                self.key = False
                return self.text

            # Один из многоалфавитных шифров. 
            # Суть таже, что и в одноалфавитном, 
            # но применяется не одинаковое смещение 
            # для каждого символа, а гамма.
            case 'Гаммирование':
                gamma = key * (self.len // len(key) + 2)
                for i in range(len(self.text)):
                    new_text += chr(ord(self.text[i]) - int(gamma[i]))
                self.text = new_text
                self.key = False
                return self.text
            
    # Функция подбора ключа.
    def break_text(self, method, word, key_power = False):
        search_keys = []
        match method:
            # Суть метода в увеличении кода каждого символа на фиксированное значение.
            case 'Одноалфавитный метод':
                for i in range(self.maxChar):
                    new_text = ''
                    for c in self.text:
                        if ord(c) > self.maxChar - 1:
                            return False
                        new_char_code = (ord(c) - i) 
                        if new_char_code < 0:
                            new_char_code = self.maxChar + new_char_code
                        new_text += chr(new_char_code)
                    if word in new_text:
                        search_keys.append(str(i))

            # Суть метода в проходе по "секторам" текста длинной в 
            # длинну ключа и перестановке символов в соответствии с ключём. 
            # Пример: 
            # абв -> 312 = ваб 
            # абв -> 321 = вба 
            # абвгде -> 321 = вбаедг: абв(123) -> вба(321) + где(123) -> едг(321) = вбаедг(321321) 
            case 'Перестановка символов':
                nums = [int(i) + 1 for i in range(key_power)]
                keys = list(itertools.permutations(nums))
                for key in keys:
                    new_text = ''
                    segments = self.len // len(key)
                    segment_number = 0
                    while (segment_number + 1) * len(key) < self.len:
                        segment = self.text[(segment_number) * len(key): len(key) * (segment_number + 1)]
                        new_segment = ['-' for i in range(len(segment))]
                        for i in range(len(key)):
                            new_segment[int(key[i])-1] = segment[i]
                        new_segment = ''.join(new_segment)
                        new_text += new_segment
                        segment_number += 1
                    if len(self.text[(segment_number * len(key)):]) == len(key):
                        segment = self.text[(segment_number)*len(key):]
                        new_segment = ['-' for i in range(len(segment))]
                        for i in range(len(key)):
                            new_segment[int(key[i])-1] = segment[i]
                        new_segment = ''.join(new_segment)
                        new_text += new_segment
                    else:
                        new_text += self.text[(segment_number)*len(key):]
                    if word in new_text:
                        search_keys.append(''.join([str(i) for i in list(key)]))

            # Один из многоалфавитных шифров. 
            # Суть таже, что и в одноалфавитном, 
            # но применяется не одинаковое смещение 
            # для каждого символа, а гамма.
            case 'Гаммирование': # При длине ключа равной 6 функция работает около 
                                 # 10ти секунд. С увеличением длинны ключа время выполнения
                                 # увеличивается в десять раз за каждый дополнительный
                                 # символ в ключе(длина: 6 - время: 10, длинна: 7 - время: 100)
                for i in range(int('9'*key_power)+1):
                    key = '0' * (key_power - len(str(i))) + str(i)
                    new_text = ''
                    gamma = key * (self.len // len(key) + 2)
                    for i in range(len(self.text)):
                        new_text += chr(ord(self.text[i]) - int(gamma[i]))
                    if word in new_text:
                        search_keys.append(key)
        return search_keys
    
    # Функция анализа текста. 
    def text_analysis(self):
        letters = {}
        for i in self.text:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        return letters
