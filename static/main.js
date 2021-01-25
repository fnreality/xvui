var xv_form_inputs = [
    "xv-form-erosion",
    "xv-form-dilation"
].map(document.getElementById);
var xv_form_elem = document.getElementById("xv-form-elem");

const update_oninput_handler = mk_update_oninput_handler(
    xv_form_elem
);
xv_form_inputs.forEach(update_oninput_handler);
