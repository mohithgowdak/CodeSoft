function appendToScreen(value) {
    document.getElementById('screen').innerText += value;
  }
  
  function calculate() {
    let result = eval(document.getElementById('screen').innerText);
    document.getElementById('screen').innerText = result;
  }
  
  function clearScreen() {
    document.getElementById('screen').innerText = '';
  }
  