$("#button_search_director").click(function(){
    let search = $("#input_for_directors").val();
    $(".row_advanced_results").remove();
    $("#advanced_results").append("<div id='rainbow_loader' class='rainbow mt-5'></div>")
    $.ajax({
        url: '/movies/advanced/search/results?by_director=' + search,
        type: 'get',
        success: function(data) {
            if (data.length === 0) {
                $('#rainbow_loader').remove();
                $("#advanced_results").append("<div class='row row_advanced_results'><div class='alert alert-warning' role='warning'>No results found</div></div>")
            } else {
                $("#advanced_results").append("<div class='row row_advanced_results'></div>");
                data.forEach(elt => {
                    $('#rainbow_loader').remove();
                    $(".row_advanced_results").append("<h5 class='mt-5'>Director: "+ elt['director'] +"</h5><hr class='w-50'><div class='row row-col-movies-"+ elt['director'].replace(/\s+/g, '') +"'></div>");
                    elt['movies'].forEach(movie => {
                        $(".row-col-movies-" + elt['director'].replace(/\s+/g, '')).append("<div class='col-lg-2 col-md-3 col-sm-6 col-6 mb-3 container-picture'><img src='" + movie[3] + "' width='220' height='300' class='image'><div class='overlay'><div class=row><div class='text'>"+ movie[1] + " ("+ movie[2] +")</div></div><div class=row><div class='card-block'><a href='/movies/get/"+ movie[0] +"'><button class='btn btn-outline-primary btn-picture'>Detail</button></a></div></div></div><div>");
                    })
                })};   
            },
        failure: function(data) { 
            $('#rainbow_loader').remove();
            $("#advanced_results").append("<div class='alert alert-danger' role='alert'>Oops, there is an error, please try again !</div>")
        }
    });
})