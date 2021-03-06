
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
        joined = !joined;
        if (joined) butn.innerHTML = "LEAVE";
        else butn.innerHTML = "JOIN!";
        update();}, false);

    function update(){
        var chatbutn = document.getElementById("chat"+id);
        if (joined) {
            joinGroup();
            chatbutn.innerHTML = 
            "<button type='button' id='chatbutn{{trip.id}}'' class = 'col-xs-6 action-button'>CHAT!</button>";
            // var cbutton = document.getElementById("chatbutn"+id);
            chatbutn.addEventListener("click",function(){
                console.log("sup");
                window.location.href = "/chat";
            })
        }
        else {
            leaveGroup();
            chatbutn.innerHTML = "";
        }
    };
    function joinGroup(){
        console.log(id);
    };
    function leaveGroup(){

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






