document.addEventListener('DOMContentLoaded', () => {
    const planSelect = document.getElementById('plan');
    const alojamientoSelect = document.getElementById('alojamiento');
    const transporteSelect = document.getElementById('transporte');
    const personasInput = document.getElementById('personas');
    const btnCotizar = document.getElementById('btn-cotizar');

    if (!btnCotizar) return;

    btnCotizar.addEventListener('click', (e) => {
        e.preventDefault();

        const planText = planSelect.options[planSelect.selectedIndex]?.text || 'No seleccionado';
        const alojamientoText = alojamientoSelect.options[alojamientoSelect.selectedIndex]?.text || 'No seleccionado';
        const transporteText = transporteSelect.options[transporteSelect.selectedIndex]?.text || 'No seleccionado';
        const personas = personasInput.value || '1';

        if (!planSelect.value) {
            alert('Por favor selecciona un plan para cotizar.');
            return;
        }

        const mensaje = `Hola QuindÃ­o Travel ðŸŒ¿, deseo solicitar una cotizaciÃ³n personalizada con los siguientes datos:\n\n` +
            `ðŸ“Œ *Plan:* ${planText}\n` +
            `ðŸ¡ *Alojamiento:* ${alojamientoText}\n` +
            `ðŸš— *Transporte:* ${transporteText}\n` +
            `ðŸ‘¥ *NÃºmero de Personas:* ${personas}\n\n` +
            `Quedo atento a la disponibilidad y tarifa final para nuestra fecha de viaje. Â¡Muchas gracias!`;

        const phone = "573174426044";
        const url = `https://wa.me/${phone}?text=${encodeURIComponent(mensaje)}`;
        
        window.open(url, '_blank');
    });
});