import $ from 'jquery';

$(document).ready(() => {
  $('DIV#toggle_header').click(() => {
    $('header').toggleClass('red');
    $('header').toggleClass('green');
  });
});
