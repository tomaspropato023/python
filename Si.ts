let numeros : number[] = new Array(12);
numeros = [4, 7, 9, 3, 1, 45, 67, 23, 29, 78, 11, 16];
let indice : number;
let mayor = numeros[0];

for (indice = 0; indice < 12; indice++) {
    if (numeros[indice] > mayor) {
        mayor = numeros[indice];
    }
}

let parImpar = function(mayor) {
    if (mayor % 2 == 0){
        console.log(`El numero ${mayor} es par.`);
    } else {
        console.log(`El numero ${mayor} es impar.`);
    }
}

console.log(`El numero mayor es ${mayor}`)
parImpar(mayor);