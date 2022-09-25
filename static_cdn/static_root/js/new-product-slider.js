let thumbnailsNew = document.getElementsByClassName("product-item-new");
let sliderNew = document.getElementById("sliderNew");
let buttonRightNew = document.getElementById("slide-right-new");
let buttonLeftNew = document.getElementById("slide-left-new");

buttonLeftNew.addEventListener("click", () => {
    sliderNew.scrollLeft -= 125;
});

buttonRightNew.addEventListener("click", () => {
    sliderNew.scrollLeft += 125;
});



const maxScrollLeftNew = sliderNew.scrollWidth - sliderNew.clientWidth;

//AutoPlay slider
function autoPlay_New() {
    if (sliderNew.scrollLeft > (maxScrollLeftNew - 1)) {
        sliderNew.scrollLeft -= maxScrollLeftNew;
    } else {
        sliderNew.scrollLeft += 2;
    }
}

let playNew = setInterval(autoPlay_New, 50);

for (let i = 0; i < thumbnailsNew.length; i++) {
    thumbnailsNew[i].addEventListener("mouseover", () => {
        clearInterval(playNew);
    })

    thumbnailsNew[i].addEventListener("mouseout", () => {
        return playNew = setInterval(autoPlay_New, 50);
    })
}