from django.contrib import admin
from django import forms
from .models import MenuItem

class MenuItemAdminForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('name', 'parent_item', 'url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent_item'].queryset = MenuItem.objects.exclude(pk=self.instance.pk)

@admin.register(MenuItem)
class MenuItemModelAdmin(admin.ModelAdmin):
    form = MenuItemAdminForm
    list_display = ("name",)
    prepopulated_fields = {"url": ("name",)}