from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pymysql
from  util import  sqlHelp
import json
@csrf_exempt
def index(request):
    method = request.method
    conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='db2')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    if method == 'GET':
        cursor.execute('select id,name from class')
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        print(method)
        return render(request, 'index.html', {
            'method': method,
            'classlist': res
        })
    else:
       name = request.POST['name']
       sql = 'insert into class (name) values ("%s")'
       print(sql)
       cursor.execute(sql,name)
       conn.commit()
       return redirect('/index')


@csrf_exempt
def dele(request):
    print(type(request))
    id = request.GET['id']
    print(id)
    conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='db2')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'delete  from class where id =%s'%id
    print('sql',sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/index')

@csrf_exempt
def login(request):
    print(request)
    return render(request, template_name='index.html')

@csrf_exempt
def addclass(request):
    print('post',request.POST)
    print('GET', request.GET)
    name = request.POST.get('name')
    if name:
        sql = 'insert into class (name) values (%s)'
        sqlHelp.insert(sql,(name,))
        return HttpResponse('ok')
    else:
        return HttpResponse('不ok')
@csrf_exempt
def get_stu_list(request):
    print('post', request.POST)
    print('GET', request.GET)
    sql = 'select s.id,s.name ,c.id as cls_id ,c.name  as clsname from stu s inner join class c on c.id =s.cls_id '
    studentlist = sqlHelp.getList(sql)
    print(1  in  studentlist)
    ret ={
        'studentlist':studentlist
    }
    print(' for page  stu_list.html',ret)
    return render(request,'stu_list.html',ret)


@csrf_exempt
def add_stu(request):
    print('post', request.POST)
    print('GET', request.GET)

    if request.method == 'GET':
        id = request.GET.get('id')
        print(' page coming add_student.html', id)
        sql1 = sql = 'select s.id,s.name ,c.id as cls_id ,c.name  as clsname from stu s inner join class c on c.id =s.cls_id  where s.id=%s'
        sql2 ='select id,name from class'
        ret1 = sqlHelp.getone(sql1,(id,))
        ret2 = sqlHelp.getList(sql2)
        ret = {
            'stu':ret1,
            'cls_list':ret2
        }
        print('for page add_student.html',ret)
        return render(request,'add_student.html',ret)
    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        clsid = request.POST.get('clsid')
        if not id:
            sql = 'insert into stu (name,cls_id) values(%s,%s)'
            print(' page coming add_student.html',name,int(clsid))
            sqlHelp.insert(sql,(name,(clsid)))
            return redirect('/stu_list')
        else:
            sql = 'update stu set name=%s,cls_id=%s where id=%s'
            print(' page coming add_student.html',id, name, clsid)
            sqlHelp.update(sql,(name,clsid,id))
            return redirect('/stu_list')






