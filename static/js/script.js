function initMap() {
    var finea = {lat: 53.779720, lng: -7.385282};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: finea
    });
    var marker = new google.maps.Marker({
        position: finea,
        map: map
    });
}
