document.addEventListener("DOMContentLoaded", function() {
    const tabLinks = document.querySelectorAll('.tab-link');
    const tabContents = document.querySelectorAll('.tab-content');

    function showTab(tabName) {
        tabContents.forEach(content => {
            content.classList.remove('active');
        });
        document.getElementById(tabName).classList.add('active');

        // Update URL hash
        window.location.hash = tabName;
    }

    tabLinks.forEach(link => {
        link.addEventListener('click', function() {
            const tabName = this.getAttribute('data-tab');
            showTab(tabName);
        });
    });

    // Check URL hash on load
    const initialHash = window.location.hash.substring(1);
    if (initialHash) {
        showTab(initialHash);
    } else {
        // Default tab
        showTab('home');
    }
});
