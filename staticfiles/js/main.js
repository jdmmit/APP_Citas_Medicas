document.addEventListener('DOMContentLoaded', function() {
  // Menú hamburguesa para dispositivos móviles
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('.nav-menu');
  const authButtons = document.querySelector('.auth-buttons');
  
  if (hamburger) {
    hamburger.addEventListener('click', function() {
      navMenu.classList.toggle('active');
      if (authButtons) {
        authButtons.classList.toggle('active');
      }
    });
  }
  
  // Cerrar menú al hacer clic en un enlace
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', function() {
      if (navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
        if (authButtons) {
          authButtons.classList.remove('active');
        }
      }
    });
  });
  
  // Añadir clase 'active' al enlace de navegación actual
  const currentLocation = window.location.pathname;
  navLinks.forEach(link => {
    const linkPath = link.getAttribute('href');
    if (linkPath === currentLocation) {
      link.classList.add('active');
    }
  });
  
  // Animación para mensajes de alerta
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(alert => {
    // Añadir animación de entrada
    alert.style.opacity = '0';
    alert.style.transform = 'translateY(-20px)';
    
    setTimeout(() => {
      alert.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      alert.style.opacity = '1';
      alert.style.transform = 'translateY(0)';
    }, 100);
    
    // Añadir botón de cierre si no existe
    if (!alert.querySelector('.close-btn')) {
      const closeBtn = document.createElement('button');
      closeBtn.className = 'close-btn';
      closeBtn.innerHTML = '&times;';
      closeBtn.style.float = 'right';
      closeBtn.style.background = 'none';
      closeBtn.style.border = 'none';
      closeBtn.style.fontSize = '1.25rem';
      closeBtn.style.cursor = 'pointer';
      closeBtn.style.marginLeft = '10px';
      
      closeBtn.addEventListener('click', function() {
        alert.style.opacity = '0';
        alert.style.transform = 'translateY(-20px)';
        
        setTimeout(() => {
          alert.remove();
        }, 500);
      });
      
      alert.insertBefore(closeBtn, alert.firstChild);
    }
    
    // Auto-cerrar alertas después de 5 segundos
    setTimeout(() => {
      if (alert) {
        alert.style.opacity = '0';
        alert.style.transform = 'translateY(-20px)';
        
        setTimeout(() => {
          if (alert.parentNode) {
            alert.remove();
          }
        }, 500);
      }
    }, 5000);
  });
  
  // Animación para tarjetas
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-5px)';
      this.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.1)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
      this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
    });
  });
});