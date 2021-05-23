import googlemaps 
from .forms import *
from .models import *
from . import config
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.serializers import serialize



# Create your views here.

gmaps = googlemaps.Client(key='AIzaSyCWSUlUYOtvj6AjAMvBE3XacynYkke_ZVc')  


@login_required(login_url = "user:login")
def index(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet
    }
    
    return render(request,"index.html",context)


def KullaniciListe(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    kullanicilar = User.objects.all()


    if request.is_ajax():
        if request.method == "POST":
            kid = request.POST['id']
            config.SecilenKullaniciID = kid
        else:
            kid = request.GET['id'] 
            config.SecilenKullaniciID = kid

        kullanici = get_object_or_404(User,id = kid)
        kullaniciExtra = UserExtra.objects.filter(user_id=kid).first()
    
        form = KullaniciDetayForm(request.POST or None,request.FILES or None,instance = kullanici)
        kExtraForm = UserExtraForm(request.POST or None,request.FILES or None,instance = kullaniciExtra)

        kEklenenFirmalar = SaglikKuruluslari.objects.filter(author_id=kid)
        context = {
            "kdetay":kullanici,
            "form":form,
            "kExtraForm":kExtraForm,
            "kEklenenFirmalar":kEklenenFirmalar
        }
        return render(request,"Detay/kullanici.html",context)
    
    if request.method == "POST":
        kid = config.SecilenKullaniciID
        kullanici = get_object_or_404(User,id = kid)
        kullaniciExtra = UserExtra.objects.filter(user_id=kid).first()
    
        form = KullaniciDetayForm(request.POST or None,request.FILES or None,instance = kullanici)
        kExtraForm = UserExtraForm(request.POST or None,request.FILES or None,instance = kullaniciExtra)
        kaydet = form.save(commit=False)
        kaydet.save()

        messages.success(request,"Ayarlar başarıyla güncellendi")
        return redirect("base:index")


    

    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "kullanicilar":kullanicilar
    }

    return render(request,"Listele/kullanicilar.html",context)

@login_required(login_url = "user:login")
def ayarlar(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    userSettings = UserExtra.objects.filter(user_id=request.user.id).first()
    if not userSettings:
        new = UserExtra.objects.create(user=request.user)
        new.save()
    kayit = get_object_or_404(UserExtra,user_id = request.user.id)
    form = UserExtraForm(request.POST or None,request.FILES or None,instance = kayit)
    if form.is_valid():
        kaydet = form.save(commit=False)
        kaydet.user = request.user
        kaydet.save()

        messages.success(request,"Ayarlar başarıyla güncellendi")
        return redirect("base:index")
    
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form
    }
    return render(request,"User/settings.html",context)


