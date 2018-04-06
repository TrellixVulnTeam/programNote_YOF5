$(function() {
  $('p.icon a').on('click', function (e) {
    e.preventDefault();
    console.log('hello');
    $('.mainRight').toggleClass('hide');
    $('.mainLeft').toggleClass('show');
  })
});
