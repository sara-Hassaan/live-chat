

console.log("integrator")
$("html").on("click" , "img.private",function(e){
	var uid = $(this).attr("value")
	console.log("ajax send")
	window.location = "http://localhost:4444/?id="+userid
												  +"&type=private&"
												  +"uid="+uid; 
	
})


$("html").on("click" , "img.public",function(e){
	var gid = $(this).attr("value")
		window.location = "http://localhost:4444/?id="+userid
												  +"&type=public&"
												  +"gid="+gid; 
})