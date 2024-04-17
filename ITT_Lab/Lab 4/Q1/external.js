document.getElementById("fibonaccibutton").onclick = function() {
    var i,j;
    let num = parseInt(document.getElementById("fibonacci").value);
    let fibo = document.getElementById("fib");
    for(i=3;i<=num;i++)
    {
        j=i-1+i-2;
        let fibo2 =` <br/>${j}<br/>`;
        fibo.innerHTML += fibo2;
    }
}


/*window.onload = function () {
    let table = document.getElementById("myTable");
    for (let i = 0; i <= 10; i++) {
        let row = `<tr> <td>${i}</td> <td>${i * i}</td> <td>${i * i * i}</td> </tr>`;
        table.innerHTML += row;
    }
} */

document.getElementById("fibonaccibutton").onclick = function() {
    var i, j;
    let num = parseInt(document.getElementById("fibonacci").value);
    let fibo = document.getElementById("fib");
    let fiboArray = [0, 1];
    for(i=2; i<=num; i++) {
        j = fiboArray[i-1] + fiboArray[i-2];
        fiboArray.push(j);
        let fibo2 = `<br/>${j}<br/>`;
        fibo.innerHTML += fibo2;
    }
}