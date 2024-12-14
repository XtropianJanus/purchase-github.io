// JavaScript for handling form submissions and interactions

document.addEventListener('DOMContentLoaded', function() {
    const purchaseForm = document.getElementById('purchase-form');
    if (purchaseForm) {
        purchaseForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission
            const orderDetails = document.getElementById('order-details').value;
            console.log(`Purchase created with details: ${orderDetails}`);
            // Add logic to handle purchase creation
        });
    }

    const reportForm = document.getElementById('report-form');
    if (reportForm) {
        reportForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const reportType = document.getElementById('report-type').value;
            console.log(`Generating report of type: ${reportType}`);
            // Add logic to generate report
        });
    }

    const ingredientForm = document.getElementById('ingredient-form');
    const recipeForm = document.getElementById('recipe-form');
    const ingredientsList = document.getElementById('ingredients-list');
    const searchIngredient = document.getElementById('search-ingredient');

    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.textContent = message;
        notification.classList.add('show');
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000); // Notification will disappear after 3 seconds
    }

    // Handle ingredient form submission
    ingredientForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        const ingredient = document.getElementById('ingredient').value;
        const quantity = document.getElementById('quantity').value;
        const supplier = document.getElementById('supplier').value;
        const price = document.getElementById('price').value;

        // Create a new ingredient entry
        const ingredientItem = document.createElement('div');
        ingredientItem.classList.add('ingredient-item');
        ingredientItem.innerHTML = `<strong>${ingredient}</strong>: ${quantity}g from ${supplier} at $${price}/kg`;

        // Append the ingredient to the ingredients list
        ingredientsList.appendChild(ingredientItem);

        // Show notification for ingredient addition
        showNotification(`Added ${quantity}g of ${ingredient}.`);

        // Clear the ingredient form
        ingredientForm.reset();
    });

    // Handle recipe form submission
    recipeForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        const recipeName = document.getElementById('recipe-name').value;
        const menuDescription = document.getElementById('menu-description').value;
        const portions = document.getElementById('portions').value;

        // Here you can add logic to save the recipe with the ingredients
        console.log(`Recipe: ${recipeName}, Description: ${menuDescription}, Portions: ${portions}`);
        showNotification(`Recipe '${recipeName}' saved!`);

        // Clear the recipe form
        recipeForm.reset();
        ingredientsList.innerHTML = ''; // Clear the ingredients list
    });

    // Implementing the search functionality
    searchIngredient.addEventListener('input', function() {
        const filter = searchIngredient.value.toLowerCase();
        const ingredientOptions = document.querySelectorAll('#ingredient option');
        ingredientOptions.forEach(option => {
            if (option.textContent.toLowerCase().includes(filter)) {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
            }
        });
    });

    const eventForm = document.getElementById('event-form');
    if (eventForm) {
        eventForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const eventDetails = document.getElementById('event-details').value;
            console.log(`Event created with details: ${eventDetails}`);
            // Add logic to handle event creation
        });
    }

    const spoilageForm = document.getElementById('spoilage-form');
    if (spoilageForm) {
        spoilageForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const itemId = document.getElementById('item-id').value;
            console.log(`Tracking spoilage for item ID: ${itemId}`);
            // Add logic to track spoilage
        });
    }

    const intertransferForm = document.getElementById('intertransfer-form');
    if (intertransferForm) {
        intertransferForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const itemId = document.getElementById('item-id').value;
            const fromLocation = document.getElementById('from-location').value;
            const toLocation = document.getElementById('to-location').value;
            console.log(`Transferring item ID ${itemId} from ${fromLocation} to ${toLocation}`);
            // Add logic to handle intertransfer
        });
    }
});
