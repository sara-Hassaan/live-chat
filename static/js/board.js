$(document).ready(function(){
  var loadBoard = function (){
    var brd = '<div id="brd"><div class="row">'
    brd +=  '<div class="col-md-3 col-xs-6">'
    brd +=      '<img  class="lbimg" src="static/img/ping1.png">'
    brd +=      '<h4  class="text-center">dummy</h4>'
    brd +=      '<h3  class="text-center">Super Friend</h3>'
    brd +=      '<ul>'
    brd +=        '<li>2 Blum</li>'
    brd +=        '<li>3 Grum</li>'
    brd +=        '<li>4 Dumbo</li>'
    brd +=        '<li>5 Iolita</li>'
    brd +=      '</ul></div>'
    brd +=    '<div class="col-md-3 col-xs-6">'
    brd +=      '<img class="lbimg" src="static/img/ping2.png">'
    brd +=      '<h4  class="text-center">gummy</h4>'
    brd +=      '<h3  class="text-center">Party Man</h3>'
    brd +=      '<ul>'
    brd +=        '<li>2 Gogo</li>'
    brd +=        '<li>3 Mark</li>'
    brd +=        '<li>4 dnimo</li>'
    brd +=        '<li>5 lucky</li>'
    brd +=      '</ul></div>'
    brd +=    '<div class="col-md-3 col-xs-6">'
    brd +=      '<img class="lbimg" src="static/img/ping3.png">'
    brd +=      '<h4 class="text-center">summy</h4>'
    brd +=      '<h3 class="text-center">Chatty One</h3>'
    brd +=      '<ul>'
    brd +=        '<li>2 sunny</li>'
    brd +=        '<li>3 moony</li>'
    brd +=        '<li>4 stary</li>'
    brd +=        '<li>5 galaxy</li>'
    brd +=      '</ul></div>'
    brd +=    '<div class="col-md-3 col-xs-6">'
    brd +=      '<img class="lbimg" src="static/img/ping4.png">'
    brd +=      '<h4 class="text-center">runny</h4>'
    brd +=      '<h3 class="text-center">Public Figure</h3>'
    brd +=      '<ul>'
    brd +=        '<li>2 swimmy</li>'
    brd +=        '<li>3 riddy</li>'
    brd +=        '<li>4 dongol</li>'
    brd +=        '<li>5 soly</li>'
    brd +=      "</ul></div></div></div>";

		$("#application").append(brd);
	}

  $('#leader').on('click', function(){
    $("#application").text("");
    loadBoard();
  })
  loadBoard();
})
