/* Write a JavaScript script that fetches the character
 name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
The name must be displayed in the HTML tag with id character.
You must use the Fetch API.
You probably should read something about usign Promises later. */

const variable = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
variable.then((response) => {
  response.json().then((data) => {
    document.getElementById('character').innerHTML = data.name;
  });
});