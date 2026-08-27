// Fixed Navigation JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Detectar si estamos en página principal para aplicar navegación fija
    const isMainPage = window.location.pathname === '/' || window.location.pathname === '/index.html';
    
    if (isMainPage) {
        // Crear navegación fija
        const existingHeader = document.querySelector('.main-header');
        if (existingHeader) {
            // Clonar el header para la versión fija
            const fixedNav = existingHeader.cloneNode(true);
            fixedNav.classList.add('fixed-navigation');
            fixedNav.classList.remove('main-header');
            fixedNav.id = 'fixed-navigation';
            
            // Insertar navegación fija después del header original
            existingHeader.parentNode.insertBefore(fixedNav, existingHeader.nextSibling);
            
            // Ocultar header original cuando se hace scroll
            window.addEventListener('scroll', function() {
                if (window.pageYOffset > 200) {
                    existingHeader.style.display = 'none';
                    fixedNav.style.display = 'block';
                    document.body.classList.add('with-fixed-nav');
                } else {
                    existingHeader.style.display = 'block';
                    fixedNav.style.display = 'none';
                    document.body.classList.remove('with-fixed-nav');
                }
            });
            
            // Ocultar navegación fija inicialmente
            fixedNav.style.display = 'none';
        }
    }
    
    // Funcionalidad de menú móvil para navegación fija
    const hamburgerBtn = document.querySelector('#fixed-navigation .hamburger-btn');
    const navMenu = document.querySelector('#fixed-navigation .nav-menu');
    
    if (hamburgerBtn && navMenu) {
        hamburgerBtn.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            hamburgerBtn.classList.toggle('active');
        });
        
        // Cerrar menú al hacer clic en un enlace
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                hamburgerBtn.classList.remove('active');
            });
        });
    }
    
    // Cerrar menú al hacer scroll
    window.addEventListener('scroll', function() {
        if (navMenu && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            if (hamburgerBtn) {
                hamburgerBtn.classList.remove('active');
            }
        }
    });
});