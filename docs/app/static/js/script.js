document.addEventListener('DOMContentLoaded', async function() {
    // Загружаем данные предприятия
    const response = await fetch('/api/data');
    const data = await response.json();
    console.log("Данные предприятия:", data);
    
    // Создаем кнопки-ссылки
    const linksContainer = document.getElementById('links-container');
    if (data.links && data.links.length > 0) {
        data.links.forEach(link => {
            const linkElement = document.createElement('a');
            linkElement.href = link.url;
            linkElement.target = "_blank";
            linkElement.className = "bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-6 rounded-lg flex items-center justify-center transition-colors";
            linkElement.innerHTML = `<i class="fas fa-${link.icon} mr-2"></i> ${link.name}`;
            linksContainer.appendChild(linkElement);
        });
    }
});

// Функция переключения темы
function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    
    // Сохраняем выбор темы в localStorage
    const isDark = document.body.classList.contains('dark-theme');
    localStorage.setItem('darkTheme', isDark);
}

// Проверяем сохранённую тему при загрузке
window.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('darkTheme') === 'true';
    if (savedTheme) {
        document.body.classList.add('dark-theme');
    }
});