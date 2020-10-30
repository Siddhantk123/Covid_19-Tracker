from django.shortcuts import render, HttpResponse, redirect
import requests
from bs4 import BeautifulSoup
import time
import json
from covid import Covid

def home(request):

    covid = Covid()
    covid= covid.get_data()
    # print(covid)
    df1=[]  #empty list
    for dic in covid: #dic me each value aayega 
        df1.append([dic['country'],dic['confirmed'], dic['active'],dic['deaths'],dic['recovered'],dic['last_update']]) #yaha 3-3 ke pair me list me append honge  #ko fetch kr rhe #3-3 ke pair me ye list me add hoge                                                                               #ko fetch kr rhe
    # print(df1)                                                                            
    #ab list mil gya us data ka and store ho ya df me


    #using the concept of data feame  of pandas
    import pandas as pd
    df1=pd.DataFrame(df1,columns=['Country','Confirmed','Active','Deaths','Recoverd','Last Update'])#ye sirf heading dega frame dega
    #df me table aayega
    
    exc1={'table0':df1.to_html()}
    #print(exc1)
    return render(request, 'home.htm',exc1) 
            







    
