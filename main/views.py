from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.timezone import utc
from django.contrib.auth.models import Group
from account.models import *


@login_required(login_url = '/login/')
def submitanswer(request,pk):

    yes = StudentProfile.objects.filter(user=request.user)
    print(yes)
    if yes:
        reviewset = get_object_or_404(ReviewSet, pk=pk)
        if yes[0].year_semester == reviewset.semester:

            doubleyes = Review.objects.filter(user=request.user, reviewfor=reviewset)
            if not doubleyes:

                now = datetime.utcnow().replace(tzinfo=utc)

                if reviewset.endtime >= now:
                    question = reviewset.question.all()
                    user = request.user

                    if request.method == 'POST':
                        reviewdetails = get_object_or_404(ReviewDetails, review=reviewset)
                        total = reviewdetails.totalpoint
                        for idx, item in enumerate(question,1):
                            name = "inp"+str(idx)
                            value = request.POST.get(name)
                            value = int(value)
                            total += value
                            newreview = Review(reviewfor=reviewset, question=item, user=user, point=value)
                            newreview.save()

                        reviewdetails.usergiven = reviewdetails.usergiven + 1

                        reviewdetails.totalpoint = reviewdetails.totalpoint + total
                        reviewdetails.save()
                        reviewdetails = get_object_or_404(ReviewDetails, review=reviewset)
                        avg = (reviewdetails.totalpoint*5)/((len(question)*5)*reviewdetails.usergiven)
                        reviewdetails.avg = avg
                        reviewdetails.save()
                        messages.info(request, 'Successfully added review')
                        return redirect('home')

                    context = {
                        'question': question,
                        'reviewset': reviewset,

                    }
                    return render(request, 'front/feedback_status.html', context )
                else:
                    return render(request, 'front/timeover.html')
            else:
                return render(request, 'front/given.html' )
        else:
            return render(request, 'front/notauthorised.html' )
    else:
        return render(request, 'front/notauthorised.html' )
