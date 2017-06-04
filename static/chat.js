//$(document).ready(function((){

var webSocket;
console.log("webSocket")
//try to add args
webSocket= new WebSocket("ws://localhost:8888/ws");
	console.log(webSocket)

$(function(){
	
	//$("#LOM").append(LOM)
	//$("#LOM").append(groupId)
	var x= document.getElementById("group");
	var selected;
	webSocket.onmessage = function(e){
		console.log(e.data);
		$("#chat-body").append("<p>"+e.data+"</p>");
	}
	var msg = $("#message").val()
	// webSocket.onclose = function(e){
	// 	// console.log(e);
	// }
	$('#change').click(function(e){
		var userName=$("#userName").val()
	})
	$('#send').click(function(e){
	//	msg = $("#userName").val()+" : "+ $("#message").val()
    	selected=x.options[x.selectedIndex].value;
		msg = selected +" : "+ $("#message").val()
		console.log(msg);
		webSocket.send(msg)
		$("#message").val('')
		
	})
})
