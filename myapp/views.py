from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from myapp.models import Image
from django.shortcuts import render, redirect
from .models import Vote
from .forms import VoteForm
from django.http import HttpResponseRedirect

# Create your views here.

def home (request):
    return render (request,'myapp/index.html')

# def voting (request):
    
#     return render (request , 'myapp/vote.html')


def voting (request):
    latest_id = Image.objects.latest('id').id
    latest_data = Image.objects.get(id=latest_id)
    return render(request, 'myapp/vote.html', {'latest_data': latest_data})

# def voting (request):
#     latest_entry = Image.objects.latest('id')
#     context = {
#         'latest_entry': latest_entry
#     }
#     return render(request, 'myapp/voting.html')














def services (request):
    return render (request , 'myapp/services.html')

def create (request):
    return render (request , 'myapp/create.html')


# def vote (request):
#     if request.method == "POST":
#         brandtitle = request.POST.get("brandtitle")
#         name = request.POST.get("name")
#         votetitle = request.POST.get("votetitle")
#         name_candidate1 = request.POST.get("name_candidate1")
#         name_candidate2 = request.POST.get("name_candidate2")
#         name_candidate3 = request.POST.get("name_candidate3")
#         name_candidate4 = request.POST.get("name_candidate4")
#         name_candidate5 = request.POST.get("name_candidate5")
#         name_candidate6 = request.POST.get("name_candidate6")
#         instagramlink = request.POST.get("instagramlink")
#         facebooklink = request.POST.get("facebooklink")
#         youtubelink = request.POST.get("youtubelink")
#         twitterlink  = request.POST.get("twitterlink ")
#         discription= request.POST.get("discription")
#         vote = Image (name=name , discription=discription,name_candidate1=name_candidate1,name_candidate2=name_candidate2,name_candidate3=name_candidate3,name_candidate4=name_candidate4,name_candidate5=name_candidate5,name_candidate6=name_candidate6, votetitle =votetitle ,brandtitle=brandtitle,instagramlink=instagramlink,facebooklink=facebooklink,youtubelink=youtubelink,twitterlink=twitterlink)
#         form = ImageForm (request.POST , request.FILES)
#         if form.is_valid():
#             form.save()
#     form = ImageForm()
#     img = Image.objects.all()
#     return render (request , 'myapp/create_vote.html')







def vote (request):
    if request.method == "POST":
        brandtitle = request.POST.get("brandtitle")
        name = request.POST.get("name")
        votetitle = request.POST.get("votetitle")
        name_candidate1 = request.POST.get("name_candidate1")
        name_candidate2 = request.POST.get("name_candidate2")
        name_candidate3 = request.POST.get("name_candidate3")
        name_candidate4 = request.POST.get("name_candidate4")
        name_candidate5 = request.POST.get("name_candidate5")
        name_candidate6 = request.POST.get("name_candidate6")
        instagramlink = request.POST.get("instagramlink")
        facebooklink = request.POST.get("facebooklink")
        youtubelink = request.POST.get("youtubelink")
        twitterlink  = request.POST.get("twitterlink ")
        discription= request.POST.get("discription")
        vote = Image (name=name , discription=discription,name_candidate1=name_candidate1,name_candidate2=name_candidate2,name_candidate3=name_candidate3,name_candidate4=name_candidate4,name_candidate5=name_candidate5,name_candidate6=name_candidate6, votetitle =votetitle ,brandtitle=brandtitle,instagramlink=instagramlink,facebooklink=facebooklink,youtubelink=youtubelink,twitterlink=twitterlink)
        form = ImageForm (request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return render (request , 'myapp/created_succes.html')
        else:
            return render (request , 'myapp/created_error.html')
    form = ImageForm()
    img = Image.objects.all()
    return render (request , 'myapp/create_vote.html')

def about (request):
    return render(request, 'myapp/about.html')

def contact (request):
    return render(request, 'myapp/contact.html')

def to_create(request):
    return render(request, 'myapp/all_create.html')

def vote_success(request):
    return render(request, 'myapp/vote_success.html')

def combined_view(request):
    latest_entry = Image.objects.latest('id')

    # Retrieve the vote counts from the database
    vote = Vote.objects.first()  # Assuming there is only one row in the Vote table
    total_votes = vote.total_votes

    # Calculate the vote percentages
    option1_percentage = (vote.option1_votes / total_votes) * 100
    option2_percentage = (vote.option2_votes / total_votes) * 100
    option3_percentage = (vote.option3_votes / total_votes) * 100
    option4_percentage = (vote.option4_votes / total_votes) * 100
    option5_percentage = (vote.option5_votes / total_votes) * 100
    option6_percentage = (vote.option6_votes / total_votes) * 100

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            candidate = form.cleaned_data['candidate']
            setattr(vote, f'{candidate}_votes', getattr(vote, f'{candidate}_votes') + 1)
            vote.total_votes += 1
            vote.save()
            option1_percentage = (vote.option1_votes / vote.total_votes) * 100
            option2_percentage = (vote.option2_votes / vote.total_votes) * 100
            option3_percentage = (vote.option3_votes / vote.total_votes) * 100
            option4_percentage = (vote.option4_votes / vote.total_votes) * 100
            option5_percentage = (vote.option5_votes / vote.total_votes) * 100
            option6_percentage = (vote.option6_votes / vote.total_votes) * 100
            return redirect('vote_success')
    else:
        form = VoteForm()

    context = {
        'latest_entry': latest_entry,
        'form': form,
        'option1_percentage': option1_percentage,
        'option2_percentage': option2_percentage,
        'option3_percentage': option3_percentage,
        'option4_percentage': option4_percentage,
        'option5_percentage': option5_percentage,
        'option6_percentage': option6_percentage,
    }

    return render(request, 'myapp/voting_page.html', context)



def graph_view(request):
    latest_entry = Image.objects.latest('id')

    # Retrieve the vote counts from the database
    vote = Vote.objects.first()  # Assuming there is only one row in the Vote table
    total_votes = vote.total_votes

    # Calculate the vote percentages
    option1_percentage = (vote.option1_votes / total_votes) * 100
    option2_percentage = (vote.option2_votes / total_votes) * 100
    option3_percentage = (vote.option3_votes / total_votes) * 100
    option4_percentage = (vote.option4_votes / total_votes) * 100
    option5_percentage = (vote.option5_votes / total_votes) * 100
    option6_percentage = (vote.option6_votes / total_votes) * 100

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            candidate = form.cleaned_data['candidate']
            setattr(vote, f'{candidate}_votes', getattr(vote, f'{candidate}_votes') + 1)
            vote.total_votes += 1
            vote.save()
            option1_percentage = (vote.option1_votes / vote.total_votes) * 100
            option2_percentage = (vote.option2_votes / vote.total_votes) * 100
            option3_percentage = (vote.option3_votes / vote.total_votes) * 100
            option4_percentage = (vote.option4_votes / vote.total_votes) * 100
            option5_percentage = (vote.option5_votes / vote.total_votes) * 100
            option6_percentage = (vote.option6_votes / vote.total_votes) * 100
            return redirect('vote_success')
    else:
        form = VoteForm()

    context = {
        'latest_entry': latest_entry,
        'form': form,
        'option1_percentage': option1_percentage,
        'option2_percentage': option2_percentage,
        'option3_percentage': option3_percentage,
        'option4_percentage': option4_percentage,
        'option5_percentage': option5_percentage,
        'option6_percentage': option6_percentage,
    }

    return render(request, 'myapp/results.html', context)