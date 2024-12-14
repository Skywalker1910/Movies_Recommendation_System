document.addEventListener("DOMContentLoaded", function() {
    const ratings = document.querySelectorAll("input[type='range']");
    ratings.forEach(rating => {
        rating.addEventListener("input", function() {
            const value = this.value;
            this.nextElementSibling.textContent = `Rating: ${value}`;
        });
    });
});