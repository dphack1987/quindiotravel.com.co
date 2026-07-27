document.addEventListener("DOMContentLoaded", () => {
  const pills = document.querySelectorAll(".filter-pills .pill");
  
  // Aquí conectaremos la lógica de filtrado cuando carguemos planes-data.js
  pills.forEach(pill => {
    pill.addEventListener("click", () => {
      pills.forEach(p => p.classList.remove("active"));
      pill.classList.add("active");
      
      const filter = pill.getAttribute("data-filter");
      console.log("Filtrando planes por:", filter);
    });
  });
});
