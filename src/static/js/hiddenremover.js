document.addEventListener("DOMContentLoaded", function() {
    // Código para mostrar elementos que estaban ocultos
    var hiddenElements = document.querySelectorAll(".hidden");
    for (var i = 0; i < hiddenElements.length; i++) {
        hiddenElements[i].classList.remove("hidden");
    }
});