from django.shortcuts import render, redirect
from Auth_App.models import User, Distributor
from django.contrib import messages
from Admin_App.models import *
# Create your views here.

# --------------------------------------- Sales Manager --------------------------------------- #

def salesmanager_list(request):
    current_page = 'salesmanager-list'
    salesmanagers = User.objects.filter(is_salesmanager=True)
    context = {
        'current_page': current_page,
        'salesmanagers' : salesmanagers
    }
    return render(request, 'admin/salesmanager-list.html', context)

def salesmanager_add(request):
    current_page = 'salesmanager-add'

    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        place = request.POST.get('place')
        
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        image = request.FILES.get('image') or None

        
        try:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('salesmanager-add')
            
            # Create the user
            user = User.objects.create_user(
                username=username, 
                password=password,
                first_name=first_name, 
                last_name=last_name,
                
                email=email,
                phone=phone,
                place=place,
                
                image=image,
                is_salesmanager = True
                )
            user.save()
            messages.success(request, 'salesmanager Added Successfully.')
            return redirect('salesmanager-list')

        except Exception as e:
            messages.error(request, f'failed {str(e)}')
            return redirect('salesmanager-add')
    context ={
        'current_page': current_page,
    }
    return render(request, 'admin/salesmanager-add.html', context)


def salesmanager_edit(request, salesmanager_id):
    current_page = 'salesmanager-edit'

    salesmanager = User.objects.get(id=salesmanager_id)

    if request.method == 'POST':

        # username = request.POST.get('username')
        # password = request.POST.get('password')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        place = request.POST.get('place')
       
        email = request.POST.get('email')
        phone = request.POST.get('phone')


        try:
            # Check if a new image file is provided
            new_image = request.FILES.get('image')
            if new_image:
                salesmanager.image = new_image  # Update the salesmanager's image


            # salesmanager.username = username
            # salesmanager.password = password

            salesmanager.first_name = first_name
            salesmanager.last_name = last_name
            salesmanager.place = place
            salesmanager.email = email
            salesmanager.phone = phone

            salesmanager.save()  

    
            messages.success(request, 'salesmanager Updated Successfully.')
            return redirect('salesmanager-list')
        except Exception as e:
            messages.error(request, f'Failed. {str(e)}')
            return redirect('salesmanager-edit')
    else:
        context = {
            'current_page': current_page,
            'salesmanager': salesmanager
        }
        return render(request, 'admin/salesmanager-edit.html', context)
    


def salesmanager_delete(request, salesmanager_id):
    salesmanager = User.objects.get(id=salesmanager_id, is_salesmanager=True)
    try:
        salesmanager.delete()
        messages.success(request, f"salesmanager '{salesmanager.username}' Delete successfully.")
        return redirect('salesmanager-list')
    except:
        messages.error(request, f"salesmanager '{salesmanager.username}' Delete Failed.")
        return redirect('salesmanager-list')
    

def salesmanager_image(request, salesmanager_id):
    salesmanager = User.objects.get(id=salesmanager_id)
    context = {
        'salesmanager' : salesmanager
    }
    return render(request, 'admin/salesmanager-image.html', context)
    

# --------------------------------------- Purchase Manager --------------------------------------- #


def purchasemanager_list(request):
    current_page = 'purchasemanager-list'
    purchasemanagers = User.objects.filter(is_purchasemanager=True)
    context = {
        'current_page': current_page,
        'purchasemanagers' : purchasemanagers
    }
    return render(request, 'admin/purchasemanager-list.html', context)

def purchasemanager_add(request):
    current_page = 'purchasemanager-add'

    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        place = request.POST.get('place')
        
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        image = request.FILES.get('image') or None

        
        try:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('purchasemanager-add')
            
            # Create the user
            user = User.objects.create_user(
                username=username, 
                password=password,
                first_name=first_name, 
                last_name=last_name,
                
                email=email,
                phone=phone,
                place=place,
                
                image=image,
                is_purchasemanager = True
                )
            user.save()
            messages.success(request, 'purchasemanager Added Successfully.')
            return redirect('purchasemanager-list')

        except Exception as e:
            messages.error(request, f'failed {str(e)}')
            return redirect('purchasemanager-add')
    context ={
        'current_page': current_page,
    }
    return render(request, 'admin/purchasemanager-add.html', context)


