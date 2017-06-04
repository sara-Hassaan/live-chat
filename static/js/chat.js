console.log("chat downloaded")
var send_data
		$(document).ready(function(){
			var ws = new WebSocket("ws://localhost:4444/ws")
			ws.onopen = function (e) {
			   var msg = {
					"type" : "set",
					"gid"  : gid,
					"name"	: name,
					"uname"	: uname
				}
				ws.send(JSON.stringify(msg))
				console.log("connection opened")
			}

			$("#btsend").click(function(){
				msg = {
					"type" : "send",
					"gid"  : gid,
					"name"	: name,
					"uname"	: uname
					"msg"  : $("#message").val()
				}
				ws.send(JSON.stringify(msg))
				console.log("pressed")
			})

			ws.onmessage = function(res){
				console.log(res)
				$("#chat-area").append("<p>"+res.data+"</p");
			}
			ws.onclose = function(e){
				console.log(e);
				$("#chat-area").append("<p>"+"Someone left the conversation"+"</p>");

		});

