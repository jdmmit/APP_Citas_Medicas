// Espera a que el DOM esté completamente cargado antes de ejecutar el código
document.addEventListener('DOMContentLoaded', function() {
  // Selección de elementos del DOM
  const hamburger = document.querySelector('.hamburger');     // Botón de menú hamburguesa para móviles
  const navMenu = document.querySelector('.nav-menu');        // Menú de navegación
  const authButtons = document.querySelector('.auth-buttons'); // Botones de autenticación
  
  // Manejo del menú móvil
  if (hamburger) {
    hamburger.addEventListener('click', function() {
      navMenu.classList.toggle('active');      // Alterna la clase 'active' en el menú de navegación
      if (authButtons) {
        authButtons.classList.toggle('active');  // Alterna la clase 'active' en los botones de autenticación
      }
    });
  }
  
  // Cierra el menú móvil cuando se hace clic en un enlace de navegación
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', function() {
      if (navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');      // Elimina la clase 'active' del menú de navegación
        if (authButtons) {
          authButtons.classList.remove('active');  // Elimina la clase 'active' de los botones de autenticación
        }
      }
    });
  });
  
  // Añade la clase 'active' al enlace de navegación correspondiente a la página actual
  const currentLocation = window.location.pathname;  // Obtiene la ruta actual de la URL
  navLinks.forEach(link => {
    const linkPath = link.getAttribute('href');       // Obtiene la ruta del enlace
    // Comprueba si la ruta del enlace coincide con la ubicación actual
    if (linkPath === currentLocation) {
      link.classList.add('active');                  // Añade la clase 'active' al enlace
    }
  });
  
  // Animación para mensajes de alerta
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(alert => {
    // Añadir animación de entrada
    alert.style.opacity = '0';                      // Inicia invisible
    alert.style.transform = 'translateY(-20px)';    // Posición inicial elevada
    
    setTimeout(() => {
      alert.style.transition = 'opacity 0.5s ease, transform 0.5s ease'; // Configura transición
      alert.style.opacity = '1';                    // Hace visible
      alert.style.transform = 'translateY(0)';      // Mueve a posición final
    }, 100);
    
    // Añadir botón de cierre si no existe
    if (!alert.querySelector('.close-btn')) {
      const closeBtn = document.createElement('button'); // Crea botón de cierre
      closeBtn.className = 'close-btn';                // Asigna clase
      closeBtn.innerHTML = '&times;';                  // Símbolo X
      closeBtn.style.float = 'right';                  // Alineado a la derecha
      closeBtn.style.background = 'none';              // Sin fondo
      closeBtn.style.border = 'none';                  // Sin borde
      closeBtn.style.fontSize = '1.25rem';             // Tamaño de fuente
      closeBtn.style.cursor = 'pointer';               // Cursor tipo mano
      closeBtn.style.marginLeft = '10px';              // Margen izquierdo
      
      closeBtn.addEventListener('click', function() {
        alert.style.opacity = '0';                     // Hace transparente
        alert.style.transform = 'translateY(-20px)';   // Mueve hacia arriba
        
        setTimeout(() => {
          alert.remove();                              // Elimina del DOM
        }, 500);
      });
      
      alert.insertBefore(closeBtn, alert.firstChild);  // Inserta al principio
    }
    
    // Auto-cerrar alertas después de 5 segundos
    setTimeout(() => {
      if (alert) {
        alert.style.opacity = '0';                     // Hace transparente
        alert.style.transform = 'translateY(-20px)';   // Mueve hacia arriba
        
        setTimeout(() => {
          if (alert.parentNode) {
            alert.remove();                            // Elimina del DOM
          }
        }, 500);
      }
    }, 5000);  // 5000 milisegundos = 5 segundos
  });
  
  // Animaciones para las tarjetas
  const cards = document.querySelectorAll('.card');    // Selecciona todas las tarjetas
  cards.forEach(card => {
    // Efecto al pasar el ratón sobre la tarjeta
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-5px)';        // Eleva la tarjeta
      this.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.1)'; // Sombra más pronunciada
    });
    
    // Efecto al quitar el ratón de la tarjeta
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';           // Vuelve a la posición original
      this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)'; // Sombra normal
    });
  });
});