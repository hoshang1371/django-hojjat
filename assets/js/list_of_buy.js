var title_of_buy = document.querySelector('.title_of_buy')

window.addEventListener('scroll', function () {
    // const nav = document.querySelector('nav ul');
    if (user_is_authenticated == true) {
        if(window.scrollY > 100){
            // console.log(window.scrollY);
            title_of_buy.style.top = "10%";
        }
        else{
            title_of_buy.style.top = "auto";
        }
        // cartDOM.classList.toggle('sticky', window.scrollY > 0);
    }
})