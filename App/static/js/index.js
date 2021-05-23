 let socket = new WebSocket('ws://localhost:8000/ws/pizza/' + order_id);
  socket.onopen = function (e) {
    console.log('Connection established');
  };

  socket.onmessage = function (e) {
    var data = JSON.parse(e.data)
    var value = data.payload.progress
    console.log(data)
    increaseProgress(value , data.payload.status)

  };
  socket.onclose = function (e) {
    console.log('Connection closed');
  };

  function increaseProgress(value , status){
   
    var progress = document.querySelector('.progress-bar')
    var status_html = document.querySelector('#status')
   
    if(value == 100){
      console.log("ss")
      progress.classList.add('bg-success')
    }

    status_html.innerHTML  = status
    progress.style.width = value + "%"
   
  }