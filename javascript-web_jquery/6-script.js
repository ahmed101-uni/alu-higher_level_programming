import $ from 'jquery';

$(document).ready(() => {
  $('DIV#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});
