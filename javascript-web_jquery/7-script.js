import $ from 'jquery';

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
  $('DIV#character').text(data.name);
});
