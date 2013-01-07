define(["jquery"], function ($) {

	'use strict';
	/**
	 * @constructor Filter
	 * @param {object} DataSource object containing datasource name
	 * and filter config options
	 */
	var Filter = function (cfg) {
		var that = this;
		that.init();
		that.cfg = cfg || {};
		that.dataSource = cfg.dataSource || {}; // dataSource object from cfg object if it exists
		that.callback = cfg.onComplete || []; // callback array from cfg object if it exists
		that.hasCallback = that.callback.length ? true : false; //bolean value if callback array exists
	};

	Filter.prototype = {

		init: function () {
			var that = this;
			that.cacheElements();
			that.bindEvents();
		},

		/**
		 * Bind DOM elements input & a.close to 
		 *      filter & reset functions respectively
		 */
		cacheElements: function () {
			var that = this;
			that.document = $(document);
			that.container = that.document.find('#example');
			that.container.find('a.close').hide();
		},

		/**
		 * Bind DOM elements input & a.close to 
		 *      filter & reset functions respectively
		 */
		bindEvents: function () {
			var that = this,
				container = that.container;

			container.on('keyup', 'input', that.filter.bind(this));
			container.on('click', 'a.close', that.reset.bind(this));
		},

		/**
		 * Filter 1 datasource or more if callback exists
		 * @param {object} e jQuery event object
		 */
		filter: function (e) {
			var that = this,
				target = e.target || e.srcElement,
				dataSource = target.id.replace('Filter', 'DataSource'),
				hasCallback = that.hasCallback;

			that.filterString = target.value.trim();

			if (that.dataSource === dataSource) {
				that[that.filterString.length ? 'show' : 'hide'](target);
				that.performFilter();

				if (hasCallback) {
					that.onComplete();
				}
			}
		},

		/**
		 * process dataSources filter object to pass in filter String 
		 * @param {object} o callback object
		 */
		performFilter: function (o) {
			var that = this,
				filterString = that.filterString,
				filterCfg = o !== undefined ? o.options : that.cfg.options,
				dataSource = window[o !== undefined ? o.dataSource : that.cfg.dataSource],
				i,
				len;

			for (i = 0, len = filterCfg.filters.length; i < len; i += 1) {

				if (filterCfg.filters[i].operator === "eq") {
					filterCfg.filters[i].value = Number(filterString);
				} else {
					filterCfg.filters[i].value = filterString;
				}

			}

			dataSource.filter(filterCfg);
			dataSource.page(1);
		},

		/**
		 * Reset datasource(s)
		 * to default/original state
		 * @param {object} e jQuery event object
		 */
		reset: function (e) {

			var that = this,
				target = e.target || e.srcElement,
				inputElem = $(target).prev(),
				dataSource = inputElem.prop('id').replace('Filter', 'DataSource'),
				hasCallback = that.hasCallback;

			if (that.dataSource === dataSource) {

				inputElem[0].value = "";
				that.filterString = "";
				that.performFilter();

				that.hide(target);

				if (hasCallback) {
					that.onComplete();
				}
			}
		},

		/**
		 * Hide close icon
		 * @param {Element} e DOM element,
		 *      textfield containing filter string.
		 */
		hide: function (e) {
			var self = $(e).hasClass('close') ? $(e) : $(e).next('.close');
			self.hide();
		},

		/**
		 * Show close icon
		 * @param {Element} e DOM element,
		 *      textfield containing filter string.
		 */
		show: function (e) {
			var self = $(e).next('.close');
			self.show();
		},

		/**
		 * Callback funtion if there is a function
		 */
		onComplete: function () {
			var that = this,
				callback = that.callback,
				i,
				len,
				obj,
				elem;

			for (i = 0, len = callback.length; i < len; i += 1) {
				obj = callback[i];
				elem = obj.dataSource.replace('DataSource', 'Filter');

				$('#' + elem)
					.prop('disabled', that.filterString.length)
					.val("")
					.next('a.close')
					.hide();

				that.performFilter(obj);
			}

		}

	};

	return Filter;

});