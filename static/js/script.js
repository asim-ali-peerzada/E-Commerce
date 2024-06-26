document.addEventListener('DOMContentLoaded', function() {
    // Remove this line to prevent the alert popup
    // console.log("JavaScript is loaded and running.");

    var sizeBoxes = document.querySelectorAll('.size-box');
    var sizeInput = document.getElementById('size-input');

    sizeBoxes.forEach(function(box) {
        box.addEventListener('click', function() {
            sizeBoxes.forEach(function(innerBox) {
                innerBox.classList.remove('selected');
            });
            box.classList.add('selected');
            sizeInput.value = box.getAttribute('data-value');
            console.log("Selected size:", sizeInput.value);  // Debug print
        });
    });

    // Ensure the form submission logic
    document.getElementById('add-to-cart-form').addEventListener('submit', function(event) {
        if (!sizeInput.value) {
            // Remove or comment out the alert message
            // alert("Please select a size before adding to cart.");
            console.log("Size not selected. Form submission prevented.");  // Debug print
            event.preventDefault();  // Prevent form submission
        } else {
            console.log("Submitting form with size:", sizeInput.value);  // Debug print
        }
    });

});
