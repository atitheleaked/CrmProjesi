/*
///// Giriş panelini deaktif ettiği için kaldırıldı
$(document).ready(function(){
    //Menüde <a> taglarına tıklandığında sayfa yenileme işlemini bloke eder.
    $('#SideMenu > ul > li > a').attr('class','ignore-click')
    console.log("Classlar eklendi.")
    $('.ignore-click').on("click",function(e){
        e.preventDefault();
        console.log("Tıklama Engellendi.")
    })
})
*/
var src = "http://maps.googleapis.com/maps/api/js?libraries=geometry&sensor=false&key=AIzaSyCWSUlUYOtvj6AjAMvBE3XacynYkke_ZVc&callback=initMap"

$('#alici').change(function(){
    $('.ui-helper-hidden-accessible').css('display','none')
})





$('#sehir').keyup(function(){
    $sehir = $('#sehir').val();
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            islem:'sehirListele',
            sehir: $sehir,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $("#sehir").autocomplete({
                source: response,
                minLength: 2,
                messages: {
                    noResults: '',
                    results: function() {}
                }
            });
        },
        error: function(){
        }
    });
})
$('#ilce').keyup(function(){
    $ilce = $('#ilce').val();
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            islem:'ilceListele',
            ilce: $ilce,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $("#ilce").autocomplete({
                source: response,
                minLength: 2,
                messages: {
                    noResults: '',
                    results: function() {}
                }
            });
        },
        error: function(){
        }
    });
})
$('#mahalle').keyup(function(){
    $mahalle = $('#mahalle').val();
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            islem:'mahalleListele',
            mahalle: $mahalle,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $("#mahalle").autocomplete({
                source: response,
                minLength: 2,
                messages: {
                    noResults: '',
                    results: function() {}
                }
            });
        },
        error: function(){
        }
    });
})
$('#sokak').keyup(function(){
    $sokak = $('#sokak').val();
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            islem:'sokakListele',
            sokak: $sokak,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $("#sokak").autocomplete({
                source: response,
                minLength: 2,
                messages: {
                    noResults: '',
                    results: function() {}
                }
            });
        },
        error: function(){
        }
    });
})
$('#cadde').keyup(function(){
    $cadde = $('#cadde').val();
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            islem:'caddeListele',
            cadde: $cadde,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $("#cadde").autocomplete({
                source: response,
                minLength: 2,
                messages: {
                    noResults: '',
                    results: function() {}
                }
            });
        },
        error: function(){
        }
    });
})




$(function () {
    $("#alici").autocomplete({
        source: '',
        minLength: 2,
        messages: {
            noResults: '',
            results: function() {}
        }
    });
});

function detayGoster(id){
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            islem:'detayGoster',
            id: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('.modal-dialog').css('display','block')
            $('#DetayModal').html(response);
            console.log("çalışmalı")
        },
        error: function(){
            alert('birşeyler hatalı!');
        }
    });
}


$('.ignore-click').on("click",function(e){
    e.preventDefault();
    console.log("Tıklama Engellendi.")
})
$('.treeview').click(function(){
    if($(this).find('ul').attr('class') == "treeview-menu"){
        $('.treeview').find('.treeview-menu-open').css('display','none')
        $('.treeview').find('.treeview-menu-open').attr('class','treeview-menu')

        $(this).find('ul').css({'display':'block'})
        $(this).find('ul').attr('class', 'treeview-menu-open');
        $(this).find('a .pull-right svg').attr('class','fa fa-angle-down')
        
    }
    else{
        $(this).find('ul').css({'display':'none'})
        $(this).find('ul').attr('class', 'treeview-menu');
        $(this).find('a .pull-right svg').attr('class','fa fa-angle-left')
    }
})
$('#HideSideNav').click(function(){

    if($('#HideSideNav svg').attr('class') == "svg-inline--fa fa-chevron-circle-left fa-w-16"){
        $('#SideMenu').hide();
        $('#TopMenu').css({"width":"100%"})
        $('#MainSide').css({"width":"100%"})
        $('#HideSideNav svg').attr("class", "fa fa-chevron-circle-right")
    }
    else{
        $('#SideMenu').show();
        $('#TopMenu').css({"width":"calc(100vw - 250px)"})
        $('#MainSide').css({"width":"calc(100vw - 250px)"})
        $('#HideSideNav svg').attr("class", "svg-inline--fa fa-chevron-circle-left fa-w-16")
    }
})


$('#TopMenu ul li').click(function(){
    
    if($(this).find('ul').attr('class') == "dropdown-menu"){
        $('#TopMenu ul li').find('.dropdown-menu-open').css('display','none')
        $('#TopMenu ul li').find('.dropdown-menu-open').attr('class','dropdown-menu')
        $(this).find('ul').css({'display':'block'})
        $(this).find('ul').attr('class','dropdown-menu-open');
        
    }
    else{
        $(this).find('ul').css({'display':'none'})
        $(this).find('ul').attr('class','dropdown-menu');
    }
    
})


$('#MesajGonder').click(function(){
    $alıcı= $('#alici').val()
    $mesaj= $('#mesajicerik').val();
    console.log($alıcı)
    console.log($mesaj)
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            alıcı: $alıcı,
            mesaj: $mesaj,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(){
            console.log("Başarılı")
            $('#alici').val() = "";
            $('#mesajicerik').val() = "";
        },
        error: function(){
            alert('birşeyler hatalı!');
        }
    });
    console.log("Alıcı: "+$alıcı)
    console.log("Mesaj: "+$mesaj)
})


$('#kurulusAjaxFiltreleme  input').keyup(function(){
    
    $kurulusID = $('#kurulusIDAra').val()
    $kurulusAdi = $('#kurulusAdiAra').val()
    $kurulusTuru = $('#kurulusTurFiltrele').val()
    $kurulusDurumu = $('#durumFiltrele').val()
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            islem:"filtrele",
            kurulusID:$kurulusID,
            kurulusAdi: $kurulusAdi,
            kurulusTuru:$kurulusTuru,
            kurulusDurumu:$kurulusDurumu,

            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            $('#ajaxYukleme').html(data)
        },
        error: function(){
            alert('birşeyler hatalı!');
        }
    });
})
$('#kurulusAjaxFiltreleme  select').change(function(){
    $kurulusID = $('#kurulusIDAra').val()
    $kurulusAdi = $('#kurulusAdiAra').val()
    $kurulusTuru = $('#kurulusTurFiltrele').val()
    $kurulusDurumu = $('#durumFiltrele').val()
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            islem:"filtrele",
            kurulusID:$kurulusID,
            kurulusAdi: $kurulusAdi,
            kurulusTuru:$kurulusTuru,
            kurulusDurumu:$kurulusDurumu,

            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            $('#ajaxYukleme').html(data)
        },
        error: function(){
            alert('birşeyler hatalı!');
        }
    });
})

$('#mesajlarAjaxFiltreleme  input').change(function(){
    $mesajOkunduAra = $('#mesajOkunduAra').val()
    if ($('#mesajOkunduAra').is(':checked'))
    {
        $mesajOkunduAra = 'Evet'
    }
    else{
        $mesajOkunduAra = 'Hayır'
    }
    console.log($mesajOkunduAra)
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            mesajOkunduAra: $mesajOkunduAra,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            $('#ajaxYukleme').html(data)
        },
        error: function(){
            alert('birşeyler hatalı!');
        }
    });
})