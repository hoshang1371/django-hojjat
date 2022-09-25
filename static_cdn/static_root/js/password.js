const pass_field = document.querySelectorAll('.password');
const show_btn = document.querySelectorAll('.show');

console.log(pass_field)
console.log(show_btn)

for(let i=0; i<show_btn.length; i++){
    show_btn[i].addEventListener('click', function () {
        if (pass_field[i].type === "password") {
            pass_field[i].type = "text";
            show_btn[i].style.color = "#3498db";
            show_btn[i].textContent = "عدم نمایش";
        } else {
            pass_field[i].type = "password";
            show_btn[i].style.color = "#222";
            show_btn[i].textContent = "نمایش";
        }
    })
}



// const pass_field_confirm = document.querySelector('.password-confirm');
// const show_btn_confirm = document.querySelector('.show-confirm');
// show_btn_confirm.addEventListener('click', function () {
//     if (pass_field_confirm.type === "password") {
//         console.log("ok");
//         pass_field_confirm.type = "text";
//         show_btn_confirm.style.color = "#3498db";
//         show_btn_confirm.textContent = "عدم نمایش";
//     } else {
//         pass_field_confirm.type = "password";
//         show_btn_confirm.style.color = "#222";
//         show_btn_confirm.textContent = "نمایش";
//     }
// })
// var x = document.getElementsByClassName("example");
// var i;
// for (i = 0; i < x.length; i++) {
//   x[i].style.backgroundColor = "red";
// }
