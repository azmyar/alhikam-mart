# Alhikam Mart.

# Questions
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

### Membuat model pada aplikasi `main` dengan nama `Item`
1. Buka file `models.py` kemudian buat objek model dengan mendefinisikan atribut-atribut yang ingin kita gunakan seperti sebagai berikut.
```python
from django.db import models

class Item(models.Model):
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

Dengan menjalankan langkah-langkah ini, kita telah berhasil membuat model pada aplikasi `main` dengan nama `Item`.

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

#####- MVC: 
&emsp;**Model** mengelola data, **View** menampilkan data, dan **Controller** mengatur logika aplikasi. Hubungan satu arah antara Model, View, dan Controller.

#####- MVT: 
&emsp;Mirip dengan MVC, tetapi Controller digantikan oleh **Template**, yang mengatur tampilan dan logika presentasi di dalam tampilan HTML. MVT biasanya terkait dengan kerangka kerja web seperti **Django.**

#####- MVVM: 
&emsp;**Model** mengelola data, **View** menampilkan data, dan **ViewModel** bertindak sebagai perantara antara keduanya. ViewModel memungkinkan View berkomunikasi dengan Model tanpa mengetahui detail implementasi Model. Digunakan terutama dalam aplikasi berbasis tampilan data seperti desktop dan mobile.