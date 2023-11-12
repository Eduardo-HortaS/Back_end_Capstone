from django.contrib import admin
from .models import Menu, Booking

# Define a list of models to register
models = [Menu, Booking]

# Register all models in the list using a loop
for model in models:
    admin.site.register(model)
