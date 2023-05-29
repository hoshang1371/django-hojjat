//! get csrf token =======================================
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


//!===================================================

function getElementOfId(inItem) {
    var id = inItem.querySelector("[type='hidden']").value;
    return id;
}

// let post_info_Item = document.querySelectorAll(".post_info>div:first-child>div:last-child>p:last-child");
let post_info_Item = document.querySelectorAll(".post_info");

// console.log(post_info_Item);

post_info_Item.forEach(inItem => {
    let remove_item = inItem.querySelector('div:nth-child(2)>div:last-child>p:last-child');
    let edit_item = inItem.querySelector('div:nth-child(2)>div:last-child>p:first-child');

    edit_item.addEventListener('click',function (){
        var id=getElementOfId(inItem)
        console.log(id);
        console.log(path);
        console.log(window.location.href);
        if(window.location.href.includes('post_info')){
            window.location.href =('edit_post_add_address/'+id);
        }
        else{
            window.location.href =('post_info/edit_post_add_address/'+id);
        }

    });

    remove_item.addEventListener('click',function (){
        console.log('kirkhar');
        
        // var id = inItem.querySelector("[type='hidden']").value;
        var id=getElementOfId(inItem)
        console.log(id);
        delete_listOfPostAddress(id, csrftoken).then(data => {
            console.log("it's ok");
            console.log(data.status);
            if (data.status == 204) {
                inItem.remove();
            }
        });
        // console.log(count);

    });
});