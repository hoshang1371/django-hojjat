let numberToProduct = document.querySelectorAll('.ToPersian');

// console.log(numberToProduct[0].innerHTML);
// console.log(numberToProduct[1].innerHTML);
//!console.log(numberToProduct.forEach(numberToProduct.innerHTML));

String.prototype.toEnglishDigit = function() { 
    var find = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
    var replace = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']; 
    var replaceString = this; 
    var regex; for (var i = 0; i < find.length; i++) { regex = new RegExp(find[i], "g"); 
    replaceString = replaceString.replace(regex, replace[i]); } return replaceString;
 };

// var fa_number = "۰۱۲۳۴۵۶۷۸۹"; 
// alert(fa_number.toEnglishDigit());


String.prototype.toPersinaDigit= function(){
    var id= ['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹']; 
    return this.replace(/[0-9]/g, function(w){ return id[+w] }); 
}

const zeroPad = (num, places) => String(num).padStart(places, '0')

for (let val of numberToProduct) { // You can use `let` instead of `const` if you like
    let en_numberPer = val.innerHTML

    // console.log(typeof(en_numberPer));
    // let numberPer = en_numberPer.toEnglishDigit();
    // number_buffer = parseInt(numberPer, 10);

    // numberPer = number_buffer.toString();
    val.innerHTML =en_numberPer.toPersinaDigit()

    // console.log(en_numberPer[0])
    // if(en_numberPer[0] != "0")
    // {
    //     let numberPer = en_numberPer.toEnglishDigit();
    //     number_buffer = parseInt(numberPer, 10);
    
    //     numberPer = number_buffer.toString();
    //     val.innerHTML =numberPer.toPersinaDigit()
    // }
    // else{
    //     let numberPer = en_numberPer.toEnglishDigit();
    //     number_buffer = parseInt(numberPer, 10);
    //     console.log(zeroPad(number_buffer, 2));
    // }

}