def purchasemanager_edit(request, purchasemanager_id):
    current_page = 'purchasemanager-edit'

    purchasemanager = User.objects.get(id=purchasemanager_id)

    if request.method == 'POST':

        # username = request.POST.get('username')
        # password = request.POST.get('password')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        place = request.POST.get('place')
       
        email = request.POST.get('email')
        phone = request.POST.get('phone')


        try:
            # Check if a new image file is provided
            new_image = request.FILES.get('image')
            if new_image:
                purchasemanager.image = new_image  # Update the purchasemanager's image


            # purchasemanager.username = username
            # purchasemanager.password = password

            purchasemanager.first_name = first_name
            purchasemanager.last_name = last_name
            purchasemanager.place = place
            purchasemanager.email = email
            purchasemanager.phone = phone

            purchasemanager.save()  

    
            messages.success(request, 'purchasemanager Updated Successfully.')
            return redirect('purchasemanager-list')
        except Exception as e:
            messages.error(request, f'Failed. {str(e)}')
            return redirect('purchasemanager-edit')
    else:
        context = {
            'current_page': current_page,
            'purchasemanager': purchasemanager
        }
        return render(request, 'admin/purchasemanager-edit.html', context)
    


def purchasemanager_delete(request, purchasemanager_id):
    purchasemanager = User.objects.get(id=purchasemanager_id, is_purchasemanager=True)
    try:
        purchasemanager.delete()
        messages.success(request, f"purchasemanager '{purchasemanager.username}' Delete successfully.")
        return redirect('purchasemanager-list')
    except:
        messages.error(request, f"purchasemanager '{purchasemanager.username}' Delete Failed.")
        return redirect('purchasemanager-list')
    

def purchasemanager_image(request, purchasemanager_id):
    purchasemanager = User.objects.get(id=purchasemanager_id)
    context = {
        'purchasemanager' : purchasemanager
    }
    return render(request, 'admin/purchasemanager-image.html', context)


# --------------------------------------- Brand --------------------------------------- #

def brand_list(request):
    current_page = 'brand-list'
    brands = Brand.objects.all().order_by('-id')
    context = {
        'current_page' : current_page,
        'brands':brands
    }
    return render(request, 'admin/brand-list.html', context)


def brand_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image') or None
        try:
            brand = Brand(
                name=name,
                image=image
            )
            brand.save()
            messages.success(request, 'Brand added Successfully')
            return redirect('brand-list')
        except Exception as e:
            messages.error(request, f'faild, {str(e)}')
            return redirect('brand-add')
    return render(request, 'admin/brand-add.html')


