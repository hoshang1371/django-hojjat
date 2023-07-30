var isTermsAndRules= document.querySelector('.isTermsAndRules');
var next = document.querySelector('.next');
var next_cover = document.querySelector('.next_cover');
var rulesClose= document.querySelector('.rules>div:first-child>div');
var rules = document.querySelector('.rules');
var paymentRule = document.querySelector('.items_for_peyment>div:last-child>p>a');
console.log(paymentRule);

next_cover.addEventListener('click',function(){
    alert('شرایط و قوانین پذیرفته نشده است.');
});

isTermsAndRules.addEventListener('click',function(){
    console.log(isTermsAndRules.checked);
    if(isTermsAndRules.checked){
        next.removeAttribute('disabled');
        next_cover.style.zIndex   = '-1';
    }
    else{
        next.setAttribute('disabled', "");
        next_cover.style.zIndex   = '1';
    }
});

rulesClose.addEventListener('click',function(){
    rules.classList.add('display_none');
});

paymentRule.addEventListener('click',function(){
    console.log('kir khar');
    rules.classList.remove('display_none');

});

