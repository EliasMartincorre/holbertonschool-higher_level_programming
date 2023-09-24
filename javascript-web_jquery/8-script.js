/* Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

All movie titles must be list in the HTML tag UL#list_movies
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API */
$.get('https://swapi-api.hbtn.io/api/films/?format=json',  (data) => {
  for (const movie of data.results) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  }
});