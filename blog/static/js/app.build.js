({
	appDir: "../",
	baseUrl: "static/js",
	dir: "static/js",
	//Comment out the optimize line if you want
	//the code minified by UglifyJS.
	optimize: "none",

	paths: {},

	modules: [
		{
			name: "main",
			exclude: ["jquery"]
		}
	]
});