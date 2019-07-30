

function our_layers( map,options ){
	var datasets = new L.GEOJSON.AJAX("{% url 'nepal' %}", {

	});
	datasets.addTo('map')
	var sidebar = L.control.sidebar('sidebar').addTo(map);

}

