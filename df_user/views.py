from django.shortcuts import render, redirect
from hashlib import sha1
from .models import UserInfo
from django.http import JsonResponse

# 显示注册页面
def register(request):
    return render(request, 'df_user/register.html')


# 处理注册的请求
def register_handler(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')

    if UserInfo.objects.filter(uname=uname.encode('utf-8')):
        return redirect('/user/register/')

    if upwd != ucpwd:
        return redirect('/user/register/')

    sa = sha1()
    sa.update(upwd.encode('utf-8'))
    spwd = sa.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upassword =  spwd
    user.uemail = uemail
    user.save()

    return redirect('/user/login/')


#在注册的过程中需要去判断注册用户是否存在
def register_exist(request):
    '''
    判断用户是否存在，实现方式是在 register.html 这个页面当用户输入用户名后，失去焦点时去通过AJAX
    请求到后去查询数据库判断用户名是否存在，如果存在就提示用户"用户名已存在"，然后不允许submit的操作
    :param request:
    :return:
    '''
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    print('uname count is: ', count)
    return JsonResponse({'count': count})


#显示登录页面
def login(request):
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0}
    return render(request, 'df_user/login.html', context=context)


#登录页面登录处理
def login_handler(request):
    post = request.POST
    username = post.get('username')
    upwd = post.get('pwd')
    remember = post.get('remember')

    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0}

    user = UserInfo.objects.filter(uname=username)
    if user:
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest() == user[0].upassword:
            print('>>> source code is here under under user and pwd is right')
            pass
        else:
            # 用户名正确，密码不正确时将 'error_pwd' 的value置为1
            # 重新渲染页面，js在后台会进行密码不正确的显示
            print('>>> source code is here under pwd is wrong')
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1}
            return render(request, 'df_user/login.html', context=context)
    else:
        # 用户名不正确时，将 'error_name' 的value置为1
        # 重新渲染页面，js在后台会进行用户名不正确的显示
        print('>>> source code is here under user is wrong')
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0}
        return render(request, 'df_user/login.html', context=context)





