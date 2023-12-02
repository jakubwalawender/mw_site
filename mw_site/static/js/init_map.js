function initMap() {
    let marker = {lat: 50.016627565490325, lng: 22.67826463942701};
    const map = new google.maps.Map(document.getElementById("map"), {
            center: marker,
            zoom: 16,
            mapTypeControlOptions: {
                mapTypeIds: ["roadmap", "satellite", "hybrid", "terrain", "styled_map"],
            },
        styles: [
             {
                    featureType: "poi.business",
                    stylers: [
                        {
                            visibility: "off"
                        }
                    ]
                },
        ]
        }
    );
    new google.maps.Marker({
        position: marker,
        map: map,
        title: "Kancelaria Adwokacka Mirosław Włoch",
    });

}

function initMapDark() {
    let marker = {lat: 50.016627565490325, lng: 22.67826463942701};
    const map = new google.maps.Map(document.getElementById("map"), {
            center: marker,
            zoom: 16,
            mapTypeControlOptions: {
                mapTypeIds: ["roadmap", "satellite", "hybrid", "terrain", "styled_map"],
            },
            styles: [
                {elementType: "geometry", stylers: [{color: "#242f3e"}]},
                {elementType: "labels.text.stroke", stylers: [{color: "#242f3e"}]},
                {elementType: "labels.text.fill", stylers: [{color: "#746855"}]},
                {
                    featureType: "administrative.locality",
                    elementType: "labels.text.fill",
                    stylers: [{color: "#d59563"}],
                },
                {
                    featureType: "poi",
                    elementType: "labels.text.fill",
                    stylers: [{color: "#d59563"}],
                },
                {
                    featureType: "poi.business",
                    stylers: [
                        {
                            visibility: "off"
                        }
                    ]
                },
                {
                    featureType: "poi.park",
                    elementType: "geometry",
                    stylers: [{color: "#263c3f"}],
                },
                {
                    featureType: "poi.park",
                    elementType: "labels.text.fill",
                    stylers: [{color: "#6b9a76"}],
                },
                {
                    featureType: "road",
                    elementType: "geometry",
                    stylers: [{color: "#38414e"}],
                },
                {
                    featureType: "road",
                    elementType: "geometry.stroke",
                    stylers: [{color: "#212a37"}],
                },
                {
                    featureType: "road",
                    elementType: "labels.text.fill",
                    stylers: [{color: "#9ca5b3"}],
                },
                {
                    featureType: "road.highway",
                    elementType: "geometry",
                    stylers: [{color: "#746855"}],
                },
                {
                    featureType: "road.highway",
                    elementType: "geometry.stroke",
                    stylers: [{color: "#1f2835"}],
                },
                {
                    featureType: "road.highway",
                    elementType: "labels.text.fill",
                    stylers: [{color: "#f3d19c"}],
                },
                {
                    featureType: "transit",
                    elementType: "geometry",
                    stylers: [{color: "#2f3948"}],
                },
                {
                    featureType: "transit.station",
                    elementType: "labels.text.fill",
                    stylers: [{color: "#d59563"}],
                },
                {
                    featureType: "water",
                    elementType: "geometry",
                    stylers: [{color: "#17263c"}],
                },
                {
                    featureType: "water",
                    elementType: "labels.text.fill",
                    stylers: [{color: "#515c6d"}],
                },
                {
                    featureType: "water",
                    elementType: "labels.text.stroke",
                    stylers: [{color: "#17263c"}],
                },
            ],
        }
    );
    new google.maps.Marker({
        position: marker,
        map: map,
        title: "Kancelaria Adwokacka Mirosław Włoch",
    });
}

window.initMap = initMap;