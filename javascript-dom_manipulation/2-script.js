/* Write a JavaScript script that adds the
class red to the header element when the user
clicks on the tag with id red_header */

const redHeader = document.querySelector('#red_header');
redHeader.addEventListener('click', () => {
    document.querySelector('header').classList.add('red');
} );
