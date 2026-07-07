//Mobile Menu Script -
document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("menu-btn");
    const menu = document.getElementById("mobile-menu");

    btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
        btn.textContent = menu.classList.contains("hidden") ? "☰" : "✕";
    });
});

// Onclick View client image
function openImage(imageUrl) {
    document.getElementById('modalImage').src = imageUrl;
    document.getElementById('imageModal').classList.remove('hidden');
    document.getElementById('imageModal').classList.add('flex');
}

function closeImage() {
    document.getElementById('imageModal').classList.add('hidden');
    document.getElementById('imageModal').classList.remove('flex');
}


// Onclick View admin image
function openImage1(imageUrl) {
    const modal = document.getElementById("imageModal");
    const image = document.getElementById("modalImage");

    image.src = imageUrl;
    modal.classList.remove("hidden");
    modal.classList.add("flex");
}

function closeImage1() {
    const modal = document.getElementById("imageModal");

    modal.classList.remove("flex");
    modal.classList.add("hidden");
}

document.getElementById("imageModal").addEventListener("click", function (e) {
    if (e.target === this) {
        closeImage1();
    }
});

// Language changing
function googleTranslateElementInit() {
    new google.translate.TranslateElement({ pageLanguage: 'en' }, 'google_translate_element');
}