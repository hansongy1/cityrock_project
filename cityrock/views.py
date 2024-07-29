from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def login(request):
    if request.method == 'GET':
        remember_id = request.COOKIES.get('id', '')
        return render(request, 'Ex_Cookie/login.html', {'remember_id':remember_id})
    else:
        id = request.POST['id']
        pw = request.POST['pw']

        # POST로 값을 꺼내올 때 값이 없을 경우 오류, 따라서 get 함수를 사용한다.
        remember = request.POST.get('remember', '')
        response = HttpResponse('로그인 성공!')
        
        if(id == pw):
            # 로그인 성공 시 remember를 확인
            request.session['login_user'] = id # ID를 세션에 저장
            if remember == '': # 값이 없다면, 쿠키를 삭제한다.
                response.delete_cookie('id')
            else:
                response.set_cookie('id', id, max_age=60) #60초만 유지
            return response
        else:
            return render(request, 'Ex_Cookie/login.html')
        
from django.shortcuts import redirect, reverse
def logout(request):
    request.session.flush() #세션과 관련된 정보들 삭제
    response = redirect(reverse('Ex_Cookie:index'))
    return response