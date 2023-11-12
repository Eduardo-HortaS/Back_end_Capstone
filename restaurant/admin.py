from django.contrib import admin
from .models import MenuItem, Booking

# Define a list of models to register
models = [MenuItem, Booking]

# Register all models in the list using a loop
for model in models:
    admin.site.register(model)
