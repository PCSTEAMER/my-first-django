from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from myapp.models import Person
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
# 4. หน้าคลังข้อมูล (ฟังก์ชันที่เพิ่มขึ้นมาใหม่เพื่อดึงฐานข้อมูล)
def person_list(request):
    all_persons = Person.objects.all() 
    context = {
        'persons': all_persons
    }
    return render(request, 'person_list.html', context)

# ฟังก์ชันสำหรับจัดการหน้า Contact
def contact_view(request):
    if request.method == 'POST':
        # รับค่าจากฟอร์มในไฟล์ contact.html
        name = request.POST.get('name')
        contact_info = request.POST.get('contact_info')
        message = request.POST.get('message')

        # จัดรูปแบบอีเมล
        subject = f"มีข้อความติดต่อใหม่จากคุณ {name} (Portfolio)"
        body = f"ชื่อ-นามสกุล: {name}\nช่องทางติดต่อกลับ: {contact_info}\n\nรายละเอียดข้อความ:\n{message}"
        
        try:
            # สั่งส่งอีเมล
            send_mail(
                subject, 
                body, 
                'lomabut33@gmail.com',  # ส่งจากอีเมลนี้
                ['lomabut33@gmail.com'],  # ส่งเข้าอีเมลตัวเอง
                fail_silently=False,
            )
            # แจ้งเตือนสีเขียวเมื่อส่งสำเร็จ
            messages.success(request, 'ส่งข้อความสำเร็จ! จะรีบติดต่อกลับนะครับ')
            return redirect('contact') 
            
        except Exception as e:
            # แจ้งเตือนสีแดงเมื่อเกิดข้อผิดพลาด
            print("💥 ตัวการที่ทำให้แจ้งเตือนแดงเด้ง:", e)
            messages.error(request, 'เกิดข้อผิดพลาดในการส่งข้อความ โปรดลองใหม่อีกครั้ง')

    return render(request, 'contact.html')
    # 1. ฟังก์ชันบันทึก
def form_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        date_of_birth = request.POST["date_of_birth"]
        address = request.POST["address"]
        email = request.POST["email"]
        
        new_person = Person(name=name, age=age, date_of_birth=date_of_birth, address=address, email=email)
        new_person.save()
        
        messages.success(request, "บันทึกข้อมูลเรียบร้อย")
        return redirect('/database/')
    return render(request, 'form_view.html')

# 2. ฟังก์ชันแก้ไข (จุดที่ไอซ์ทำในคลิป)
def edit(request, person_id):
    person = Person.objects.get(id=person_id)
    if request.method == "POST":
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.date_of_birth = request.POST["date_of_birth"]
        person.address = request.POST["address"]
        person.email = request.POST["email"]
        person.save()
        
        # 🟢 เติมแค่บรรทัดนี้บรรทัดเดียวพอ 
        messages.success(request, "แก้ไขข้อมูลเรียบร้อย")
        return redirect('/database/')
    return render(request, "edit.html", {"person": person})

# 3. ฟังก์ชันลบ
def delete(request, person_id):
    delete_person = Person.objects.get(id=person_id)
    delete_person.delete()
    
    # 🟢 เติมตรงนี้ด้วย
    request.session.flush()
    
    messages.success(request, "ลบข้อมูลเรียบร้อย")
    return redirect('/database/')