def mesajYeni(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    if 'term' in request.GET:
        qs = User.objects.filter(username__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            if product.username != request.user.username:
                titles.append(product.username)
        return JsonResponse(titles, safe=False)
    if request.is_ajax():
        aliciusername = request.POST["alıcı"]
        mesaj = request.POST["mesaj"]
        alıcı = User.objects.get(username = aliciusername)
        if alıcı != request.user:
            mesajk = Mesajlar.objects.create(gonderen=request.user, alıcı=alıcı,mesaj=mesaj)
        
    
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet
            }
    return render(request, 'Mesaj/mesajyeni.html',context)


def mesajListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarHepsi = Mesajlar.objects.filter(alıcı=request.user)
    mesajlarAdet = len(mesajlar)
    context={
                "mesajlar":mesajlar,
                "mesajlarAdet":mesajlarAdet,
                "mesajlarHepsi":mesajlarHepsi
            }
    if request.is_ajax():
        
        mesajOkunduAra = request.POST['mesajOkunduAra']
        if mesajOkunduAra == 'Evet':
            mesajlarHepsi = Mesajlar.objects.filter(alıcı=request.user,okundu = False)
        else:
            mesajlarHepsi = Mesajlar.objects.filter(alıcı=request.user)
        
        
        context={
                "mesajlar":mesajlar,
                "mesajlarAdet":mesajlarAdet,
                "mesajlarHepsi":mesajlarHepsi
            }
        return render(request,"Mesaj/mesajlarajax.html",context)

    return render(request,"Mesaj/mesajlar.html",context)


def mesajDetay(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    mdetay = get_object_or_404(Mesajlar,id = id)
    mdetay.okundu = True
    mdetay.save()

    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "mdetay":mdetay
    }
    return render(request,"Mesaj/detay.html",context)


def saglikKuruluslariListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    kuruluslar = SaglikKuruluslari.objects.all()
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "kuruluslar":kuruluslar
    }
    if request.is_ajax():
        islem = request.POST['islem']
        if islem == "detayGoster":
            kid = request.POST['id']
            kdetay = get_object_or_404(SaglikKuruluslari,id = kid)

            return render(request,"Detay/kurulus.html",{"kdetay":kdetay})
        else:
            kurulusID = request.POST['kurulusID']
            kurulusAdi = request.POST['kurulusAdi']
            kurulusTuru= request.POST['kurulusTuru']
            kurulusDurumu = request.POST['kurulusDurumu']
    
            if kurulusID != "":
                kuruluslar = SaglikKuruluslari.objects.filter(id = kurulusID)
                context={
                    "mesajlar":mesajlar,
                    "mesajlarAdet":mesajlarAdet,
                    "kuruluslar":kuruluslar
                }
                return render(request,"Listele/ajaxListeleme/kurulus.html",context)
    
            else:
                if kurulusTuru == "Hepsi":
                    if kurulusDurumu == "Hepsi":
                        kuruluslar = SaglikKuruluslari.objects.filter(kurulusAdi__icontains=kurulusAdi)
                    else:
                        kuruluslar = SaglikKuruluslari.objects.filter(kurulusAdi__icontains=kurulusAdi,durum__icontains=kurulusDurumu)
                else:
                    if kurulusDurumu == "Hepsi":
                        kuruluslar = SaglikKuruluslari.objects.filter(kurulusAdi__icontains=kurulusAdi,kurulusTuru__icontains=kurulusTuru)
                    else:
                        kuruluslar = SaglikKuruluslari.objects.filter(kurulusAdi__icontains=kurulusAdi,kurulusTuru__icontains=kurulusTuru,durum__icontains=kurulusDurumu)

                context={
                    "mesajlar":mesajlar,
                    "mesajlarAdet":mesajlarAdet,
                    "kuruluslar":kuruluslar
                }
                return render(request,"Listele/ajaxListeleme/kurulus.html",context)

    
    return render(request,"Listele/kurulus.html",context)


def saglikKuruluslariHarita(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    kuruluslar = SaglikKuruluslari.objects.all().order_by("sehir")
    if request.is_ajax():
        islem = request.POST['islem']
        if islem == "sehirListele":
            sehir = request.POST['sehir']
            qs = Sehir.objects.filter(sehirAdi__icontains=sehir).order_by('sehirAdi')
            sehirler = list()
            for i in qs:
                sehirler.append(i.sehirAdi)
            return JsonResponse(sehirler, safe=False)
    if request.method == "POST":
        sehir = request.POST['sehir']
        ksehir = Sehir.objects.filter(sehirAdi=sehir).first()
        kuruluslar = SaglikKuruluslari.objects.filter(sehir=ksehir.id)
        context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "kuruluslar":kuruluslar
        }
            
        return render(request,"Listele/kurulusHarita.html",context)


    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "kuruluslar":kuruluslar
    }
    return render(request,"Listele/kurulusHarita.html",context)

def saglikKuruluslariEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    form = SaglikKuruluslariForm(request.POST or None,request.FILES or None)
    form2 = LocationForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        sehir = request.POST['sehir'].strip()
        ilce = request.POST['ilce'].strip()
        mahalle = request.POST['mahalle'].strip()
        sokak = request.POST['sokak'].strip()
        cadde = request.POST['cadde'].strip()
        kapiNo = request.POST['kapiNo'].strip()
        postaKodu = request.POST['pKodu'].strip()
        enlem = request.POST['enlem'].strip()
        boylam = request.POST['boylam'].strip()

        fsehir = Sehir.objects.filter(sehirAdi__icontains=sehir)
        filce= Ilce.objects.filter(ilceAdi__icontains=ilce)
        fmahalle = Mahalle.objects.filter(mahalleAdi__icontains=mahalle)
        fsokak = Sokak.objects.filter(sokakAdi__icontains=sokak)
        fcadde = Cadde.objects.filter(caddeAdi__icontains=cadde)
        
        if sehir != "":
            if not fsehir:
                ksehir = Sehir.objects.create(sehirAdi=sehir)
                ksehir.save()
                objSehir = Sehir.objects.get(id=ksehir.id)
            else:
                objSehir = Sehir.objects.get(sehirAdi=sehir)
        
        if ilce != "":
            if not filce:
                kilce = Ilce.objects.create(ilceAdi=ilce,sehir=objSehir)
                kilce.save()
                objIlce = Ilce.objects.get(id=kilce.id)
            else:
                objIlce = Ilce.objects.get(ilceAdi=ilce)
        
        if mahalle != "":
            if not fmahalle:
                kmahalle = Mahalle.objects.create(mahalleAdi=mahalle,ilce=objIlce)
                kmahalle.save()
                objMahalle = Mahalle.objects.get(id=kmahalle.id)
            else:
                objMahalle = Mahalle.objects.get(mahalleAdi=mahalle)
        
        if sokak != "":
            if not fsokak:
                ksokak = Sokak.objects.create(sokakAdi=sokak,mahalle=objMahalle)
                ksokak.save()
                objSokak = Sokak.objects.get(id=ksokak.id)
            else:
                objSokak = Sokak.objects.get(sokakAdi=sokak)
        
        if cadde != "":
            if not fcadde:
                kcadde = Cadde.objects.create(caddeAdi=cadde,sokak=objSokak)
                kcadde.save()
                objCadde = Cadde.objects.get(id=kcadde.id)
            else:
                objCadde = Cadde.objects.get(caddeAdi=cadde)
        
        kisiDetay = UserExtra.objects.get(user_id = request.user.id)
        kisiEnlem = kisiDetay.latitude
        kisiBoylam = kisiDetay.longitude
        uzaklik = gmaps.distance_matrix([str(kisiEnlem) + " " + str(kisiBoylam)], [str(enlem) + " " + str(boylam)], mode='driving')['rows'][0]['elements'][0]["distance"]["text"]
        uzaklik = uzaklik.replace("km","")
        uzaklik = uzaklik.strip()


        kurulus = form.save(commit=False)
        
        kurulus.author = request.user
        kurulus.sehir = objSehir
        kurulus.ilce = objIlce
        kurulus.mahalle = objMahalle
        kurulus.sokak = objSokak
        kurulus.cadde = objCadde
        kurulus.kapiNo = kapiNo
        kurulus.postaKodu = postaKodu
        kurulus.kisiUzaklik = uzaklik
        kurulus.save()

        messages.success(request,"Yeni -Sağlık Kuruluşu- başarıyla eklendi")
        
        return redirect("base:index")
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form,
        "form2":form2
    }   
    if request.is_ajax():
        islem = request.POST['islem']
        if islem == "sehirListele":
            sehir = request.POST['sehir']
            qs = Sehir.objects.filter(sehirAdi__icontains=sehir).order_by('sehirAdi')
            sehirler = list()
            for i in qs:
                sehirler.append(i.sehirAdi)
            return JsonResponse(sehirler, safe=False)
        if islem == "ilceListele":
            ilce = request.POST['ilce']
            qs = Ilce.objects.filter(ilceAdi__icontains=ilce).order_by('ilceAdi')
            ilceler = list()
            for i in qs:
                ilceler.append(i.ilceAdi)
            return JsonResponse(ilceler, safe=False)
        if islem == "mahalleListele":
            mahalle = request.POST['mahalle']
            qs = Mahalle.objects.filter(mahalleAdi__icontains=mahalle).order_by('mahalleAdi')
            mahalleler = list()
            for i in qs:
                mahalleler.append(i.mahalleAdi)
            return JsonResponse(mahalleler, safe=False)
        if islem == "sokakListele":
            sokak = request.POST['sokak']
            qs = Sokak.objects.filter(sokakAdi__icontains=sokak).order_by('sokakAdi')
            sokaklar = list()
            for i in qs:
                sokaklar.append(i.sokakAdi)
            return JsonResponse(sokaklar, safe=False)
        if islem == "caddeListele":
            cadde = request.POST['cadde']
            qs = Cadde.objects.filter(caddeAdi__icontains=cadde).order_by('caddeAdi')
            caddeler = list()
            for i in qs:
                caddeler.append(i.caddeAdi)
            return JsonResponse(caddeler, safe=False)
    
    return render(request,"Islem/kurulusekle.html",context)



def saglikKuruluslariDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    kurulus = get_object_or_404(SaglikKuruluslari,id = id)
    form = SaglikKuruluslariFullForm(request.POST or None,request.FILES or None,instance = kurulus)
    if form.is_valid():
        kurulus = form.save(commit=False)
        kurulus.author = request.user
        kurulus.save()

        messages.success(request,"Kurulus başarıyla güncellendi")
        return redirect("base:index")
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form
    }   
    return render(request,"Islem/duzenle.html",context)


def saglikKuruluslariSil(request,id):
    kurulus = get_object_or_404(SaglikKuruluslari,id = id)

    kurulus.delete()

    messages.success(request,"Kurulus Başarıyla Silindi")

    return redirect("base:index")


def hizmetListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    
    hizmetler = Hizmetler.objects.all()

    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "hizmetler":hizmetler
    } 
    return render(request,"Listele/hizmet.html",context)


def hizmetEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    form = HizmetlerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        hizmet = form.save(commit=False)
        hizmet.save()

        messages.success(request,"Yeni -Hizmet- başarıyla eklendi")
        return redirect("base:index")
    
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form
    } 
    return render(request,"Islem/ekle.html",context)


def hizmetDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    hizmet = get_object_or_404(Hizmetler,id = id)
    form = HizmetlerForm(request.POST or None,request.FILES or None,instance = hizmet)
    p
    if form.is_valid():
        hizmet = form.save(commit=False)
        hizmet.save()

        messages.success(request,"Hizmet başarıyla güncellendi")
        return redirect("base:index")

    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form
    }
    return render(request,"Islem/duzenle.html",context)


def hizmetSil(request,id):
    hizmet = get_object_or_404(Hizmetler,id = id)

    hizmet.delete()

    messages.success(request,"Hizmet Başarıyla Silindi")

    return redirect("base:index")


def saglikHizmetListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    hizmetler = SaglikHizmetler.objects.all()

    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "hizmetler":hizmetler
    }
    return render(request,"Listele/saglikhizmet.html",context)


def saglikHizmetEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = SaglikHizmetlerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        hizmet = form.save(commit=False)
        hizmet.save()

        messages.success(request,"Yeni -Sağlık Hizmeti- başarıyla eklendi")
        return redirect("base:index")
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form
    }
    return render(request,"Islem/ekle.html",context)


def saglikHizmetDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    hizmet = get_object_or_404(SaglikHizmetler,id = id)
    form = SaglikHizmetlerForm(request.POST or None,request.FILES or None,instance = hizmet)
    if form.is_valid():
        hizmet = form.save(commit=False)
        hizmet.save()

        messages.success(request,"Sağlık Hizmeti başarıyla güncellendi")
        return redirect("base:index")
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form
    }
    return render(request,"Islem/duzenle.html",{"form":form})


def saglikHizmetSil(request,id):
    hizmet = get_object_or_404(SaglikHizmetler,id = id)

    hizmet.delete()

    messages.success(request,"Sağlık Hizmeti Başarıyla Silindi")

    return redirect("base:index")


def kisilerListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    kisiler = Kisiler.objects.all()

    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "kisiler":kisiler
    }
    return render(request,"Listele/kisiler.html",context)


def kisilerEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = KisilerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        kisi = form.save(commit=False)
        kisi.save()

        messages.success(request,"Yeni -Kisi- başarıyla eklendi")
        return redirect("base:index")
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form
    }
    return render(request,"Islem/ekle.html",context)

def kisilerEkleByKurulus(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = KisilerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        kisi = form.save(commit=False)
        kisi.save()

        sagKurulus = SaglikKuruluslari.objects.get(id=id)
        sagKisi = SaglikKisiler.objects.create(kisiID=kisi,saglikID=sagKurulus)
        messages.success(request,"Yeni -Kisi-Kurulus- başarıyla eklendi")
        return redirect("base:index")
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form
    }
    return render(request,"Islem/ekle.html",context)


def kisilerDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    kisi = get_object_or_404(Kisiler,id = id)
    form = KisilerForm(request.POST or None,request.FILES or None,instance = kisi)
    if form.is_valid():
        kisi = form.save(commit=False)
        kisi.save()

        messages.success(request,"Kişi başarıyla güncellendi")
        return redirect("base:index")
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form
    }
    return render(request,"Islem/duzenle.html",context)


def kisilerSil(request,id):
    kisi = get_object_or_404(Kisiler,id = id)

    kisi.delete()

    messages.success(request,"Kişi Başarıyla Silindi")

    return redirect("base:index")


def saglikKisilerListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    kisiler = SaglikKisiler.objects.all()
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "kisiler":kisiler
    }
    return render(request,"Listele/saglikkisiler.html",context)


def saglikKisilerEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = SaglikKisilerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        kisi = form.save(commit=False)
        kisi.save()

        messages.success(request,"Yeni -Sağlık Kisi- başarıyla eklendi")
        return redirect("base:index")
    context={
        "mesajlar":mesajlar,
        "mesajlarAdet":mesajlarAdet,
        "form":form
    }
    return render(request,"Islem/ekle.html",context)


def saglikKisilerDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    kisi = get_object_or_404(SaglikKisiler,id = id)
    form = SaglikKisilerForm(request.POST or None,request.FILES or None,instance = kisi)
   
    if form.is_valid():
        kisi = form.save(commit=False)
        kisi.save()

        messages.success(request,"Kişi başarıyla güncellendi")
        return redirect("base:index")

    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/duzenle.html",context)


def saglikKisilerSil(request,id):
    kisi = get_object_or_404(SaglikKisiler,id = id)

    kisi.delete()

    messages.success(request,"Kişi Başarıyla Silindi")

    return redirect("base:index")


def uzmanliklarListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    uzmanliklar = Uzmanliklar.objects.all()
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "uzmanliklar":uzmanliklar
        }
    return render(request,"Listele/uzmanliklar.html",context)


def uzmanliklarEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = UzmanliklarForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        uzmanlik = form.save(commit=False)
        uzmanlik.save()

        messages.success(request,"Yeni -Uzmanlık- başarıyla eklendi")
        return redirect("base:index")
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/ekle.html",context)


def uzmanliklarDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    uzmanlik = get_object_or_404(Uzmanliklar,id = id)
    form = UzmanliklarForm(request.POST or None,request.FILES or None,instance = uzmanlik)
    if form.is_valid():
        uzmanlik = form.save(commit=False)
        uzmanlik.save()

        messages.success(request,"Uzmanlik başarıyla güncellendi")
        return redirect("base:index")
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/duzenle.html",context)


def uzmanliklarSil(request,id):
    uzmanlik = get_object_or_404(Uzmanliklar,id = id)

    uzmanlik.delete()

    messages.success(request,"Uzmanlık Başarıyla Silindi")

    return redirect("base:index")


def tedavilerListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    tedaviler = Tedaviler.objects.all()
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "tedaviler":tedaviler
        }
    return render(request,"Listele/tedaviler.html",context)


def tedavilerEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = TedavilerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        tedavi = form.save(commit=False)
        tedavi.save()

        messages.success(request,"Yeni -Tedavi- başarıyla eklendi")
        return redirect("base:index")
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/ekle.html",context)


def tedavilerDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    tedavi = get_object_or_404(Tedaviler,id = id)
    form = TedavilerForm(request.POST or None,request.FILES or None,instance = tedavi)
    if form.is_valid():
        tedavi = form.save(commit=False)
        tedavi.save()

        messages.success(request,"Tedavi başarıyla güncellendi")
        return redirect("base:index")

    context={
                "mesajlar":mesajlar,
                "mesajlarAdet":mesajlarAdet,
                "form":form
            }
    return render(request,"Islem/duzenle.html",context)


def tedavilerSil(request,id):
    tedavi = get_object_or_404(Tedaviler,id = id)

    tedavi.delete()

    messages.success(request,"Tedavi Başarıyla Silindi")

    return redirect("base:index")


def saglikTedavilerListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    tedaviler = SaglikTedaviler.objects.all()
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "tedaviler":tedaviler
        }
    return render(request,"Listele/sagliktedaviler.html",context)


def saglikTedavilerEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = SaglikTedavilerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        tedavi = form.save(commit=False)
        tedavi.save()

        messages.success(request,"Yeni -Sağlık Tedavi- başarıyla eklendi")
        return redirect("base:index")
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/ekle.html",context)


def saglikTedavilerDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    tedavi = get_object_or_404(SaglikTedaviler,id = id)
    form = SaglikTedavilerForm(request.POST or None,request.FILES or None,instance = tedavi)
    if form.is_valid():
        tedavi = form.save(commit=False)
        tedavi.save()

        messages.success(request,"Sağlık Tedavi başarıyla güncellendi")
        return redirect("base:index")


    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/duzenle.html",context)


def saglikTedavilerSil(request,id):
    tedavi = get_object_or_404(SaglikTedaviler,id = id)

    tedavi.delete()

    messages.success(request,"Sağlık Tedavi Başarıyla Silindi")

    return redirect("base:index")


def seviyelerListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    seviyeler = Seviyeler.objects.all()
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "seviyeler":seviyeler
        }
    return render(request,"Listele/seviyeler.html",context)


def seviyelerEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = SeviyelerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        seviye = form.save(commit=False)
        seviye.save()

        messages.success(request,"Yeni -Seviye- başarıyla eklendi")
        return redirect("base:index")
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/ekle.html",context)


def seviyelerDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    seviye = get_object_or_404(Seviyeler,id = id)
    form = SeviyelerForm(request.POST or None,request.FILES or None,instance = seviye)
    if form.is_valid():
        seviye = form.save(commit=False)
        seviye.save()

        messages.success(request,"Seviye başarıyla güncellendi")
        return redirect("base:index")


    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/duzenle.html",context)


def seviyelerSil(request,id):
    seviye = get_object_or_404(Seviyeler,id = id)

    seviye.delete()

    messages.success(request,"Seviye Başarıyla Silindi")

    return redirect("base:index")


def personelListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    personeller = Personeller.objects.all()
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "personeller":personeller
        }
    return render(request,"Listele/personeller.html",context)


def personelEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = PersonellerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        personel = form.save(commit=False)
        personel.save()

        messages.success(request,"Yeni -Personel- başarıyla eklendi")
        return redirect("base:index")
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/ekle.html",context)


def personelDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    personel = get_object_or_404(Personeller,id = id)
    form = PersonellerForm(request.POST or None,request.FILES or None,instance = personel)
    if form.is_valid():
        personel = form.save(commit=False)
        personel.save()

        messages.success(request,"Personel başarıyla güncellendi")
        return redirect("base:index")


    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/duzenle.html",context)


def personelSil(request,id):
    personel = get_object_or_404(Personeller,id = id)

    personel.delete()

    messages.success(request,"Personel Başarıyla Silindi")

    return redirect("base:index")


def notlarListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    
    notlar = Notlar.objects.all()
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "notlar":notlar
        }
    return render(request,"Listele/notlar.html",context)


def notlarEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = NotlarForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        notv = form.save(commit=False)
        notv.save()

        messages.success(request,"Yeni -Not- başarıyla eklendi")
        return redirect("base:index")
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/ekle.html",context)


def notlarDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    notv = get_object_or_404(Notlar,id = id)
    form = NotlarForm(request.POST or None,request.FILES or None,instance = notv)
    if form.is_valid():
        notv = form.save(commit=False)
        notv.save()

        messages.success(request,"Not başarıyla güncellendi")
        return redirect("base:index")


    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/duzenle.html",context)


def notlarSil(request,id):
    notv = get_object_or_404(Notlar,id = id)

    notv.delete()

    messages.success(request,"Not Başarıyla Silindi")

    return redirect("base:index")


def kisiNotlarListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    notlar = KisiNotlar.objects.all()
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "notlar":notlar
        }
    return render(request,"Listele/kisinotlar.html",context)


def kisiNotlarEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = KisiNotlarForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        notv = form.save(commit=False)
        notv.save()

        messages.success(request,"Yeni -Kişi Notu- başarıyla eklendi")
        return redirect("base:index")
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/ekle.html",context)


def kisiNotlarDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    notv = get_object_or_404(KisiNotlar,id = id)
    form = KisiNotlarForm(request.POST or None,request.FILES or None,instance = notv)
    if form.is_valid():
        notv = form.save(commit=False)
        notv.save()

        messages.success(request,"Kişi notu başarıyla güncellendi")
        return redirect("base:index")


    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/duzenle.html",context)


def kisiNotlarSil(request,id):
    notv = get_object_or_404(KisiNotlar,id = id)

    notv.delete()

    messages.success(request,"Kişi Notu Başarıyla Silindi")

    return redirect("base:index")


def saglikNotlarListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    notlar = SaglikNotlar.objects.all()
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "notlar":notlar
        }
    return render(request,"Listele/sagliknotlar.html",context)


def saglikNotlarEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = SaglikNotlarForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        notv = form.save(commit=False)
        notv.save()

        messages.success(request,"Yeni -Sağlık Notu- başarıyla eklendi")
        return redirect("base:index")
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/ekle.html",context)


def saglikNotlarDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    notv = get_object_or_404(SaglikNotlar,id = id)
    form =SaglikNotlarForm(request.POST or None,request.FILES or None,instance = notv)
    if form.is_valid():
        notv = form.save(commit=False)
        notv.save()

        messages.success(request,"Sağlık notu başarıyla güncellendi")
        return redirect("base:index")


    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/duzenle.html",context)


def saglikNotlarSil(request,id):
    notv = get_object_or_404(SaglikNotlar,id = id)

    notv.delete()

    messages.success(request,"Sağlık Notu Başarıyla Silindi")

    return redirect("base:index")


def personelSaglikListele(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)

    psaglik = PersonelSaglik.objects.all()
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "psaglik":psaglik
        }
    return render(request,"Listele/personelsaglik.html",context)


def personelSaglikEkle(request):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    form = PersonelSaglikForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        psaglik = form.save(commit=False)
        psaglik.save()

        messages.success(request,"Yeni -Personel Sağlık- başarıyla eklendi")
        return redirect("base:index")
    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/ekle.html",context)


def personelSaglikDuzenle(request,id):
    mesajlar = Mesajlar.objects.filter(alıcı=request.user,okundu=False)
    mesajlarAdet = len(mesajlar)
    psaglik = get_object_or_404(PersonelSaglik,id = id)
    form =PersonelSaglikForm(request.POST or None,request.FILES or None,instance = psaglik)
    if form.is_valid():
        psaglik = form.save(commit=False)
        psagliknotv.save()

        messages.success(request,"Personel Sağlık başarıyla güncellendi")
        return redirect("base:index")


    context={
            "mesajlar":mesajlar,
            "mesajlarAdet":mesajlarAdet,
            "form":form
        }
    return render(request,"Islem/duzenle.html",context)


def personelSaglikSil(request,id):
    psaglik = get_object_or_404(PersonelSaglik,id = id)

    psaglik.delete()

    messages.success(request,"Personel Saglik Başarıyla Silindi")

    return redirect("base:index")