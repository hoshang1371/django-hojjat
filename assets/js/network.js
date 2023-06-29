

const url ="http://192.168.1.51:8000"
// const url ="http://127.0.0.1:8000"
const url_put_item_list_of_buy = url+"/buy/update_for_buy/"
const delete_put_item_list_of_buy = url+"/buy/Order_product_delete_list_of_buy/"
const delete_listOfPostAddress_list = url+"/PostAddress_delete_list_of_buy/"
const sendSmsForVarifyUrl = url+"/post_info/send_code_for_varify_mobile_address"

// alert(url_put_item_list_of_buy);  http://192.168.1.52:8000/buy/Order_product_delete_list_of_buy/

async function  put_item_list_of_buy(data,token) 
{
    const response = await fetch(url_put_item_list_of_buy, {
        method: 'PUT',
        headers: {
          'Content-type': 'application/json',
          'X-CSRFToken': token,
        },
        body: JSON.stringify(data)
      });
      const resData = await response.json();
    //   console.log(token);
      return resData;
}


    // Make an HTTP PUT Request
async function delete_item_list_of_buy(id,token) {
        const response = await fetch((delete_put_item_list_of_buy+id), {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': token,
            }
        });
        // const resData = 'resource deleted...';
        const resData = await response;

        return resData;
}

async function delete_listOfPostAddress(id,token) {
  const response = await fetch((delete_listOfPostAddress_list+id), {
      method: 'DELETE',
      headers: {
          'Content-type': 'application/json',
          'X-CSRFToken': token,
      }
  });
  // const resData = 'resource deleted...';
  const resData = await response;
  return resData;
}

//! send sms for varify

async function sendSmsForVarify(token,mobNum) {
    let data = {mobNum: mobNum};
    const response = await fetch((sendSmsForVarifyUrl), {
        // method: 'GET',
        method: "POST",
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': token,
        },
        body: JSON.stringify(data)
    });
    // const resData = 'resource deleted...';

    // const resData = await response.json();
    // return resData;
    
    const resData = await response;
    return resData;
  }
