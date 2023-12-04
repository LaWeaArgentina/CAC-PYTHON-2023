function validarForm() {

    // Datos de formulario
    var nombre = document.getElementById("nombre").value;
    var email = document.getElementById("email").value;
    var mensaje = document.getElementById("mensaje").value;

    // variables de error
    var nombreError = document.getElementById("nombreError");
    var emailError = document.getElementById("emailError");
    var mensajeError = document.getElementById("mensajeError");

    // Validar nombre obligatorio
    if (nombre === "") {
        nombreError.textContent = "Debe de ingresar el nombre";
        return false; // Evita que el formulario se envíe
    } else {
        nombreError.textContent = "";
    }

    // Validar email
    var emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (email === "") {
        emailError.textContent = "Debe de ingresar el email";
        return false;
    } else if (!emailRegex.test(email)) {
        emailError.textContent = "El email no es válido";
        return false;
    } else {
        emailError.textContent = "";
    }

    // Validar mensaje 
    if (mensaje === "") {
        mensajeError.textContent = "El mensaje es obligatorio";
        return false;
    } else {
        mensajeError.textContent = "";
    }

    // Si esta todo ok,se envia
    return true;
}