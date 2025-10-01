from django.shortcuts import render
from .models import Product, Feature, ProcessStep, Benefit, Testimonial

def products(request):
    # Get the active product
    product = Product.objects.filter(is_active=True).first()
    
    # Get all related data
    features = Feature.objects.filter(is_active=True, product=product)
    process_steps = ProcessStep.objects.all()
    benefits = Benefit.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)
    
    # Group features by category
    feature_categories = {}
    for feature in features:
        if feature.category not in feature_categories:
            feature_categories[feature.category] = []
        feature_categories[feature.category].append(feature)
    
    context = {
        'product': product,
        'features': features,
        'process_steps': process_steps,
        'benefits': benefits,
        'testimonials': testimonials,
        'feature_categories': feature_categories,
    }
    
    return render(request, 'products/products.html', context)