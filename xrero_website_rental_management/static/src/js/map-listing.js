/** @odoo-module **/

import { jsonrpc } from "@web/core/network/rpc_service";

async function mainMap() {
    function locationData(locationURL, locationImg, locationTitle, locationAddress, locationCategory, propertyAmount, locationRevievsCounter, locationStatus) {
        return ('<div class="map-popup-wrap"><div class="map-popup"><div class="infoBox-close"><i class="fal fa-times"></i></div><a href="' + locationURL + '" class="listing-img-content fl-wrap"><div class="infobox-status ' + locationStatus + '">' + locationStatus + '</div><img src="' + locationImg + '" alt=""><div class="card-popup-raining map-card-rainting"><span class="map-popup-reviews-count">' + propertyAmount + '</span></div></a><div class="listing-content"><div class="listing-content-item fl-wrap"><div class="map-popup-location-category yg-bg"><i class="fal ' + locationCategory + ' map-prop-icon"></i></div><div class="listing-title fl-wrap"><h4><a href=' + locationURL + '>' + locationTitle + '</a></h4><div class="map-popup-location-info"><i class="fas fa-map-marker-alt"></i>' + locationAddress + '</div></div><div class="map-popup-footer"><a href=' + locationURL + ' class="main-link">Details</a></div></div></div></div></div>')
    }
    let latitude;
    let longitude;
    let zoom_level;
    let map_center;
    let locations = [];
    let url_data = window.location.href.split(window.location.origin)[1]
    let query_str = url_data.split('?')[1]

    await jsonrpc("/map" + window.location.pathname, {'param': query_str}).then(function (results) {
        if (results && results['properties']) {
            results['properties'].forEach(function (result) {
                locations.push([locationData(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]), result[8], result[9], result[10], result[11]])
            });
            map_center = results['center'];
            latitude = results['latitude'];
            longitude = results['longitude'];
            zoom_level = results['zoom_level']
        }
    });
    var map = new google.maps.Map(document.getElementById('map-main'), {
        zoom: zoom_level,
        scrollwheel: false,
        center: new google.maps.LatLng(latitude, longitude),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        panControl: false,
        fullscreenControl: true,
        navigationControl: false,
        streetViewControl: false,
        animation: google.maps.Animation.BOUNCE,
        gestureHandling: 'cooperative',
//            styles: [{
//                "featureType": "administrative",
//                "elementType": "labels.text.fill",
//                "stylers": [{
//                    "color": "#444444"
//                }]
//            }]
    });

    var geocoder = new google.maps.Geocoder();

    geocoder.geocode({'address': map_center}, function (results, status) {
        if (status === 'OK') {
            map.setCenter(results[0].geometry.location);
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });

    var boxText = document.createElement("div");
    boxText.className = 'map-box'
    var currentInfobox;
    var boxOptions = {
        content: boxText,
        disableAutoPan: true,
        alignBottom: true,
        maxWidth: 0,
        pixelOffset: new google.maps.Size(-150, -55),
        zIndex: null,
        boxStyle: {
            width: "300px"
        },
        closeBoxMargin: "0",
        closeBoxURL: "",
        infoBoxClearance: new google.maps.Size(1, 1),
        isHidden: false,
        pane: "floatPane",
        enableEventPropagation: false,
    };


    var markerCluster, overlay, i;
    var allMarkers = [];

    var clusterStyles = [
        {
            textColor: 'white',
            url: '',
            height: 50,
            width: 50
        }
    ];

    var ib = new InfoBox();
    google.maps.event.addListener(ib, "domready", function () {
        cardRaining();

    });
    var markerImg;
    var markerCount;
    for (i = 0; i < locations.length; i++) {
        var labels = '123456789';
        markerImg = locations[i][4];
        markerCount = locations[i][3] + 1;
        var overlaypositions = new google.maps.LatLng(locations[i][1], locations[i][2]),

            overlay = new CustomMarker(
                overlaypositions, map, {marker_id: i}, markerImg, markerCount
            );

        allMarkers.push(overlay);

        google.maps.event.addDomListener(overlay, 'click', (function (overlay, i) {

            return function () {
                ib.setOptions(boxOptions);
                boxText.innerHTML = locations[i][0];
                ib.close();
                ib.open(map, overlay);
                currentInfobox = locations[i][3];

                var latLng = new google.maps.LatLng(locations[i][1], locations[i][2]);
                map.panTo(latLng);
                map.panBy(0, -110);

                google.maps.event.addListener(ib, 'domready', function () {
                    $('.infoBox-close').click(function (e) {
                        e.preventDefault();
                        ib.close();
                        $('.map-marker-container').removeClass('clicked infoBox-opened');
                    });

                });

            }
        })(overlay, i));

    }
    var options2 = {
        imagePath: '',
        styles: clusterStyles,
        minClusterSize: 2
    };
    markerCluster = new MarkerClusterer(map, allMarkers, options2);
    google.maps.event.addDomListener(window, "resize", function () {
        var center = map.getCenter();
        google.maps.event.trigger(map, "resize");
        map.setCenter(center);
    });

    $('.map-item').on("click", function (e) {
        e.preventDefault();
        map.setZoom(15);
        var index = currentInfobox;
        var marker_index = parseInt($(this).attr('href').split('#')[1], 10);
        google.maps.event.trigger(allMarkers[marker_index - 1], "click");
        if ($(window).width() > 1064) {
            if ($(".map-container").hasClass("fw-map")) {
                $('html, body').animate({
                    scrollTop: $(".map-container").offset().top + "-110px"
                }, 1000)
                return false;
            }
        }
    });
    $('.nextmap-nav').on("click", function (e) {
        e.preventDefault();
        map.setZoom(15);
        var index = currentInfobox;
        if (index + 1 < allMarkers.length) {
            google.maps.event.trigger(allMarkers[index + 1], 'click');
        } else {
            google.maps.event.trigger(allMarkers[0], 'click');
        }
    });
    $('.prevmap-nav').on("click", function (e) {
        e.preventDefault();
        map.setZoom(15);
        if (typeof (currentInfobox) == "undefined") {
            google.maps.event.trigger(allMarkers[allMarkers.length - 1], 'click');
        } else {
            var index = currentInfobox;
            if (index - 1 < 0) {
                google.maps.event.trigger(allMarkers[allMarkers.length - 1], 'click');
            } else {
                google.maps.event.trigger(allMarkers[index - 1], 'click');
            }
        }
    });
    // Scroll enabling button
    var scrollEnabling = $('.scrollContorl');

    $(scrollEnabling).click(function (e) {
        e.preventDefault();
        $(this).toggleClass("enabledsroll");

        if ($(this).is(".enabledsroll")) {
            map.setOptions({'scrollwheel': true});
        } else {
            map.setOptions({'scrollwheel': false});
        }
    });
    var zoomControlDiv = document.createElement('div');
    var zoomControl = new ZoomControl(zoomControlDiv, map);

    function ZoomControl(controlDiv, map) {
        zoomControlDiv.index = 1;
        map.controls[google.maps.ControlPosition.RIGHT_CENTER].push(zoomControlDiv);
        controlDiv.style.padding = '5px';
        var controlWrapper = document.createElement('div');
        controlDiv.appendChild(controlWrapper);
        var zoomInButton = document.createElement('div');
        zoomInButton.className = "mapzoom-in";
        controlWrapper.appendChild(zoomInButton);
        var zoomOutButton = document.createElement('div');
        zoomOutButton.className = "mapzoom-out";
        controlWrapper.appendChild(zoomOutButton);
        google.maps.event.addDomListener(zoomInButton, 'click', function () {
            map.setZoom(map.getZoom() + 1);
        });
        google.maps.event.addDomListener(zoomOutButton, 'click', function () {
            map.setZoom(map.getZoom() - 1);
        });
    }


    // Geo Location Button
    $(".geoLocation, .input-with-icon.location a").on("click", function (e) {
        e.preventDefault();
        geolocate();
    });

    function geolocate() {

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                map.setCenter(pos);
                map.setZoom(12);

                var avrtimg = $(".avatar-img").attr("data-srcav");
                var markerIcon3 = {
                    url: avrtimg,
                }
                var marker3 = new google.maps.Marker({
                    position: pos,
                    map: map,

                    icon: markerIcon3,
                    title: 'Your location'
                });
                var myoverlay = new google.maps.OverlayView();
                myoverlay.draw = function () {
                    // add an id to the layer that includes all the markers so you can use it in CSS
                    this.getPanes().markerLayer.id = 'markerLayer';
                };
                myoverlay.setMap(map);

            });
        }
    }
}


