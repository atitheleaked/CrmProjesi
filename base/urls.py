
from django.urls import path
from . import views

app_name="base"


urlpatterns = [
    path('', views.index, name = "index"),

    ## Mesajlar    
    path('mesajyeni/', views.mesajYeni, name = "mesajYeni"),
    path('mesajlar/', views.mesajListele, name = "mesajListele"),
    path('mesajdetay/<int:id>', views.mesajDetay, name = "mesajDetay"),


    ## SaglikKuruluslari
    path('kuruluslistele/', views.saglikKuruluslariListele, name = "kurulusListele"),
    path('kurulusharita/', views.saglikKuruluslariHarita, name = "kurulusHarita"),
    path('kurulusekle/', views.saglikKuruluslariEkle, name = "kurulusEkle"),
    path('kurulusduzenle/<int:id>',views.saglikKuruluslariDuzenle,name = "kurulusDuzenle"),
    path('kurulussil/<int:id>',views.saglikKuruluslariSil,name = "kurulusSil"),

    ## SağlıkHizmet
    path('saglikhizmetlistele/', views.saglikHizmetListele, name = "saglikHizmetListele"),
    path('saglikhizmetekle/', views.saglikHizmetEkle, name = "saglikHizmetEkle"),
    path('saglikhizmetduzenle/<int:id>',views.saglikHizmetDuzenle,name = "saglikHizmetDuzenle"),
    path('saglikhizmetsil/<int:id>',views.saglikHizmetSil,name = "saglikHizmetSil"),

    ## Hizmetler
    path('hizmetlistele/', views.hizmetListele, name = "hizmetListele"),
    path('hizmetekle/', views.hizmetEkle, name = "hizmetEkle"),
    path('hizmetduzenle/<int:id>',views.hizmetDuzenle,name = "hizmetDuzenle"),
    path('hizmetsil/<int:id>',views.hizmetSil,name = "hizmetSil"),

    ## Kişiler
    path('kisilerlistele/', views.kisilerListele, name = "kisilerListele"),
    path('kisilerekle/', views.kisilerEkle, name = "kisilerEkle"),
    path('kisilerduzenle/<int:id>',views.kisilerDuzenle,name = "kisilerDuzenle"),
    path('kisilersil/<int:id>',views.kisilerSil,name = "kisilerSil"),

    ## Sağlık Kişiler
    path('saglikkisilerlistele/', views.saglikKisilerListele, name = "saglikKisilerListele"),
    path('saglikkisilerekle/', views.saglikKisilerEkle, name = "saglikKisilerEkle"),
    path('saglikkisilerduzenle/<int:id>',views.saglikKisilerDuzenle,name = "saglikKisilerDuzenle"),
    path('saglikkisilersil/<int:id>',views.saglikKisilerSil,name = "saglikKisilerSil"),

    ## Uzmanlıklar
    path('uzmanliklarlistele/', views.uzmanliklarListele, name = "uzmanliklarListele"),
    path('uzmanliklarekle/', views.uzmanliklarEkle, name = "uzmanliklarEkle"),
    path('uzmanliklarduzenle/<int:id>',views.uzmanliklarDuzenle,name = "uzmanliklarDuzenle"),
    path('uzmanliklarsil/<int:id>',views.uzmanliklarSil,name = "uzmanliklarSil"),

    ## Tedaviler
    path('tedavilerlistele/', views.tedavilerListele, name = "tedavilerListele"),
    path('tedavilerekle/', views.tedavilerEkle, name = "tedavilerEkle"),
    path('tedavilerduzenle/<int:id>',views.tedavilerDuzenle,name = "tedavilerDuzenle"),
    path('tedavilersil/<int:id>',views.tedavilerSil,name = "tedavilerSil"),

    ## Sağlık Tedaviler
    path('sagliktedavilerlistele/', views.saglikTedavilerListele, name = "saglikTedavilerListele"),
    path('sagliktedavilerekle/', views.saglikTedavilerEkle, name = "saglikTedavilerEkle"),
    path('sagliktedavilerduzenle/<int:id>',views.saglikTedavilerDuzenle,name = "saglikTedavilerDuzenle"),
    path('sagliktedavilersil/<int:id>',views.saglikTedavilerSil,name = "saglikTedavilerSil"),

    ## Seviyeler
    path('seviyelerlistele/', views.seviyelerListele, name = "seviyelerListele"),
    path('seviyelerekle/', views.seviyelerEkle, name = "seviyelerEkle"),
    path('seviyelerduzenle/<int:id>',views.seviyelerDuzenle,name = "seviyelerDuzenle"),
    path('seviyelersil/<int:id>',views.seviyelerSil,name = "seviyelerSil"),

    ## Personeller
    path('personellistele/', views.personelListele, name = "personelListele"),
    path('personelekle/', views.personelEkle, name = "personelEkle"),
    path('personelduzenle/<int:id>',views.personelDuzenle,name = "personelDuzenle"),
    path('personelsil/<int:id>',views.personelSil,name = "personelSil"),

    ## Notlar
    path('notlarlistele/', views.notlarListele, name = "notlarListele"),
    path('notlarekle/', views.notlarEkle, name = "notlarEkle"),
    path('notlarduzenle/<int:id>',views.notlarDuzenle,name = "notlarDuzenle"),
    path('notlarsil/<int:id>',views.notlarSil,name = "notlarSil"),

    ## Kişi Notlar
    path('kisinotlarlistele/', views.kisiNotlarListele, name = "kisiNotlarListele"),
    path('kisinotlarekle/', views.kisiNotlarEkle, name = "kisiNotlarEkle"),
    path('kisinotlarduzenle/<int:id>',views.kisiNotlarDuzenle,name = "kisiNotlarDuzenle"),
    path('kisinotlarsil/<int:id>',views.kisiNotlarSil,name = "kisiNotlarSil"),

    ## Sağlık Notlar
    path('saglikNotlarlistele/', views.saglikNotlarListele, name = "saglikNotlarListele"),
    path('saglikNotlarekle/', views.saglikNotlarEkle, name = "saglikNotlarEkle"),
    path('saglikNotlarduzenle/<int:id>',views.saglikNotlarDuzenle,name = "saglikNotlarDuzenle"),
    path('saglikNotlarsil/<int:id>',views.saglikNotlarSil,name = "saglikNotlarSil"),

    ## Personel Sağlık
    path('personelsagliklistele/', views.personelSaglikListele, name = "personelSaglikListele"),
    path('personelsaglikekle/', views.personelSaglikEkle, name = "personelSaglikEkle"),
    path('personelsaglikduzenle/<int:id>',views.personelSaglikDuzenle,name = "personelSaglikDuzenle"),
    path('personelsagliksil/<int:id>',views.personelSaglikSil,name = "personelSaglikSil"),
    
    
]
