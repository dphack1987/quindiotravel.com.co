/**
 * Countdown Timer de Urgencia para Conversiones
 * Sistema de urgencia con countdown timer dinámico para incentivar reservas inmediatas
 */

(function() {
    'use strict';

    // Configuración del countdown
    const COUNTDOWN_CONFIG = {
        initialHours: 2,
        initialMinutes: 34,
        initialSeconds: 56,
        resetOnZero: true,
        showMessage: true,
        urgentMessage: "¡ÚLTIMOS CUPOS!"
    };

    class UrgencyCountdown {
        constructor(config) {
            this.config = config;
            this.timerElement = document.getElementById('countdown-timer');
            this.bannerElement = document.getElementById('urgency-banner');
            this.remainingTime = this.getInitialTime();
            this.interval = null;
            
            this.init();
        }

        getInitialTime() {
            // Tiempo inicial en segundos
            return this.config.initialHours * 3600 + 
                   this.config.initialMinutes * 60 + 
                   this.config.initialSeconds;
        }

        init() {
            if (!this.timerElement) {
                console.warn('Elemento countdown-timer no encontrado');
                return;
            }

            this.startTimer();
            this.bindEvents();
            this.checkUrgencyLevel();
        }

        startTimer() {
            this.updateDisplay();
            
            this.interval = setInterval(() => {
                this.remainingTime--;
                
                if (this.remainingTime <= 0) {
                    if (this.config.resetOnZero) {
                        this.resetTimer();
                    } else {
                        this.stopTimer();
                    }
                }
                
                this.updateDisplay();
                this.checkUrgencyLevel();
            }, 1000);
        }

        stopTimer() {
            if (this.interval) {
                clearInterval(this.interval);
                this.interval = null;
            }
        }

        resetTimer() {
            this.remainingTime = this.getInitialTime();
            this.startTimer();
        }

        updateDisplay() {
            const hours = Math.floor(this.remainingTime / 3600);
            const minutes = Math.floor((this.remainingTime % 3600) / 60);
            const seconds = this.remainingTime % 60;

            const display = this.formatTime(hours, minutes, seconds);
            this.timerElement.textContent = display;
            
            // Actualizar atributo para accesibilidad
            this.timerElement.setAttribute('aria-live', 'polite');
        }

        formatTime(hours, minutes, seconds) {
            return `${this.padZero(hours)}:${this.padZero(minutes)}:${this.padZero(seconds)}`;
        }

        padZero(num) {
            return num.toString().padStart(2, '0');
        }

        checkUrgencyLevel() {
            const totalSeconds = this.remainingTime;
            const urgencyLevels = {
                critical: 300,    // 5 minutos
                high: 900,       // 15 minutos
                medium: 1800     // 30 minutos
            };

            let urgencyClass = '';
            let urgencyMessage = '';

            if (totalSeconds <= urgencyLevels.critical) {
                urgencyClass = 'urgency-critical';
                urgencyMessage = this.config.urgentMessage;
            } else if (totalSeconds <= urgencyLevels.high) {
                urgencyClass = 'urgency-high';
                urgencyMessage = 'CUPOS LIMITADOS';
            } else if (totalSeconds <= urgencyLevels.medium) {
                urgencyClass = 'urgency-medium';
                urgencyMessage = 'RESERVA PRONTO';
            }

            if (urgencyClass) {
                this.bannerElement.classList.add(urgencyClass);
            }

            if (urgencyMessage && this.config.showMessage) {
                this.updateUrgencyMessage(urgencyMessage);
            }
        }

        updateUrgencyMessage(message) {
            const messageElement = this.bannerElement.querySelector('.urgency-message');
            if (messageElement) {
                messageElement.textContent = message;
            }
        }

        bindEvents() {
            // Pausar timer cuando el usuario está en la página
            document.addEventListener('visibilitychange', () => {
                if (document.hidden) {
                    this.stopTimer();
                } else {
                    this.startTimer();
                }
            });

            // Click en CTA para tracking
            const ctaButton = this.bannerElement.querySelector('a');
            if (ctaButton) {
                ctaButton.addEventListener('click', (e) => {
                    this.trackConversion('urgency_banner_click');
                });
            }
        }

        trackConversion(eventType) {
            // Tracking de conversiones (puedes integrar con Google Analytics)
            if (typeof gtag !== 'undefined') {
                gtag('event', eventType, {
                    'event_category': 'urgency_banner',
                    'event_label': 'countdown_timer',
                    'value': this.remainingTime
                });
            }
            
            console.log(`Conversion event tracked: ${eventType}`);
        }
    }

    // Inicializar cuando el DOM esté listo
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            new UrgencyCountdown(COUNTDOWN_CONFIG);
        });
    } else {
        new UrgencyCountdown(COUNTDOWN_CONFIG);
    }

})();