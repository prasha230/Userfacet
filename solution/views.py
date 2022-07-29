from calendar import weekday
import json
from django.http import HttpResponse
from django.shortcuts import render
import requests
from datetime import date
from .models import scheduled_class
from .forms import ClassForm
from datetime import timedelta

# import smtplib


# Create your views here.
def home(request,day='',time=''):
    schedule=requests.get('https://raw.githubusercontent.com/rohit-userfacet/userfacet-backend-testcase/main/teacher_availability.json').json()
    
    if request.method=="POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            day=form.cleaned_data['weekday']
            #if teacher does not teaches that day
            if(day not in schedule['availability']):
                l={'slot_confirmed':False,
                   'reason':"Teacher does not teaches that day"}
                return HttpResponse(json.dumps(l))
            
            
            #if teacher does teaches that day
            cls = form.save(commit=False)
            st=form.cleaned_data['start_time']
            et=form.cleaned_data['end_time']
            classes = scheduled_class.objects.filter(weekday=day,start_time=st,end_time=et).order_by('date')
            weekdays={'monday':0,'teusday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5}

            #if class if already scheduled for that day and time
            if(classes):
                last_date=classes.last().date
                print(last_date)
                cls.date = (last_date+timedelta(days=7))
                print(cls.date)
            else:
                #otherwise calculate next that day(monday/wednesday/friday)'s date
                cls.date = (date.today()+timedelta(days=(weekdays[day]-date.today().weekday())%7))
            #save class in database
            cls.save()

            data = {'slot_confirmed':True,
                    'weekday':day,
                    'start_time':str(form.cleaned_data['start_time']),
                    'end_time':str(form.cleaned_data['end_time']),
                    'date':str(cls.date)}

                                                
                                                
                                                # # send class info email to student


            # sender = 'teacher@domain.com'
            # receivers = ['student@domain.com']

            # # Credentials   

            # password = 'password'

            # message = """From: From Person <teacher@domain.com>
            # To: To Person <student@domain.com>
            # Subject: Class Info

            # Class information is given below:\n\n
            # Name : {}
            # Class Date : {}, ({}),\n
            # Class Timings : {} to {}
            # """.format(form.cleaned_data['student_name'],cls.date,day,st,et)
            
            
            # smtpObj = smtplib.SMTP('localhost')
            # smtpObj.starttls()  
            # smtpObj.login(sender,password)
            # smtpObj.sendmail(sender, receivers, message)

            # smtpObj.quit()
            
                                                # # email code ends here
            
            
            #return json response
            return HttpResponse(json.dumps(data))
    else:
        form = ClassForm
        teacher = schedule["full_name"]
    return render(request,'solution/home.html',{'form':form,'teacher':teacher})