from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import user,posts
from mysql import connector
dict={"obj":[]}
def fun(request):
    return render(request,'index.html')
def reg(request):
    return render(request,'reg.html')
def login(request):
    return render(request,'login.html')
def page(req):
    obj=user(name=req.POST["name"],email=req.POST["email"],password=req.POST["password"])
    obj.save()
    db=connector.connect(user='root',host='localhost',password='akshay',database='blogdata',auth_plugin='mysql_native_password')
    cur=db.cursor()
    cur.execute("set sql_safe_updates=0")
    cur.execute("select name,title,decription from blog_posts where name="+repr(req.POST["name"]))
    val=cur.fetchall()
    db.commit()
    db.close()
    globals()["dict"]={"name":req.POST["name"],"email":req.POST["email"],"password":req.POST["password"],"obj":val}
    return render(req,'page.html',globals()["dict"])
def addposts(request):
    print(request.GET["name"])
    return render(request,'addposts.html',{"name":request.GET["name"]})
def addpost(request):
    obj=posts(title=request.POST["title"],decription=request.POST["desc"],name=request.POST["name"])
    obj.save()
    db=connector.connect(user='root',host='localhost',password='akshay',database='blogdata',auth_plugin='mysql_native_password')
    cur=db.cursor()
    cur.execute("set sql_safe_updates=0")
    cur.execute("select name,title,decription from blog_posts where name="+repr(request.POST["name"]))
    val=cur.fetchall()
    db.commit()
    db.close()
    return render(request,'page.html',{"name":request.POST["name"],"obj":val})
def dell(request):
    db=connector.connect(user='root',host='localhost',password='akshay',database='blogdata',auth_plugin='mysql_native_password')
    cur=db.cursor()
    cur.execute("delete from blog_posts where title="+repr(request.POST["title"]))
    db.commit()
    db.close()
    return JsonResponse({"name":request.POST["title"]})