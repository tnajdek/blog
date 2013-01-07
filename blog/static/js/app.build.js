({
	appDir: "../",
	baseUrl: "static/js",
	dir: "../../webapp-build",
	//Comment out the optimize line if you want
	//the code minified by UglifyJS.
	optimize: "none",

	paths: {
		"handlebars": "libs/handlebars.js",
		"jquery": "libs/require-jquery",
		"bootstrap": "libs/bootstrap.min"
	},

	modules: [
		{
			name: "main",
			exclude: ["jquery"]
		}
	]
});