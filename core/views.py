from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Contact, Project, Service, SiteSetting, Skill


def home(request):

    setting = SiteSetting.objects.first()
    skills = Skill.objects.all()
    services = Service.objects.all()
    projects = Project.objects.filter(featured=True)

    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        messages.success(
            request,
            "Your message has been sent successfully."
        )

        return redirect("home")

    context = {
        "setting": setting,
        "skills": skills,
        "services": services,
        "projects": projects,
    }

    return render(request, "index.html", context)