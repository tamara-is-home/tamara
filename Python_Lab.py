#!/usr/bin/env python
# coding: utf-8

# # Python and algorithms

# ##### Сomplete this part of test without using any libs (your code must not contain keyword 'import')

# #### 1. Implement function str_to_dict(some_str) which returnes dictionary, where keys are string characters, and values are their quantity in the string:
# 
# <div style="text-align: right">1 point</div>

# In[1]:


def str_to_dict(some_str):  
    dict = {}
    for i in some_str:
        dict[i]=some_str.count(i)
    return dict


# In[2]:


print('Str to dict:', str_to_dict('dataroot_university'))


# Expected Output: 
# <table>
#   <tr>
#     <td>Str to dict:</td>
#     <td> {'d': 1, 'a': 2, 't': 3, 'r': 2, 'o': 2, '_': 1, 'u': 1, 'n': 1, 'i': 2, 'v': 1, 'e': 1, 's': 1, 'y': 1} </td> 
#   </tr>

# #### 2. Implement function sec_smallest(numbers) which returns second smallest item in the list, without using the built-in sorting methods (your code mustn't contain such words as 'sort', 'sorted'):
# 
# <div style="text-align: right">1 point
#   

# In[27]:


def sec_smallest(numbers):
    no_dup = list(dict.fromkeys(numbers))
    for i in no_dup:
        if i == min(no_dup):
            no_dup.remove(i)
    return min(no_dup)
    


# In[29]:


print('Sec_smallest:', sec_smallest([1, 2, -8, -8, -2, 0,-9,-9,-9]))


# Expected Output: 
# <table>
#   <tr>
#     <td>Sec_smallest:</td>
#     <td> -2 </td> 
#   </tr>

# #### 3. Implement function prime_nums(n) that returns list of numbers which  are simple and < n:
# 
# <div style="text-align: right">1 point</div>

# In[58]:


def prime_nums(n):
    num=[]
    for i in range (2,n):
        for j in range (2,i):
            if i%j==0:
                break
        else: 
            num.append(i)
    return num


# In[59]:


print('Prime numbers:', prime_nums(30))


# Expected Output:
# <table>
#   <tr>
#     <td>Prime numbers:</td>
#     <td>[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]</td>
#   </tr>

# **4. Implement function max_sum_index(tuples), which returnes index of tuple in the list with maximum sum of elements:**
# 
# <div style="text-align: right">1 point</div>

# In[77]:


def max_sum_index(tuples):  
    lt = [x+y for x,y in tuples]
    i =lt.index(max(lt))
    return i


# In[79]:


print(max_sum_index([(10, 20), (40, 32), (30, 25),(90,10)]))


# Expected Output: 
# <table>
#   <tr>
#     <td>Index:</td>
#     <td> 1 </td> 
#   </tr>

# **5. Implement function gcd(x, y), which returns the greatest common divisor of n and m.**
# <div style="text-align: right">1 point</div>

# In[110]:


def gcd(x, y):   
    while y != 0:
        (x,y)=(y,x%y)
        print (x,y)    
    return x


# In[109]:


print(gcd(160, 220))


# Expected Output: 
# <table>
#   <tr>
#     <td>GCD:</td>
#     <td> 20 </td> 
#   </tr>

# #### 6. Implement recursive sum of the list:
# <div style="text-align: right">1 point</div>

# In[122]:


def recursive_list_sum(data_list):
    sum = 0
    for i in data_list:
        if type(i)==int:
            sum+=i
        else:
            sum+=recursive_list_sum(i)
    return sum


# In[124]:


print('The sum of a list is ', recursive_list_sum([1, 2, [3, 4,5],8, [5, 6], [7, 8, 9, [10]]]))


# Expected Output:
# <table>
#   <tr>
#     <td>The sum of a list is 55</td> 
#   </tr>

# #### 7. Implement decorator which returns function signature and it's return value:
# <div style="text-align: right">1 point</div>

# In[380]:


def debug(func):
    def wrap(a,b):
        z = func(a,b)
        print (f"{func} was called and returned {z}")
    return wrap


# In[381]:


@debug
def add(a, b):
    return a + b

add(3, 4)


# Expected Output:
# <table>
#   <tr>
#     <td>add(3, 4) was called and returned 7</td>
#   </tr>

# #### 8. Implement class Conv, that contains method to_roman(self, n), which converts decimal numbers to Roman numerals:
# 
# <div style="text-align: right">2 points</div>

# In[377]:


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
        


# In[379]:


print('Converted:', Conv().to_roman(1284))


# Expected Output:
# <table>
#   <tr>
#     <td>Converted:</td>
#     <td>XLIV</td> 
#   </tr>

# #### 9. Implement class CombinationsList, that contains method get_combinations(self, my_list), which returns all combinations of elements of given list, including empty element and in order, law of which can be discrovered from the expected output:
# <div style="text-align: right">3 points</div>

# In[ ]:


class CombinationsList:
    @staticmethod
    def get_combinations(my_list):
        """
        :param self:
        :param my_list: list
        :return: list[list]
        """
        # YOUR CODE HERE


# In[ ]:


print('Combinations:', CombinationsList().get_combinations([1, 'a', 2]))


# Expected Output:
# <table>
#   <tr>
#     <td>Combinations:</td>
#     <td>[[], [1], ['a'], [2], [1, 'a'], [1, 2], ['a', 2], [1, 'a', 2]]</td> 
#   </tr>

# #### 10. Create base class <code>Rocket</code> and it's subclass <code>Shuttle</code>. The parent class contains methods <code>getMission()</code>, <code>addMission()</code> and <code>getName()</code>. The subclass <code>Shuttle</code> contains method <code>getDescription()</code>. Notice that we have not defined <code>getName()</code>, <code>getMission()</code>, <code>addMission()</code> in the <code>Shuttle</code> class but we are still able to access them, because the class <code>Shuttle</code> inherits them from the <code>Rocket</code> class. Use <code>super()</code> method to have ability to call those methods of the base class.
# <div style="text-align: right">3 points</div>

# In[ ]:


class Rocket:

    def __init__(self, name, mission):
        """
        :param name: str
        :param mission: str or list
        """
        # attributes are private to class Rocket
        self.__name = name      
        self.__mission = mission

    def getMission(self): 
        """
        : return str or list
        """
        # YOUR CODE HERE

    def addMission(self, mission): 
        # procedure method which adds a new mission. There can be one (str) or multiple (list) existing missions
        """
        : param mission: str
        """
        # YOUR CODE HERE

    def getName(self):
        """
        : return str
        """
        # YOUR CODE HERE

    
class Shuttle(Rocket):

    def __init__(self, name, mission, model):
        # call parent constructor to set name and mission  
        """
        :param name: str
        :param mission: str or list
        : param model: str
        """
        # YOUR CODE HERE

    def getDescription(self):
        return 'Name: {0}\nModel: {1}\nMissions: {2}'.format(self.getName(), self.__model, str(self.getMission()))


# In[ ]:


dragon = Shuttle("Crew Dragon", "Dragon 2 pad abort test", "V2")
print(dragon.getDescription(), '\n')
dragon.addMission('Dragon 2 in-flight abort test')
print(dragon.getDescription())


# Expected Output: 
# 
#                 Name: Crew Dragon
#                 Model: V2
#                 Missions: Dragon 2 pad abort test
#                 
#                 Name: Crew Dragon
#                 Model: V2
#                 Missions: ['Dragon 2 pad abort test', 'Dragon 2 in-flight abort test']
# 
# 
