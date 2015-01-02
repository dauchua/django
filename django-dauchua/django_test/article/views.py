from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context,loader
#from django.shortcuts import render_to_respond
from django.views.generic.base import TemplateView
import subprocess

# Create your views here.

def render_to_response(tmpl, data): # render_to_respond no worked @@
    t = loader.get_template(tmpl)
    c = Context(data)
    return HttpResponse(t.render(c))

def hello(request):
    name = "Dauchua"
    html = "<html><body>Hi %s, this worked!!! </body></html>" %name
    return HttpResponse(html)

def hello_template(request):
    name = "dauchua"
    t = get_template('hello.html') #get template from hello.html
    html = t.render(Context({'name': name})) #html rendered from template + arg

    return HttpResponse(html)
def hello_template_simple(request):
    name = "dauchua simple template"
    return render_to_response('hello.html',{'name': name})

class HelloTemplate(TemplateView):
    template_name = 'hello_class.html'
    def get_context_data(self,**kwargs):
        context = super(HelloTemplate,self).get_context_data(**kwargs)
	#call bash function :
	process = subprocess.call(["nmap","-v","-A","www.genk.vn"])
        #context['name']= 'dauchua class'
        return context




