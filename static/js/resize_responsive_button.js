if ($(window).width() > 990) {
    $( ".watchlist_item" ).hover(function() {
        $(this).find('button').css('visibility', 'visible')
    });
    $('.watchlist_item').on("mouseleave", function() {
        $(this).find('button').css('visibility', 'hidden');
    });
}
else {
    $('.watchlist_item').find('button').each(function(){
        this.css('visibily', 'visible');
    });
}    