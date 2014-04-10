from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
# Create your views here.


def home(request):
    return render_to_response("index.html",
                       locals(),
                       context_instance=RequestContext(request))

def about(request):
        
    return render_to_response("aboutus.html",
                              locals(),
                              context_instance=RequestContext(request))

def services(request):
        
    return render_to_response("services.html",
                              locals(),
                              context_instance=RequestContext(request))

def contact(request):
    if request.method='POST':
        formdata = request.POST
        if formdata.is_valid():
            from django.core.mail import send_mail
            subject = formdata.cleaned_data['subject']
            message = formdata.cleaned_data['message']
            frommail = formdata.cleaned_data['mail']
            try:
                send_mail('Subject here', 'Here is the message.', 'from@example.com',
                          ['to@example.com'], fail_silently=False)
            except:
                pass
    return render_to_response("contact.html",
                              locals(),
                              context_instance=RequestContext(request))

def cataloge(request):
        
    return render_to_response("cataloge.html",
                              locals(),
                              context_instance=RequestContext(request))

def specials(request):
        
    return render_to_response("specials.html",
                              locals(),
                              context_instance=RequestContext(request))

#def gallery(request):
        
 #   return render_to_response("gallery.html",
  #                            locals(),
   #
#                           context_instance=RequestContext(request))
def about(request):
        
    return render_to_response("aboutus.html",
                              locals(),
                              context_instance=RequestContext(request))
