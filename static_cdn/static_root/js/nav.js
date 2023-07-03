const toggle = document.querySelector(".toggle");
const menu = document.querySelector(".menu");
const submenu = document.querySelectorAll(".submenu.mega-menu");
//const subdaste1 = document.querySelector(".daste-1");
const subdaste2 = document.querySelector(".daste-2");
const mobileClose = document.querySelectorAll(".mobile-menu-close");
const basket = document.querySelector(".clickBasket");
const cartDOM = document.querySelector('.cart__items');
// let cartDOM_before = document.getComputedStyle(cartDOM, '::before')

// console.log("user_is_authenticated");

if (user_is_authenticated == true) {
    const MobileClosecartDOM = document.querySelector('.mobile-cart-close');
    MobileClosecartDOM.addEventListener('click', function () {
        if (cartDOM.classList.contains("active")) {
            cartDOM.classList.remove("active");
        }
    })
}


// var w = window.innerWidth;
// widthOfcard();
// function widthOfcard() {
//     if( (w <= 760) && (w > 640)){
//         cartDOM.style.width = "auto";
//         cartDOM.style.background = "red";
//     }
//     else if(w < 700)
//     {
//         cartDOM.style.width = 500+"px";
//         cartDOM.style.background = "yellow";
//          console.log("yellow");
//     }
//     else if(w > 760)
//     {
//         cartDOM.style.width = 700+"px";
//         cartDOM.style.background = "blue";
//         // console.log("blue");
//     }

// } 

if ('scrollRestoration' in window.history) {
    window.history.scrollRestoration = 'manual'
}

// w = window.innerWidth;

window.addEventListener('resize', function () {
    let w = window.innerWidth;
    // console.log(w)
    if (w > 959) {
        for (let i = 0; i < submenu.length; i++) {
            if (submenu[i].classList.contains("active")) {
                submenu[i].classList.remove("active");
            }
        }

    }
    else if(w < 699)
        document.querySelector(".cart__items").style.height= "100%";
    else if(w > 700)
        document.querySelector(".cart__items").style.height= "70vh";
    // widthOfcard();
})


window.addEventListener('scroll', function () {
    // const nav = document.querySelector('nav ul');
    menu.classList.toggle('sticky', window.scrollY > 0);
    if (user_is_authenticated == true) {
        cartDOM.classList.toggle('sticky', window.scrollY > 0);
    }
})

/* Toggle mobile menu */
function toggleMenu() {
    if (menu.classList.contains("active")) {
        menu.classList.remove("active");
        // adds the menu (hamburger) icon
        toggle.querySelector("a").innerHTML = "<i class='fas fa-bars'></i>";

        // navbar_item.style.background = "none"
    } else {
        menu.classList.add("active");
        // menu.className = "active";
        // navbar_item.style.background = "rgba(0,0,0,.6)"
        // adds the close (x) icon
        toggle.querySelector("a").innerHTML = "<i class='fas fa-times'></i>";
    }
}

function togglesubmenu1() {
    if (submenu[0].classList.contains("active")) {
        submenu[0].classList.remove("active");
        // adds the menu (hamburger) icon
        //toggle.querySelector("a").innerHTML = "<i class='fas fa-bars'></i>";

        // navbar_item.style.background = "none"
    } else {
        submenu[0].classList.add("active");
        // menu.className = "active";
        // navbar_item.style.background = "rgba(0,0,0,.6)"
        // adds the close (x) icon
        //toggle.querySelector("a").innerHTML = "<i class='fas fa-times'></i>";
    }
}

function togglesubmenu2() {
    let w = window.innerWidth;
    // let y = document.querySelector('.'+submenu[0].classList[0])
    // console.log(y.style)
    // console.log(w);
    // console.log(submenu[0].classList);
    console.log(submenu[0].classList.item(0));
    // console.log(submenu[0].style);
    if(w <952)
    {
        submenu[0].classList.add("active");
    }


    // submenu[1].classList.add("active");
}

function mobile_Close_subdaste() {
    // console.log("submenu[0]=",submenu[0])
    // console.log("submenu[1]=",submenu[1])
    if (submenu[0].classList.contains("active")) {
        submenu[0].classList.remove("active");
    }
    else if (submenu[1].classList.contains("active")) {
        submenu[1].classList.remove("active");
    }
}


// function basket_click() {
//     cartDOM.classList.toggle('active')
//     console.log("ko")
// }

// basket.addEventListener('click', basket_click)

/* Event Listener */
toggle.addEventListener("click", toggleMenu, false);

//subdaste1.addEventListener("click", togglesubmenu1, false);
//todo
subdaste2.addEventListener("click", togglesubmenu2, false);

for (let x = 0; x < mobileClose.length; x++)
    mobileClose[x].addEventListener("click", mobile_Close_subdaste, false);

