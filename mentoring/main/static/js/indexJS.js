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
