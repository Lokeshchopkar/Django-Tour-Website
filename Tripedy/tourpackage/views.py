from django.shortcuts import render
from .models import Package, Contact, Booking
from math import ceil

def index(request):
    allPackage = []
    catpackage = Package.objects.values('category', 'id')
    cats = {item['category'] for item in catpackage}
    for cat in cats:
        pack = Package.objects.filter(category=cat)
        n = len(pack)
        nSlides = n//4 + ceil((n / 4) - (n // 4))
        allPackage.append([pack, range(1, nSlides), nSlides])
    params = {'allPackage': allPackage}
    return render(request, 'tourpackage/index.html', params)

def searchMatch(query, item):
    # returntrue only if query matches the item
    if query in item.desc.lower() or query in item.package_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allPackage = []
    catpackage = Package.objects.values('category', 'id')
    cats = {item['category'] for item in catpackage}
    for cat in cats:
        packtemp = Package.objects.filter(category=cat)
        pack = [item for item in packtemp if searchMatch(query, item)]

        n = len(pack)
        nSlides = n//4 + ceil((n / 4) - (n // 4))
        if len(pack) != 0:
            allPackage.append([pack, range(1, nSlides), nSlides])
    params = {'allPackage': allPackage, "msg": ""}
    if len(allPackage) == 0:
        params = {'msg': "Please Make sure to enter relevant search query"}

    return render(request, 'tourpackage/search.html', params)

def about(request):
    return render(request, 'tourpackage/about.html')

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        peraddress = request.POST.get('peraddress', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, peraddress=peraddress, city=city, state=state, zip=zip, desc=desc)
        contact.save()
        thank = True
    return render(request, 'tourpackage/contact.html', {'thank': thank})


    
def packView(request, myid):
    # Fetch the package using id
    package = Package.objects.filter(id = myid)
    return render(request, 'tourpackage/packview.html', {'package': package[0]})

def checkout(request, myid=None):
    if request.method == "POST":
        inputTraveller = request.POST.get('inputTraveller', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount')
        if not amount:
            amount = 0  # Or handle appropriately
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        textarea = request.POST.get('textarea', '')

        booking = Booking(inputTraveller=inputTraveller, name=name, email=email, 
                          phone=phone, address=address, city=city, state=state, textarea=textarea, amount=amount)
        booking.save() 
        thank = True
        id = booking.booking_id 
        return render(request, 'tourpackage/checkout.html', {'thank': thank, 'id': id,})
    packagenew = Package.objects.filter(id = myid)
    return render(request, 'tourpackage/checkout.html', {'package': packagenew[0]})