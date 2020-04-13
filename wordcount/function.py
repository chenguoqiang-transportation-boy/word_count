# -*- coding: utf-8 -*-
# @Time : 2020/4/8 20:02
# @Author : 番茄炒鸡蛋
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    # request.GET['text']    —————————— 获取name="text"的文本文字
    total_count = len(request.GET['text'])
    user_text = request.GET['text']

    word_dict = {}#统计相同字 出现次数
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(),key=lambda w:w[1],reverse=True)#以word_dict的字数排序，从大到小

    return render(request, 'count.html',{'count':total_count,
                                         'text':user_text,
                                         'word_dict':word_dict,
                                         'sorted_dict':sorted_dict})

    '''# html文件中，可以在{% %}里面可以写python代码'''

def about(request):
    return render(request,'about.html')