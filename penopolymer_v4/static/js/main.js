$(window).on('load', function () {
    $('.main-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: false,
        fade: true,
        appendArrows: '.main-slider',
        prevArrow: '<i class="nav-prev"></i>',
        nextArrow: '<i class="nav-next"></i>'
    });
    if (document.querySelector('.fancybox'))  {
        $(".fancybox").fancybox({
        prevEffect: 'none',
        nextEffect: 'none',
        helpers: {
            title: {
                type: 'outside'
            },
            thumbs: {
                width: 50,
                height: 50
            }
        }
    });
    }
    

    // $('.responsive-calendar').responsiveCalendar();


    $('#send').addClass("disabled");
    $('#Check').on("change", function() {
    if($('#Check').is(":checked")) {
      $('#send').removeClass("disabled");
      }else {
      $('#send').addClass("disabled");
      }
    })
});

(function ($) {
    $(document).ready(function () {
        $('ul.dropdown-menu [data-toggle=dropdown]').on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            $(this).parent().siblings().removeClass('open');
            $(this).parent().toggleClass('open');
        });
    });
})(jQuery);
// Скрытие и появление label при вводе значения в input
let telOrMail = $('#choice');
telOrMail.on("change", function(e) {
    if ($(this).val() == "") {
        $('.telOrMail').css("display", "block");
    } else {
        $('.telOrMail').css("display", "none");
    }
});

// Ajax запрос для формы обратной связи
let feedbackBtn = $("#sendDocAjax");
feedbackBtn.on("click", function(e) {
    let fio = $("#fio").val(),
        company = $("#organization").val(),
        tel = $("#tel").val(),
        email = $("#email").val(),
        choice = $("#choice").val(),
        checkBox = $("#checkDoc");
    if (fio == '' || company == '' || email == "" || !checkBox.prop("checked") || !validateEmail(email) || tel == '' || choice == '') {
        let parent = $(this).parent(".form-group");
        parent.append("<span>Заполните поля формы!!!</span>");
    } else {
        $.ajax({
            type: "POST",
            url: "/req/sendFeedBack/",
            data: {
                fio: fio,
                company: company,
                tel: tel,
                email: email, 
                choice: choice
            }
        }).done(function(data) {
            if (data == 1) {
                $('.d-r').css("display", "none");
                $('.f-r').css("display", "flex");
            } else {
                $('.f-r').css("display", "none");
                $('.d-r').css("display", "flex");
            }
        })
    }
});
function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}
(function(d, w, c) {
    w.ChatraID = 'ExveuDvPcBA7g26jc';
    var s = d.createElement('script');
    w[c] = w[c] || function() {
        (w[c].q = w[c].q || []).push(arguments);
    };
    s.async = true;
    s.src = (d.location.protocol === 'https:' ? 'https:': 'http:')
    + '//call.chatra.io/chatra.js';
    if (d.head) d.head.appendChild(s);
})(document, window, 'Chatra');


function funcsendmail(){
    var name = $("#callback_name").val(); 
    var phone = $("#callback_phone").val(); 
    var company = $("#callback_company").val();    
    var response = grecaptcha.getResponse();
    $.ajax({
            type: "POST",
            url: "/req/feedbackCaptcha/",
            data: {
                name:name,
                phone:phone,
                company:company,
                response:response,
            }
        }).done(function(data) {
            if(data == '1'){
                console.log(data);
                //document.getElementById("output").innerHTML = "<span style='color: #3f3'>Сообщение отправлено!</span>";
                window.location.href = 'http://ppmi.t.ener.ru/faq/send.html';
            }else{
                console.log(data);
                document.getElementById("output").innerHTML = "<span style='color: #f22'>Ошибка ввода данных!</span>";
            }
        });
}
$(function () {
    $('a[href^="#"]').click(function () {
        let _href = $(this).attr('href');
        $('html, body').animate({scrollTop: $(_href).offset().top + 'px'});
        return false;
    });
});
$("#project-form").submit(function (e) {
    event.preventDefault();
    $(this).find(".btn").attr("disabled", true);
    let fd = new FormData();
    let data = $(this).serializeArray();
    checkBox = $("#checkDoc");
    data.forEach(function (v, k) {
        fd.append(v.name, v.value);
    });
    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "/req/feedbackProject/",
        data: fd,
        processData: false,
        contentType: false,
        cache: false,
    }).done(function (data) {
        console.log(data);
        $.fancybox.open('<h1 class="text-center">Ваша заяка отправлена!</h1>');
    });
});


$(function(){
    if (document.querySelector('#phone')) {
        $('#phone').mask("+7(999) 999-9999", {placeholder: "+7(999) 999-9999"}); 
    }
    
});
let docBtn = $("#sendDocAjax");
docBtn.on("click", function(e) {
    let fio = $("#fio").val(),
        organization = $("#organization").val(),
        mail = $("#email").val(),
        phone = $("#phone").val(),
        checkBox = $("#checkDoc");
        // console.log(fio);
    if (fio == '' || organization == '' || mail == "" || !checkBox.prop("checked") || !validateEmail(mail)) {
        let parent = $(this).parent(".form-group");
        parent.find('span').remove();
        parent.append("<span>Заполните поля формы!!!</span>");
    } else {
        $.ajax({
            type: "POST",
            url: "/req/sendDoc/",
            data: {
                fio: fio,
                organization: organization,
                mail: mail,
                phone: phone
            }
        }).done(function(data) {
            // console.log(data);
            if (data == 1) {
                var link = document.createElement('a');
                link.setAttribute('href', '/local/images/newppmi/012_rd-001-a4_redaktsija_5_1_pdf_1517295073.pdf');
                link.setAttribute('download', '012_rd-001-a4_redaktsija_5_1_pdf_1517295073.pdf');
                link.click();
            } else {
                let parentOfParent = parent.parent("form");
                parentOfParent.append("<span>Руководящий документ не скачался!!!</span>")
            }
        });
    }
});
function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}
function cross_download(url, fileName) {
    var req = new XMLHttpRequest();
    req.addEventListener("loadend", loadEnd, false);
    req.open("GET", url, true);
    req.responseType = "blob";
    var __fileName = fileName;
    req.onload = function (event) {
        var blob = req.response;
        var contentType = req.getResponseHeader("content-type");
        if (window.navigator.msSaveOrOpenBlob) {
            // IE
            window.navigator.msSaveOrOpenBlob(new Blob([blob], {type: contentType}), fileName);
        } else {
            var link = document.createElement('a');
            document.body.appendChild(link);
            link.download = __fileName;
            link.href = window.URL.createObjectURL(blob);
            link.click();
            document.body.removeChild(link);
        }
    };
    req.send();
}