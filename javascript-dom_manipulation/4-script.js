const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', function () {
  const myList = document.querySelector('.my_list');
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  myList.appendChild(newItem);
});
