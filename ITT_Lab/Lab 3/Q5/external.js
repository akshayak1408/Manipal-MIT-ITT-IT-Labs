window.onload = function () {
    let table = document.getElementById("myTable");
    for (let i = 0; i <= 10; i++) {
        let row = `<tr> <td>${i}</td> <td>${i * i}</td> <td>${i * i * i}</td> </tr>`;
        table.innerHTML += row;
    }
} 
