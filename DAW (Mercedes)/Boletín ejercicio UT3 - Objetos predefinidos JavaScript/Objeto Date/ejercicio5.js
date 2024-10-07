/*Realizar un programa que muestre cuántos días faltan para el próximo cumpleaños del usuario y muestre “¡Felicidades!” si es el día señalado.*/

let cumpleanios = prompt("Introduce tu cumpleaños, en formato año-mes-dia");

let fechaCumpleanios = new Date(cumpleanios);

let diaCum = fechaCumpleanios.getDate();
let mesCum = fechaCumpleanios.getMonth();


let hoy = new Date();

let diaHoy = hoy.getDate();
let mesHoy = hoy.getMonth();



if (diaCum == diaHoy && mesCum == mesHoy ) {
    console.log("Felicidades es tu cumpleaños");
}