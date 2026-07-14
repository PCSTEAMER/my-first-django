from django.urls import path
from myapp import views 

urlpatterns = [
    path('', views.index, name='index'), # ผูกเข้ากับฟังก์ชัน index ใน views.py
    path('about/', views.about, name='about'), # ผูกเข้ากับฟังก์ชัน about ใน views.py
    path('contact/', views.contact_view, name='contact'), # ผูกเข้ากับฟังก์ชัน contact ใน views.py
    path('database/', views.person_list, name='person_list'), # 🚀 เส้นทางของหน้าคลังข้อมูลใหม่
    # 3 เส้นทางนี้คือของใหม่ที่เราเพิ่งสร้างหน้าเว็บไปครับ
    path('form_view/', views.form_view, name='form_view'),
    path('edit/<int:person_id>/', views.edit, name='edit'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
    
]