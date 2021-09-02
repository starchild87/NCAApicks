PROCESS_URL = "/process";

var ta = document.getElementById("textarea");
ta.onpaste = handlePaste;

function handlePaste(event) {
	let pastedText = (event.clipboardData || window.clipboardData).getData('text');
 	//alert('Pasted!\n' + pastedText);
    let form = document.createElement('form');
    form.action = PROCESS_URL;
    form.method = 'POST';
    form.innerHTML = '<input name="lines" value="' + pastedText + '">';
    document.body.append(form);
    form.submit();
}