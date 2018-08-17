from __future__ import print_function

import math
import random
from IPython.display import display, Markdown, Latex, HTML
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

get_ipython().run_line_magic('reload_ext', 'tikzmagic')

interactif = False

def activite(title):
    display(Markdown('#### Activité : '+title))

def yes_no(question,default=False):
    rep=''
    print('', end='', flush=True)
    if len(question)>0:
        question=question+' '
    if default:
        question=question+'[o/N]> '
    else:
        question=question+'[O/n]> '
    if not interactif:
        if default:
            print(question+'o',flush=True)
        else:
            print(question+'n',flush=True)
        return default
    while rep!='o' and rep!='n':
        rep=input(question)
    return rep == 'o'

def question(markdown):
    print('', end='', flush=True)
    display(Markdown(markdown))
    if interactif:
        rep=input('Votre proposition > ')
    else:
        display(Markdown('`_____________________________________________________`'))

def solution(markdown):
    print('', end='', flush=True)
    if interactif:
        rep=input('Votre proposition > ')
    else:
        display(Markdown('Votre proposition > `_____________________________________________________`'))
    display(Markdown('**Solution:** '+markdown))

def solutioncheck(question, answer, feedback_yes, feedback_no):
    print('', end='', flush=True)
    ret=False
    if interactif:
        rep=input(question+' > ')
        display(Markdown('Vous avez répondu : '+rep))        
        if rep==answer:
            display(Markdown(feedback_yes))
            ret=True
        else:
            display(Markdown(feedback_no))
    else:
        display(Markdown(question+' > `_____________________________________________________`'))
    display(Markdown('**Solution :** '+answer))
    return ret

def reasonablenumbertostr(f):
    sign=True
    if f<0:
        sign=False
        f=-f
    a=math.floor(f)
    b=f-a
    if b<0.000001:
        b=0.0
    if b > 0.999999:
        b=0.0
        a=a+1
    s=''
    e=0
    while(a>0):
        e=e+1
        if e>3 and e%3 == 1:
            s='~'+s
        s=str(a%10)+s
        a=a//10
    if b>0:
        if s=='':
            s='0,'
        else:
            s=s+','
        e=0
        while(b>0):
            e=e+1
            if e>3 and e%3 == 1:
                s=s+'~'
            b=b*10
            if b-math.floor(b)>.999999:
                b=math.floor(b)+1
            s=s+str(int(math.floor(b)))
            b=b-math.floor(b)
            if b<0.000001:
                b=0.0
    if s=='':
        return '0'
    if sign:
        return s
    return '-'+s

def numbertostr(f,dollar=True):
    e=0
    d=''
    if dollar:
        d='$'
    if (abs(f))<0.01 and f>0:
        while abs(f)<0.999999 and f>0:
            f=10*f
            e=e-1
    x=reasonablenumbertostr(f)
    if e<0 or e>0:
        if x!='1':
            return d+x+'×10^{'+str(e)+'}'+d
        else:
            return d+'10^{'+str(e)+'}'+d
    else:
        return d+x+d
    
def n2s(f):
    return numbertostr(f,dollar=False)

def twobyten(lead,two,ten,final):
    # if final, eliminate small powers of two and all powers of ten
    if final:
        if two<-8 or two>8:
            lead=lead*math.pow(10,ten)
            ten=0
        else:
            lead=lead*math.pow(2,two)*math.pow(10,ten)
            two=0
            ten=0
        if lead == 0:
            two=0
            ten=0

    root=numbertostr(lead)
    root=root.replace('$','') # remove math markers
    if two!=0:
        if root != '1':
            root = root+'×2^{'+str(two)+'}'
        else:
            root = '2^{'+str(two)+'}'
    if ten!=0:
        if root != '1':
            root = root+'×10^{'+str(ten)+'}'
        else:
            root = '10^{'+str(ten)+'}'
    return '$'+root+'$'

interactif = False
import datetime
print('Ce cours a été régénéré le',datetime.datetime.now())
