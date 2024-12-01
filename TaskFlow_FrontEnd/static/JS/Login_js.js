// Select elements
const loginForm = document.querySelector(".cntr_login");
const signupForm = document.querySelector(".cntr_signup");
const showSignupLink = document.getElementById("show-signup");
const showSigninLink = document.getElementById("show-signin");

// Event Listener for Showing Sign-Up Form
showSignupLink.addEventListener("click", () => {
  loginForm.classList.remove("active");
  signupForm.classList.add("active");
  showSignupLink.classList.add("hidden");
  showSigninLink.classList.remove("hidden");
});

// Event Listener for Showing Sign-In Form
showSigninLink.addEventListener("click", () => {
  signupForm.classList.remove("active");
  loginForm.classList.add("active");
  showSigninLink.classList.add("hidden");
  showSignupLink.classList.remove("hidden");
});

// Set initial state
const showSignup = "{{ show_signup|default:'false' }}" === "True";
if (showSignup) {
  signupForm.classList.add("active");
  loginForm.classList.remove("active");
  showSigninLink.classList.remove("hidden");
  showSignupLink.classList.add("hidden");
} else {
  loginForm.classList.add("active");
  signupForm.classList.remove("active");
  showSignupLink.classList.remove("hidden");
  showSigninLink.classList.add("hidden");
}

// Password Validation for Signup Form
function validateForm() {
  const password = document.getElementById("Password").value;
  const confirmPassword = document.getElementById("ConfirmPassword").value;

  // Check if passwords match
  if (password !== confirmPassword) {
    alert("Passwords do not match!");
    return false; // Prevent form submission
  }

  return true; // Allow form submission
}
