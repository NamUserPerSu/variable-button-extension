define([
    'base/js/namespace',
    'jquery',
    'base/js/utils',
    'base/js/dialog'
],  function(Jupyter, $, utils, dialog) {
    alert("Hello, i am an alert box :-D");
})
    function place_button() {
    if (!Jupyter.toolbar) {
        $([Jupyter.events]).on("app_initialized.NotebookApp", place_button);
        return;
    }
    Jupyter.toolbar.add_buttons_group([{
        label: 'Variable Button',
        icon: 'fa-car',
        callback: get_variable_req
    }])
    }

    function get_pizza_req() {
    console.log("Sending get req for variable")
    var variableUrl = utils.url_path_join(utils.get_body_data('baseUrl'), 'variable_me')
    console.log("Variable url: ", variableUrl)
    $.getJSON(variableUrl, function(data) {
        console.log("Data: ", data)
        dialog.modal(data)
    })
    }