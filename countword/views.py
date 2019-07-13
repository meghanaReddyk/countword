from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
  return render(request,'home.html')


def count(request):
    fulltext=request.GET['fulltext']
    # print('full text: '+fulltext)
    wordslist=fulltext.split()
    wrdDict={}
    for i in wordslist:
        if i not in wrdDict:
            wrdDict[i]=1
        else:
            wrdDict[i]+=1
    sortedwords=sorted(wrdDict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordslist), 'worddict':sortedwords})


def about(request):
    return  render(request,'about.html')