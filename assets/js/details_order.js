var upDetails = document.querySelector('.upDetails>div>div:last-child>p');
var table = document.querySelector('.table');


upDetails.addEventListener('click',function(){
    table.classList.toggle('show');
});