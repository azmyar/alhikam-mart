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

#### XML (Extensible Markup Language):

- Sebuah bahasa *markup* yang digunakan untuk mendefinisikan struktur data hierarkis dengan menggunakan tag `<>` untuk mengidentifikasi elemen-elemen dalam data.
- Biasanya dipakai untuk mengirimkan data antara berbagai aplikasi dan sebagai format penyimpanan yang dapat diurai oleh berbagai program.
- Dikenal karena memiliki aturan sintaksis yang ketat dan menghasilkan dokumen yang cenderung lebih besar dan sulit dibaca jika dibandingkan dengan JSON.

#### JSON (JavaScript Object Notation):

- Sebuah format pertukaran data yang menggunakan struktur objek dan array yang sangat mudah dibaca, dengan data disusun dalam pasangan `key` dan `value`.
- Sering digunakan untuk berkomunikasi data antara aplikasi web dan server, serta sebagai format konfigurasi yang dapat dengan mudah dimengerti.
- Lebih ringan dan lebih mudah dibaca daripada XML, menjadikannya pilihan yang lebih populer untuk pertukaran data di web.

#### HTML (HyperText Markup Language):

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

<details>
<summary>&ensp;Tugas 4</summary>

### 1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

`UserCreationForm` merupakan form bawaan yang disediakan oleh Django dalam modul `django.contrib.auth` untuk mengelola proses autentikasi dan otorisasi pengguna. Form ini digunakan untuk membuat formulir pendaftaran (sign-up) pengguna baru di aplikasi web.

- #### **Kelebihan**
    - **Mudah Digunakan**, `UserCreationForm` menyediakan form pendaftaran siap pakai yang dapat gunakan dengan mudah dalam proyek Django.
    - **Dukungan Keamanan**, `UserCreationForm` memiliki dukungan keamanan bawaan, termasuk hashing kata sandi pengguna dan pemastian kata sandi yang cukup kuat.
    - **Integrasi dengan Django Model**, `UserCreationForm` sudah terintegrasi dengan model user bawaan Django, sehingga tidak perlu menulis kode tambahan untuk menyimpan data user ke dalam *database*.
- #### **Kekurangan**
    - **Keterbatasan Desain**, `UserCreationForm` memiliki tampilan standar yang mungkin tidak sesuai dengan desain antarmuka pengguna (UI) yang diinginkan sehingga perlu ada penyesuasian tampilan.
    - **Keterbatasan Kustomisasi**, `UserCreationForm` hanya mengumpulkan informasi dasar seperti username dan password. Informasi tambahan seperti alamat email atau data profil lainnya harus ditambahkan secara manual.

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
|| Autentikasi | Otorisasi |
|:-:|:-:|:-:|
|Definisi|Proses verifikasi identitas pengguna yang menentukan apakah pengguna adalah orang yang mereka klaim sebagai identitasnya.|Proses menentukan apa yang diizinkan atau dilarang oleh pengguna yang telah diautentikasi. Ini menentukan apa yang dapat diakses atau dilakukan oleh pengguna yang telah terautentikasi dalam aplikasi.|
|Tujuan|Untuk memverifikasi apakah seorang pengguna adalah pengguna yang sah atau telah terdaftar dalam sistem.|Untuk mengendalikan hak akses pengguna terhadap sumber daya atau fitur tertentu dalam aplikasi.|

&emsp;Autentikasi dan otorisasi adalah dua aspek penting dan saling melengkapi dalam mengelola keamanan dan akses dalam aplikasi web. Kedua konsep ini bekerja bersama untuk menjaga keamanan dan pengelolaan hak akses, memastikan bahwa pengguna hanya dapat mengakses informasi dan melakukan tindakan yang sesuai dengan *role* dan izin mereka.

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

