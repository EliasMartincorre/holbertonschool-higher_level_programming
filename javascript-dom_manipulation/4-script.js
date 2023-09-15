/* Write a JavaScript script that adds a
li element to a list when the user
clicks on the element with id add_item:
The new element must be: <li>Item</li> 
The new element must be added to the ul
element with class my_list */

const variable = document.getElementById('add_item');
variable.addEventListener('click', function () {
const mylista = document.querySelector('ul.my_list');
const newElement = document.createElement('li');
newElement.innerText = 'Item';
mylista.appendChild(newElement);
});