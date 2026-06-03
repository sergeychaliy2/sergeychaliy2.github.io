# Sergey Chaliy — Portfolio

Личный сайт-портфолио Unity / XR разработчика. Статический сайт (HTML/CSS/JS, без сборщиков), готов к бесплатному хостингу на **GitHub Pages**.

- **Языки:** RU / EN (переключатель в шапке, выбор запоминается)
- **Стиль:** премиум тёмная тема, 3D-эффекты, анимации
- **Страницы:** `index.html` (главная) · `projects.html` (проекты + фильтры + лайтбокс) · `about.html` (опыт, навыки) · `contact.html` (контакты)

## Структура

```
WebSite/
├─ index.html, projects.html, about.html, contact.html, 404.html
├─ .nojekyll                     # отключает обработку Jekyll на GitHub Pages
├─ assets/
│  ├─ css/style.css              # вся вёрстка и анимации
│  ├─ js/data.js                 # данные проектов + строки RU/EN  ← редактировать здесь
│  ├─ js/main.js                 # логика (меню, язык, лайтбокс, частицы)
│  └─ img/
│     ├─ favicon.svg
│     └─ projects/p01.jpg … p45.jpg
```

## Локальный просмотр

Просто откройте `index.html` в браузере (двойной клик). Всё работает без сервера.
Либо запустите локальный сервер для «чистых» путей:

```powershell
# из папки WebSite
python -m http.server 8080
# затем откройте http://localhost:8080
```

## Публикация на GitHub Pages (бесплатно, без домена)

> Username на GitHub: **sergeychaliy2** → итоговый адрес будет **https://sergeychaliy2.github.io**

### Вариант A — персональный сайт (рекомендуется)

1. Создайте на GitHub репозиторий с именем **`sergeychaliy2.github.io`** (Public).
2. В этой папке выполните:

   ```powershell
   git init
   git add .
   git commit -m "Portfolio website"
   git branch -M main
   git remote add origin https://github.com/sergeychaliy2/sergeychaliy2.github.io.git
   git push -u origin main
   ```

3. GitHub → репозиторий → **Settings → Pages** → Source: **Deploy from a branch**, ветка **main**, папка **/(root)** → Save.
4. Через 1–2 минуты сайт будет доступен по адресу **https://sergeychaliy2.github.io**

### Вариант B — обычный репозиторий (адрес с подпапкой)

Если назвать репозиторий иначе (например `portfolio`), адрес будет
`https://sergeychaliy2.github.io/portfolio/`. Шаги те же, только меняется имя репозитория в `git remote add`.

## Свой домен (опционально)

Купив домен, добавьте файл `CNAME` со строкой `ваш-домен.com` и пропишите DNS-записи по [инструкции GitHub Pages](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site). Это не обязательно — адрес `*.github.io` бесплатный и постоянный.

## Как редактировать контент

- **Проекты:** `assets/js/data.js` — массив `PROJECTS`. У каждого: `title`, `desc` ({ru, en}), `img` (массив путей), `cat` (категория для фильтра), `tags`, опционально `yt` (id видео YouTube) и `featured: true` (показывать на главной).
- **Тексты страниц:** прямо в `.html` — два варианта в `<span class="lang-ru">…</span><span class="lang-en">…</span>`.
- **Контакты / ссылки:** объект `LINKS` в начале `assets/js/main.js` (плюс продублированы в `contact.html`).
- **Картинки:** кладите в `assets/img/projects/` и указывайте путь в `data.js`. Желательно сжимать (JPEG, ширина ≤ 1600px).

## Лицензия

Контент и изображения © Sergey Chaliy.
