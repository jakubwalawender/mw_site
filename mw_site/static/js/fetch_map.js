let script = document.createElement('script');
if (localStorage.getItem('darkMode') === 'dark') {
    script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyCgnDX5HpCfxg-dcC0Yv0e90Vl5MY9eTc4&callback=initMapDark&v=weekly"
} else {
    script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyCgnDX5HpCfxg-dcC0Yv0e90Vl5MY9eTc4&callback=initMap&v=weekly"
}
document.body.appendChild(script);