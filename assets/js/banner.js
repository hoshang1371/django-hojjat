const imgBx = document.querySelector('.imgBx');
const slides = imgBx.getElementsByTagName('img');
const slidesparaf = imgBx.getElementsByTagName('p');
let i =0;
let j =0;

setInterval(nextSlide, 10000);

function nextSlide(){
    slides[i].classList.remove('active');
    i = (i + 1) % slides.length;
    slides[i].classList.add('active');
    nextSlideParaf();
}

function nextSlideParaf(){
    slidesparaf[j].classList.remove('active');
    j = (j + 1) % slidesparaf.length;
    slidesparaf[j].classList.add('active');
}

function prevSlideParaf(){
    slidesparaf[j].classList.remove('active');
    j = (j - 1 + slidesparaf.length) % slidesparaf.length;
    slidesparaf[j].classList.add('active');
}


function prevSlide(){
    slides[i].classList.remove('active');
    i = (i - 1 + slides.length) % slides.length;
    slides[i].classList.add('active');
    prevSlideParaf();
}

