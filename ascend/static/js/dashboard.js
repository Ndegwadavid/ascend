document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById('sidebar');
    const hamburger = document.getElementById('hamburger');
    const closeBtn = document.querySelector('.close-btn');

    hamburger.addEventListener('click', function() {
        sidebar.classList.add('active');
    });

    closeBtn.addEventListener('click', function() {
        sidebar.classList.remove('active');
    });
    
});
