function mk_update_oninput_handler(form_elem) {
    return function(input_elem) {
        input_elem.oninput = function() {
            handle_input_update(form_elem);
            return undefined;
        };
        return undefined;
    };
}

function function_name(form_elem) {
    form_elem.submit();
    return undefined;
}
