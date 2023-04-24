from django.shortcuts import render, redirect
from .forms import (Applied_Science_Engineering,
Architecture,
Convocation_Office,
Dala_Lana_School_of_Public_Health,
Data_Governance_Group,
Dentistry,
Electrical_Computer_Eng,
Harthouse,
Information,
Health_Policy_Management_Evaluation,
Health_Wellness,
Law,
Mechanical_Industrial_Eng,
Music,
Nursing,
Ontario_Institute_for_Studies_in_Education,
Pharmacy,
Research_Oversight_Compliance,
Rotman,
Social_Work,
UTM,
UTSClibrary,
UTSC,
Anthropology,
Art_History,
Astronomy_Astrophysics,
Cells_and_Systems_Biology,
Chemistry,
Classics,
Computer_Science,
Earth_Sciences,
East_Asian_Studies,
Ecology_and_Evolutionary_Biology,
Economics,
English,
French,
Geography_and_Planning,
Germanic_Language_and_Literature,
History,
Italian_Studies,
Linguistics,
Mathematics,
Near_and_Middle_Eastern_Civilizations,
Philosophy,
Physics,
Political_Science,
Psychology,
Religion,
Slavic_Languages_and_Literatures,
Sociology,
Spanish_and_Portuguese,
Statistical_Sciences,
Centre_for_Jewish_Studies,
Archaeology_Centre,
Asian_Institute,
Canadian_Institute_for_Theoretical_Astrophysics,
Canadian_Statistical_Sciences_Institute_Ontario_Regional_Centre,
d_etude_de_la_Frances_et_du_monde_francophone,
Centre_for_Comparative_Literature,
Centre_for_Criminology_and_Sociolegal_studies,
Centre_for_Diaspora_and_Transnational_studies,
Centre_for_Drama_Theatre_Performance_studies,
Centre_for_Entrepreneurship,
Centre_for_Ethics,
Centre_for_European_Russian_and_Eurasian_studies,
Centre_for_Global_Change_Science,
Centre_for_Global_Social_Policy,
Centre_for_Indigenous_studies,
Centre_for_Industrial_Relations_and_Human_Resources,
Centre_for_Medieval_Studies,
Centre_for_Quantum_Information_and_Quantum_Control,
Centre_for_Quantum_materials,
Centre_for_Research_in_Early_English_Drama,
Centre_for_South_Asian_Studies,
Centre_for_the_Study_of_Global_Japan,
Centre_for_the_study_of_Korea,
Centre_for_the_Study_of_the_United_States,
Cinema_studies,
India_Innovation_Institute,
Institute_for_the_History_and_philosophy_of_science_and_technology,
Institute_of_Islamic_Studies,
Jackman_Humanities_Building,
Koffler_Scientific_Reserve,
Centre_for_Sexual_Diversity_Studies,
Munk_School_of_Global_Affairs_and_PublicPolicy,
Centre_for_Buddhist_Studies,
School_of_Cities,
School_of_Environment,
Statisc_Canada_Research_Data_Centre,
Trudeau_Centre_for_PeaceConflictJustice,
Women_and_Gender_Studies_Institute,
Urban_Studies,
Writing_and_Rhetoric,
African_studies,
Buddhism_psychology_mental_health,
Caribbean_studies,
Equity_studies,
Book_and_Media_Studies,
Celtic_studies,
Christianity_Culture,
Medieval_Studies,
Ethics_Society_Law,
International_Relations,
Canadian_Studies,
Cognitive_Science,
Health_Studies,
Creative_Expression_Society,
Education_Society,
Literature_Critical_Theory,
Material_Culture,
Renaissance_Studies,
Science_and_Society,
Semiotics_and_Communication_Studies,
Digital_Humanities,
Medicine_Admin,
Obstetrics_and_Gynecology,
Family_Community_Medicine,
Anesthesiology_pain_and_Medicine,
Biochemistry,
Biomedical_Engineering,
Immunology,
Laboratory_Medicine_and_Pathobiology,
Medical_Biophysics,
Medical_Imaging,
Institute_Medical_Science,
Molecular_Genetics,
Nutritional_Sciences,
Occupational_Science_and_Occupational_Therapy,
Ophthamalogy_and_Vision_Sciences,
Otolaryngology_Head_and_Neck_Surgery,
Pediatrics,
Pharmacology_and_Toxicology,
Physical_Therapy,
Physiology,
Psychiatry,
Radiation_Oncology,
Rehabilitation,
Speech_Language_Pathology,
Surgery)


from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings


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

def home_page(request):
    return render(request,'redcap_database/home_page.html')  #new

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

