from django.shortcuts import render
from card.forms import CardForms


def new(request):
    form = CardForms()

    context = {"cardform":form}
    return render(request,'project/new-card.html',context=context)




