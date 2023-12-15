from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import ReceiptItem
from django.core.paginator import Paginator

def register(request):
    """
    User Registration form
    Args:
        request (POST): New user registered
    """    
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "receipt/register.html", context)
@login_required
def home(request):
    """
    Create todo item and view other todo items as well.
    """
    if request.method == 'POST':
        # "new-todo" is the name of the input in crud.html file
        receipt_name = request.POST.get("receipt_name")
        receipt_items = request.POST.get("receipt_items")
        receipt_amount = request.POST.get("receipt_amount")


        todo = ReceiptItem.objects.create(name=receipt_name,
                                          purchase_items = receipt_items,
                                          total_amount = receipt_amount , 
                                           user=request.user)
        return redirect("home")

    # retrieveing todo items which are not completed todo items
    items = ReceiptItem.objects.filter(user=request.user)
    paginator = Paginator(items, 4)
    
    # It's URL param for getting the current page number
    page_number = request.GET.get("page")
    
    # retrieving all the todo items for that page
    page_obj = paginator.get_page(page_number)

    context = {"items": items, "page_obj": page_obj}
    return render(request, "receipt/crud.html", context)




def update_receipt(request, pk):
    """
    Update receipt item
    Args:
        pk (Integer): Todo ID - primary key
    """
    
    receipt = get_object_or_404(ReceiptItem, id=pk, user=request.user)

  
    receipt.name = request.POST.get(f"receipt_{pk}")
    receipt.purchase_items = request.POST.get(f"receipt_items_{pk}")
    receipt.total_amount = request.POST.get(f"receipt_amount_{pk}")
    receipt.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_receipt(request, pk):
    """
    Delete receipt item
    Args:
        pk (Integer): receipt ID - Primary key
    """    
    receipt = get_object_or_404(ReceiptItem, id=pk, user=request.user)
    receipt.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))