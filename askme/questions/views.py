from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from questions.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *
from questions.forms import *


def genDict(count):
    data = []
    for i in range(1, count):
        data.append(
            {
                'id': i,
                'nickname': 'name' + str(i),
                'imgurl': '../static/img/av' + str(i % 5 + 1) + '.png',
                'qheader': 'Im looking forward to Alive2017!' + str(i),
                'qtext': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
                         ' Alias consectetur debitis dignissimos dolorum, esse facilis '
                         'in ipsam iusto labore laudantium maiores nam neque nulla numquam '
                         'obcaecati quidem recusandae saepe sapiente suscipit tempora vel veniam'
                         'voluptatibus. Cumque dicta dignissimos dolore et facere, inventore ipsam'
                         ' iusto magni nemo neque quasi quisquam ullam!' + str(i),
                'likecount': i % 20,
                'discount': i % 4,
                'answercount': i,
                'firsttag': 'Alive200' + str(i % 10),
                'secondtag': 'FrenchHaus',
                'date': str(i),
            }
        )
    return data


def paginate(data, page):
    paginator = Paginator(data, 10)
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)


# Create your views here.

def question(request, qnum):
    data = genDict(50)
    post = dict()
    for i in data:
        if i.get('id') == qnum:
            post = i
            break
    return render(request, 'question.html', {'i': post, 'qnum': qnum})


#transaction.atomic

def index(request):
    form = None
    if not request.user.is_authenticated:
        form = LoginForm()
    page = request.GET.get('page')
    quests = paginate(Question.objects.all(), page)
    view_dict = dict(items=quests, paginator=True, title='MAIN-PAGE', pagination=True, form=form)
    return render(request, 'index.html', view_dict)


def ask(request):
    if not request.user.is_authenticated:
        return redirect('/daft-log')
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        tags = request.POST.get('tags').split(' ')
        quest = Question(header=title, text=text, author=request.user.profile)
        quest.save()
        for i in tags:
            try:
                tag = Tag.objects.get(tag_text=i)
                quest.tags.add(tag)
            except:
                tag = Tag(tag_text=i)
                tag.save()
                quest.tags.add(tag)
        quest.save()
        return redirect('/') #редиректить на страницу вопроса
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


def tag(request):
    tagg = Tag.objects.get(tag_text=request.GET.get('tag'))
    data = list()
    for i in Question.objects.all().filter(tags=tagg):
        data.append(i)
    return render(request, 'index.html', {'items': data})


@login_required
def settings(request):
    return render(request, 'settings.html', locals())

# редирект туда откуда он пришел


def logIn(request):
    redirect_path = '/'
    if request.method == 'POST':
        redirect_path = request.POST.get('referer')
        print(redirect_path)
        if request.user.is_authenticated:
            return redirect(redirect_path)
        if request.method == 'POST':
            user = authenticate(username=request.POST.get('nickname'), password=request.POST.get('password'))
            if user is not None:
                if user.is_active:
                    login(request, user)
    return redirect(redirect_path)


def logOut(request):
    redirect_path = '/'
    if request.user.is_authenticated:
        if request.method == "GET":
            redirect_path = request.GET.get('referer')
        logout(request)
    return redirect(redirect_path)


# сделать все через форму
#clean методы форм
def register(request):
    print('register')
    return_path = '/'
    if request.method == 'POST':
        print('POST')
        nickname = request.POST.get('nickname')
        print(nickname)
        email = request.POST.get('email')
        print(email)
        avatar = request.FILES.get('avatar')
        print(avatar)
        password = request.POST.get('password')
        print(password)
        try:
            User.objects.get(username=nickname)
            return render(request, '', locals())
        except:
            try:
                User.objects.get(username=email)
                error = 'Etot email zanyat!'
                return render(request, 'reg.html', locals())
            except:
                user = User.objects.create_user(username=nickname, password=password, email=email)
                profile = Profile(avatar=avatar, usr_key=user)
                profile.save()
        return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'reg.html', locals())


def test(request):
    print(User.objects.get(username='edgar1999').password)
    return redirect('/')


def hot(request):
    quests = (i for i in Question.objects.all().order_by('-like'))
    page = request.GET.get('page')
    #quests = paginate(quests, page)  # починить пагинацию

    view_dict = {
        'items': quests,
        'title': 'HOT',
        'pagination': True,
    }

    return render(request, 'index.html', view_dict)


#@login_required
#@require_POST
def like(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST.get('user'))
        quest = Question.objects.get(id=int(request.POST.get('question')))
        print(request.POST.get('positive'))
        if request.POST.get('positive') == 'true':
            print('positive')
            try:
                lk = Like(question_key=quest, like_author=user, rate=True)
                lk.save()

                return JsonResponse({'likecount': quest.likes()}, status=200)
            except:
                return JsonResponse({'ErrorMSG': "Alredy liked"}, status=403)

        else:
            try:
                print('negative')
                lk = Like(question_key=quest, like_author=user, rate=False)
                lk.save()
                return JsonResponse({'discount': quest.dislikes()}, status=200)
            except:
                return JsonResponse({'ErrorMSG': "Already disliked"}, status=403)
    return HttpResponse()


def load_data(request):
    if request.method == 'POST':
        temp = int(request.POST.get('temp'))
        data = [i for i in Question.objects.all()[temp, temp+5]]
        return JsonResponse({'data': data}, status=200)
    return redirect('/')
