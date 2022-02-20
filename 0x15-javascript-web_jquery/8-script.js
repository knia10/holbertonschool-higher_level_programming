$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movie = data.results;
  for (const i in movie) {
    $('UL#list_movies').append('<li>' + movie[i].title + '<li>');
  }
});
