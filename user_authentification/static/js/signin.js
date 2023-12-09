const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".containerr");
//inputs
const firstName = document.getElementById("firstName");
const lastName = document.getElementById("lastName");
const username = document.getElementById("username");

const email = document.getElementById("email");
const password = document.getElementById("password");
//the errors to display 
const firstnameerror = document.querySelector('#firstNameError');
const lastnameerror = document.querySelector('#lastNameError');
const usernameerror = document.querySelector('#usernameError');

const emailerror = document.querySelector('#emailError');
const passworderror = document.querySelector('#passwordError');
var isvalidf = false;
var isvalidl = false;
var isvalidu = false;

var isvalide = false;
var isvalidp = false;
// Animation
sign_up_btn.addEventListener('click', () => {
  container.classList.add("sign-up-mode");
  document.querySelector('.header-area').style.backgroundColor = "#F46036";
  document.querySelector('.header-area .main-nav').style.backgroundColor = "#F46036";
  document.querySelector('.header-area .main-nav .nav li:last-child a').style.backgroundColor = "#376996";
});

sign_in_btn.addEventListener('click', () => {
  container.classList.remove("sign-up-mode");
  document.querySelector('.header-area').style.backgroundColor = "#376996";
  document.querySelector('.header-area .main-nav').style.backgroundColor = "#376996";
  document.querySelector('.header-area .main-nav .nav li:last-child a').style.backgroundColor = "#F46036";
});

document.getElementById("signupForm").addEventListener("submit", function (event) {
  if (isvalidf && isvalidl && isvalidu && isvalide && isvalidp) {
    alert('Submitted with success');
  } else {
    event.preventDefault();
  }
});

firstName.addEventListener('input', () => {
  if (/\d/.test(firstName.value)) {
    firstnameerror.style.color = "#F46036";
    firstnameerror.innerHTML = "Should not include a number";
    isvalidf = false;
  } else {
    firstnameerror.style.color = "#376996";
    firstnameerror.innerHTML = "done!";
    isvalidf = true;
  }
});

lastName.addEventListener('input', () => {
  if (/\d/.test(lastName.value)) {
    lastnameerror.style.color = "#F46036";
    lastnameerror.innerHTML = "Should not include a number";
    isvalidl = false;
  } else {
    lastnameerror.style.color = "#376996";
    lastnameerror.innerHTML = "done!";
    isvalidl = true;
  }
});

username.addEventListener('input', () => {
  if (username.value.includes(' ')) {
    usernameerror.style.color = "#F46036";
    usernameerror.innerHTML = "Invalid username, should not contain spaces.";
    isvalidu = false;
  } else {
    usernameerror.style.color = "#376996";
    usernameerror.innerHTML = "done!";
    isvalidu = true;
  }
});

email.addEventListener('input', () => {
  const emailValue = email.value.trim();

  if (!/@.*\S/.test(emailValue) || emailValue.includes(' ')) {
    emailerror.style.color = "#F46036";
    emailerror.innerHTML = "Invalid email, please enter a valid one";
    isvalide = false;
  } else {
    emailerror.style.color = "#376996";
    emailerror.innerHTML = "done!";
    isvalide = true;
  }
});



password.addEventListener('input', () => {
  if (password.value.length < 6) {
    passworderror.style.color = "#F46036";
    passworderror.innerHTML = "Password too short";
    isvalidp = false;
  } else {
    passworderror.style.color = "#376996";
    passworderror.innerHTML = "done!";
    isvalidp = true;
  }
});
