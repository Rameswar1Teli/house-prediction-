// Wait until the page loads
document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const button = document.querySelector("button");

    form.addEventListener("submit", function (e) {

        // Get input values
        const rm = document.querySelector('input[name="rm"]').value;
        const pt = document.querySelector('input[name="pt"]').value;
        const lstat = document.querySelector('input[name="lstat"]').value;

        // Validation
        if (rm === "" || pt === "" || lstat === "") {
            alert("Please fill all the fields.");
            e.preventDefault();
            return;
        }

        // Disable button
        button.disabled = true;

        // Loading animation
        button.innerHTML =
            `<i class="fa-solid fa-spinner fa-spin"></i> Predicting...`;

    });

});