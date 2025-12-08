from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    """Форма для модели Product"""
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'owner')

    forbidden_words = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    def clean(self):
        """Валидация полей name и description на запрещенные слова"""
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        forbidden_words_in_name = []
        forbidden_words_in_description = []

        for word in self.forbidden_words:
            if word in name.lower():
                forbidden_words_in_name.append(word)

        for word in self.forbidden_words:
            if word in description.lower():
                forbidden_words_in_description.append(word)

        if forbidden_words_in_name and forbidden_words_in_description:
            raise ValidationError(f'В названии и описании есть запрещенные слова: {", ".join(forbidden_words_in_name)}, {", ".join(forbidden_words_in_description)}')
        elif forbidden_words_in_name:
            raise ValidationError(f'В названии есть запрещенные слова: {", ".join(forbidden_words_in_name)}')
        elif forbidden_words_in_description:
            raise ValidationError(f'В описании есть запрещенные слова: {", ".join(forbidden_words_in_description)}')

        return cleaned_data


    def clean_price(self):
        """Валидация поля price на отрицательное значение"""
        price = self.cleaned_data['price']

        if price <= 0:
            raise ValidationError('Цена продукта не может быть нулевой или отрицательной.')

        return price