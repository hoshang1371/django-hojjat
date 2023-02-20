// const pass_field_S = document.querySelectorAll('.password');
var show_btn_s = document.querySelectorAll('.show');
//.password:valid ~ .show

show_btn_s.forEach(inItem => {
    inItem.addEventListener('click', function(){
        var pass_f = inItem.previousElementSibling;
        if (pass_f.type === "password") {
            pass_f.type = "text";
            inItem.style.color = "#3498db";
            inItem.textContent = "عدم نمایش";
        } else {
            pass_f.type = "password";
            inItem.style.color = "#222";
            inItem.textContent = "نمایش";
        }
    });
});


// show_btn.addEventListener('click', function () {
//     if (pass_field.type === "password") {
//         pass_field.type = "text";
//         show_btn.style.color = "#3498db";
//         show_btn.textContent = "عدم نمایش";
//     } else {
//         pass_field.type = "password";
//         show_btn.style.color = "#222";
//         show_btn.textContent = "نمایش";
//     }
// })