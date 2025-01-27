<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = htmlspecialchars($_POST['name']);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $message = htmlspecialchars($_POST['message']);

    if (!empty($name) && !empty($email) && !empty($message)) {

        // Validate the email format
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            echo "Please enter a valid email address.";
            exit;
        }

        // Send the email
        $to = 'vivekworks51@gmail.com';
        $subject = 'New Contact Form Submission';
        $body = "Name: $name\nEmail: $email\nMessage: $message";
        $headers = 'From: ' . $email . "\r\n" .
                   'Reply-To: ' . $email . "\r\n" .
                   'X-Mailer: PHP/' . phpversion();

        if (mail($to, $subject, $body, $headers)) {
            echo "Thank you, $name. Your message has been successfully received. We will get back to you soon!";
        } else {
            echo "Sorry, there was an issue sending your message. Please try again later.";
        }

    } else {
        echo "Please fill in all fields before submitting the form.";
    }
} else {
    echo "There was an issue with the form submission.";
}
?>
