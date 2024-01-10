let btn = document.querySelector(".mobile-btn");

const burgerFunc = (
  menuClassName,
  showClassName,
  btnClassName,
  btnToggleClass
) => {
  let menu = document.querySelector(`.${menuClassName}`);
  let btn = document.querySelector(`.${btnClassName}`);

  if (menu.classList.contains(showClassName)) {
    menu.classList.remove(showClassName);
    btn.classList.remove(btnToggleClass);
  } else {
    menu.classList.add(showClassName);
    btn.classList.add(btnToggleClass);
  }
};

btn.addEventListener("click", () => {
  burgerFunc("header__relative", "active", "mobile-btn", "active-btn");
});

function validateEmail(email) {
  var reg =
    /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return reg.test(email);
}

$(document).ready(function () {
  $(".modalbox").fancybox();
  $("#contact").submit(function () {
    return false;
  });

  $("#send").on("click", function () {
    var emailval = $("#email").val();
    var msgval = $("#msg").val();
    var msglen = msgval.length;
    var mailvalid = validateEmail(emailval);

    if (mailvalid == false) {
      $("#email").addClass("error");
    } else if (mailvalid == true) {
      $("#email").removeClass("error");
    }

    if (msglen < 4) {
      $("#msg").addClass("error");
    } else if (msglen >= 4) {
      $("#msg").removeClass("error");
    }

    if (mailvalid == true && msglen >= 4) {
      // если обе проверки пройдены
      // сначала мы скрываем кнопку отправки
      $("#send").replaceWith("<em>отправка...</em>");

      $.ajax({
        type: "POST",
        url: "sendmessage.php",
        data: $("#contact").serialize(),
        success: function (data) {
          if (data == "true") {
            $("#contact").fadeOut("fast", function () {
              $(this).before(
                "<p><strong>Успешно! Ваше сообщение отправлено  :)</strong></p>"
              );
              setTimeout("$.fancybox.close()", 1000);
            });
          }
        },
      });
    }
  });
});

const swiperEl = document.querySelector("swiper-container");

// swiper parameters
const swiperParams = {
  slidesPerView: 1,
  breakpoints: {
    280: {
      slidesPerView: 1,
    },
    325: {
      slidesPerView: 1,
    },
    424: {
      slidesPerView: 1,
    },
    576: {
      slidesPerView: 1,
    },
    640: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
  on: {
    init() {
      // ...
    },
  },
};

// now we need to assign all parameters to Swiper element
Object.assign(swiperEl, swiperParams);

// and now initialize it
swiperEl.initialize();
