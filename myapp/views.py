from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe
stripe.api_key=settings.STRIPE_SECRET_KEY
class Homepage(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **Kwargs):
        context=super().get_context_data(**Kwargs)
        context['key']=settings.STRIPE_PUBLISHABLE_KEY
        return  context
def charge(request):
    if request.method == 'POST':
        def charge(request):
            charge=stripe.charge.create(
                amount=500,
                currency='inr',
                description='payment geteway',
                source=request.POST['StripeToken']
            )
    return render(request,'charge.html')






# Create your views here.
