from django.shortcuts import render, redirect
from .models import About, Team, Contact, Plan, Mails, Emails
from django.contrib.auth.models import User, auth
from django.contrib import messages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.
def home(request):
    request.session['is_login'] = False
    try:
        if request.method=='POST' and 'sendmail' in request.POST:
            Sender_Name = request.POST['name']
            Sender_Email = request.POST['sender']
            Sender_Message = request.POST['message']

            sender_address = 'mysmtp@primusglobalgh.com'
            sender_password = 'ZOOFi7pxIZhv'
            receiver_address = 'pmxshare@gmail.com'

            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Message From Biwas Page'
            message.attach(MIMEText(f'Sender Name: {Sender_Name}, \nSenders Email: {Sender_Email}, \nMessage: {Sender_Message}', 'plain'))

            session = smtplib.SMTP('mail.primusglobalgh.com', 587)
            session.starttls()
            session.login(sender_address, sender_password)

            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()


            
            # name = request.POST['name']
            # sender = request.POST['sender']
            # message = request.POST['message']
            # SendMail = Mails()
            # SendMail.name = name
            # SendMail.sender = sender
            # SendMail.message = message
            # SendMail.save()

            return render(request, 'index.html', {'msg': 'Message Delivered!'})

        about = About.objects.get(id=1)
        teams = Team.objects.all()
        contact = Contact.objects.get(id=1)
        plans = Plan.objects.all()
        return render(request, 'index.html', {'about':about, 'teams':teams, 'contact':contact, 'plans':plans})
    except Exception as err:
        return render(request, 'index.html')
    
def register(request):
    if request.method == 'POST' and 'register' in request.POST:
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        usrname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        pwdConfirm = request.POST['confirm_password']

        if pwd == pwdConfirm:
            UserObj = User.objects.create_user(first_name=fn, last_name=ln, email=email, username=usrname, password=pwd)
            UserObj.save()

            return redirect('/')
        else:
            return render(request, 'register.html', {'message':'Password mismatch!'})
            #return messages.info(request, 'Password mismatch!')
        
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST['username']
        password = request.POST['password']

        UserObj = auth.authenticate(username=username, password=password)
        if UserObj is not None:
            request.session['is_login'] = True
            request.session['signin_name'] = username
            return render(request, 'login.html', {'is_login':True})

    return render(request, 'login.html', {'is_login':False})

def logout(request):
    request.session['is_login'] = False
    auth.logout(request)
    return redirect('/')

def email(request):
    is_login = request.session.get('is_login')
    if is_login:
        emailObj = Mails.objects.all()
        # emails = Emails()
        # lstemails = list()
        # count = 0
        # for email in emailObj:
        #     count += 1
        #     emails.id = count
        #     emails.name = email.name
        #     emails.sender = email.sender
        #     emails.message = email.message
        #     lstemails.append(emails)
        signin_name = request.session.get('signin_name')
        return render(request, 'emails.html', {'emails':emailObj, 'signin_name':signin_name})
    else:
        return render(request, 'emails.html', {'error': "You don't have the rights to view this page!!" })