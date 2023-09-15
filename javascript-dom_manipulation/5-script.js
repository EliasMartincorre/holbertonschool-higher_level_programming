/* Write a JavaScript script that updates
the text of the header element to New Header!!!
when the user clicks
on the element with id update_header */

const variable = document.getElementById('update_header');
variable.addEventListener('click', function () {
  const myHeader = document.querySelector('header');
  myHeader.innerText = 'New Header!!!';
});