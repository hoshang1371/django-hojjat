const pass_field = document.querySelector('.password');
const show_btn = document.querySelector('.show');
show_btn.addEventListener('click', function () {
    if (pass_field.type === "password") {
        pass_field.type = "text";
        show_btn.style.color = "#3498db";
        show_btn.textContent = "عدم نمایش";
    } else {
        pass_field.type = "password";
        show_btn.style.color = "#222";
        show_btn.textContent = "نمایش";
    }
})


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
