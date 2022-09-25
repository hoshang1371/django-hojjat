from django.shortcuts import render
from spad_eshop_products.models import Product, ProductGallery
from django.http import Http404, request

from spad_eshop_products_category.models import ProductCategory

from spad_eshop_CustomersComments.models import CustomerComment
from spad_eshop_CustomersComments.forms import CustomersCommentsForm

from django.views.generic import ListView
import itertools
from spad_eshop_order.forms import UserNewOrderForm

# Create your views here.
def products(request):
    context = {}
    #return render(request, 'products/product_detail.html', context)
    return render(request, 'products/products_list.html', context)


class ProductList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.get_active_products()

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        #context['cate'] = ProductCategory.objects.filter(title__iexact=Product.title).first()
        #context['cates'] = ProductCategory.objects.order_by('title') 
        return context

class ProductListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 4

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.get_products_by_category(category_name)

def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    contex = {
        'categories': categories
    }
    return render(request ,'products/product_category_partial.html',contex)

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def product_detail(request, *args, **kwargs):

    selected_product_id = kwargs['productId']    
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': selected_product_id})
    
    contact_form_comment = CustomersCommentsForm(request.POST or None)



    product_name = kwargs['name']

    product = Product.objects.get_by_id(selected_product_id)

    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')
        
    if contact_form_comment.is_valid():
        full_name = contact_form_comment.cleaned_data.get('full_name')
        email = contact_form_comment.cleaned_data.get('email')
        subject = contact_form_comment.cleaned_data.get('subject')
        text = contact_form_comment.cleaned_data.get('text')
        CustomerComment.objects.create(full_name=full_name, email=email,
                                        subject=subject, text=text,
                                        CommentProduct=product, is_ok=False)
        # todo : show user a success message
        contact_form = CustomersCommentsForm()
    product.visit_count += 1
    product.save()

    customercomments =CustomerComment.objects.filter(CommentProduct=product).all()

    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()

    grouped_related_products = list(my_grouper(3, related_products))

    galleries = ProductGallery.objects.filter(product_id=selected_product_id)


    grouped_galleries = list(my_grouper(1, galleries))
    context = {
        'product': product,
        'galleries' : grouped_galleries,
        'related_products' : grouped_related_products,
        'new_order_form' : new_order_form,
        'customercomments' : customercomments,
        'contact_form_comment' : contact_form_comment,
    }

    # tag = Tag.objects.first()
    # print(tag.products.all())
    #print(product.tag_set.all())

    return render(request, 'products/product_detail.html', context)

class SearchProductsView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 4
    
    def get_queryset(self):       
        request = self.request
        #print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            #print(query)
            #return Product.objects.filter(title__icontains=query)
            return Product.objects.search(query)
        return Product.objects.get_active_products()