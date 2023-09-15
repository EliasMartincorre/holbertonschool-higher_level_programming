/* Write a JavaScript script that fetches and
lists the title for all movies
by using this URL:
https://swapi-api.hbtn.io/api/films/?format=json
All movie titles must be list in the HTML ul
element with id list_movies
You must use the Fetch API */

let peliculas = fetch("https://swapi-api.hbtn.io/api/films/?format=json");
peliculas.then((response) => {
  return response.json();
}).then((data) => {
  let lista = document.querySelector("ul#list_movies");
  for (let i = 0; i < data.results.length; i++) {
    let li = document.createElement("li");
    li.innerHTML = data.results[i].title + " " + data.results[i].episode_id;
    lista.appendChild(li);
  }
});