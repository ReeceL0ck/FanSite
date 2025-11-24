function openModal() {
    document.getElementById('modal').classList.add('active');
}

function closeModal() {
    document.getElementById('modal').classList.remove('active');
}

function closeModalOnOverlay(event) {
    if (event.target.id === 'modal') {
        closeModal();
    }
}