// Slidebar
function openSidebar() {
    document.getElementById('sidebar').style.right = '0';
    document.getElementById('overlay').classList.remove('hidden');
}

function closeSidebar() {
    document.getElementById('sidebar').style.right = '-300px';
    document.getElementById('overlay').classList.add('hidden');
}