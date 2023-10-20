document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle");
    const nav = document.querySelector(".nav");
    const navShowMenu = document.querySelector(".nav.show-menu");
    const closeButton = document.querySelector(".close-button");

    // Agrega un evento de clic al botón de hamburguesa
    menuToggle.addEventListener("click", function () {
        // Si la pantalla tiene una resolución menor o igual a 800px
        if (window.innerWidth <= 800) {
            // Muestra el menú desplegable
            navShowMenu.style.display = "block";
            // Oculta el botón de hamburguesa
            menuToggle.style.display = "none";
        }
    });

    // Agrega un evento de clic al botón de cierre (close-button) en el menú desplegable
    closeButton.addEventListener("click", function () {
        // Oculta el menú desplegable
        navShowMenu.style.display = "none";
        // Muestra el botón de hamburguesa si la resolución es menor o igual a 800px
        if (window.innerWidth <= 800) {
            menuToggle.style.display = "block";
        }
    });

    // Comprueba la resolución inicial y muestra u oculta elementos en consecuencia
    if (window.innerWidth > 800) {
        menuToggle.style.display = "none";
        navShowMenu.style.display = "none";
    } else {
        menuToggle.style.display = "block";
        navShowMenu.style.display = "none";
    }
});
