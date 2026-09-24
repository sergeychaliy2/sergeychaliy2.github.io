/* ============================================================
   Project & UI data  (RU / EN)
   img paths relative to site root (assets/img/projects/pNN.jpg)
   yt = YouTube id (optional)  ·  cat = filter category
   featured = show on the home page
   ============================================================ */

const IMG = "assets/img/projects/";
const ytThumb = (id) => `https://i.ytimg.com/vi/${id}/hqdefault.jpg`;

const CATEGORIES = [
  { id:"all",      ru:"Все",                 en:"All" },
  { id:"training", ru:"VR/AR тренажёры",      en:"VR/AR Training" },
  { id:"twin",     ru:"Цифровые двойники",    en:"Digital Twins" },
  { id:"game",     ru:"Игры",                 en:"Games" },
  { id:"ai",       ru:"ИИ / LLM",             en:"AI / LLM" },
  { id:"mobile",   ru:"Мобильные приложения", en:"Mobile Apps" },
  { id:"web",      ru:"Веб / Backend",        en:"Web / Backend" },
  { id:"tools",    ru:"Инструменты / Embedded", en:"Tools & Embedded" },
  { id:"art",      ru:"3D / Окружение",       en:"3D / Environments" },
];

const PROJECTS = [
  /* ---------- TRAINING (UAE / industrial) ---------- */
  {
    cat:"twin", yt:"yCqns8rhgOQ", featured:true,
    img:[IMG+"p21.jpg"],
    title:{ ru:"Dubai Mixed Reality Platform", en:"Dubai Map Mixed Reality Platform" },
    desc:{
      ru:"MR-платформа интерактивной 3D-карты Дубая: голографическая модель города с ключевыми объектами (Burj Khalifa) для презентаций и навигации.",
      en:"Mixed-reality interactive 3D map of Dubai: a holographic city model with landmarks (Burj Khalifa) for presentations and navigation."
    },
    tags:["Unity","MR","HoloLens","Spatial Anchors"]
  },
  {
    cat:"training", yt:"yrK9r7-7B7E", featured:true,
    img:[IMG+"p19.jpg", IMG+"p18.jpg"],
    title:{ ru:"Подготовка спецподразделений", en:"Special Forces Military Training" },
    desc:{
      ru:"VR-тренажёр тактической подготовки для государственного заказчика ОАЭ (национальная учебная академия): отработка штурмовых сценариев в фотореалистичных окружениях.",
      en:"Tactical VR trainer for a UAE government client (a national training academy): assault scenario rehearsal in photoreal environments."
    },
    tags:["Unity","Meta Quest","OpenXR","Multiplayer"]
  },
  {
    cat:"training", yt:"mdwfxaavwzQ",
    img:[IMG+"p24.jpg"],
    title:{ ru:"Тренажёр пожарной автоцистерны", en:"Firefighting Truck Operation Training" },
    desc:{
      ru:"Интерактивное обучение работе с пожарным расчётом и оборудованием автоцистерны: развёртывание, регламенты, командное взаимодействие в VR.",
      en:"Interactive VR training for fire-crew operations and truck equipment: deployment, procedures and team coordination."
    },
    tags:["Unity","VR","Simulation","Procedure"]
  },
  {
    cat:"training", yt:"7mNIN8ij2_g",
    img:[IMG+"p25.jpg"],
    title:{ ru:"Пожарная безопасность", en:"Fire Safety Training" },
    desc:{
      ru:"VR-курс по пожарной безопасности с интерактивным разбором устройства огнетушителя (CO₂) и отработкой действий при возгорании.",
      en:"VR fire-safety course with interactive breakdown of a CO₂ extinguisher and hands-on fire response practice."
    },
    tags:["Unity","VR","Interactive UI","Training"]
  },
  {
    cat:"training", yt:"ClJ7ZI2SgnY",
    img:[IMG+"p30.jpg", IMG+"p31.jpg"],
    title:{ ru:"Промышленный ремонт и диагностика", en:"Industrial Repairing & Troubleshooting" },
    desc:{
      ru:"VR-обучение обслуживанию и сборке трубопроводных узлов: пошаговые инструкции, информационные панели, контроль правильности операций.",
      en:"VR maintenance & assembly trainer for piping units: step-by-step guidance, info panels and correctness validation."
    },
    tags:["Unity","VR","BIM","Guided Tasks"]
  },
  {
    cat:"training", yt:"phO8KVeMJFk",
    img:[IMG+"p33.jpg"],
    title:{ ru:"Промышленная безопасность", en:"Environmental & Industrial Safety" },
    desc:{
      ru:"Тренажёр охраны труда: подбор и проверка средств индивидуальной защиты, безопасные процедуры на промышленном объекте в VR.",
      en:"Occupational-safety trainer: selecting and checking PPE and following safe procedures on an industrial site in VR."
    },
    tags:["Unity","VR","PPE","Safety"]
  },
  {
    cat:"training", yt:"B1iKENFw3_Q",
    img:[ytThumb("B1iKENFw3_Q")],
    title:{ ru:"AI-тренажёр с оценкой действий", en:"AI Training Simulator" },
    desc:{
      ru:"VR-тренажёр с ИИ-оценкой: алгоритмы машинного обучения (MLP, SVM) анализируют действия и движения пользователя и дают рекомендации.",
      en:"VR trainer with AI assessment: ML algorithms (MLP, SVM) analyse the user's actions and movements and provide feedback."
    },
    tags:["Unity","ML","MLP/SVM","VR"]
  },
  {
    cat:"training", yt:"YYXdjZ7qXyw",
    img:[ytThumb("YYXdjZ7qXyw")],
    title:{ ru:"UAE Mars Hope — VR-симуляция", en:"UAE Mars Hope — VR Simulation" },
    desc:{
      ru:"Интерактивная VR-симуляция миссии «Надежда» (UAE Mars Hope) — образовательно-выставочный проект для аудитории ОАЭ.",
      en:"Interactive VR simulation of the UAE Mars Hope mission — an educational / exhibition experience for UAE audiences."
    },
    tags:["Unity","VR","Education","Space"]
  },
  {
    cat:"training",
    img:[IMG+"p42.jpg"],
    title:{ ru:"Симулятор тира и обращения с оружием", en:"Shooting Range & Weapon Handling Simulator" },
    desc:{
      ru:"VR-симулятор тира: стрелковая практика, управление оружием, изучение его устройства, разборка и сборка.",
      en:"VR shooting-range simulator: marksmanship practice, weapon handling and learning weapon structure, disassembly and assembly."
    },
    tags:["Unity","VR","Simulation","Training"]
  },
  {
    cat:"training",
    img:[IMG+"p22.jpg"],
    title:{ ru:"Обучение в академии (VR)", en:"Academy Training (VR)" },
    desc:{
      ru:"VR-платформа для обучения в академии: интерактивные лекции и практические занятия с разбором учебного материала.",
      en:"A VR academy-education platform: interactive lectures and hands-on practice sessions with guided material."
    },
    tags:["Unity","VR","Education","LMS"]
  },
  {
    cat:"training",
    img:[IMG+"p41.jpg"],
    title:{ ru:"VR-шутер для полицейской академии", en:"Police Academy — Tactical Shooter" },
    desc:{
      ru:"Тактический VR-шутер для полицейской академии ОАЭ: отработка действий в нештатных ситуациях, мультиплеер и командное взаимодействие.",
      en:"A tactical VR shooter for the Dubai Police Academy: emergency-situation drills with multiplayer and team coordination."
    },
    tags:["Unity","VR","Multiplayer","Tactical"]
  },

  /* ---------- DIGITAL TWIN ---------- */
  {
    cat:"twin", featured:true,
    img:[IMG+"p04.jpg", IMG+"p32.jpg", IMG+"p44.jpg"],
    title:{ ru:"Цифровой двойник химического завода", en:"Digital Twin — Chemical Plant" },
    desc:{
      ru:"Цифровой двойник химического производства: интеграция BIM-модели и полной технологической логики, облачная синхронизация данных.",
      en:"Digital twin of a chemical production site: BIM-model integration with full process logic and cloud data synchronisation."
    },
    tags:["Unity","BIM","Azure","Digital Twin"]
  },

  /* ---------- GAMES ---------- */
  {
    cat:"game", yt:"_N6lsTr-XqE", featured:true,
    img:[IMG+"p01.jpg"],
    title:{ ru:"Eternal Battle — VR-шутер", en:"Eternal Battle — VR Shooter" },
    desc:{
      ru:"Мультиплеерный VR-шутер: процедурная генерация карт, синхронизация на Photon/Mirror, встроенный редактор уровней и голосовые команды.",
      en:"Multiplayer VR shooter: procedural map generation, Photon/Mirror sync, a built-in level editor and voice commands."
    },
    tags:["Unity","Photon","Mirror","Procedural"]
  },
  {
    cat:"game",
    img:[IMG+"p35.jpg", IMG+"p03.jpg"],
    title:{ ru:"VR Detective — квест", en:"VR Detective — Quest" },
    desc:{
      ru:"Детективный VR-квест: взаимодействие с NPC, поиск и анализ улик, нелинейное прохождение и интерактивное окружение.",
      en:"A detective VR quest: NPC interaction, clue gathering and analysis, non-linear progression and interactive environments."
    },
    tags:["Unity","VR","NPC AI","Narrative"]
  },
  {
    cat:"game",
    img:[IMG+"p09.jpg", IMG+"p45.jpg"],
    title:{ ru:"VR Rhythm & Dance", en:"VR Rhythm & Dance" },
    desc:{
      ru:"Ритм-игра в стиле Beat Saber с кастомными аудиотреками и танцевальным режимом — корпоративная интеграция и развлекательный контур.",
      en:"A Beat Saber-style rhythm game with custom audio tracks and a dance mode — corporate integration and entertainment."
    },
    tags:["Unity","VR","Audio","Gameplay"]
  },
  {
    cat:"game",
    img:[IMG+"p27.jpg"],
    title:{ ru:"VR Cooking", en:"VR Cooking" },
    desc:{
      ru:"VR-игра-симулятор кухни: физика взаимодействия с предметами, приготовление блюд и аркадная механика на время.",
      en:"A VR kitchen simulator: physics-based object interaction, cooking mechanics and timed arcade gameplay."
    },
    tags:["Unity","VR","Physics","Hand Tracking"]
  },
  {
    cat:"game",
    img:[IMG+"p34.jpg"],
    title:{ ru:"Maze Run — VR", en:"Maze Run — VR" },
    desc:{
      ru:"Атмосферный VR-лабиринт с нарративом: процедурные коридоры, головоломки и динамическое освещение.",
      en:"An atmospheric narrative VR maze: procedural corridors, puzzles and dynamic lighting."
    },
    tags:["Unity","VR","Puzzle","Lighting"]
  },
  {
    cat:"game",
    img:[IMG+"p28.jpg"],
    title:{ ru:"Симулятор вождения", en:"Professional Driving Simulator" },
    desc:{
      ru:"Симулятор профессионального вождения: подключение рулевых контроллеров, кастомная физика автомобиля и реалистичные трассы.",
      en:"Professional driving simulator: steering-wheel controller support, custom vehicle physics and realistic tracks."
    },
    tags:["Unity","Physics","Hardware","Simulation"]
  },
  {
    cat:"game",
    img:[IMG+"p26.jpg"],
    title:{ ru:"Sky Gardens (VK Play)", en:"Sky Gardens (VK Play)" },
    desc:{
      ru:"Игровой проект, опубликованный в VK Play: стилизованный low-poly мир, расслабляющий геймплей и развитие острова.",
      en:"A game published on VK Play: a stylised low-poly world, relaxing gameplay and island progression."
    },
    tags:["Unity","Low-poly","VK Play","Gamedev"]
  },
  {
    cat:"game",
    img:[IMG+"p36.jpg"],
    title:{ ru:"Мобильная игра-выживание", en:"Survival Mobile Game" },
    desc:{
      ru:"Мобильная игра в жанре выживания: low-poly острова, строительство, добыча и менеджмент ресурсов.",
      en:"A survival mobile game: low-poly islands, building, gathering and resource management."
    },
    tags:["Unity","Mobile","Survival","Low-poly"]
  },

  /* ---------- AI / LLM ---------- */
  {
    cat:"ai", featured:true,
    img:[IMG+"p08.jpg"],
    title:{ ru:"AI-ассистент с аватаром (LLM)", en:"AI Avatar Assistant (LLM)" },
    desc:{
      ru:"Интерактивный AI-ассистент с фотореалистичным 3D-аватаром и развёртыванием LLM — для корпоративного контура и презентаций.",
      en:"Interactive AI assistant with a photoreal 3D avatar and LLM deployment — for corporate environments and presentations."
    },
    tags:["LLM","Unity","Avatars","Enterprise"]
  },
  {
    cat:"ai",
    img:[IMG+"p23.jpg"],
    title:{ ru:"AI-ассистент-экскурсовод", en:"AI Tour-Guide Assistant" },
    desc:{
      ru:"Виртуальный ассистент-экскурсовод с фотореалистичным 3D-аватаром и LLM: проводит по локации, отвечает на вопросы и сопровождает пользователя.",
      en:"A virtual tour-guide assistant with a photoreal 3D avatar and LLM: walks users through a location, answers questions and accompanies them."
    },
    tags:["LLM","Avatars","Guide","Unity"]
  },
  {
    cat:"ai",
    img:[IMG+"p06.jpg", IMG+"p07.jpg"],
    title:{ ru:"Мобильный AI-ассистент", en:"Mobile AI Assistant" },
    desc:{
      ru:"Мобильное приложение-ассистент: голосовой диалог в реальном времени, видеосвязь и интеграция языковой модели.",
      en:"A mobile assistant app: real-time voice dialogue, video calls and language-model integration."
    },
    tags:["LLM","iOS / Android","Voice","Realtime"]
  },
  {
    cat:"ai", featured:true,
    img:[IMG+"p49.jpg", IMG+"p50.jpg", IMG+"p05.jpg", IMG+"p51.jpg"],
    title:{ ru:"Редактор карточек для маркетплейсов (LLM)", en:"Marketplace Card Editor (LLM)" },
    desc:{
      ru:"Веб-редактор инфографики и карточек товаров со встроенными LLM: генерация и обработка контента, редактирование изображений, автоматическое удаление фона, подбор тематического оформления и экспорт в PNG/JPG/WebP.",
      en:"Web editor for marketplace product cards & infographics with built-in LLMs: content generation and processing, image editing, automatic background removal, themed templates and export to PNG/JPG/WebP."
    },
    tags:["LLM","Image Editing","Background Removal","Web"]
  },
  {
    cat:"ai", featured:true,
    img:[IMG+"p54.jpg"],
    title:{ ru:"PolyBot — торговый бот для бирж (ML)", en:"PolyBot — ML Trading Bot" },
    desc:{
      ru:"Биржевой торговый бот с непрерывным анализом рынка: самообучающиеся ML-модели переобучаются и корректируют себя на исторических и реальных данных, рассчитывают уверенность и сигналы (RSI и др.) и автоматически принимают решения о сделках.",
      en:"An exchange trading bot with continuous market analysis: self-learning ML models retrain and correct themselves on historical and live data, compute confidence and signals (RSI etc.) and make automated trade decisions."
    },
    tags:["Python","Machine Learning","Trading","Analytics"]
  },

  /* ---------- 3D / ENVIRONMENTS ---------- */
  {
    cat:"art", featured:true,
    img:[IMG+"p39.jpg", IMG+"p40.jpg"],
    title:{ ru:"Рюриково городище (Unreal Engine)", en:"Rurikovo Gorodishche (Unreal Engine)" },
    desc:{
      ru:"Реконструкция объекта культурного наследия на Unreal Engine: фотореалистичные окружения, природа, свет и атмосфера.",
      en:"A cultural-heritage reconstruction built in Unreal Engine: photoreal environments, nature, lighting and atmosphere."
    },
    tags:["Unreal Engine","Environment","Heritage","Lumen"]
  },
  {
    cat:"art",
    img:[IMG+"p02.jpg", IMG+"p20.jpg"],
    title:{ ru:"VR-музей Ф. М. Достоевского", en:"VR Museum — Dostoevsky" },
    desc:{
      ru:"Виртуальная реконструкция дома-музея Ф. М. Достоевского: точные интерьеры, предметы эпохи и атмосферное освещение.",
      en:"Virtual reconstruction of the Dostoevsky house-museum: accurate interiors, period objects and atmospheric lighting."
    },
    tags:["Unity","VR","Heritage","URP"]
  },
  {
    cat:"art", yt:"ywP1XHdAXHg",
    img:[IMG+"p43.jpg"],
    title:{ ru:"Детская образовательная платформа", en:"Kids Educational Platform" },
    desc:{
      ru:"Игровая образовательная платформа для детей: стилизованные low-poly миры, интерактивные уроки и геймификация обучения.",
      en:"A gamified educational platform for kids: stylised low-poly worlds, interactive lessons and learning gamification."
    },
    tags:["Unity","Low-poly","Education","Gamedev"]
  },
  {
    cat:"art",
    img:[IMG+"p37.jpg", IMG+"p29.jpg"],
    title:{ ru:"AR / Mixed Reality эксперименты", en:"AR / Mixed Reality Experiments" },
    desc:{
      ru:"AR-проекты с пространственной привязкой: настольные интерактивные сцены, измерения и наложение объектов на реальное окружение.",
      en:"AR projects with spatial anchoring: interactive tabletop scenes, measurement and overlaying objects onto the real world."
    },
    tags:["AR","Vuforia","Spatial Anchors","Mobile"]
  },

  /* ---------- MOBILE ---------- */
  {
    cat:"mobile",
    img:[IMG+"p15.jpg", IMG+"p16.jpg", IMG+"p17.jpg"],
    title:{ ru:"Замер лесоматериалов (AI)", en:"Timber Measurement App (AI)" },
    desc:{
      ru:"Мобильное приложение для автоматического обмера штабелей и лесовозов по фотографии: ИИ-распознавание брёвен, подсчёт и аналитика.",
      en:"Mobile app for automatic measurement of timber stacks and log trucks from a photo: AI log detection, counting and analytics."
    },
    tags:["Android","iOS","Computer Vision","AI"]
  },
  {
    cat:"mobile",
    img:[IMG+"p10.jpg", IMG+"p14.jpg", IMG+"p12.jpg", IMG+"p13.jpg", IMG+"p11.jpg"],
    title:{ ru:"GPS-трекер и навигация", en:"GPS Tracker & Navigation" },
    desc:{
      ru:"Мобильный навигатор-трекер: запись треков, спидометр и компас, пользовательские точки на карте и голосовое сопровождение.",
      en:"A mobile tracker-navigator: track recording, speedometer & compass, custom map markers and voice guidance."
    },
    tags:["Android","iOS","Geolocation","Maps"]
  },
  {
    cat:"mobile", featured:true,
    img:[IMG+"p52.jpg"],
    title:{ ru:"Приложение университета", en:"University App" },
    desc:{
      ru:"Официальное мобильное приложение Новгородского университета для студентов и преподавателей: расписание, оценки, схемы корпусов и навигатор по кампусу, университетские сервисы. Опубликовано в Google Play.",
      en:"Official mobile app of a state university for students and staff: schedule, grades, building maps and a campus navigator, plus university services. Published on Google Play."
    },
    tags:["Android","iOS","University","Navigation"]
  },
  {
    cat:"mobile",
    img:[IMG+"p38.jpg"],
    title:{ ru:"Hyper-casual раннер", en:"Hyper-casual Runner" },
    desc:{
      ru:"Мобильная аркада-раннер с внутриигровыми покупками, подписками и серверной валидацией транзакций (ЮKassa, Firebase Functions).",
      en:"A mobile runner arcade with in-app purchases, subscriptions and server-side transaction validation (YooKassa, Firebase Functions)."
    },
    tags:["Unity","IAP","Firebase","Mobile"]
  },

  /* ---------- WEB / BACKEND ---------- */
  {
    cat:"web", featured:true,
    img:[IMG+"p48.jpg", IMG+"p47.jpg"],
    title:{ ru:"Backend и админ-консоль платформы обучения", en:"Backend & Admin Console — Learning Platform" },
    desc:{
      ru:"Серверная часть и веб-админка для VR-платформы обучения (Immersive Learning): библиотека сценариев, настройка этапов, роли и права, запуск и мониторинг сессий, подключение клиентов к серверу.",
      en:"Backend and web admin panel for a VR learning platform (Immersive Learning): scenario library, stage configuration, roles & permissions, session launch and monitoring, and client-to-server connection."
    },
    tags:["Backend","REST API","Admin Panel","WebSockets"]
  },
  {
    cat:"web",
    img:[IMG+"p46.jpg"],
    title:{ ru:"E-commerce платформа (веб)", en:"E-commerce Platform (web)" },
    desc:{
      ru:"Интернет-магазин: каталог с фильтрами и категориями, карточки товаров, корзина и оформление заказа — разработка фронтенда и серверной части.",
      en:"An online store: a filterable catalog with categories, product cards, cart and checkout — front-end and back-end development."
    },
    tags:["Web","Frontend","Backend","E-commerce"]
  },

  /* ---------- DEV TOOLS ---------- */
  {
    cat:"tools", featured:true,
    img:[IMG+"p53.jpg"],
    title:{ ru:"NexusBuild — кастомный профайлер и сборщик", en:"NexusBuild — Custom Profiler & Build Tool" },
    desc:{
      ru:"Кастомный инструмент для движка: автоматизация сборок и профилирование производительности — дашборд статусов, профили сборки под платформы, метрики (время сборки, размер ассетов, оптимизация) и подробный лог.",
      en:"A custom engine tool for build automation and performance profiling — a status dashboard, per-platform build profiles, metrics (build time, asset size, optimisation) and a detailed log."
    },
    tags:["Unity","Editor Tooling","Profiling","CI/CD"]
  },
  {
    cat:"tools",
    img:[IMG+"p55.jpg"],
    title:{ ru:"Прошивки для автомобилей", en:"Automotive Firmware" },
    desc:{
      ru:"Разработка прошивок для автомобилей: кастомный бортовой интерфейс и навигация на большом сенсорном дисплее, низкоуровневая интеграция с системами автомобиля.",
      en:"Automotive firmware development: a custom in-car interface and navigation on a large touchscreen, with low-level integration into vehicle systems."
    },
    tags:["C / C++","Firmware","Automotive","Embedded"]
  }
];

/* small UI strings rendered from JS */
const UI = {
  watchDemo:   { ru:"Смотреть демо", en:"Watch demo" },
  viewProject: { ru:"Подробнее",     en:"View details" },
  gallery:     { ru:"Галерея",       en:"Gallery" },
  noResults:   { ru:"Нет проектов в этой категории", en:"No projects in this category" },
  featured:    { ru:"Избранные проекты", en:"Featured projects" }
};
