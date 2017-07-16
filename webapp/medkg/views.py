from django.shortcuts import render
import json
# Create your views here.


def index(request):
    return render(request, 'index.html', {})



def show_graph(request):

    nodes = [ { 'name': "桂林" ,'type':1    }, { 'name': "广州" ,'type':1   },
                      { 'name': "厦门",'type':2    }, { 'name': "杭州" ,'type':3  },
                      { 'name': "上海"  ,'type':3 }, { 'name': "青岛" ,'type':2   },
                      { 'name': "天津" , 'type':3   } ]
    edges = [  { 'source' : 0  , 'target': 1 } , { 'source' : 0  , 'target': 2 } ,
               { 'source' : 0  , 'target': 3 } , { 'source' : 1  , 'target': 4 } ,
               { 'source' : 1  , 'target': 5 } , { 'source' : 1  , 'target': 6 }  ]
    return render(request, 'show_graph.html', {"nodes": json.dumps(nodes), 'edges':json.dumps(edges) })
