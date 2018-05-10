$(function() {
  // toggle mobile menu
  $('p.icon a').on('click', function (e) {
    e.preventDefault();
    $('.mainRight').toggleClass('hide');
    $('.mainLeft').toggleClass('show');
  });

// show note content
  $('p.title').on("click", function() {
    var id = $(this).parent().attr('id');
    $('#' + id + " div.note_content").toggle();
  });

// show note categories
  $('p.category_list').on("click", function() {
    var id = $(this).parent().attr('id');
    $('#' + id + " ul").toggle();
  });

});
