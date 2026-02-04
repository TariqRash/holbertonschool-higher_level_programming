document.addEventListener('DOMContentLoaded', function () {
  const btnTranslate = document.querySelector('#btn_translate');
  const languageCode = document.querySelector('#language_code');
  const hello = document.querySelector('#hello');

  btnTranslate.addEventListener('click', function () {
    const lang = languageCode.value;
    fetch(`https://hellosalut.stefanbohacek.com/?lang=${lang}`)
      .then(response => response.json())
      .then(data => {
        hello.textContent = data.hello;
      });
  });
});
