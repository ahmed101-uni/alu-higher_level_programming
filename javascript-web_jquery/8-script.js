import $ from 'jquery';

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  const movies = data.results;
  movies.forEach(movie => {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  });
});
