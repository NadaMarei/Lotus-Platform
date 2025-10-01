from django.contrib import admin
from .models import Product, Feature, ProcessStep, Benefit, Testimonial

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_editable = ['is_active']

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'category', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    list_editable = ['order', 'is_active']

@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author', 'rating', 'company', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['rating', 'is_active']