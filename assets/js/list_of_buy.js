// import myFunction from "./network.js"
// document.write('<script type="text/javascript" src="./network.js" ></script>');
// document.write('<script type="module" src="./network.js" ></script>');

var title_of_buy = document.querySelector('.title_of_buy');


window.addEventListener('scroll', function () {
    // const nav = document.querySelector('nav ul');
    if (user_is_authenticated == true) {
        if (window.scrollY > 100) {
            // console.log(window.scrollY);
            title_of_buy.style.top = "10%";
        }
        else {
            title_of_buy.style.top = "auto";
        }
    }
});

//! get csrf token =======================================
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// console.log(csrftoken);
//!===================================================

String.prototype.toPersinaDigit = function () {
    var id = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
    return this.replace(/[0-9]/g, function (w) { return id[+w] });
}

let numberToPersianValue = document.querySelectorAll('.ToPersianValue');

let btn__small__list_of_buy = document.querySelectorAll('.btn__small__list_of_buy');

// console.log(btn__small__list_of_buy);

for (let val of numberToPersianValue) { // You can use `let` instead of `const` if you like
    let en_numberPer = val.value;
    val.value = en_numberPer.toPersinaDigit();
    let en_number = "";
    val.addEventListener('keyup', function (k) {


        if ((k.key >= "0" && k.key <= "9") || k.key == "Backspace") {
            en_number = val.value;

            let number = en_number.toEnglishDigit();
            number_buffer = parseInt(number, 10);
            number = number_buffer.toString();
            if (isNaN(number))
                number = "0";
            val.value = (number.toPersinaDigit());
        }
        else {
            val.value = (en_number.toPersinaDigit());
        }
    });
}
//! put data===================================

// document.write('<script type="text/javascript" src="./network.js" ></script>');
// myFunction();
//!====================== content_list_of_buy
let content_list_of_buy = document.querySelectorAll(".content_list_of_buy>div");

// console.log(content_list_of_buy);
function getElementOfIdAndCount(inItem) {
    var id = inItem.querySelector("[type='hidden']").value;
    var count = inItem.querySelector(".ToPersianValue").value.toEnglishDigit();
    return [id, count];
}


content_list_of_buy.forEach(inItem => {

    increaseItemBuy(inItem);
    decreaseItemBuy(inItem);
    removeItembuy(inItem);
    //TODo
    let input_item = inItem.querySelector('.input_off_number_product_item')
    input_item.addEventListener("keypress", function () {
        console.log("kosKesh");
        var [id, count] = getElementOfIdAndCount(inItem);
        var data_toSend = {
            id: id,
            count: count,
        }

        put_item_list_of_buy(data_toSend, csrftoken).then(data => {
            console.log(data);
            // makeChanges(inItem,data);
            var totalPrice = document.querySelector(".Total_price_for_all_product_buyData");
            var count_off_all_product = document.querySelector(".count_off_all_product");
            var Total_price_postPrice = document.querySelector(".Total_price_postPrice");

            totalPrice.textContent = data.Total_price_for_all_product_buy.toString().toPersinaDigit();
            count_off_all_product.textContent = data.count_off_all_product.toString().toPersinaDigit();
            Total_price_postPrice.textContent = data.Total_price_postPrice.toString().toPersinaDigit();
        });
    });
});

function makeChanges(inItem, data) {
    inItem.querySelector(".ToPersianValue").value = (data.count.toString()).toPersinaDigit();
    var totalPrice = document.querySelector(".Total_price_for_all_product_buyData");
    var count_off_all_product = document.querySelector(".count_off_all_product");
    var Total_price_postPrice = document.querySelector(".Total_price_postPrice");
    var total__counter_a= document.querySelector(".total__counter a");
    total__counter_a.innerText = data.count_all.toString().toPersinaDigit();
    totalPrice.textContent = data.Total_price_for_all_product_buy.toString().toPersinaDigit();
    count_off_all_product.textContent = data.count_off_all_product.toString().toPersinaDigit();
    Total_price_postPrice.textContent = data.Total_price_postPrice.toString().toPersinaDigit();
}

function increaseItemBuy(inItem) {


    inItem.querySelector("[action='increase']").addEventListener('click', function () {
        // console.log("increase");
        var [id, count] = getElementOfIdAndCount(inItem);
        // console.log(id);        // console.log('csrftoken=',csrftoken);
        var Intcount = parseInt(count);
        Intcount++;
        count = Intcount.toString();
        var data_toSend = {
            id: id,
            count: count,
        }

        put_item_list_of_buy(data_toSend, csrftoken).then(data => {
            makeChanges(inItem, data);
        });
    });
};


function decreaseItemBuy(inItem) {
    inItem.querySelector("[action='decrease']").addEventListener('click', function () {
        console.log("decrease");
        var [id, count] = getElementOfIdAndCount(inItem);
        // console.log(id);        // console.log('csrftoken=',csrftoken);
        var Intcount = parseInt(count);
        Intcount--;
        count = Intcount.toString();
        var data_toSend = {
            id: id,
            count: count,
        }

        put_item_list_of_buy(data_toSend, csrftoken).then(data => {
            makeChanges(inItem, data);
        });

    });
};

function removeItembuy(inItem) {
    inItem.querySelector("[action='remove']").addEventListener('click', function () {
        console.log("remove");
        var [id, count] = getElementOfIdAndCount(inItem);
        delete_item_list_of_buy(id, csrftoken).then(data => {
            console.log("it's ok");
            console.log(data.status);
            if (data.status == 204) {
                var parent = inItem.parentElement;
                inItem.remove();
                parent.remove();
            }
        });
    });
};