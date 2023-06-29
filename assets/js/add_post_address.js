
send_code = document.querySelector('.varifyMobile>p:last-child');
timerCountDown = document.querySelector('.varifyMobile>p:nth-child(2)');
Continue = document.querySelector('.continue');


const csrftoken11 = getCookie('csrftoken');//! get csrf token =======================================
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
// console.log(csrftoken);
//!===================================================


function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    let myVar =  setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        display.textContent = minutes.toPersinaDigit() + ":" + seconds.toString().toPersinaDigit();
        if (--timer < 0) {
            timer = duration;
            clearInterval(myVar);
            Continue.setAttribute('disabled', "");
            send_code.style.opacity = '1';
            send_code.innerText  = 'ارسال کد تایید';
            send_code.style.cursor = 'pointer';
            send_code.classList.add('varifyMobileHover');
            timerCountDown.classList.remove('countdownTimerDisplayFlex');
            timerCountDown.classList.add('countdownTimerDisplayNone');
            send_code.addEventListener('click',send_codeFunctionClick);
        }
    }, 1000);
}


// send_code.addEventListener('click',function(){
//     console.log('kos nane');
//     timerCountDown.classList.remove('countdownTimerDisplayNone');
//     timerCountDown.classList.remove('varifyMobileHover');
//     timerCountDown.classList.add('countdownTimerDisplayFlex');
//     startTimer(60*2, timerCountDown);
//     send_code.style.opacity = '0.5';
//     console.log(send_code.innerText);
//     send_code.innerText="کد تایید ارسال شد";
//     send_code.style.cursor = 'auto';
//     console.log(timerCountDown);
// });

send_code.addEventListener('click',send_codeFunctionClick);

function send_codeFunctionClick(){
    Continue.removeAttribute('disabled');
    mobNumber = document.querySelector('.mobNumber');
    console.log(mobNumber.value);

    sendSmsForVarify(csrftoken,mobNumber.value).then(async (data) => {
        console.log('data.status=',data.status);
        console.log('data.body',data.body); 
        const dataEnd = await data.json();
        // console.log(data.json());
        console.log(dataEnd);
        // console.log(data.json().Object);
        console.log(dataEnd.mobNum);
        // if(data.mobNum == 'ok'){
        //     console.log('kos nanat')
        // }
        if(data.status == 200  && dataEnd.mobNum == 'ok'){
            console.log("it's ok");
            timerCountDown.classList.remove('countdownTimerDisplayNone');
            send_code.classList.remove('varifyMobileHover');
            timerCountDown.classList.add('countdownTimerDisplayFlex');
            startTimer(60*2, timerCountDown);
            send_code.style.opacity = '0.5';
            send_code.innerText="کد تایید ارسال شد";
            send_code.style.cursor = 'auto';
            send_code.removeEventListener("click", send_codeFunctionClick);
        }
        else if(dataEnd.mobNum == 'not ok'){
            alert("شماره موبایل خود را وارد کنید");
        }

    });


};
