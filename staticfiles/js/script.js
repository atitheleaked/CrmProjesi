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
$('#alici').change(function(){
    $('.ui-helper-hidden-accessible').css('display','none')
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

/*$('#ReceiverSearch').click(function(){
    $aranacak = $('#ReceiverUsername').val();
    console.log($aranacak)
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
            islem:'KullaniciAra',
            aranacak: $aranacak,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('#result').html(response);
        }
    });
})
$ReceiverUsername = '';

$('.ReceiverSelect').click(function(){
    $ReceiverUsername = $(this).text();
    console.log($ReceiverUsername)
    $('#ReceiverFinal').text($ReceiverUsername);
})
*/

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
    $kurulusTuru = $('#kurulusTuruAra').val()
    $kurulusDurumu = $('#kurulusDurumuAra').val()
    $.ajax({
        url: '',
        type: 'POST',
        async: false,
        data:{
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