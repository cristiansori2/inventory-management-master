from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView, 
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Stock
from .forms import StockForm
from django_filters.views import FilterView
from .filters import StockFilter


class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.filter(is_deleted=False,isApartado = False)
    template_name = 'inventory.html'
    paginate_by = 10


class EliminadosListView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.filter(is_deleted=True,isApartado = False)
    template_name = 'eliminado.html'
    paginate_by = 10



class ApartadoslistView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.filter(is_deleted=False,isApartado = True)
    template_name = 'apartados.html'
    paginate_by = 10


class StockCreateView(SuccessMessageMixin, CreateView):                               # createview class to add new stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm 
    template_name = "edit_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Prenda creada correctamente"                             # displays message when form is submitted

    def form_valid(self, form):
        form.instance.telefono = ''
        form.instance.apartadoPor = ''
        form.instance.precioApartado = 0

        form.instance.quantity = 1
        form.instance.date = date.today()
        form.instance.is_deleted = False
        return super().form_valid(form)
    def form_invalid(self, form):
        # Debugging print statement for an invalid form
        print("Form is invalid. Errors:", form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    def get_context_data(self, **kwargs):
        print('helooooo')
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nueva Prenda'
        context["savebtn"] = 'Adicionar al inventario'
        return context    


class StockUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been updated successfully"              
    
                   # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar Joya'
        context["savebtn"] = 'Actualizar Joya'
        context["delbtn"] = 'Borrar Joya'
        return context

class StockApartarView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "apartar_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory/apartados'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "La prenda ha sido apartada" 
    
    def form_valid(self, form):

        form.instance.quantity = 1
        form.instance.isApartado = True
        form.instance.date = date.today()
        form.instance.fechaApartado = date.today()
        form.instance.is_deleted = False
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Debugging print statement for an invalid form
        print("Form is invalid. Errors:", form.errors)
        return self.render_to_response(self.get_context_data(form=form))                            # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar Joya'
        context["savebtn"] = 'Actualizar Joya'
        context["delbtn"] = 'Borrar Joya'
        return context

class StockDeleteView(View):                                                            # view class to delete stock
    template_name = "delete_stock.html"                                                 # 'delete_stock.html' used as the template
    success_message = "Eliminado Correctamente"                             # displays message when form is submitted
    
    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object' : stock})

    def post(self, request, pk):  
        stock = get_object_or_404(Stock, pk=pk)
        stock.is_deleted = True
        stock.save()                                               
        messages.success(request, self.success_message)
        return redirect('inventory')
    
class ApartarDeleteView(View):                 
    print('BBBBBBBB')                                           # view class to delete stock
    template_name = "delete_apartado.html"                                                 # 'delete_stock.html' used as the template
    success_message = "Apartado Correctamente"                             # displays message when form is submitted
    
    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object' : stock})

    def post(self, request, pk):  
        stock = get_object_or_404(Stock, pk=pk)
        stock.isApartado = False
        stock.save()                                               
        messages.success(request, self.success_message)
        return redirect('apartados')