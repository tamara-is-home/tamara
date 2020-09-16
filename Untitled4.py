#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Conv:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        self.syb = [
            'M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV',
            'I'
        ]
        
    def to_roman(self, num):
        """
        засунул поля в словарь - так мне казалось будет проще потом
        """
        dic = dict(zip(self.val,self.syb)) 
        lst=[] #list of decimal split
        lsy=[] #list of ready-to-convert split
        """
        ниже я пробую разложить число на степени 10 и записываю результат в lst
        т.е делаю из 1234 - 1000,200,30,4
        """
        num1=num
        while num1!=0:
            num1=num1%(10**(len(str(num1))-1))
            lst.append(num - num1)
            num=num1
        """
        тут я очень долго и тупо раскладываю числа на те, которые уже есть в словаре
        типо я же не могу оставить 30 - я должен сделать 10, 10, 10, а из 200 - 100,100
        при этом я не должен делать из 40 тоже самое - для 40 есть отдельное обозначение
        крч на эту часть я проебал часа 1,5 и думаю что можно было сделать проще =)
        """
        for i in lst:
            if i%1000==0:
                n=i//1000
                for z in range(0,n):
                    lsy.append(1000)
            elif i%100==0 and i not in dic.keys():
                if i<500:
                    n=i//100
                    for z in range(0,n):
                        lsy.append(100)
                else:
                    lsy.append(500)
                    n=(i-500)//100
                    for z in range(0,n):
                        lsy.append(100)
            elif i%10==0 and i not in dic.keys():
                if i<50:
                    n=i//10
                    for z in range(0,n):
                        lsy.append(10)
                else:
                    lsy.append(50)
                    n=(i-50)//10
                    for z in range(0,n):
                        lsy.append(10)
            elif i<10 and i not in dic.keys():
                if i < 5:
                    n=i//1
                    for z in range(0,n):
                        lsy.append(1)
                else:
                    lsy.append(5)
                    n=(i-5)//1
                    for z in range(0,n):
                        lsy.append(1)
            else:
                lsy.append(i)
        
        lsy.sort(reverse=True)
        result=''
        for i in lsy:
            result +=dic[i] # final-ochka
        print(lst)
        print(lsy)
        print(result)
        return result
print('Converted:', Conv().to_roman(1284))

