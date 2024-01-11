from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Size, Brand


class ProductForm(forms.ModelForm):
    """ Form for adding and editing products """
    class Meta:
        model = Product
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter product description'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter product price'}),
            'category': forms.Select(attrs={'placeholder': 'Select product category'}),
            'size': forms.Select(attrs={'placeholder': 'Select product size'}),
            'brand': forms.Select(attrs={'placeholder': 'Select product brand'}),
            'image': forms.FileInput(attrs={'placeholder': 'Select product image'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Enter product image URL'}),
            'sku': forms.TextInput(attrs={'placeholder': 'Enter product SKU'}),
    }

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

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
