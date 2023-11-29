let script = document.createElement('script');
if (localStorage.getItem('darkMode') === 'dark') {
    script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyCYKQF8PAh3MvYMRCY89-fh1jHvKzoFzpM&callback=initMapDark&v=weekly"
} else {
    script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyCYKQF8PAh3MvYMRCY89-fh1jHvKzoFzpM&callback=initMap&v=weekly"
}
document.body.appendChild(script);