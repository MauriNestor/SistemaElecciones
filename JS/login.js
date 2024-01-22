function loguearUs() {
    var carnetInput = document.getElementById('input-carnet').value;
    var fechaNacimientoInput = document.getElementById('input-fn').value;

    var credencialesAlmacenadas = {
        carnet: '9344284',
        fechaNacimiento: '2003-09-20' 
    };

    if (carnetInput === credencialesAlmacenadas.carnet && fechaNacimientoInput === credencialesAlmacenadas.fechaNacimiento) {
        window.location ="/../perfil.html";
    } else {
        alert('Error: Los campos no coinciden. Verifica la información ingresada.');
    }
}
function loguearCorte(){

let ci = document.getElementById("input-ci").value;
let pass = document.getElementById("input-contra").value;
var credencialesAlmacenadas = {
    carnet: '12345',
    contraseña: 'holaqtal' 
};
if(ci ==credencialesAlmacenadas.carnet && pass==credencialesAlmacenadas.contraseña){
    window.location ="/../corteElectoral.html";
}else{
    alert("Datos incorrectos, intente nuevamente");
}
}
function loguearAdmin(){

let us = document.getElementById("input-usuario").value;
let pass = document.getElementById("input-contraseña").value;

var credencialesAlmacenadas = {
    usuario: 'mauricio',
    contraseña: 'holabuenas' 
};

if(us == credencialesAlmacenadas.usuario && pass == credencialesAlmacenadas.contraseña){
    alert('Inicio de sesión exitoso');
}else{
    alert("Datos incorrectos");
}

}
