function checkGreeting() {
  const input = document.getElementById("inputText").value;
  if (!input || !isNaN(input)) {
    alert("Error");
    document.getElementById("inputText").value = "";
    return;
  }
}

function resetGreeting() {
  document.getElementById("greeting").innerText = "Hello User!";
}

function passCheck() {
  document
    .getElementById("signin-form")
    .addEventListener("submit", function (event) {
      let passwordInput = document.getElementById("pass");
      let passwordConfirm = document.getElementById("pass-conf");

      let password = passwordInput.value;
      let passwordC = passwordConfirm.value;

      if (password !== passwordC) {
        alert("Passwords doesn`t match!");
        event.preventDefault();
        return;
      }
    });
}

function alertExistingEmail() {
  alert("This email is already existing");
}
