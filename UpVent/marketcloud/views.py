import stripe

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

# Import Stripe Keys
stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        # Change this to your actual domain
        YOUR_DOMAIN = "https://127.0.0.1:8000/"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'mxn',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })





def MarketCloud(request):
    return render(request, 'marketcloud/shop.html')

def Product(request, slug):
    return render(request, 'marketcloud/product.html')
