# Alhikam Mart.
Your neighborhood's one-stop shop for groceries and essentials with a touch of local charm.
## Questions
<details>
<summary>&ensp;Tugas 2</summary>

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

### Membuat proyek Django baru
#### Step 1: Buat direktori baru dan aktifkan _Virtual environment_
1. Buat direktori baru dengan nama `alhikam-mart`.
2. Buka direktori pada _terminal_ kemudian jalankan perintah berikut.
```
python3 -m venv env
```
3. Aktifkan *Virtual Environment* dengan perintah berikut.
```
source env/bin/activate
```

#### Step 2: _Install_ semua dependencies yang dibutuhkan dan buat proyek Django baru
1. _Install_ semua dependencies di dalam _virtual environment_ dengan menjalankan perintah `pip3 install django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3`
2. Setelah itu, buat proyek Django baru menggunakan perintah `django-admin startproject alhikam-mart .`

### Membuat aplikasi dengan nama main.
1. *Di dalam _virtual environment_*, jalankan perintah
`python manage.py startapp main`. Sebuah direktori aplikasi baru bernama `main` akan terbuat di dalam direktori utama.
2. Buka file `settings.py` pada direktori proyek, kemudian tambahkan `main` ke dalam variabel `INSTALLED_APPS` seperti berikut:
```python
INSTALLED_APPS = [
    ...
    'main',
    ...
]
```
3. Setelah itu, aplikasi main sudah berhasil terbuat dan terdaftar ke dalam proyek `alhikam-mart`.

### Melakukan _routing_ pada proyek.
1. Buka file `urls.py` pada direktori proyek `alhikam-mart`.
2. Pada variable `urlpatterns`, tambahkan kode berikut.
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    ...,
    path('main/', include('main.urls')),
    ...
]
```

### Membuat model pada aplikasi `main` dengan nama `Product`
1. Buka file `models.py` kemudian buat objek model dengan mendefinisikan atribut-atribut yang ingin kita gunakan seperti sebagai berikut.
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```

2. Buat dan aplikasikan migrasi pada model dengan menjalankan perintah berikut.
* Buat migrasi model
```
python3 manage.py makemigrations
```
> perintah ini berfungsi untuk membuat berkas migrasi yang berisi perubahan pada model yang telah kita buat.

* Aplikasikan migrasi ke basis data.
```
python3 manage.py migrate
```
> perintah ini berfungsi untuk mengaplikasikan perubahan pada berkas migrasi ke basis data.

Dengan menjalankan langkah-langkah ini, kita telah berhasil membuat model pada aplikasi `main` dengan nama `Product`.

###  Membuat dan menghubungkan fungsi pada `views.py` dengan template.
1. Buat fungsi `show_main` pada `views.py` untuk mengimplementasikan template yang ingin dirender, definisikan juga variabel-variabel yang dibutuhkan di dalam template di dalam variable `context` seperti kode berikut.
```python
from django.shortcuts import render

def show_main(request):
    context = {
        'title': 'Welcome to Alhikam Mart',
        'name': 'M. Azmy Arya Rizaldi M.',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
```

2. Di dalam direktori `main`, buat direktori baru bernama `templates` kemudian buat file `main.html` di dalamnya. Pada file `main.html`, modifikasi tampilan pada template dengan menggunakan variable-variable yang di-_passing_ dari `views`.
```html
<h1>{{ title }}</h1>

<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```

> Dengan melakukan langkah ini, views telah terhubung dengan template dan siap untuk dirender menggunakan fungsi `show_main`.

## Membuat _routing_ pada aplikasi `main`.
1. Buat file dengan nama `urls.py` di dalam direktori `main`.
2. Setelah itu, masukkan kode berikut untuk mengatur views yang diinginkan pada tiap _path_.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

Dengan melakukan langkah ini, fungsi `show_main` yang telah dibuat pada `views.py` dapat dipetakan ke URL yang diinginkan.


### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

![Bagan](/img/bagan.png "Bagan")


### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
&emsp; **Virtual environment** digunakan untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Kita tetap dapat membuat aplikasi web berbasis Django **tanpa** menggunakan **virtual environment** tetapi penggunaannya sangat disarankan untuk menghindari konflik dependensi dan memudahkan pengelolaan proyek secara keseluruhan.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
&emsp;MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola desain yang memisahkan logika aplikasi, tampilan, dan data:

##### - MVC: 
&emsp;**Model** mengelola data, **View** menampilkan data, dan **Controller** mengatur logika aplikasi. Hubungan satu arah antara Model, View, dan Controller.

##### - MVT: 
&emsp;Mirip dengan MVC, tetapi Controller digantikan oleh **Template**, yang mengatur tampilan dan logika presentasi di dalam tampilan HTML. MVT biasanya terkait dengan kerangka kerja web seperti **Django.**

##### - MVVM: 
&emsp;**Model** mengelola data, **View** menampilkan data, dan **ViewModel** bertindak sebagai perantara antara keduanya. ViewModel memungkinkan View berkomunikasi dengan Model tanpa mengetahui detail implementasi Model. Digunakan terutama dalam aplikasi berbasis tampilan data seperti desktop dan mobile.
</details>
<details>
<summary>&ensp;Tugas 3</summary>

### 1. Apa perbedaan antara form POST dan form GET dalam Django?

