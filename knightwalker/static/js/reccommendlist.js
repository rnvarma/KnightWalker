
function initialize(fromX, fromY, toX, toY, id) {
    console.log(fromX)
    console.log(fromY)
    console.log(toX)
    console.log(toY)
    // console.log(description)
    var joined = false;
    var centerX = (fromX + toX)/2;
    var centerY = (fromY + toY)/2;
    var fromLatlng = new google.maps.LatLng(fromX, fromY);
    var toLatlng = new google.maps.LatLng(toX, toY);
    var labels = 'AB';
    var mapProp = {
        center:new google.maps.LatLng(centerX, centerY),
        zoom:15,
        mapTypeId:google.maps.MapTypeId.ROADMAP,
        scrollwheel: false,
        mapTypeControl: false,
    };
    var map=new google.maps.Map(document.getElementById("googleMap" + id),mapProp);
	var fromMarker = new google.maps.Marker({
		position: fromLatlng,
		title: "Meetup Position",
        label: labels[0]
	});
	var toMarker = new google.maps.Marker({
		position: toLatlng,
		title: "Destination",
        label: labels[1]
	});
	fromMarker.setMap(map);
	toMarker.setMap(map);
    var markers = [fromMarker, toMarker];//some array
    var bounds = new google.maps.LatLngBounds();
    for (var i = 0; i < markers.length; i++) {
        bounds.extend(markers[i].getPosition());
    }
    var butn = document.getElementById("join"+id);

    butn.addEventListener("click", function() {        
        send(id);
        joined = !joined;
        if (joined) butn.innerHTML = "LEAVE";
        else butn.innerHTML = "JOIN!";
        updateButn();}, false);

    function updateButn(){
        var chatbutn = document.getElementById("chat"+id);
        if (joined) {
            chatbutn.innerHTML = 
            "<button type='button' id='chatbutn{{trip.id}}'' class = 'col-xs-3 action-button'>CHAT!</button>";
        }
        else {
            chatbutn.innerHTML = "";
        }
    };
    function send(id){
        console.log(id);
    };
    map.fitBounds(bounds);
}


$(document).ready(function() {
    $(".google-map-data").each(function() {
        startLon = $(this).attr("data-startlon")
        startLat = $(this).attr("data-startlat")
        destLat = $(this).attr("data-destlat")
        destLon = $(this).attr("data-destlon")
        id = $(this).attr("data-id")
        initialize(startLat, startLon, destLat, destLon, id);
    })
})






