/* Write a JavaScript script that fetches
from https://hellosalut.stefanbohacek.dev/?lang=fr
and displays the value of hello from that fetch
in the HTML element with id hello */


let hola = fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
hola.then((response) => {
  return response.json();
}).then((data) => {
  document.getElementById("hello").innerHTML = data.hello;
});
