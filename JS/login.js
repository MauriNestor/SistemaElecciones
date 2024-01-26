function loginUs() {
    var carnetInput = document.getElementById('input-carnet').value;
    var fechaNacimientoInput = document.getElementById('input-fn').value;
    
    var birthdateYear = new Date(fechaNacimientoInput).getFullYear();

    if (birthdateYear > 2006) {
        alert("Lo siento, debes ser mayor de 18 años para iniciar sesión.");
        return; // Detener la ejecución si la fecha no es válida
    }

    if (carnetInput === '' || fechaNacimientoInput === '') {
        alert("Por favor, complete ambos campos.");
        return; 
    }
    loginElector(carnetInput,fechaNacimientoInput);
}
function loginComite(){

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
            window.location ="/../verResultados.html";
        }else{
            alert("Verifique que su usuario y contraseña sean los correctos");
            document.getElementById('input-ci').value = '';
            document.getElementById('input-contra').value = '';
        }
    }
}
function loginAdmin(){

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
        document.getElementById('input-usuario').value = '';
        document.getElementById('input-contraseña').value = '';
    }

}

async function loginElector(c_i,fec_n){
    const url = `http://127.0.0.1:8000/auth/token?ci=${c_i}&fecha_nac=${fec_n}`; //esto es el link del api local
    try{
        const response = await fetch(url, {
            method: 'POST',
            mode: 'cors', // Importante: Habilitar CORS
        });
        
        if (response.ok){
            const data = await response.json();
            console.log('OK', data.access_token);
            localStorage.setItem('access_token',data.access_token);
            window.location.href = "http://127.0.0.1:5500/perfil.html";
        }
        else{
            console.log('error al autenticar', response.status, response.statusText);
        }
    }
    catch (error){
        console.error('error en red',error);
    }
}