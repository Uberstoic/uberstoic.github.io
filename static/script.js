document.addEventListener('DOMContentLoaded', () => {
    const noteButton = document.getElementById('noteButton');
    const noteModal = document.getElementById('noteModal');
    const closeModal = document.getElementsByClassName('close')[0];
    const saveNoteButton = document.getElementById('saveNoteButton');
    const notesList = document.getElementById('notesList');
    const noteInput = document.getElementById('noteInput');

    // Открытие модального окна
    noteButton.addEventListener('click', () => {
        noteModal.style.display = 'block';
    });

    // Закрытие модального окна
    closeModal.addEventListener('click', () => {
        noteModal.style.display = 'none';
    });

    // Закрытие модального окна при клике вне окна
    window.addEventListener('click', (event) => {
        if (event.target === noteModal) {
            noteModal.style.display = 'none';
        }
    });

    // Сохранение заметки
    saveNoteButton.addEventListener('click', () => {
        const noteText = noteInput.value.trim();
        if (noteText) {
            const noteItem = document.createElement('li');
            noteItem.textContent = noteText;
            notesList.appendChild(noteItem);
            noteInput.value = '';
            noteModal.style.display = 'none';
        }
    });
});
