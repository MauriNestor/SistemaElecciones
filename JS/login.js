function loguearUs() {
    var carnetInput = document.getElementById('input-carnet').value;
    var fechaNacimientoInput = document.getElementById('input-fn').value;
    
    var birthdateYear = new Date(fechaNacimientoInput).getFullYear();

    if (birthdateYear > 2006) {
        alert("Lo siento, debes ser mayor de 18 años para iniciar sesión.");
        return; // Detener la ejecución si la fecha no es válida
    }

    var credencialesAlmacenadas = {
        carnet: '9344284',
        fechaNacimiento: '2003-09-20' 
    };

    if (carnetInput === '' || fechaNacimientoInput === '') {
        alert("Por favor, complete ambos campos.");
        return; 
    }else{

        if (carnetInput === credencialesAlmacenadas.carnet && fechaNacimientoInput === credencialesAlmacenadas.fechaNacimiento) {
            window.location ="/../perfil.html";
        } else {
            alert('CI y/o incorrecta, por favor vuelve a iniciar los datos');
            document.getElementById('input-carnet').value = '';
            document.getElementById('input-fn').value = '';
        }
    }    
}
function loguearCorte(){

    let ci = document.getElementById("input-ci").value;
    let pass = document.getElementById("input-contra").value;
    var credencialesAlmacenadas = {
        carnet: '12345',
        contraseña: 'holaqtal' 
    };
    if (ci === '' || pass === '') {
        alert("Por favor, complete ambos campos.");
        return; 
    }else{

        if(ci ==credencialesAlmacenadas.carnet && pass==credencialesAlmacenadas.contraseña){
            window.location ="/../corteElectoral.html";
        }else{
            alert("Verifique que su usuario y contraseña sean los correctos");
            document.getElementById('input-ci').value = '';
            document.getElementById('input-contra').value = '';
        }
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
