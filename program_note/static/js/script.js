$(function() {
  var doc = $(document),
      nav = $('nav'),
      lastScrollTop = 0;

  doc.on('scroll', function() {
    var currentScrollTop = $(this).scrollTop();
    if (currentScrollTop > lastScrollTop) {
      nav.addClass('hidden');
    } else {
      nav.removeClass('hidden');
    }
    lastScrollTop = currentScrollTop;
  });

  $("button[type='reset']").on("click", function() {
    $("form ul li input").val('');
  });


  $('p.icon a').on('click', function (e) {
    e.preventDefault();
    console.log('hello');
    $('.mainRight').toggleClass('hide');
    $('.mainLeft').toggleClass('show');
  })

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
