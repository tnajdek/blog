({
	appDir: "../",
	baseUrl: "static/js",
	dir: "../../webapp-build",
	//Comment out the optimize line if you want
	//the code minified by UglifyJS.
	optimize: "none",

	paths: {
		"handlebars": "handlebars.js",
		"jquery": "require-jquery",
		"bootstrap": "bootstrap.min"
	},

	modules: [
		{
			name: "main",
			exclude: ["jquery"]
		}
	]
});