&emsp;Cookies dalam konteks aplikasi web adalah sejenis data kecil yang disimpan di komputer pengguna oleh server web. Cookies digunakan untuk menyimpan informasi spesifik di sisi klien (browser pengguna) yang dapat diakses oleh server saat pengguna melakukan permintaan kembali ke situs web tertentu.

&emsp;Django menggunakan cookies untuk mengelola data sesi pengguna dengan menggunakan komponen yang disebut "Session Framework." Ini memungkinkan Anda menyimpan data sesi pengguna di server, sementara hanya session ID yang disimpan di cookie pengguna. Dengan session ID ini, Django dapat mengidentifikasi sesi pengguna saat pengguna kembali ke situs web dan mengakses data sesi tersebut. Ini memungkinkan penyimpanan informasi seperti status otentikasi pengguna, preferensi, dan lainnya dengan aman dan efisien.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

&emsp;Penggunaan cookies dalam pengembangan web bisa menjadi **aman secara default,** tetapi **ada potensi risiko** yang harus diwaspadai dan dikelola dengan baik. Beberapa risiko potensial yang terkait dengan penggunaan cookies meliputi:

- **Kehilangan Privasi:** Cookies dapat digunakan untuk melacak perilaku pengguna di seluruh situs web dan bahkan melintasi berbagai situs web. Jika tidak dikelola dengan baik, ini dapat mengancam privasi pengguna dan menciptakan potensi untuk pelacakan yang tidak diinginkan.

- **Cookie Theft (Pencurian Cookie):** Jika cookie yang berisi data sensitif atau otentikasi pengguna dicuri oleh pihak yang tidak sah, maka pihak tersebut dapat mengakses akun pengguna tanpa izin. Ini adalah risiko yang perlu diwaspadai terutama dalam konteks otentikasi.

- **Cross-Site Scripting (XSS):** Serangan XSS dapat mengakibatkan injeksi kode jahat ke dalam cookie pengguna, yang dapat menyebabkan risiko keamanan yang serius jika cookie tersebut digunakan untuk otentikasi.

- **Cross-Site Request Forgery (CSRF):** Serangan CSRF dapat memanipulasi cookie pengguna untuk melakukan tindakan tidak diinginkan atas nama pengguna yang diautentikasi.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Mengimplementasikan Autentikasi

#### Step 1: Menambahkan *import* dan fungsi yang sesuai pada file views.py

- #### Imports
```python
...
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
```
- #### Fungsi
##### 1. Fungsi Register
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

##### 2. Fungsi Login
```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

##### 3. Fungsi Logout
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

#### Step 2: Menambahkan template untuk tampilan login dan register
Buat berkas HTML baru dengan nama `register.html` dan `login.html` pada folder `main/templates`

- ##### Template Login
login.html
```python
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
- #### Template Register
register.html
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

#### Step 3: Menambahkan *import* dan *url path* yang sesuai pada file views.py
- #### Imports
```python
from main.views import register, login_user, logout_user
```
- #### URL Paths
```python
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
path('register/', register, name='register'),
```
### Mengimplementasikan Otentikasi
#### Step 1: Menambahkan *import* yang sesuai pada file views.py
```python
from django.contrib.auth.decorators import login_required
```
#### Step 2: Menambahkan *code* diatas fungsi yang akan direstriksi / memerlukan otentikasi
```python
@login_required(login_url='/login')
def restricted_function(request):
...
```
### Menghubungkan Model `Product` dengan `User`
#### Step 1: Menambahkan *import* yang sesuai pada file models.py
```python
from django.contrib.auth.decorators import login_required
```
#### Step 2: Menambahkan *attribute*  `user` pada Class `Product`
```python
...
user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```
#### Step 3: Memodifikasi Fungsi pada views.py
- create_product
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    # Modified
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

- context pada show_main
```python
context = {
    'name': request.user.username,  
    'class': 'PBP A',
    'products': products,
}
```