// Custom Map Marker
// ----------------------------------------------- //

function CustomMarker(latlng, map, args, markerImg, markerCount) {
    this.latlng = latlng;
    this.args = args;

    this.markerImg = markerImg;
    this.markerCount = markerCount;
    this.setMap(map);
}

CustomMarker.prototype = new google.maps.OverlayView();

CustomMarker.prototype.draw = function () {

    var self = this;

    var div = this.div;

    if (!div) {

        div = this.div = document.createElement('div');
        div.className = 'map-marker-container';

        div.innerHTML = '<div class="marker-container">' +
            '<span class="marker-count">' + self.markerCount + '</span>' +
            '<div class="marker-card">' +
            '<div class="marker-holder"><img src="' + self.markerImg + '" alt=""></div>' +
            '</div>' +
            '</div>'


        // Clicked marker highlight
        google.maps.event.addDomListener(div, "click", function (event) {
            $('.map-marker-container').removeClass('clicked infoBox-opened');
            google.maps.event.trigger(self, "click");
            $(this).addClass('clicked infoBox-opened');
        });


        if (typeof (self.args.marker_id) !== 'undefined') {
            div.dataset.marker_id = self.args.marker_id;
        }

        var panes = this.getPanes();
        panes.overlayImage.appendChild(div);
    }

    var point = this.getProjection().fromLatLngToDivPixel(this.latlng);

    if (point) {
        div.style.left = (point.x) + 'px';
        div.style.top = (point.y) + 'px';
    }
};

CustomMarker.prototype.remove = function () {
    if (this.div) {
        this.div.parentNode.removeChild(this.div);
        this.div = null;
        $(this).removeClass('clicked');
    }
};

CustomMarker.prototype.getPosition = function () {
    return this.latlng;
};

// -------------- Custom Map Marker / End -------------- //


var head = document.getElementsByTagName('head')[0];

// Save the original method
var insertBefore = head.insertBefore;

// Replace it!
head.insertBefore = function (newElement, referenceElement) {

    if (newElement.href && newElement.href.indexOf('https://fonts.googleapis.com/css?family=Roboto') === 0) {
        return;
    }

    insertBefore.call(head, newElement, referenceElement);
};


$(document).ready(function () {
    var map = document.getElementById('map-main');
    if (typeof (map) != 'undefined' && map != null) {
        mainMap()
    }

});