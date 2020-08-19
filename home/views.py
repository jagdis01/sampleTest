from django.shortcuts import render
from django.forms import (formset_factory, modelformset_factory)
from .forms import *
from django.http import JsonResponse
from django.template.loader import render_to_string, get_template


# Create your views here.
def get_bil(request):
	formset = BillFormset()
	return render(request,'bill.html',{'formset':formset})


def load_products(request):
	ctx = {}
	url_parameter = request.GET.get("pk")

	if url_parameter:
		product = Product.objects.filter(name__icontains=url_parameter)
	else:
		product = Product.objects.all()

	ctx["product"] = product
	if request.is_ajax():
		html = render_to_string(
			template_name="product-list.html", 
			context={"product": product}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request, "product-list.html", context=ctx)
	