window.addEventListener('load', function() {
    const api = fetch('http://localhost:5000/products')
    api
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
});