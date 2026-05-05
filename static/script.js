document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const fileInputs = document.querySelectorAll("input[type='file']");
    const button = document.querySelector("button");

    // 🔥 Show loading effect on submit
    if (form) {
        form.addEventListener("submit", function () {

            // basic validation
            let valid = true;

            fileInputs.forEach(input => {
                if (!input.files.length) {
                    valid = false;
                }
            });

            if (!valid) {
                alert("Please upload both files!");
                event.preventDefault();
                return;
            }

            // loading animation
            button.innerText = "Analyzing...";
            button.style.opacity = "0.7";
            button.disabled = true;
        });
    }

    // 🔥 File type validation
    fileInputs.forEach(input => {
        input.addEventListener("change", function () {

            const file = this.files[0];
            if (!file) return;

            const allowedTypes = [
                "application/pdf",
                "text/plain"
            ];

            if (!allowedTypes.includes(file.type)) {
                alert("Only PDF or TXT files allowed!");
                this.value = "";
            }
        });
    });

});