frappe.provide('posnext.PointOfSale');
(function() {
	console.log("HERERE")
    var scriptPath = '/assets/posnext/js/pos_controller.js';
    var scriptUrl = scriptPath + '?v=' + Date.now();

    var script = document.createElement('script');
    script.src = scriptUrl;

    document.head.appendChild(script);
})();
frappe.pages['posnext'].on_page_load = function(wrapper) {
	frappe.ui.make_app_page({
		parent: wrapper,
		title: __('Point of Sale'),
		single_column: true
	});
		window.wrapper = wrapper
		wrapper.pos = new posnext.PointOfSale.Controller(wrapper);
		window.cur_pos = wrapper.pos;
}
frappe.pages['posnext'].refresh = function(wrapper,onscan = "",value="") {
	// if (document.scannerDetectionData) {
		if(!onscan){
			window.onScan.detachFrom(document)
		}
		wrapper.pos.wrapper.html("");
		wrapper.pos.check_opening_entry(value);
	// }
};