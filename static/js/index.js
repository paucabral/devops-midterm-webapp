// JavaScript
function check_pass() {
    if (document.getElementById('inputPassword').value ==
      document.getElementById('inputPassword2').value) {
      document.getElementById('submit').disabled = false;
    } else {
      document.getElementById('submit').disabled = true;
    }
  }