def brand_edit(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            new_image = request.FILES.get('image')
            if new_image:
                brand.image = new_image

            brand.name = name
            brand.save()
            messages.success(request, 'brand added success fully')
            return redirect('brand-list')
        except Exception as e:
            messages.error(request, f'faild, {str(e)}')
            return redirect('brand-edit')
    
    context = {
        'brand' : brand
    }

    return render(request, 'admin/brand-edit.html', context)


def brand_delete(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    try:
        brand.delete()
        messages.success(request, 'brand deleted successfully')
        return redirect('brand-list')
    except Exception as e:
        messages.error(request, f'delete Failde, {str(e)}')
        return redirect('brand-list')


# --------------------------------------- Product --------------------------------------- #

def product_brand_list(request, brand_id):
    current_page = 'product-brand-list'
    brand = Brand.objects.get(id=brand_id)
    products = Product.objects.filter(brand=brand).order_by('-id')
    context = {
        'brand' : brand,
        'products' : products,
        'current_page' : current_page
    }
    return render(request, 'admin/product-brand-list.html', context)

def product_brand_add(request, brand_id):
    current_page = 'product-brand-add'
    brand = Brand.objects.get(id=brand_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image') or None
        mrp = request.POST.get('mrp') or None
        purchase_rate = request.POST.get('purchase_rate') or None
        purchase_quantity = request.POST.get('purchase_quantity') or None
        selling_price = request.POST.get('selling_price') or None

        try:
            product = Product(
                brand=brand,
                name=name,
                image=image,
                mrp=mrp,
                purchase_rate=purchase_rate,
                purchase_quantity=purchase_quantity,
                selling_price=selling_price
            )
            product.save()
            messages.success(request, 'product addedd successfully')
            return redirect('product-brand-list', brand_id=brand.id)
        except Exception as e:
            messages.error(request, f'product added faild, {str(e)}')
            return redirect('product-brand-add')
        
    context = {
        'current_page' : current_page,
        'brand' : brand
    }
        
    return render(request, 'admin/product-brand-add.html', context)

def product_brand_edit(request, brand_id, product_id):
    current_page = 'product-brand-edit'

    brand = Brand.objects.get(id=brand_id)
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        mrp = request.POST.get('mrp') or None
        purchase_rate = request.POST.get('purchase_rate') or None
        purchase_quantity = request.POST.get('purchase_quantity') or None
        selling_price = request.POST.get('selling_price') or None

        try:
            new_image = request.FILES.get('image')
            if new_image:
                product.image = new_image

            product.brand = brand
            product.name = name
            product.mrp = mrp
            product.purchase_rate = purchase_rate
            product.purchase_quantity = purchase_quantity
            product.selling_price = selling_price
            product.save()
            messages.success(request, 'product updated successfully')
            return redirect('product-brand-list', brand_id=brand.id)
        except Exception as e:
            messages.error(request, f'failed, {str(e)}')
            return redirect('product-brand-edit', brand_id=brand.id, product_id=product.id)
    
    context = {
        'current_page' : current_page,
        'brand' : brand,
        'product' : product
    }
        
    return render(request, 'admin/product-brand-edit.html', context)

def product_brand_delete(request, brand_id, product_id):
    brand = Brand.objects.get(id=brand_id)
    product = Product.objects.get(id=product_id)
    try:
        product.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('product-brand-list', brand_id=brand.id)
    except Exception as e:
        messages.error(request, f'product delelete failed, {str(e)}')
        return redirect('product-brand-list', brand_id=brand.id)


            
# --------------------------------------- Distributor --------------------------------------- #

def distributor_list(request):
    current_page = 'distributor-list'
    distributors = Distributor.objects.all()
    context = {
        'distributors' : distributors,
        'current_page' : current_page
    }
    return render(request, 'admin/distributor-list.html', context)

def distributor_add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        place = request.POST.get('place') 
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        image = request.FILES.get('image') or None



        blood_group = request.POST.get('blood_group')
        whatsapp_number = request.POST.get('whatsapp_number')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        address_one = request.POST.get('address_one')
        address_two = request.POST.get('address_two')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        district = request.POST.get('district')
        education = request.POST.get('education')
        education_description = request.POST.get('education_description')
        father_name = request.POST.get('father_name')
        father_number = request.POST.get('father_number')
        father_job = request.POST.get('father_job')
        mother_name = request.POST.get('mother_name')
        mother_number = request.POST.get('mother_number')
        mother_job = request.POST.get('mother_job')
        friend_one_name = request.POST.get('friend_one_name')
        friend_one_number = request.POST.get('friend_one_number')
        friend_one_job = request.POST.get('friend_one_job')
        friend_two_name = request.POST.get('friend_two_name')
        friend_two_number = request.POST.get('friend_two_number')
        friend_two_job = request.POST.get('friend_two_job')
        distribution_area = request.POST.get('distribution_area')
        aadhaar_number = request.POST.get('aadhaar_number')
        aadhaar_image = request.FILES.get('aadhaar_image') or None  # Assuming it's a file upload field
        pan_card_number = request.POST.get('pan_card_number')
        pan_card_image = request.FILES.get('pan_card_image') or None  # Assuming it's a file upload field
        bank_name = request.POST.get('bank_name')
        bank_branch_name = request.POST.get('bank_branch_name')
        bank_holder_name = request.POST.get('bank_holder_name')
        bank_account_number = request.POST.get('bank_account_number')
        bank_ifc_code = request.POST.get('bank_ifc_code')
        
        try:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('distributor_add')
            
            # Create the user
            user = User.objects.create_user(
                username=username, 
                password=password,
                first_name=first_name, 
                last_name=last_name,
                
                email=email,
                phone=phone,
                place=place,
                
                image=image,
                is_distributor = True
                )
            user.save()


            distributor = Distributor(
                user=user,
                blood_group=blood_group,
                whatsapp_number=whatsapp_number,
                gender=gender,
                date_of_birth=date_of_birth,
                address_one=address_one,
                address_two=address_two,
                city=city,
                pincode=pincode,
                district=district,
                education=education,
                education_description=education_description,
                father_name=father_name,
                father_number=father_number,
                father_job=father_job,
                mother_name=mother_name,
                mother_number=mother_number,
                mother_job=mother_job,
                friend_one_name=friend_one_name,
                friend_one_number=friend_one_number,
                friend_one_job=friend_one_job,
                friend_two_name=friend_two_name,
                friend_two_number=friend_two_number,
                friend_two_job=friend_two_job,
                distribution_area=distribution_area,
                aadhaar_number=aadhaar_number,
                aadhaar_image=aadhaar_image,
                pan_card_number=pan_card_number,
                pan_card_image=pan_card_image,
                bank_name=bank_name,
                bank_branch_name=bank_branch_name,
                bank_holder_name=bank_holder_name,
                bank_account_number=bank_account_number,
                bank_ifc_code=bank_ifc_code,
            )
            distributor.save()
            messages.success(request, 'Distributoradded successfully')
            return redirect('distributor-list')
        except Exception as e:
            messages.error(request, f'faild to add, {str(e)}')
            return redirect('distributor-add')
    
    return render(request, 'admin/distributor-add.html')



def distributor_edit(request, distributor_id):
    # Get the distributor object based on the distributor_id
    distributor = Distributor.objects.get(id=distributor_id)

    if request.method == 'POST':
      

        try:
            # Update the distributor object with the new data
            distributor.blood_group = request.POST.get('blood_group')
            distributor.whatsapp_number = request.POST.get('whatsapp_number')
            distributor.gender = request.POST.get('gender')
            distributor.date_of_birth = request.POST.get('date_of_birth')
            distributor.address_one = request.POST.get('address_one')
            distributor.address_two = request.POST.get('address_two')
            distributor.city = request.POST.get('city')
            distributor.pincode = request.POST.get('pincode')
            distributor.district = request.POST.get('district')
            distributor.education = request.POST.get('education')
            distributor.education_description = request.POST.get('education_description')
            distributor.father_name = request.POST.get('father_name')
            distributor.father_number = request.POST.get('father_number')
            distributor.father_job = request.POST.get('father_job')
            distributor.mother_name = request.POST.get('mother_name')
            distributor.mother_number = request.POST.get('mother_number')
            distributor.mother_job = request.POST.get('mother_job')
            distributor.friend_one_name = request.POST.get('friend_one_name')
            distributor.friend_one_number = request.POST.get('friend_one_number')
            distributor.friend_one_job = request.POST.get('friend_one_job')
            distributor.friend_two_name = request.POST.get('friend_two_name')
            distributor.friend_two_number = request.POST.get('friend_two_number')
            distributor.friend_two_job = request.POST.get('friend_two_job')
            distributor.distribution_area = request.POST.get('distribution_area')
            distributor.aadhaar_number = request.POST.get('aadhaar_number')
            distributor.pan_card_number = request.POST.get('pan_card_number')
            distributor.bank_name = request.POST.get('bank_name')
            distributor.bank_branch_name = request.POST.get('bank_branch_name')
            distributor.bank_holder_name = request.POST.get('bank_holder_name')
            distributor.bank_account_number = request.POST.get(' bank_account_number')
            distributor.bank_ifc_code = request.POST.get('bank_ifc_code')

            
            # Capture additional fields
            distributor.user.first_name = request.POST.get('first_name')
            distributor.user.last_name = request.POST.get('last_name')
            distributor.user.place = request.POST.get('place')
            distributor.user.email = request.POST.get('email')
            distributor.user.phone = request.POST.get('phone')
            
            # Update the distributor's fields that can be changed
            distributor.save()
            distributor.user.save()  # Save the user-related fields
            messages.success(request, 'Distributor updated successfully')
            return redirect('distributor-list')
        except Exception as e:
            messages.error(request, f'Failed to update distributor: {str(e)}')
            return redirect('distributor-edit', distributor_id=distributor_id)
        
    context = {
        'distributor': distributor
    }

    # If the request method is not 'POST', render the t ediform with the distributor data
    return render(request, 'admin/distributor-edit.html', context)


def distributor_delete(request,distributor_id):
    # Get the distributor object  based on the distributor_id
    distributor = Distributor.objects.get(id=distributor_id) 
    try:
        distributor.delete()
        messages.success(request, 'delted sucssussfully')
        return redirect('distributor-list')
    except Exception as e:
        messages.error(request, f'faild to delete, {str(e)}')
        return redirect(request, 'distributor_list')


def distributor_view(request,distributor_id):
    distributor = Distributor.objects.get(id=distributor_id) 
    context = {
        'distributor': distributor
    }
    return render(request, 'distributor_view.html', context)

    
