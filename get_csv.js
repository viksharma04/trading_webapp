window.addEventListener('load', function () {
    const file = 'sample.csv'; // Replace 'filename.csv' with the actual file name
  
    fetch(file)
      .then(response => response.text())
      .then(contents => {
        const lines = contents.split('\n');
  
        for (let i = 0; i < lines.length; i++) {
          const values = lines[i].split(',');
          const number = parseFloat(values[0]);
  
          const numberElement = document.createElement('p');
          numberElement.textContent = number;
  
          const numbersContainer = document.getElementById('numbers-container');
          numbersContainer.appendChild(numberElement);
        }
      })
      .catch(error => {
        console.error('Error reading the file:', error);
      });
  });
  
  