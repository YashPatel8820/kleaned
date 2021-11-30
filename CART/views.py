from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from USER.models import *
from HOME.models import *
from CART.models import *
import random
import smtplib
import email.message
from email.message import EmailMessage
import razorpay
# import razorpay


# Create your views here.
def hii(request):
    return HttpResponse("Welcome here")


#=================================\\Displaying Cart page//===============================
def cart_page(request):
    if request.session.has_key('name'):
        per = Registration.objects.get(Name = request.session['name'])
        item = Mycart.objects.filter(person_id=per.id, status = False)
        obj = Mycart.objects.filter(person_id = per.id, status = False)
        num = Mycart.objects.filter(person_id=per.id, status = False).count()
        cn = Registration.objects.get(Name = request.session['name'])
        total = 0
        for q in item:
            total = total + q.product.Price
        print(total)
        return render(request,'CART/cart.html', {'per': per, 'x': obj, 'final': total, 'cn' : cn })
    else:
        return render(request, 'CART/cart.html')


#=================================\\Displaying Checkout page//===============================
def checkout_page(request):
    if request.session.has_key('name'):
        per = Registration.objects.get(Name = request.session['name'])
        item = Mycart.objects.filter(person_id=per.id, status = False)
        obj = Mycart.objects.filter(person_id = per.id, status = False)
        nam = Registration.objects.filter(Name=request.session['name'])
        print(nam)
        total = 0
        for q in item:
            total = total + q.product.Price
        print(total)
        return render(request, 'CART/checkout.html', {'check' : obj, 'Ctotal':total, 'item' : item, 'n':nam, 'dtotal': total*100   } )
    else:
        war = "Login First"
        return render(request, 'USER/loginnew.html', {'log' : war})


#=================================\\Logic of add to cart page//===============================
def addcart_page(request, pk):
    
    if request.session.has_key('name'):
        per = Registration.objects.get(Name = request.session['name'])
        item = Mycart.objects.filter(person_id=per.id, status = False)
        obj = Mycart.objects.filter(person_id = per.id, status = False)
        obj1 = get_object_or_404(Service,pk=pk )
        print(obj1.Price) 
       
        num = Mycart.objects.filter(person_id=per.id, status = False).count()
        ser_id = get_object_or_404(Service,pk=pk )
        s= Service.objects.get(id=pk)
        if Mycart.objects.filter(product__id=pk, person__id=per.id, status=False).exists():
            messages.warning(request, 'Item already in the cart')
            return redirect('Home')
        else:
            sr= get_object_or_404(Service, id=pk)
            c = Mycart.objects.create(person=per, product=sr)
            c.save()
            request.session['order_id']=c.id
            messages.warning(request, 'Item has beed added to cart')
          
            total = 0
            for q in item:
                total = total + q.product.Price
            print(total)

         
            return render(request,'CART/cart.html', {'s': s, 'per': per, 'x': obj, 'final': total})
    else:
        return redirect('Home')


#=================================\\Logic of removing from cart page//===============================
def remove_cart(request,pk):
    if  request.session.has_key('name'):
        s = get_object_or_404(Mycart, pk=pk)
        s.delete()
        return redirect('Cart')
    else:
        return redirect('Login')

#=================================\\Logic of Pay with razorpay button//===============================
def place_order(request):
    if  request.session.has_key('name'):
        o_id = ''
        r2 = random.choice('1234567890')
        r3 = random.choice('1234567890')
        r4 = random.choice('1234567890')
        r6 = random.choice('1234567890')
        r7 = random.choice('1234567890')
        r8 = random.choice('1234567890')
        o_id = r2+r3+r4+r6+r7+r8
        print(o_id)


        naam = Registration.objects.filter(Name=request.session['name'])
        per = Registration.objects.get(Name = request.session['name'])
        for e in naam:
            em = e.Email
            na = e.Name
        print(em)
        print(na)
        item = Mycart.objects.filter(person_id=per.id, status = False)
        num = Mycart.objects.filter(person_id=per.id, status = False).count()
        total = 0
        for q in item:
            total = total + q.product.Price
        print(total)

        r = Order()
        r.order_id = o_id
        r.person = per
        r.no_of_services = num
        r.order_amount = total
        r.save()

        client = razorpay.Client(auth=("rzp_test_796VLaiwc0lHMw", "YSZI1gafE4n0tY9QNxR1oRgl"))
        DATA = {
            'amount': total,
            "currency": "INR",
            "receipt": "receipt#1",
            'payment_capture': '1',
            # "notes": {
            #     "key1": "value3",
            #     "key2": "value2"
            # }
        }
        client.order.create(data=DATA)

        sender_email = "yash19959@gmail.com"
        sender_pass = '5awanmelaggai@ag'
        reciv_email = em
        print(reciv_email)
        server = smtplib.SMTP('smtp.gmail.com',587)
        
        mes1 = f"""
            Your Order Details are:   {"<br></br>"}

            Full Name       :  {na}  {"<br></br>"}
            Order-Id        :  {o_id} {"<br></br>"}
            Amount          :  {total} {"<br></br>"}
            No of Sercices  :  {num}  {"<br></br>"}

            """
        msg = email.message.Message()
        msg['Subject'] = "Klean Services"
        msg['From'] = sender_email
        msg['To'] = reciv_email
        password = sender_pass
        msg.add_header('Content-Type','text/html')
        msg.set_payload(mes1)
        server.starttls()
        server.login(msg['From'],password)
        server.sendmail(msg['From'],msg['To'],msg.as_string()) 

        return render(request, 'CART/place.html', {'num' : num, 'nams' : naam, 'final' : total, 'order' : o_id })
    


        
        



    

