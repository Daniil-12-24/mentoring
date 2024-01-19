function changeGreeting() {
  var userText = document.getElementById("inputText").value;

  var newText = "Hello " + userText + "!";

  document.getElementById("greeting").innerText = newText;

  document.getElementById("inputText").value = "";
}

function resetGreeting() {
  document.getElementById("greeting").innerText = "Hello User!";
}
