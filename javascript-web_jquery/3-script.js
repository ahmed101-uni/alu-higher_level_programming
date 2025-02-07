import $ from 'jquery';

$(document).ready(() => {
  $('DIV#red_header').click(() => {
    $('header').addClass('red');
  });
});
