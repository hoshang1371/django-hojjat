const check_out_btn = document.querySelector('.check_out_btn');
const totalCost = document.querySelector('.total__cost');
const cartDOMItems = document.querySelectorAll('.cart__item');

var totalAllhh =0;
// var carName = "Volvo";
check_out_btn.addEventListener('click', function(){
if(confirm('آیا از حذف محصولات در سبد خرید مطمئنید؟')){
    console.log("ok");
    clearCatItems();
}
});

let bufferId = "", bufferCount = "";
cartDOMItems.forEach(inItem => {
increaseItem(inItem);
decreaseItem(inItem);
removeItem(inItem);

});


function removeItem(inItem) {
bufferId = inItem.querySelector('#product__id').value;
inItem.querySelector("[action='remove']").addEventListener('click', function () {
    $.ajax({
        url: '{% url "crud_ajax_delete" %}',
        data: {
            'id': bufferId,
        },
        dataType: 'json',
        success: function (data) {
            if (data.deleted) {
                inItem.remove();
            }
        }
    });

});
}

function decreaseItem(inItem) {
inItem.querySelector("[action='decrease']").addEventListener('click', function () {

    bufferId = inItem.querySelector('#product__id').value;
    bufferCount = inItem.querySelector('.product__quantity').innerText;
    var bufferCountB = parseInt(bufferCount.toEnglishDigit());

    if (bufferCountB > 1) {
        --bufferCountB;
        saveToStorage(bufferId, bufferCountB, inItem);
    } else {
        $.ajax({
            url: '{% url "crud_ajax_delete" %}',
            data: {
                'id': bufferId,
            },
            dataType: 'json',
            success: function (data) {
                if (data.deleted) {
                    inItem.remove();
                }
            }
        });
    }
});
};

function increaseItem(inItem) {

inItem.querySelector("[action='increase']").addEventListener('click', function () {
    bufferId = inItem.querySelector('#product__id').value;
    bufferCount = inItem.querySelector('.product__quantity').innerText;
    var bufferCountA = parseInt(bufferCount.toEnglishDigit()) + 1;

    saveToStorage(bufferId, bufferCountA, inItem);

});
}

function saveToStorage(bufferId, bufferCountA, inItem) {
$.ajax({
    url: 'ajax/crud/update/',
    data: {
        'id': bufferId,
        'count': bufferCountA
    },
    dataType: 'json',
    success: function (data) {
        if(data.user == 'not exist'){
            alert('این تعداد کالا موجود نیست.')
        }
        else if (data.user) {
            console.log('kir khaar')
            inItem.querySelector('.product__quantity').innerText = (bufferCountA.toString()).toPersinaDigit();
            inItem.querySelector('.product_price').innerText = ((data.user.price).toString()).toPersinaDigit();
            calculateAllTotal();
        }

    }
});
};

//const totalCost = document.querySelector('.total__cost');


function calculateAllTotal(){
console.log(cartDOMItems)

cartDOMItems.forEach(inItemh => {
   // console.log(parseInt((inItemh.querySelector(".product_price").innerText).toEnglishDigit()));
    totalAllhh = totalAllhh+parseInt((inItemh.querySelector(".product_price").innerText).toEnglishDigit());
    document.querySelector(".total__cost").innerText =(totalAllhh.toString()).toPersinaDigit();
    //console.log(totalAllhh)
});
//return totalAllhh;
}

function clearCatItems(){      
document.querySelectorAll('.cart__item').forEach(item => {
    bufferId = item.querySelector('#product__id').value;
    $.ajax({
        url: 'ajax/crud/delete/',
        data: {
            'id': bufferId,
        },
        dataType: 'json',
        success: function (data) {
            if (data.deleted) {
                total =0;
                totalCost.innerText = (total.toString()).toPersinaDigit();
                item.remove();
            }
        }
    });
})
}


