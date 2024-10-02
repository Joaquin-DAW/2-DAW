/*Diseñar un script que lea una dirección de email y la valide. No se terminará hasta introducir una dirección correcta. 
Modificar el ejercicio anterior para una vez validado el correo mostrar el usuario y el servidor de correo en dos mensajes.*/ 

let email = prompt("Introduce una dirección de email");

const regex = /^[a-z]+@[a-z]+\.[a-z]{2,3}$/;

while (email){
    email = prompt("Introduce una dirección de email valida, por favor");
}