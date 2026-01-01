// Select all buttons and product cards
console.log("FILTER JS LOADED");

const buttons = document.querySelectorAll('#category-buttons button');
const products = document.querySelectorAll('.product-card');

// Function to filter products
function filterProducts(categoryId) {
    products.forEach(product => {
        if (categoryId === 'all' || product.dataset.category === categoryId) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });
}

// Add click event to all buttons
buttons.forEach(button => {
    button.onclick = function() {
        const categoryId = this.dataset.category;

        // If clicked button is already active and not "All", reset to All
        if (this.classList.contains('active-btn') && categoryId !== 'all') {
            filterProducts('all'); // Show all products
            buttons.forEach(btn => btn.classList.remove('active-btn'));
            buttons[0].classList.add('active-btn'); // Make "All" active
        } else {
            // Regular filter
            buttons.forEach(btn => btn.classList.remove('active-btn'));
            this.classList.add('active-btn');
            filterProducts(categoryId);
        }
    };
});

// Set default active button to "All"
buttons[0].classList.add('active-btn');
filterProducts('all'); // Show all products by default

console.log("Buttons found:", buttons.length);
console.log("Products found:", products.length);
