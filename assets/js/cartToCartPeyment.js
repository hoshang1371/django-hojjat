

bill = document.querySelector('.bill');

button = document.querySelector('.title_Order_bay button');

console.log(bill);
console.log(button);

// bill.setAttribute("style", "display: none;");


button.addEventListener('click',function(){
    bill.classList.toggle('toggle_display');
//    if(bill.style.display === "none"){
//     // bill.style.display === "block";
// }
console.log("kir khar");
//    else{
//     bill.style.display === "none";
//    }
});