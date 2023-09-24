/* Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

The name must be displayed in the HTML tag DIV#character
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API */

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
})