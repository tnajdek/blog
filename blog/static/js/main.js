require.config({
	paths: {
		"jquery": "libs/require-jquery",
		"bootstrap": "libs/bootstrap.min",
		"handlebars": "libs/handlebars"
	},
	shim: {
	// 'bootstrap': ['jquery']
	}
});

require(["jquery", "bootstrap"], function ($) {
	"use strict";
});