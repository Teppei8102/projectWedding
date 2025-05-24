from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import EntryForm,FavoriteModel,GalleryModel
from .forms import EntryFormForm
#region Const
TITLE = 'SEKIRECORDS'
#endregion

#region Home
def GoHome(request):
    context = {
        "title":TITLE,
        "isFooterVisible":False,
    }
    return render(request,'home.html',context)
#endregion

#region Access
def GoAccess(request):
    message = {
        "title":TITLE,
        "isFooterVisible":False,
    }
    return render(request,'access.html',message)
#endregion

#region Gallery
def GoGallery(request):
    image_list = GalleryModel.objects.all()
    message = {
        "title":TITLE,
        "isFooterVisible":False,
        "image":image_list,
    }
    return render(request,'gallery.html',message)
#endregion

#region Favorite
def GoFavorite(request):
    artist_list = FavoriteModel.objects.all()
    message = {
        "title":TITLE,
        "isFooterVisible":False,
        "artist":artist_list,
    }
    return render(request,'favorite.html',message)
#endregion

#region Form
class FormView(View):
    def get(self, request, *args, **kwargs):
        context = {
        "title":TITLE,
        "isFooterVisible":False,
        "prefectures":[ p[0] for p in EntryForm.prefecture.field.choices ]
        }
        return render(request,"form.html",context)

    def post(self, request, *args, **kwargs):
        form = EntryFormForm(data=request.POST)
        if form.is_valid():
            model = EntryForm()
            model.attendance = (request.POST.get('attendance') == 'True')
            model.nameFamily = form.cleaned_data['nameFamily']
            model.nameFirst = form.cleaned_data['nameFirst']
            model.nameHFamily = form.cleaned_data['nameHFamily']
            model.nameHFirst = form.cleaned_data['nameHFirst']
            model.telNumber = form.cleaned_data['telNumber']
            model.email = form.cleaned_data['email']
            model.postalCode = form.cleaned_data['postalCode']
            model.prefecture = form.cleaned_data['prefecture']
            model.city = form.cleaned_data['city']
            model.streetAddress = form.cleaned_data['streetAddress']
            model.building = form.cleaned_data['building']
            model.allergy = form.cleaned_data['allergy']
            model.bus = (request.POST.get('bus') == 'True')
            model.save()
            form.save()
            return HttpResponseRedirect(".")
        else:
            return render(request,"form.html",form.errors)
index = FormView.as_view()

def GoForm(request):
    context = {
        "title":TITLE,
        "isFooterVisible":False,
        "prefectures":[ p[0] for p in EntryForm.prefecture.field.choices ]
    }
    return render(request,'form.html',context)






#endregion

#region Ticket
def GoTicket(request):
    message = {
        "title":TITLE,
        "isFooterVisible":False,
    }
    return render(request,'ticket.html',message)
#endregion

#region TicketEntry
def GoTicketEntry(request):
    message = {
        "title":TITLE,
        "isFooterVisible":False,
    }
    return render(request,'ticket_entry.html',message)
#endregion

#region Profile
def GoProfile(request):
    message = {
        "title":TITLE,
        "isFooterVisible":False,
    }
    return render(request,'profile.html',message)
#endregion