document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const hello = document.querySelector('#hello');
      hello.textContent = data.hello;
    });
});