### Menggunakan Data Dari Cookies
#### Step 1: Menambahkan *import* yang sesuai pada file views.py
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
#### Step 2: Memodifikasi Fungsi pada views.py
- login_user
```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # Modified
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

- context pada show_main
```python
context = {
    'name': request.user.username,  
    'class': 'PBP A',
    'products': products,
    'last_login': request.COOKIES['last_login'],
}
```

- logout_user
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
#### Step 3: Tampilkan data dari Cookies pada template
tambahkan kode berikut pada `main.html`
```python
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

</details>

<details>
<summary>&ensp;Tugas 5</summary>

### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

- #### Element Selector
&emsp;Digunakan ketika ingin menggunakan *styling* yang sama pada semua elemen dengan **tag HTML**tertentu pada halaman web.

- #### ID Selector

&emsp;Digunakan ketika ingin menggunakan *styling* pada elemen spesifik dalam halaman web karena **ID bersifat unik.**jadi ini sangat berguna untuk mengidentifikasi elemen spesifik yang akan diubah tampilannya.

- #### Class Selector
&emsp;Digunakan ketika Anda ingin menggunakan *styling* pada sekelompok elemen yang memiliki kelas yang sama. Ini memungkinkan untuk mengaplikasikan *styling* yang sama pada beberapa elemen **tanpa** harus mengulangi kode CSS yang sama **berulang-ulang.**

### 2. Jelaskan HTML5 Tag yang kamu ketahui.
`<html>`: Tag ini menandai awal dan akhir dari dokumen HTML dan berisi seluruh konten halaman web.

`<head>`: Bagian ini berisi informasi meta tentang halaman web, seperti judul, meta deskripsi, dan link ke file CSS atau JavaScript.

`<title>`: Ini digunakan untuk menentukan judul halaman web yang akan ditampilkan di tab browser.

`<link>`: Tag ini digunakan untuk menghubungkan halaman web dengan file eksternal, seperti stylesheet (CSS).

`<style>`: Ini adalah tempat Anda menempatkan kode CSS untuk menggaya halaman web secara internal.

`<script>`: Ini adalah tempat Anda menempatkan kode JavaScript yang akan dieksekusi oleh browser.

`<body>`: Bagian ini berisi konten yang akan ditampilkan pada halaman web, seperti teks, gambar, video, dan elemen lainnya.

`<h1>`,`<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`: Tag-tag ini digunakan untuk membuat heading atau judul dengan tingkat kepentingan yang berbeda. `<h1>` adalah yang tertinggi, sedangkan `<h6>` adalah yang terendah.

`<p>`: Ini digunakan untuk membuat paragraf teks.

`<a>`: Ini digunakan untuk membuat tautan atau hyperlink.

`<img>`: Tag ini digunakan untuk menampilkan gambar pada halaman web.

`<div>`: Tag ini digunakan untuk mengelompokkan dan mengatur konten dalam blok atau wadah.

### 3. Jelaskan perbedaan antara margin dan padding.
![Bagan](/img/MarginPadding.png "Bagan")
- **Margin** merupakan jarak antara border ke elemen lainnya di luar border
- **Padding** merupakan jarak antara border ke konten di dalamnya

### 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

- Bootstrap merupakan framework CSS dengan pendekatan desain yang lebih terstruktur dan telah mendefinisikan komponen UI yang siap pakai.

- Tailwind CSS adalah framework CSS yang lebih mengutamakan fleksibilitas. Ini memberikan sejumlah kelas *styling* yang dapat digunakan untuk membangun komponen dan tampilan sesuai kebutuhan.

Jika ingin membangun web yang memiliki **tampilan konsisten** dan **tidak banyak waktu** untuk merancang tampilan dari awal, maka adalah ide bagus untuk memilih framework **Bootstrap**. 

Namun jika ingin membangun web yang memerlukan **kustomisasi yang lebih besar** dan **tampilan yang unik**, maka akan lebih cocok jika menggunakan framework **Tailwind.**

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Styling menggunakan inline dan internal CSS.

</details>