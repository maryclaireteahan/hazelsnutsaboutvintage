from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Size, Brand

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        sizes = Size.objects.all()
        brands = Brand.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_sizes = [(s.id, s.get_friendly_name()) for s in sizes]
        friendly_brands = [(b.id, b.get_friendly_name()) for b in brands]
        
        self.fields['category'].choices = friendly_names
        self.fields['size'].choices = friendly_sizes
        self.fields['brand'].choices = friendly_brands
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'