def data_governance_group(request):
    form = Data_Governance_Group()
    if request.method == 'POST':
        form = Data_Governance_Group(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Data Governance Group at UofT"
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
    return render(request, 'redcap_database/data_governance_group.html', {'form': form})

def dentistry(request):
    form = Dentistry()
    if request.method == 'POST':
        form = Dentistry(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Faculty of Dentistry"
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
    return render(request, 'redcap_database/dentistry.html', {'form': form})

def electrical_computer_eng(request):
    form = Electrical_Computer_Eng()
    if request.method == 'POST':
        form = Electrical_Computer_Eng(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Electrical & Computer Engineering"
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
    return render(request, 'redcap_database/electrical_computer_eng.html', {'form': form})

def hart_house(request):
    form = Harthouse()
    if request.method == 'POST':
        form = Harthouse(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from Harthouse"
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
    return render(request, 'redcap_database/hart_house.html', {'form': form})

def information(request):
    form = Information()
    if request.method == 'POST':
        form = Information(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Faculty of Information"
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
    return render(request, 'redcap_database/i_school.html', {'form': form})

def health_policy_management_evaluation(request):
    form = Health_Policy_Management_Evaluation()
    if request.method == 'POST':
        form = Health_Policy_Management_Evaluation(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Health Policy Management & Evaluation"
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
    return render(request, 'redcap_database/hpme.html', {'form': form})

def health_wellness(request):
    form = Health_Wellness()
    if request.method == 'POST':
        form = Health_Wellness(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Health & Wellness"
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
    return render(request, 'redcap_database/health_wellness.html', {'form': form})

def law(request):
    form = Law()
    if request.method == 'POST':
        form = Law(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Faculty of Law"
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
    return render(request, 'redcap_database/law.html', {'form': form})

def mechanical_industrial_eng(request):
    form = Mechanical_Industrial_Eng()
    if request.method == 'POST':
        form = Mechanical_Industrial_Eng(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Mechanical Engineering"
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
    return render(request, 'redcap_database/mec_eng.html', {'form': form})

def music(request):
    form = Music()
    if request.method == 'POST':
        form = Music(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Faculty of Music"
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
    return render(request, 'redcap_database/music.html', {'form': form})

def nursing(request):
    form = Nursing()
    if request.method == 'POST':
        form = Nursing(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Faculty of Nursing"
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
    return render(request, 'redcap_database/nursing.html', {'form': form})

def ontario_institute_for_studies_in_education(request):
    form = Ontario_Institute_for_Studies_in_Education()
    if request.method == 'POST':
        form = Ontario_Institute_for_Studies_in_Education(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from OISE"
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
    return render(request, 'redcap_database/oise.html', {'form': form})

def pharmacy(request):
    form = Pharmacy()
    if request.method == 'POST':
        form = Pharmacy(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Faculty of Pharmacy"
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
    return render(request, 'redcap_database/pharmacy.html', {'form': form})

def research_oversight_compliance(request):
    form = Research_Oversight_Compliance()
    if request.method == 'POST':
        form = Research_Oversight_Compliance(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from Harthouse"
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
    return render(request, 'redcap_database/research_oversight_compliance.html', {'form': form})

def rotman(request):
    form = Rotman()
    if request.method == 'POST':
        form = Rotman(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from Rotman School of Commerce"
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
    return render(request, 'redcap_database/rotman.html', {'form': form})

def social_work(request):
    form = Social_Work()
    if request.method == 'POST':
        form = Social_Work(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Faculty of Social Work"
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
    return render(request, 'redcap_database/social_work.html', {'form': form})

def utm(request):
    form = UTM()
    if request.method == 'POST':
        form = UTM(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from University of Toronto Mississauga"
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
    return render(request, 'redcap_database/utm.html', {'form': form})

def utsc_library(request):
    form = UTSClibrary()
    if request.method == 'POST':
        form = UTSClibrary(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the University of Toronto Scarborough Library"
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
    return render(request, 'redcap_database/utsc_library.html', {'form': form})

def utsc(request):
    form = UTSC()
    if request.method == 'POST':
        form = UTSC(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the University of Toronto Scarborough"
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
    return render(request, 'redcap_database/utsc.html', {'form': form})

def anthropology(request):
    form = Anthropology()
    if request.method == 'POST':
        form = Anthropology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Anthropology"
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
    return render(request, 'redcap_database/anthropology.html', {'form': form})

def art_history(request):
    form = Art_History()
    if request.method == 'POST':
        form = Art_History(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Art History"
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
    return render(request, 'redcap_database/art_history.html', {'form': form})

def astronomy_astrophysics(request):
    form = Astronomy_Astrophysics()
    if request.method == 'POST':
        form = Astronomy_Astrophysics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Astronomy & Astrophysics"
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
    return render(request, 'redcap_database/astronomy_astrophysics.html', {'form': form})

def cells_and_systems_biology(request):
    form = Cells_and_Systems_Biology()
    if request.method == 'POST':
        form = Cells_and_Systems_Biology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Cells_and_Systems_Biology"
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
    return render(request, 'redcap_database/cells_and_systems_biology.html', {'form': form})

def chemistry(request):
    form = Chemistry()
    if request.method == 'POST':
        form = Chemistry(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Chemistry"
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
    return render(request, 'redcap_database/chemistry.html', {'form': form})

def classics(request):
    form = Classics()
    if request.method == 'POST':
        form = Classics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Classics"
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
    return render(request, 'redcap_database/classics.html', {'form': form})

def computer_science(request):
    form = Computer_Science()
    if request.method == 'POST':
        form = Computer_Science(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Computer Science"
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
    return render(request, 'redcap_database/computer_science.html', {'form': form})

def earth_sciences(request):
    form = Earth_Sciences()
    if request.method == 'POST':
        form = Earth_Sciences(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Earth Sciences"
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
    return render(request, 'redcap_database/earth_sciences.html', {'form': form})

def east_asian_studies(request):
    form = East_Asian_Studies()
    if request.method == 'POST':
        form = East_Asian_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of East Asian Studies"
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
    return render(request, 'redcap_database/east_asian_studies.html', {'form': form})

def ecology_and_evolutionary_biology(request):
    form = Ecology_and_Evolutionary_Biology()
    if request.method == 'POST':
        form = Ecology_and_Evolutionary_Biology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Ecology and Evolutionary Biology"
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
    return render(request, 'redcap_database/ecology_and_evolutionary_biology.html', {'form': form})

def economics(request):
    form = Economics()
    if request.method == 'POST':
        form = Economics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Economics"
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
    return render(request, 'redcap_database/economics.html', {'form': form})

def english(request):
    form = English()
    if request.method == 'POST':
        form = Englishh(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of English"
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
    return render(request, 'redcap_database/english.html', {'form': form})

def french(request):
    form = French()
    if request.method == 'POST':
        form = French(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of French"
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
    return render(request, 'redcap_database/french.html', {'form': form})

def geography_and_planning(request):
    form = Geography_and_Planning()
    if request.method == 'POST':
        form = Geography_and_Planning(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Geography & Planning"
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
    return render(request, 'redcap_database/geography_and_planning.html', {'form': form})

def germanic_language_and_literature(request):
    form = Germanic_Language_and_Literature()
    if request.method == 'POST':
        form = Germanic_Language_and_Literature(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Germanic Language & Literature"
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
    return render(request, 'redcap_database/germanic_language_and_literature.html', {'form': form})

def history(request):
    form = History()
    if request.method == 'POST':
        form = History(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of History"
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
    return render(request, 'redcap_database/history.html', {'form': form})

def italian_studies(request):
    form = Italian_Studies()
    if request.method == 'POST':
        form = Italian_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Italian Studies"
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
    return render(request, 'redcap_database/italian_studies.html', {'form': form})

def linguistics(request):
    form = Linguistics()
    if request.method == 'POST':
        form = Linguistics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Linguistics"
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
    return render(request, 'redcap_database/linguistics.html', {'form': form})

def mathematics(request):
    form = Mathematics()
    if request.method == 'POST':
        form = Mathematics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Mathematics"
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
    return render(request, 'redcap_database/mathematics.html', {'form': form})

def near_and_middle_eastern_civilizations(request):
    form = Near_and_Middle_Eastern_Civilizations()
    if request.method == 'POST':
        form = Near_and_Middle_Eastern_Civilizations(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Near and Middle Eastern Civilizations"
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
    return render(request, 'redcap_database/nmec.html', {'form': form})

def philosophy(request):
    form = Philosophy()
    if request.method == 'POST':
        form = Philosophy(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Philosophy"
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
    return render(request, 'redcap_database/philosophy.html', {'form': form})

def physics(request):
    form = Physics()
    if request.method == 'POST':
        form = Physics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Physics"
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
    return render(request, 'redcap_database/physics.html', {'form': form})

def political_science(request):
    form = Political_Science()
    if request.method == 'POST':
        form = Political_Science(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Political Science"
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
    return render(request, 'redcap_database/political_science.html', {'form': form})

def psychology(request):
    form = Psychology()
    if request.method == 'POST':
        form = Psychology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Psychology"
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
    return render(request, 'redcap_database/psychology.html', {'form': form})

def religion(request):
    form = Religion()
    if request.method == 'POST':
        form = Religion(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Religion"
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
    return render(request, 'redcap_database/religion.html', {'form': form})

def slavic_languages_and_literatures(request):
    form = Slavic_Language_and_Literatures()
    if request.method == 'POST':
        form = Slavic_Language_and_Literatures(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Slavic Languages and Literatures"
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
    return render(request, 'redcap_database/slavic_languages_and_literatures.html', {'form': form})

def sociology(request):
    form = Sociology()
    if request.method == 'POST':
        form = Sociology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Sociology"
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
    return render(request, 'redcap_database/sociology.html', {'form': form})

def spanish_and_portuguese(request):
    form = Spanish_and_Portuguese()
    if request.method == 'POST':
        form = Spanish_and_Portuguese(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Spanish & Spanish_and_Portuguese"
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
    return render(request, 'redcap_database/spanish_and_portuguese.html', {'form': form})

def statistical_sciences(request):
    form = Statistical_Sciences()
    if request.method == 'POST':
        form = Statistical_Sciences(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Statistical Sciences"
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
    return render(request, 'redcap_database/statistical_sciences.html', {'form': form})

def centre_for_jewish_studies(request):
    form = Centre_for_Jewish_Studies()
    if request.method == 'POST':
        form = Centre_for_Jewish_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Jewish Studies"
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
    return render(request, 'redcap_database/centre_for_jewish_studies.html', {'form': form})

def archaeology_centre(request):
    form = Archaeology_Centre()
    if request.method == 'POST':
        form = Archaeology_Centre(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Archaeology Centre"
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
    return render(request, 'redcap_database/archaeology_centre.html', {'form': form})

def asian_institute(request):
    form = Asian_Institute()
    if request.method == 'POST':
        form = Asian_Institute(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Asian Institute"
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
    return render(request, 'redcap_database/asian_institute.html', {'form': form})

def canadian_institute_for_theoretical_astrophysics(request):
    form = Canadian_Institute_for_Theoretical_Astrophysics()
    if request.method == 'POST':
        form = Canadian_Institute_for_Theoretical_Astrophysics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Canadian Institute for Theoretical Astrophysics"
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
    return render(request, 'redcap_database/canadian_institute_for_theoretical_astrophysics.html', {'form': form})

def canadian_statistical_sciences_institute_ontario_regional_centre(request):
    form = Canadian_Statistical_Sciences_Institute_Ontario_Regional_Centre()
    if request.method == 'POST':
        form = Canadian_Statistical_Sciences_Institute_Ontario_Regional_Centre(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Canadian Statistical Sciences Institute Ontario Regional Centre"
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
    return render(request, 'redcap_database/canadian_statistical_sciences_institute_ontario_regional_centre.html', {'form': form})

def d_etude_de_la_frances_et_du_monde_francophone(request):
    form = d_etude_de_la_Frances_et_du_monde_francophone()
    if request.method == 'POST':
        form = d_etude_de_la_Frances_et_du_monde_francophone(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the d'etude de la Frances et du monde francophone"
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
    return render(request, 'redcap_database/d_francophone.html', {'form': form})

def centre_for_comparative_literature(request):
    form = Centre_for_Comparative_Literature()
    if request.method == 'POST':
        form = Centre_for_Comparative_Literature(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Comparative Literature"
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
    return render(request, 'redcap_database/centre_for_comparative_literature.html', {'form': form})

def centre_for_criminology_and_sociolegal_studies(request):
    form = Centre_for_Criminology_and_Sociolegal_studies()
    if request.method == 'POST':
        form = Centre_for_Criminology_and_Sociolegal_studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Criminology and Sociolegal studies"
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
    return render(request, 'redcap_database/centre_for_criminology_and_sociolegal_studies.html', {'form': form})

def centre_for_diaspora_and_transnational_studies(request):
    form = Centre_for_Diaspora_and_Transnational_studies()
    if request.method == 'POST':
        form = Centre_for_Diaspora_and_Transnational_studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Diaspora and Transnational studies"
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
    return render(request, 'redcap_database/centre_for_diaspora_and_transnational_studies.html', {'form': form})

def centre_for_drama_theatre_performance_studies(request):
    form = Centre_for_Drama_Theatre_Performance_studies()
    if request.method == 'POST':
        form = Centre_for_Drama_Theatre_Performance_studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Drama & Theatre Performance studies"
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
    return render(request, 'redcap_database/centre_for_drama_theatre_performance_studies.html', {'form': form})

def centre_for_entrepreurship(request):
    form = Centre_for_Entrepreneurship()
    if request.method == 'POST':
        form = Centre_for_Entrepreneurship(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Entrepreneurship"
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
    return render(request, 'redcap_database/centre_for_entrepreurship.html', {'form': form})

def centre_for_ethics(request):
    form = Centre_for_Ethics()
    if request.method == 'POST':
        form = Centre_for_Ethics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Ethics"
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
    return render(request, 'redcap_database/centre_for_ethics.html', {'form': form})


def centre_for_european_russion_eurasian_studies(request):
    form = Centre_for_European_Russian_and_Eurasian_studies()
    if request.method == 'POST':
        form = Centre_for_European_Russian_and_Eurasian_studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Ethics"
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
    return render(request, 'redcap_database/centre_for_european_russion_eurasian_studies.html', {'form': form})

def centre_for_global_change_science(request):
    form = Centre_for_Global_Change_Science()
    if request.method == 'POST':
        form = Centre_for_Global_Change_Science(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Global Change Science"
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
    return render(request, 'redcap_database/centre_for_global_change_science.html', {'form': form})

def centre_for_global_social_policy(request):
    form = Centre_for_Global_Social_Policy()
    if request.method == 'POST':
        form = Centre_for_Global_Social_Policy(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Global Social Policy"
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
    return render(request, 'redcap_database/centre_for_global_social_policy.html', {'form': form})

def centre_for_indigenous_studies(request):
    form = Centre_for_Indigenous_studies()
    if request.method == 'POST':
        form = Centre_for_Indigenous_studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Indigenous Studies"
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
    return render(request, 'redcap_database/centre_for_indigenous_studies.html', {'form': form})

def centre_for_industrial_relations_and_human_resources(request):
    form = Centre_for_Industrial_Relations_and_Human_Resources()
    if request.method == 'POST':
        form = Centre_for_Industrial_Relations_and_Human_Resources(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Industrial Relations and Human Resources"
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
    return render(request, 'redcap_database/centre_for_industrial_relations_and_human_resources.html', {'form': form})

def centre_for_medieval_studies(request):
    form = Centre_for_Medieval_Studies()
    if request.method == 'POST':
        form = Centre_for_Medieval_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Medieval Studies"
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
    return render(request, 'redcap_database/centre_for_medieval_studies.html', {'form': form})

def centre_for_quantum_information_and_quantum_control(request):
    form = Centre_for_Quantum_Information_and_Quantum_Control()
    if request.method == 'POST':
        form = Centre_for_Quantum_Information_and_Quantum_Control(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Quantum Information & Quantum Control"
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
    return render(request, 'redcap_database/centre_for_quantum_information_and_quantum_control.html', {'form': form})

def centre_for_quantum_materials(request):
    form = Centre_for_Quantum_materials()
    if request.method == 'POST':
        form = Centre_for_Quantum_materials(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Quantum Materials"
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
    return render(request, 'redcap_database/centre_for_quantum_materials.html', {'form': form})

def centre_for_research_in_early_english_drama(request):
    form = Centre_for_Research_in_Early_English_Drama()
    if request.method == 'POST':
        form = Centre_for_Research_in_Early_English_Drama(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Research in Early English Drama"
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
    return render(request, 'redcap_database/centre_for_research_in_early_english_drama.html', {'form': form})

def centre_for_south_asian_studies(request):
    form = Centre_for_South_Asian_Studies()
    if request.method == 'POST':
        form = Centre_for_South_Asian_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for South Asian Studies"
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
    return render(request, 'redcap_database/centre_for_south_asian_studies.html', {'form': form})

def centre_for_the_study_of_global_japan(request):
    form = Centre_for_the_Study_of_Global_Japan()
    if request.method == 'POST':
        form = Centre_for_the_Study_of_Global_Japan(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for the Study of Global Japan"
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
    return render(request, 'redcap_database/centre_for_the_study_of_global_japan.html', {'form': form})

def centre_for_the_study_of_korea(request):
    form = Centre_for_the_study_of_Korea()
    if request.method == 'POST':
        form = Centre_for_the_study_of_Korea(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for the Study of Korea"
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
    return render(request, 'redcap_database/centre_for_the_study_of_korea.html', {'form': form})

def centre_for_the_study_of_the_united_states(request):
    form = Centre_for_the_Study_of_the_United_States()
    if request.method == 'POST':
        form = Centre_for_the_Study_of_the_United_States(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for the Study of the United States"
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
    return render(request, 'redcap_database/centre_for_the_study_of_the_united_states.html', {'form': form})

def cinema_studies(request):
    form = Cinema_studies()
    if request.method == 'POST':
        form = Cinema_studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Cinema Studies"
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
    return render(request, 'redcap_database/cinema_studies.html', {'form': form})

def india_innovation_institute(request):
    form = India_Innovation_Institute()
    if request.method == 'POST':
        form = India_Innovation_Institute(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Indian Innovation Institute"
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
    return render(request, 'redcap_database/india_innovation_institute.html', {'form': form})

def institute_for_the_history_and_philosophy_of_science_and_technology(request):
    form = Institute_for_the_History_and_philosophy_of_science_and_technology()
    if request.method == 'POST':
        form = Institute_for_the_History_and_philosophy_of_science_and_technology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Institute for the History and Philosophy of Science and Technology"
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
    return render(request, 'redcap_database/institute_for_the_history_and_philosophy_of_science_and_technology.html', {'form': form})

def institute_of_islamic_studies(request):
    form = Institute_of_Islamic_Studies()
    if request.method == 'POST':
        form = Institute_of_Islamic_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Institute of Islamic Studies"
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
    return render(request, 'redcap_database/institute_of_islamic_studies.html', {'form': form})

def jackman_humanities_building(request):
    form = Jackman_Humanities_Building()
    if request.method == 'POST':
        form = Jackman_Humanities_Building(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Jackman Humanities Building"
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
    return render(request, 'redcap_database/jackman_humanities_building.html', {'form': form})

def koffler_scientific_reserve(request):
    form = Koffler_Scientific_Reserve()
    if request.method == 'POST':
        form = Koffler_Scientific_Reserve(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Koffler Scientific Reserve"
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
    return render(request, 'redcap_database/koffler_scientific_reserve.html', {'form': form})

def munk_school_of_global_affairs_and_publicpolicy(request):
    form = Munk_School_of_Global_Affairs_and_PublicPolicy()
    if request.method == 'POST':
        form = Munk_School_of_Global_Affairs_and_PublicPolicy(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for the Munk School of Global Affairs"
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
    return render(request, 'redcap_database/munk_school_of_global_affairs_and_publicpolicy.html', {'form': form})

def centre_for_buddhist_studies(request):
    form = Centre_for_Buddhist_Studies()
    if request.method == 'POST':
        form = Centre_for_Buddhist_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for Buddhist Studies"
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
    return render(request, 'redcap_database/centre_for_buddhist_studies.html', {'form': form})

def school_of_cities(request):
    form = School_of_Cities()
    if request.method == 'POST':
        form = School_of_Cities(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the School of Cities"
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
    return render(request, 'redcap_database/school_of_cities.html', {'form': form})

def school_of_environment(request):
    form = School_of_Environment()
    if request.method == 'POST':
        form = School_of_Environment(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for the School of Environment"
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
    return render(request, 'redcap_database/school_of_environment.html', {'form': form})

def statistisc_canada_research_data_centre(request):
    form = Statisc_Canada_Research_Data_Centre()
    if request.method == 'POST':
        form = Statisc_Canada_Research_Data_Centre(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Centre for the Statistics Canada Research Data Centre"
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
    return render(request, 'redcap_database/statistisc_canada_research_data_centre.html', {'form': form})

def trudeau_centre_for_peaceconflictjustice(request):
    form = Trudeau_Centre_for_PeaceConflictJustice()
    if request.method == 'POST':
        form = Trudeau_Centre_for_PeaceConflictJustice(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Trudeau Centre for Peace, Conflict & Justice"
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
    return render(request, 'redcap_database/trudeau_centre_for_peaceconflictjustice.html', {'form': form})

def women_and_gender_studies_institute(request):
    form = Women_and_Gender_Studies_Institute()
    if request.method == 'POST':
        form = Women_and_Gender_Studies_Institute(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Women and Gender Studies Institute"
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
    return render(request, 'redcap_database/women_and_gender_studies_institute.html', {'form': form})

def urban_studies(request):
    form = Urban_Studies()
    if request.method == 'POST':
        form = Urban_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Urban Studies"
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
    return render(request, 'redcap_database/urban_studies.html', {'form': form})

def writing_and_rhetoric(request):
    form = Writing_and_Rhetoric()
    if request.method == 'POST':
        form = Writing_and_Rhetoric(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Writing and Rhetoric"
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
    return render(request, 'redcap_database/writing_and_rhetoric.html', {'form': form})

def african_studies(request):
    form = African_studies()
    if request.method == 'POST':
        form = African_studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of African Studies"
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
    return render(request, 'redcap_database/african_studies.html', {'form': form})

def buddhism_psychology_mental_health(request):
    form = Buddhism_psychology_mental_health()
    if request.method == 'POST':
        form = Buddhism_psychology_mental_health(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Buddhism Psychology & Mental Health"
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
    return render(request, 'redcap_database/buddhism_psychology_mental_health.html', {'form': form})

def caribbean_studies(request):
    form = Caribbean_studies()
    if request.method == 'POST':
        form = Caribbean_studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Caribbean Studies"
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
    return render(request, 'redcap_database/caribbean_studies.html', {'form': form})

def equity_studies(request):
    form = Equity_Studies()
    if request.method == 'POST':
        form = Equity_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Equity Studies"
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
    return render(request, 'redcap_database/equity_studies.html', {'form': form})

def book_and_media_studies(request):
    form = Book_and_Media_Studies()
    if request.method == 'POST':
        form = Book_and_Media_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Book & Media Studies"
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
    return render(request, 'redcap_database/book_and_media_studies.html', {'form': form})

def celtic_studies(request):
    form = Celtic_Studies()
    if request.method == 'POST':
        form = Celtic_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Celtic Studies"
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
    return render(request, 'redcap_database/celtic_studies.html', {'form': form})

def christianity_culture(request):
    form = Christianity_Culture()
    if request.method == 'POST':
        form = Christianity_Culture(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Christianity and Culture"
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
    return render(request, 'redcap_database/christianity_culture.html', {'form': form})

def medieval_studies(request):
    form = Medieval_Studies()
    if request.method == 'POST':
        form = Urban_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Medieval Studies"
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
    return render(request, 'redcap_database/medieval_studies.html', {'form': form})

def ethics_society_law(request):
    form = Ethics_Society_Law()
    if request.method == 'POST':
        form = Ethics_Society_Law(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Ethics, Society & Law"
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
    return render(request, 'redcap_database/ethics_society_law.html', {'form': form})

def international_relations(request):
    form = International_Relations()
    if request.method == 'POST':
        form = International_Relations(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of International Relations"
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
    return render(request, 'redcap_database/international_relations.html', {'form': form})

def canadian_studies(request):
    form = Canadian_Studies()
    if request.method == 'POST':
        form = Canadian_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Canadian Studies"
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
    return render(request, 'redcap_database/canadian_studies.html', {'form': form})

def cognitive_science(request):
    form = Cognitive_Science_Studies()
    if request.method == 'POST':
        form = Cognitive_Science(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Cognitive Science"
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
    return render(request, 'redcap_database/cognitive_science.html', {'form': form})

def health_studies(request):
    form = Health_Studies()
    if request.method == 'POST':
        form = Health_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Health Studies"
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
    return render(request, 'redcap_database/health_studies.html', {'form': form})

def creative_expression_society(request):
    form = Creative_Expression_Society()
    if request.method == 'POST':
        form = Creative_Expression_Society(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of the Creative Expression Society"
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
    return render(request, 'redcap_database/creative_expression_society.html', {'form': form})

def education_society(request):
    form = Education_Society()
    if request.method == 'POST':
        form = Education_Society(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Education Society"
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
    return render(request, 'redcap_database/education_society.html', {'form': form})

def literature_critical_theory(request):
    form = Literature_Critical_Theory()
    if request.method == 'POST':
        form = Literature_Critical_Theory(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Literature & Critical Theory"
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
    return render(request, 'redcap_database/literature_critical_theory.html', {'form': form})

def material_culture(request):
    form = Material_Culture()
    if request.method == 'POST':
        form = Material_Culture(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Material Culture"
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
    return render(request, 'redcap_database/material_culture.html', {'form': form})

def renaissance_studies(request):
    form = Renaissance_Studies()
    if request.method == 'POST':
        form = Renaissance_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Renaissance Studies"
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
    return render(request, 'redcap_database/renaissance_studies.html', {'form': form})

def science_and_society(request):
    form = Science_and_Society()
    if request.method == 'POST':
        form = Science_and_Society(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Science and Society"
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
    return render(request, 'redcap_database/science_and_society.html', {'form': form})

def semiotics_and_communication_studies(request):
    form = Semiotics_and_Communication_Studies()
    if request.method == 'POST':
        form = Semiotics_and_Communication_Studies(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Semiotics and Communication Studies"
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
    return render(request, 'redcap_database/semiotics_and_communication_studies.html', {'form': form})

def digitial_humanities(request):
    form = Digital_Humanities()
    if request.method == 'POST':
        form = Digital_Humanities(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Digital Humanities"
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
    return render(request, 'redcap_database/digital_humanities.html', {'form': form})

def medicine_admin(request):
    form = Medicine_Admin()
    if request.method == 'POST':
        form = Medicine_Admin(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Administrative section of the Faculty of Medicine"
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
    return render(request, 'redcap_database/medicine_admin.html', {'form': form})

def obstetrics_and_gynecology(request):
    form = Obstetrics_and_Gynecology()
    if request.method == 'POST':
        form = Obstetrics_and_Gynecology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Obstetrics and Gynecology"
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
    return render(request, 'redcap_database/obstetrics_and_gynecology.html', {'form': form})

def family_community_medicine(request):
    form = Family_Community_Medicine()
    if request.method == 'POST':
        form = Family_Community_Medicine(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Family & Community Medicine"
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
    return render(request, 'redcap_database/family_community_medicine.html', {'form': form})

def anesthesiology_pain_and_medicine(request):
    form = Anesthesiology_pain_and_Medicine()
    if request.method == 'POST':
        form = Anesthesiology_pain_and_Medicine(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Anesthesiology Pain & Medicine"
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
    return render(request, 'redcap_database/anesthesiology_pain_and_medicine.html', {'form': form})

def biochemistry(request):
    form = Biochemistry()
    if request.method == 'POST':
        form = Biochemistry(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Biochemistry"
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
    return render(request, 'redcap_database/biochemistry.html', {'form': form})

def biomedical_engineering(request):
    form = Biomedical_Engineering()
    if request.method == 'POST':
        form = Biomedical_Engineering(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Biomedical Engineering"
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
    return render(request, 'redcap_database/biomedical_engineering.html', {'form': form})

def immunology(request):
    form = Immunology()
    if request.method == 'POST':
        form = Immunology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Immunology"
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
    return render(request, 'redcap_database/immunology.html', {'form': form})

def laboratory_medicine_and_pathobiology(request):
    form = Laboratory_Medicine_and_Pathobiology()
    if request.method == 'POST':
        form = Laboratory_Medicine_and_Pathobiology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Laboratory Medicine & Pathobiology"
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
    return render(request, 'redcap_database/laboratory_medicine_and_pathobiology.html', {'form': form})

def medical_biophysics(request):
    form = medical_biophysics()
    if request.method == 'POST':
        form = medical_biophysics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Medical Biophysics"
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
    return render(request, 'redcap_database/medical_biophysics.html', {'form': form})

def medical_imaging(request):
    form = Medical_Imaging()
    if request.method == 'POST':
        form = Medical_Imaging(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Medical Imaging"
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
    return render(request, 'redcap_database/medical_imaging.html', {'form': form})

def institute_of_medical_science(request):
    form = Institute_Medical_Science()
    if request.method == 'POST':
        form = Institute_Medical_Science(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Institute of Medical Science"
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
    return render(request, 'redcap_database/institute_of_medical_science.html', {'form': form})

def molecular_genetics(request):
    form = Molecular_Genetics()
    if request.method == 'POST':
        form = Molecular_Genetics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Molecular_Genetics"
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
    return render(request, 'redcap_database/molecular_genetics.html', {'form': form})

def nutritional_sciences(request):
    form = Nutritional_Sciences()
    if request.method == 'POST':
        form = Nutritional_Sciences(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Nutritional Sciences"
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
    return render(request, 'redcap_database/nutritional_sciences.html', {'form': form})

def occupational_science_and_occupational_therapy(request):
    form = Occupational_Science_and_Occupational_Therapy()
    if request.method == 'POST':
        form = Occupational_Science_and_Occupational_Therapy(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Occupational Science & Occupational Therapy"
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
    return render(request, 'redcap_database/occupational_science_and_occupational_therapy.html', {'form': form})

def opthamalogy_and_vision_sciences(request):
    form = Ophthamalogy_and_Vision_Sciences()
    if request.method == 'POST':
        form = Ophthamalogy_and_Vision_Sciences(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Opthamalogy and Vision Sciences"
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
    return render(request, 'redcap_database/opthamalogy_and_vision_sciences.html', {'form': form})

def otolarynology_head_and_neck_surgery(request):
    form = Otolaryngology_Head_and_Neck_Surgery()
    if request.method == 'POST':
        form = Otolaryngology_Head_and_Neck_Surgery(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Otolaryngology, Head and Neck Surgery"
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
    return render(request, 'redcap_database/otolarynology_head_and_neck_surgery.html', {'form': form})

def pediatrics(request):
    form = Pediatrics()
    if request.method == 'POST':
        form = Pediatrics(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Pediatrics"
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
    return render(request, 'redcap_database/pediatrics.html', {'form': form})

def pharmacology_and_toxicology(request):
    form = Pharmacology_and_Toxicology()
    if request.method == 'POST':
        form = Pharmacology_and_Toxicology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Pharmacology & Toxicology"
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
    return render(request, 'redcap_database/pharmacology_and_toxicology.html', {'form': form})

def physical_therapy(request):
    form = Physical_Therapy()
    if request.method == 'POST':
        form = Physical_Therapy(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Physical Therapy"
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
    return render(request, 'redcap_database/physical_therapy.html', {'form': form})

def physiology(request):
    form = Physiology()
    if request.method == 'POST':
        form = Physiology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Physiology"
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
    return render(request, 'redcap_database/physiology.html', {'form': form})

def psychiatry(request):
    form = Psychiatry()
    if request.method == 'POST':
        form = Psychiatry(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Psychiatry"
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
    return render(request, 'redcap_database/psychiatry.html', {'form': form})

def radiation_oncology(request):
    form = Radiation_Oncology()
    if request.method == 'POST':
        form = Radiation_Oncology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Radiation Oncology"
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
    return render(request, 'redcap_database/radiation_oncology.html', {'form': form})

def rehabilitation(request):
    form = Rehabilitation()
    if request.method == 'POST':
        form = Rehabilitation(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Rehabilitation"
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
    return render(request, 'redcap_database/rehabilitation.html', {'form': form})

def speech_language_pathology(request):
    form = Speech_Language_Pathology()
    if request.method == 'POST':
        form = Speech_Language_Pathology(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Speech Language & Pathology"
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
    return render(request, 'redcap_database/speech_language_pathology.html', {'form': form})

def surgery(request):
    form = Surgery()
    if request.method == 'POST':
        form = Surgery(request.POST)
        if form.is_valid():
            form.save()
            subject = "REDCap request from the Department of Surgery"
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
    return render(request, 'redcap_database/surgery.html', {'form': form})
