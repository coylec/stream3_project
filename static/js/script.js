$(document).ready(function() {

	var offset = 10;

	var duration = 300;

$(window).scroll(function() {

		if ($(this).scrollTop() > offset) {

			$(".back-to-top").fadeIn(duration);

		} else {

			$(".back-to-top").fadeOut(duration);

		}

});



$(".back-to-top").click(function(event) {

	event.preventDefault();

	$("html, body").animate({scrollTop: 0}, duration);

	return false;

	});


$('.logout-confirm').confirm({
    content: 'If you logout you will lose the contents of your shopping cart!',
    buttons: {
        confirm: function(){
            location.href = this.$target.attr('href');
        },
        cancel: function () {
            $.alert('Canceled!');
        }
    }
});

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

});
