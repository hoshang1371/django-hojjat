const btn = document.querySelector('.search-icon');
const overlay = document.querySelector('.search-overlay');
const popup = document.querySelector('.search-popup');

var path = window.location.pathname;
var page = path.split("/").pop();
// console.log( page );
if(page == ""){
    // console.log("ok");
    popup.style.top = "5%";
}

btn.addEventListener('click',function(){
    overlay.classList.add('active');
    popup.classList.add('active')
});


overlay.addEventListener('click', function(){
    overlay.classList.remove('active');
    popup.classList.remove('active')
})