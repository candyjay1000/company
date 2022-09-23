from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title': 'HomePage'
    } 
    return render(request,'spacce/index.html',context)

def about(request):
    context={
        'title' :'About'
    }        
    return render(request,'spacce/about.html',context)

def contact(request):
    context={
        'title': 'Contact'
    }        
    return render(request,'spacce/contact.html',context)

def services(request):
    context={
        'title': 'Services'
    }     
    return render(request,'spacce/services.html',context)

def team(request):
    context={
        'title': 'Team'
    }     
    return render(request,'spacce/team.html',context)

def pricing(request):
    context={
        'title': 'Pricing'
    }     
    return render(request,'spacce/pricing.html',context)

def portfolio(request):
    context={
        'title': 'Portfolio'
    }     
    return render(request,'spacce/portfolio.html',context)

def portfolio_details(request):
    context={
        'title': 'Portfolio Details'
    }       
    return render(request,'spacce/portfolio-details.html',context)

def testimonials(request):
    context={
        'title': 'Testimonials'
    }       
    return render(request,'spacce/testimonials.html',context)

def blog(request):
    context={
        'title': 'Blog'
    }       
    return render(request,'spacce/blog.html',context)

def blog_single(request):
    context={
        'title': 'Blog-Single'
    }      
    return render(request,'spacce/blog-single.html',context)


