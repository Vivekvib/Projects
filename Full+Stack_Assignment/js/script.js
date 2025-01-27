// Contact Form Validation
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form data
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let message = document.getElementById('message').value;

    // Validate form fields
    if (name === '' || email === '' || message === '') {
        alert('Please fill in all fields.');
    } else {
        // Submit the form via AJAX (instead of a standard submission)
        let formData = new FormData(this);
        
        fetch('form_handler.php', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            alert(data); // Show server response (success or error message)
            // Optionally reset the form
            document.getElementById('contact-form').reset();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error submitting your form.');
        });
    }
});

// Registration Form Validation
document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form data
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    // Validate form fields
    if (name === '' || email === '' || password === '') {
        alert('Please fill in all fields.');
    } else {
        // Submit the form via AJAX (instead of a standard submission)
        let formData = new FormData(this);

        fetch('register_handler.php', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            alert(data); // Show server response (success or error message)
            // Optionally reset the form or redirect user
            document.getElementById('registration-form').reset();
            // window.location.href = 'login.html'; // Redirect to login page after registration (if needed)
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error submitting your form.');
        });
    }
});

// Optional: Smooth Scroll for Navigation Links (Enhance user experience)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
