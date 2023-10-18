let elRegion = document.querySelector('.region')
let elTableBody = document.querySelector('.table tbody')

// if (elRegion) {
//     districts.forEach(district => {
//         elRegion.innerHTML += `
//             <option value="${district.value}" >${district.name}</option>
//         `
//     });
// }


if (elTableBody) {
    districts.forEach((district, index) => {
        elTableBody.innerHTML += `
        <tr>
        <th scope="row">${index + 1}</th>
        <td>${district.name}</td>
        <td>13.09.2023</td>
        </tr>
        `
    });
}

// MAP

let elMap = document.getElementById('map')

if (elMap) {
    var map = L.map('map').setView([51.505, -0.09], 13);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([51.5, -0.09]).addTo(map)
        .bindPopup('A pretty CSS popup.<br> Easily customizable.')
        .openPopup();


    let submit = document.querySelector('.form__watch-btn')
    let enter = document.querySelector('.form__enter-btn')
    let elIndex = document.querySelector('.index')
    let elDate = document.querySelector('.form-date')
    let elFile = document.querySelector('.form-file')
}