from django.shortcuts import render, redirect
from .forms import (Applied_Science_Engineering,
Architecture,
Convocation_Office,
Dala_Lana_School_of_Public_Health)
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def test_datalist(request):
    return render(request,'redcap_database/test_datalist.html')

def applied_science_engineering(request):
    form = Applied_Science_Engineering()
    if request.method == 'POST':
        form = Applied_Science_Engineering(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Faculty of Applied Science and Engineering"
            first_name = request.POST.get("first_name", "")
            last_name = request.POST.get("last_name", "")
            mfa_use = request.POST.get("mfa_use", "")
            usage_type = request.POST.get("usage_type", "")
            email = request.POST.get("email", "")
            utorid = request.POST.get("utorid", "")
            project_start = request.POST.get("project_begin", "")
            project_end = request.POST.get("project_end", "")
            date = request.POST.get("date", "")

            body = [mfa_use,usage_type,date,project_start,project_end,email,utorid,first_name,last_name]
            separator = ','
            message = separator.join(body)
            from_email = settings.EMAIL_HOST_USER
            receiving_email = ['redcapdb@zohomail.com']

            send_mail(
                subject,
                message,
                from_email,
                receiving_email,
                fail_silently = False)
            return HttpResponse('success')
    return render(request, 'redcap_database/applied_science_engineering_edit.html', {'form': form})

def architecture(request):
    form = Architecture()
    if request.method == 'POST':
        form = Architecture(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Faculty of Architecture"
            first_name = request.POST.get("first_name", "")
            last_name = request.POST.get("last_name", "")
            mfa_use = request.POST.get("mfa_use", "")
            usage_type = request.POST.get("usage_type", "")
            email = request.POST.get("email", "")
            utorid = request.POST.get("utorid", "")
            project_start = request.POST.get("project_begin", "")
            project_end = request.POST.get("project_end", "")
            date = request.POST.get("date", "")

            body = [mfa_use,usage_type,date,project_start,project_end,email,utorid,first_name,last_name]
            separator = ','
            message = separator.join(body)
            from_email = settings.EMAIL_HOST_USER
            receiving_email = ['redcapdb@zohomail.com']

            send_mail(
                subject,
                message,
                from_email,
                receiving_email,
                fail_silently = False)
            return HttpResponse('success')
    return render(request, 'redcap_database/architecture.html', {'form': form})

def convocation_office(request):
    form = Convocation_Office()
    if request.method == 'POST':
        form = Convocation_Office(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Convocation Office"
            first_name = request.POST.get("first_name", "")
            last_name = request.POST.get("last_name", "")
            mfa_use = request.POST.get("mfa_use", "")
            usage_type = request.POST.get("usage_type", "")
            email = request.POST.get("email", "")
            utorid = request.POST.get("utorid", "")
            project_start = request.POST.get("project_begin", "")
            project_end = request.POST.get("project_end", "")
            date = request.POST.get("date", "")

            body = [mfa_use,usage_type,date,project_start,project_end,email,utorid,first_name,last_name]
            separator = ','
            message = separator.join(body)
            from_email = settings.EMAIL_HOST_USER
            receiving_email = ['redcapdb@zohomail.com']

            send_mail(
                subject,
                message,
                from_email,
                receiving_email,
                fail_silently = False)
            return HttpResponse('success')
    return render(request, 'redcap_database/convocation_office.html', {'form': form})

def dala_lana_school_of_public_health(request):
    form = Dala_Lana_School_of_Public_Health()
    if request.method == 'POST':
        form = Dala_Lana_School_of_Public_Health(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Dalla Lana School of Public Health"
            first_name = request.POST.get("first_name", "")
            last_name = request.POST.get("last_name", "")
            mfa_use = request.POST.get("mfa_use", "")
            usage_type = request.POST.get("usage_type", "")
            email = request.POST.get("email", "")
            utorid = request.POST.get("utorid", "")
            project_start = request.POST.get("project_begin", "")
            project_end = request.POST.get("project_end", "")
            date = request.POST.get("date", "")

            body = [mfa_use,usage_type,date,project_start,project_end,email,utorid,first_name,last_name]
            separator = ','
            message = separator.join(body)
            from_email = settings.EMAIL_HOST_USER
            receiving_email = ['redcapdb@zohomail.com']

            send_mail(
                subject,
                message,
                from_email,
                receiving_email,
                fail_silently = False)
            return HttpResponse('success')
    return render(request, 'redcap_database/dlsph.html', {'form': form})
