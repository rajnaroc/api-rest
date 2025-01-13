let caja_principal = document.getElementById('principal');

let productos = async () => { 
    const response = await fetch('http://localhost:5000/products');
    const data = await response.json();
    console.log(data.products);
    return data.products;
}

let valores = async () => {
    let valores = await productos();
    for (let i = 0; i < valores.length; i++) {
        caja_principal.innerHTML += `
            <div class="bg-white shadow-md rounded-lg p-4 mb-4 sm:w-full md:w-1/2 lg:w-1/3 xl:w-1/4 mx-auto">
                <h2 class="text-xl font-bold mb-2">${valores[i].nombre}</h2>
                <p class="text-gray-700 mb-2">${valores[i].precio}</p>
                <img class="w-full h-auto mb-2" src="${valores[i].foto}">
                <p class="text-gray-700 p-5">${valores[i].cantidad}</p>
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Comprar</button>
            </div>
        `;
    }
}

valores();