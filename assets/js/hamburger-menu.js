/**
 * Hamburger Menu Component for Quindío Travel
 * Handles mobile navigation menu functionality
 */

class HamburgerMenu {
    constructor(options = {}) {
        this.toggleSelector = options.toggleSelector || '#hamburger-btn';
        this.menuSelector = options.menuSelector || '#nav-menu';
        this.activeClass = options.activeClass || 'nav-menu-open';
        this.bodyClass = options.bodyClass || 'menu-open';
        
        this.toggle = document.querySelector(this.toggleSelector);
        this.menu = document.querySelector(this.menuSelector);
        
        if (this.toggle && this.menu) {
            this.init();
        } else {
            console.warn('HamburgerMenu: Toggle or menu element not found');
        }
    }
    
    init() {
        this.bindEvents();
        this.setupARIA();
        this.handleResize();
    }
    
    bindEvents() {
        // Toggle menu on click
        this.toggle.addEventListener('click', (e) => {
            e.preventDefault();
            this.toggleMenu();
        });
        
        // Close menu on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.isMenuOpen()) {
                this.closeMenu();
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (this.isMenuOpen() && 
                !this.menu.contains(e.target) && 
                !this.toggle.contains(e.target)) {
                this.closeMenu();
            }
        });
        
        // Close menu on window resize
        window.addEventListener('resize', this.handleResize.bind(this));
        
        // Close menu when clicking on menu links
        if (this.menu) {
            const menuLinks = this.menu.querySelectorAll('a');
            menuLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (this.isMenuOpen()) {
                        this.closeMenu();
                    }
                });
            });
        }
    }
    
    setupARIA() {
        this.toggle.setAttribute('aria-expanded', 'false');
        this.toggle.setAttribute('aria-controls', this.menuSelector.replace('.', ''));
        this.menu.setAttribute('aria-hidden', 'true');
    }
    
    handleResize() {
        // Close menu on desktop breakpoint
        if (window.innerWidth >= 768 && this.isMenuOpen()) {
            this.closeMenu();
        }
    }
    
    toggleMenu() {
        if (this.isMenuOpen()) {
            this.closeMenu();
        } else {
            this.openMenu();
        }
    }
    
    openMenu() {
        this.menu.classList.add(this.activeClass);
        this.toggle.classList.add(this.activeClass);
        document.body.classList.add(this.bodyClass);
        
        // Update ARIA attributes
        this.toggle.setAttribute('aria-expanded', 'true');
        this.menu.setAttribute('aria-hidden', 'false');
        
        // Focus first menu item
        const firstLink = this.menu.querySelector('a');
        if (firstLink) {
            setTimeout(() => firstLink.focus(), 100);
        }
        
        // Prevent body scroll
        document.body.style.overflow = 'hidden';
    }
    
    closeMenu() {
        this.menu.classList.remove(this.activeClass);
        this.toggle.classList.remove(this.activeClass);
        document.body.classList.remove(this.bodyClass);
        
        // Update ARIA attributes
        this.toggle.setAttribute('aria-expanded', 'false');
        this.menu.setAttribute('aria-hidden', 'true');
        
        // Restore body scroll
        document.body.style.overflow = '';
        
        // Return focus to toggle
        this.toggle.focus();
    }
    
    isMenuOpen() {
        return this.menu.classList.contains(this.activeClass);
    }
    
    destroy() {
        // Remove event listeners and cleanup
        this.toggle.removeEventListener('click', this.toggleMenu);
        document.removeEventListener('keydown', this.handleKeydown);
        document.removeEventListener('click', this.handleClickOutside);
        window.removeEventListener('resize', this.handleResize);
        
        this.closeMenu();
    }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.hamburgerMenu = new HamburgerMenu();
    });
} else {
    window.hamburgerMenu = new HamburgerMenu();
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = HamburgerMenu;
}