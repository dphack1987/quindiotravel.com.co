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

            const fixedHamburgerBtn = fixedNav.querySelector('#hamburger-btn');
            const fixedNavMenu = fixedNav.querySelector('#nav-menu');
            const fixedLanguageSelector = fixedNav.querySelector('#language-selector');
            if (fixedHamburgerBtn) {
                fixedHamburgerBtn.id = 'fixed-hamburger-btn';
                fixedHamburgerBtn.setAttribute('aria-controls', 'fixed-nav-menu');
            }
            if (fixedNavMenu) {
                fixedNavMenu.id = 'fixed-nav-menu';
            }
            if (fixedLanguageSelector) {
                fixedLanguageSelector.id = 'fixed-language-selector';
            }
            
            // Insertar navegación fija después del header original
            existingHeader.parentNode.insertBefore(fixedNav, existingHeader.nextSibling);

            if (fixedLanguageSelector) {
                fixedLanguageSelector.addEventListener('change', function() {
                    const mainLanguageSelector = document.getElementById('language-selector');
                    if (mainLanguageSelector) {
                        mainLanguageSelector.value = fixedLanguageSelector.value;
                        mainLanguageSelector.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                });
            }
            
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
    const hamburgerBtn = document.querySelector('#fixed-hamburger-btn');
    const navMenu = document.querySelector('#fixed-nav-menu');
    
    if (hamburgerBtn && navMenu) {
        hamburgerBtn.addEventListener('click', function() {
            const isOpen = navMenu.classList.toggle('nav-menu-open');
            hamburgerBtn.classList.toggle('nav-menu-open', isOpen);
            hamburgerBtn.setAttribute('aria-expanded', String(isOpen));
            navMenu.setAttribute('aria-hidden', String(!isOpen));
        });
        
        // Cerrar menú al hacer clic en un enlace
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('nav-menu-open');
                hamburgerBtn.classList.remove('nav-menu-open');
                hamburgerBtn.setAttribute('aria-expanded', 'false');
                navMenu.setAttribute('aria-hidden', 'true');
            });
        });
    }
    
    // Cerrar menú al hacer scroll
    window.addEventListener('scroll', function() {
        if (navMenu && navMenu.classList.contains('nav-menu-open')) {
            navMenu.classList.remove('nav-menu-open');
            if (hamburgerBtn) {
                hamburgerBtn.classList.remove('nav-menu-open');
                hamburgerBtn.setAttribute('aria-expanded', 'false');
            }
            navMenu.setAttribute('aria-hidden', 'true');
        }
    });
});