| `POST`          | `GET`          |
| :-------------: |:-------------:|
|Data dikirim dalam *request body* sehingga tidak terlihat di URL  | Data dikirim sebagai bagian dari URL dan terlihat oleh semua orang yang melihat URL tersebut
|Lebih aman untuk mengirim data sensitif karena tidak dapat dilihat oleh penggun |Tidak cocok untuk mengirim data sensitif karena kerentanannya terhadap pihak ketiga yang dapat melihat data|
|Biasanya digunakan untuk mengirim data yang akan memengaruhi perubahan status di server|Biasanya digunakan untuk mengambil data dari server tanpa mengubah statusnya|
|Tidak terbatas oleh batasan panjang URL karena data dikirim dalam *request body* sehingga lebih cocok untuk mengirim data besar atau kompleks |Terbatas dalam kapasitas data yang dapat dikirimkan karena tergantung pada panjang URL maksimum yang didukung oleh server dan browser|

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

####XML (Extensible Markup Language):

- Sebuah bahasa *markup* yang digunakan untuk mendefinisikan struktur data hierarkis dengan menggunakan tag `<>` untuk mengidentifikasi elemen-elemen dalam data.
- Biasanya dipakai untuk mengirimkan data antara berbagai aplikasi dan sebagai format penyimpanan yang dapat diurai oleh berbagai program.
- Dikenal karena memiliki aturan sintaksis yang ketat dan menghasilkan dokumen yang cenderung lebih besar dan sulit dibaca jika dibandingkan dengan JSON.

####JSON (JavaScript Object Notation):

- Sebuah format pertukaran data yang menggunakan struktur objek dan array yang sangat mudah dibaca, dengan data disusun dalam pasangan `key` dan `value`.
- Sering digunakan untuk berkomunikasi data antara aplikasi web dan server, serta sebagai format konfigurasi yang dapat dengan mudah dimengerti.
- Lebih ringan dan lebih mudah dibaca daripada XML, menjadikannya pilihan yang lebih populer untuk pertukaran data di web.

####HTML (HyperText Markup Language):

- Bahasa *markup* yang digunakan untuk membangun halaman web dengan fokus pada tampilan dan presentasi halaman.
- Utamanya digunakan untuk membuat halaman web yang bisa diakses melalui browser web dan bukan digunakan untuk pertukaran data.
- Memiliki aturan sintaksis yang ketat, tetapi tujuannya lebih ke representasi visual daripada manipulasi data mentah.

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena kelebihan berikut:

- JSON memiliki format data yang sangat ringan dan mudah dibaca. Sintaksisnya sederhana dan terdiri dari pasangan `key`-`value` yang membuatnya mudah dipahami.

- JSON cocok untuk berbagai jenis data. Anda dapat dengan mudah mewakili data kompleks, termasuk objek, array, dan tipe data primitif, menjadikannya format yang sangat fleksibel.

- JSON didukung oleh banyak bahasa pemrograman sehingga sangat cocok untuk pengembangan aplikasi web yang melibatkan berbagai teknologi.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

## Membuat Page Untuk Input Data
1. Buat file `forms.py` pada direktori main dan tambahkan kode berikut.
```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "description"]
```

2. Buka `views.py` pada folder main dan tambahkan import berikut. 
```python
from django.urls import reverse
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import Product
```

kemudian buatlah fungsi baru `create_product` untuk menerima data secara otomatis ketika data di-*submit* dari *form*.

```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

3. Ubah fungsi `show_main` pada `views.py` menjadi seperti berikut.

```python
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'M Azmy Arya Rizaldi M',
        'class': 'PBP A',
        'products': products
    }

    return render(request, "main.html", context)
```
4. Buat file HTML baru bernama `create_product.html` pada `main/templates` sebagai tampilan `form` saat akan menambahkan product

```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
5. Tampilkan tombol `Add New Product` pada `main.html`
```html
...
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
    
        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.amount}}</td>
                <td>{{product.description}}</td>
                <td>{{product.date_added}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
{% endblock content %}
```

## **Fungsi untuk mengembalikan data dalam bentuk XML dan JSON**
1. Pada `views.py` yang berada di folder `main` tambahkan *import* berikut.
```python
from django.http import HttpResponse
from django.core import serializers
```

2. Buatlah fungsi untuk mengambil semua objek `Product` dan mengembalikannya dalam bentuk `HttpResponse` berisi data yang sudah di-_serialize_ menggunakan `serializers` sesuai format yang diinginkan. 
```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

## **Membuat _routing_**
1. Buka `urls.py` pada `main` dan import semua fungsi yang sudah dibuat.
```python
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```

2. Tambahkan *path url* untuk masing-masing fungsi ke dalam `urlpatterns`.
```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
]
```  
Jalankan dengan perintah `python manage.py runserver` dan aplikasi dapat diakses pada [http://localhost:8000](http://localhost:8000).

### 5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman.

#### HTML
![Bagan](/img/html.png "HTML")
#### JSON
![Bagan](/img/json.png "JSON")
#### JSON by ID
![Bagan](/img/json_by_id.png "JSON by ID")
#### XML
![Bagan](/img/xml.png "XML")
#### XML by ID
![Bagan](/img/xml_by_id.png "XML by ID")

</details>