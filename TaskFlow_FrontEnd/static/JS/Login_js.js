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

// Set the default state (show Login initially)
loginForm.classList.add("active");
