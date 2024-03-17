from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill
from django.db.models import Sum, Q
from transactions.models import SaleItem


class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        labels = ['Cadenas','Pulsos','Anillos','Aretes','Piercing','Dijes']
        data = []        
        weight_data = {}
        count_data = {}
        most_sold_stocks = SaleItem.objects.values('stock__name').annotate(total_sold=Sum('quantity')).order_by('-total_sold')



        Cadenas_sum = Stock.objects.filter(type='Cadenas', is_deleted=False,isApartado = False).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        Pulsos_sum = Stock.objects.filter(type='Pulsos', is_deleted=False,isApartado = False).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        Anillos_sum = Stock.objects.filter(type='Anillos', is_deleted=False,isApartado = False).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        Aretes_sum = Stock.objects.filter(type='Aretes', is_deleted=False,isApartado = False).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        Piercing_sum = Stock.objects.filter(type='Piercing', is_deleted=False,isApartado = False).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        Dijes_sum = Stock.objects.filter(type='Dijes', is_deleted=False,isApartado = False).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        data.append(Cadenas_sum)
        data.append(Pulsos_sum)
        data.append(Anillos_sum)
        data.append(Aretes_sum)
        data.append(Piercing_sum)
        data.append(Dijes_sum)
        # stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        # for item in stockqueryset:
        #     labels.append(item.name)
        #     data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        for stock_type in labels:
            matching_stocks = Stock.objects.filter(type=stock_type, is_deleted=False,isApartado = False)
            total_weight = Stock.objects.filter(type=stock_type, is_deleted=False,isApartado = False).aggregate(Sum('weight'))['weight__sum'] or 0
            total_count = matching_stocks.count()  # Count of items per type

            weight_data[stock_type] = total_weight
            count_data[stock_type] = total_count
        context = {
            'labels'    : labels,
            'data'      : data,
            'sales'     : sales,
            'purchases' : purchases,
            'most_sold_stocks': most_sold_stocks,
        }
        context.update({
            'weight_data': weight_data,  # Add weight data to the context
            'count_data': count_data,  # Add count data to the context
        })
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"