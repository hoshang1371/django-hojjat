const indicator = document.querySelectorAll('.indicator');
const main = document.querySelector('.content_img');


//const img = document.querySelector('.content_img');
const span = document.querySelector('.content_span');
const div = document.querySelector('.product_view');

let BCup = document.querySelector('.BCup');
let BCdown = document.querySelector('.BCdown');
let numberProduct = document.querySelector('#numberProduct');


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



document.addEventListener('keyup',function(k){
    let en_number =""
    if((k.key >= "0" && k.key <= "9")||k.key== "Backspace"){
        en_number = numberProduct.value;

        let number = en_number.toEnglishDigit();
        number_buffer = parseInt(number, 10);
        number = number_buffer.toString();
        if(isNaN(number))
            number ="0";
        numberProduct.value = (number.toPersinaDigit());
    }
    else{
        numberProduct.value = (en_number.toPersinaDigit());
    }

    })


BCup.addEventListener("click", function(){
    let fa_number = numberProduct.value;
    let en_number = fa_number.toEnglishDigit();
    ++en_number;
    fa_number =en_number.toString();
    numberProduct.value = (fa_number.toPersinaDigit());

    BCup.classList.add('active');
    setTimeout(function(){ BCup.classList.remove('active');}, 100);
});

BCdown.addEventListener("click", function(){
    let fa_number = numberProduct.value;
    let en_number = fa_number.toEnglishDigit();
    if(en_number > 1)
        --en_number;
    fa_number =en_number.toString();
    numberProduct.value = (fa_number.toPersinaDigit());
    
    BCdown.classList.add('active');
    setTimeout(function(){ BCdown.classList.remove('active');}, 100);
});

let cx = div.offsetWidth / (span.offsetWidth);
let cy = div.offsetHeight / (span.offsetHeight);


//console.log(main.style.left,main.offsetTop);


function imageZoomer(){
    span.addEventListener('mousemove', movespan);
    main.addEventListener('mousemove', movespan);

    span.addEventListener('mouseleave', leave);
    main.addEventListener('mouseleave', leave);



    function movespan(e){
        span.style.visibility = 'visible';
        div.style.visibility = 'visible';

        // console.log("span", span.offsetWidth,span.offsetHeight);
        // console.log("div",div.offsetWidth,div.offsetHeight);
        // console.log("window",window.innerWidth);

        let pos,x,y;
        pos = getCursorPosition(e);
        x = pos.x - (span.offsetWidth/2);
        y = pos.y - (span.offsetHeight/2);
//main.offsetLeft
        if(x>(main.width) - span.offsetWidth){
        x = ((main.width) - span.offsetWidth);
        }
        if(x<0){
            x=0
        }
//main.offsetTop
        if(y>(main.height) - span.offsetHeight){
            y = ((main.clientHeight) - span.offsetHeight);
        }
        if(y<0){
            y=0
        }
//
        span.style.left = x +main.offsetLeft+ 'px';
        span.style.top = y +main.offsetTop+'px';
        //200 50
        // console.log("x",(x+main.offsetLeft));
        // console.log("y",(y+main.offsetTop));
        // console.log("div.style.background-size",div.style.background-size);
        div.style.backgroundPosition = "-" + (x*cx) + "px -" + ((y)*cy) + "px"
//        div.style.backgroundPosition = "-" + (((x)*(cx))) + "px -" + (((y)*cy)) + "px"
//        div.style.backgroundPosition = "-" + (((x)*(cx))+1250) + "px -" + (((y)*cy)+500) + "px"


        function getCursorPosition(e){
            div.style.backgroundImage = "url('"+ main.src +"')";
            let a;
            let x=0;
            let y=0;
            e=e||event.window;
            a = main.getBoundingClientRect();
            x = e.pageX - a.left;
            y = e.pageY - a.top;
            x = (x) - window.pageXOffset;
            y = (y) - window.pageYOffset;
            return{x:x,y:y}
        }
    }

    function leave(){
        span.style.visibility = 'hidden';
        div.style.visibility = 'hidden';
    }
}

imageZoomer();


for(let i = 0; i< indicator.length; i++){
    indicator[i].onclick = (e)=>{

        for(let a = 0; a<indicator.length; a++){
            indicator[a].classList.remove('active');
        }
        indicator[i].classList.add('active');
        main.src = e.target.src;

    }
}

// var input = document.getElementById('non-persian');
// var charMap = [
//   {
//     pattern: /\u0660/,
//     replace: '0'
//   },
//   {
//     pattern: /\u0661/,
//     replace: '1'
//   },
//   {
//     pattern: /\u0662/,
//     replace: '2'
//   },
//   {
//     pattern: /\u0663/,
//     replace: '3'
//   },
//   {
//     pattern: /\u0664/,
//     replace: '4'
//   },
//   {
//     pattern: /\u0665/,
//     replace: '5'
//   },
//   {
//     pattern: /\u0666/,
//     replace: '6'
//   },
//   {
//     pattern: /\u0667/,
//     replace: '7'
//   },
//   {
//     pattern: /\u0668/,
//     replace: '8'
//   },
//   {
//     pattern: /\u0669/,
//     replace: '9'
//   },
  
// ];

// input.onkeyup = function (e) {
//   console.log(e);
//   for (i = 0; i < charMap.length; i++) {
// 		input.value = input.value.replace(charMap[i].pattern, charMap[i].replace);
//   }
// }

// var en_number = "0123456789"; 
// alert(en_number.toPersinaDigit());

