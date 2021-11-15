
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index1(request):

    return render(request,'lg.html')
#登录
def login(request):
    if request.method=='GET':
        return render(request,'lg.html')
    else:
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username and password:

            # 判断查询
            import jsonpickle
            c = User.objects.get(uname=username)
            if check_password(password, c.password):

                #将登录session 存为对象
                user = Users(username,password)
                request.session['login']=jsonpickle.dumps(user)
                return HttpResponseRedirect('/book/index')
    return HttpResponseRedirect('/book')
#将登录信息存为对象
class Users(object):
    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd
#注册
def to_register(request):
    return render(request,'reg.html')
def register(request):
    uno = request.POST.get('uno','')
    uname = request.POST.get('uname','')
    password = request.POST.get('password','')
    User.objects.create(uno=uno,uname=uname,
                        password=make_password(password))
    return HttpResponseRedirect('/book')
#index页面+分页
def index(request):
    import jsonpickle
    #获取session
    user = request.session['login']
    uuser = jsonpickle.loads(user)
    #分页操作
    page_number = request.GET.get('num',1)
    page_size = request.GET.get('size',5)
    book = Book.objects.all()
    pager = Paginator(book,int(page_size))#实例化分页
    try:
        page_data = pager.page(int(page_number))
    except PageNotAnInteger:
        page_data = pager.page(1)  # 第一页
    except EmptyPage:
        page_data = pager.page(pager.num_pages)
    return render(request,'index.html',{'book':book,'pager':pager,
                                        'page_data':page_data,'uname':uuser.uname})

#增加
def add(request):
    if request.method=='Get':
        return redirect('/book/index')
    elif request.method=='POST':
        # book_id = request.POST.get('book_id','')
        book_name = request.POST.get('book_name','')
        book_publisher = request.POST.get('book_publisher','')
        book_img = request.FILES.get('book_img','')
        book_count = request.POST.get('book_count','')
        Book.objects.create(book_img=book_img,book_name=book_name,book_count=book_count,
                            book_publisher=book_publisher)
        return redirect('/book')
    return HttpResponse('未知错误！！！')
def to_add(request):
    return render(request,'add.html')
#删除操作
def delete(request):
    book_id = request.GET.get('book_id','')
    Book.objects.filter(book_id=book_id).delete()
    return redirect('/book')
#更新操作
def update1(request):
    book_id = request.GET.get('book_id','')
    book = Book.objects.filter(book_id=book_id)
    return render(request,'update.html',{'book':book})
def update2(request):
    if request.method=='Get':
        return redirect('/book')
    elif request.method=='POST':
        book_id = request.POST.get('book_id','')
        book_name = request.POST.get('book_name','')
        book_publisher = request.POST.get('book_publisher','')
        book_img = request.FILES.get('book_img','')
        print("---------",book_img)
        book_count = request.POST.get('book_count','')
        book = Book.objects.filter(book_id=book_id)
        book.update(book_name=book_name,
                    book_count=book_count,
                    book_publisher=book_publisher)
        b = Book.objects.get(book_id=book_id)
        b.book_img = book_img
        b.save()
        return redirect('/book')
    return HttpResponse('未知错误！！！')

#个人中心
def person(request):
    #获取用户名
    uname = request.GET.get('uname')
    person = User.objects.filter(uname=uname)
    return render(request,'personal.html',{'person':person})
#借阅功能
def lend(request):
    import jsonpickle
    user = request.session['login']
    uuser = jsonpickle.loads(user)#将python对象转化为序列化字符串
    lbookid = request.GET.get('book_id')
    lbook = request.GET.get('book_name')
    lpublisher = request.GET.get('book_publisher')
    #借阅前判断是否已借
    count = Lend.objects.filter(lbookid=lbookid).count()
    if count!=0:
        return HttpResponse('已经借过咯！！')
    else:
        #添加到借阅表
        Lend.objects.create(uname=uuser.uname, lbook=lbook, lbookid=lbookid,
                            lpublisher=lpublisher)
        #用户借阅数+1  最大借阅数-1 库存-1
        u = User.objects.get(uname=uuser.uname)
        book = Book.objects.get(book_id=lbookid)
        if u.max_num>0 and book.book_count>0:
            u.lend_num = u.lend_num+1
            u.max_num = u.max_num-1
            u.save()
            book.book_count = book.book_count - 1
            book.save()
            return HttpResponseRedirect('/book/index')
        else:
            return HttpResponse('您目前没有借书余额！！')

#借阅历史
def lend_history(request):
    uname = request.GET.get('uname')
    lend = Lend.objects.filter(uname=uname).order_by('-ltime',)
    return render(request,'lendhistory.html',{'lend':lend})

#还书功能
def returnbook(request):
    #获取id
    bbookid = request.GET.get('bookid')
    #根据借书记录查询该书信息
    b = Lend.objects.get(lbookid=bbookid)
    uname = b.uname
    bbook = b.lbook
    bpublisher = b.lpublisher
    #存入还书记录中
    Back.objects.create(bbookid=bbookid,uname=uname,bbook=bbook,bpublisher=bpublisher)
    #还原库存
    b.delete()#删除借书记录
    book = Book.objects.get(book_id=bbookid)
    book.book_count = book.book_count+1
    book.save()
    #个人借书更新
    u = User.objects.get(uname=uname)
    u.lend_num = u.lend_num - 1
    u.max_num = u.max_num + 1
    u.save()
    return HttpResponseRedirect('/book/index')

#还书记录
def back_history(request):
    uname = request.GET.get('uname')
    back = Back.objects.filter(uname=uname).order_by('-btime', )
    return render(request, 'backbook.html', {'back': back})