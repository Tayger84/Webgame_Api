document.querySelectorAll('.drop-area').forEach((dropArea, index) => {
    const fileInput = dropArea.querySelector('input[type="file"]');

    // Změna vzhledu při přetažení
    dropArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropArea.classList.add('dragover');
    });

    dropArea.addEventListener('dragleave', () => {
        dropArea.classList.remove('dragover');
    });

    dropArea.addEventListener('drop', (e) => {
        e.preventDefault();
        dropArea.classList.remove('dragover');

        if (e.dataTransfer.files.length > 0) {
            fileInput.files = e.dataTransfer.files;
        }
    });

    dropArea.addEventListener('click', () => {
        fileInput.click();
    });
});

