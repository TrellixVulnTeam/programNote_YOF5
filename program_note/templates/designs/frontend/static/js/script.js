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
});
