/*Diseña una expresión regular que valide contraseñas que contengan al menos una letra mayúscula, una letra minúscula, un número 
y un carácter especial, y que tengan entre 8 y 20 caracteres.*/ 

let frase = prompt("Introduce una contraseña");

let validadorContrasena= new RegExp(/^\s+|\s+$/g);