/*Write a JavaScript script that updates the text color
 of the header element to red (#FF0000) when the user
 clicks on the tag with id red_header:*/

const redHeader = document.querySelector('#red_header');
redHeader.addEventListener('click', () => {
  redHeader.style.color = '#FF0000';
} );
