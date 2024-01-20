function changeGreeting() {
  let input = document.getElementById("inputText").value;
  if (input === "" || !isNaN(input)) {
    alert("Error");
    document.getElementById("inputText").value = "";
  } else {
    let userText = input;

    let newText = "Hello " + userText + "!";

    document.getElementById("greeting").innerText = newText;

    document.getElementById("inputText").value = "";
  }
}

function resetGreeting() {
  document.getElementById("greeting").innerText = "Hello User!";
}
