/* ============================================================
   main.js — site behaviour
   ============================================================ */
(function () {
  "use strict";

  /* ---------- language ---------- */
  const LANG_KEY = "scz-lang";
  const urlLang = new URLSearchParams(location.search).get("lang");
  let lang = (urlLang === "ru" || urlLang === "en") ? urlLang
           : (localStorage.getItem(LANG_KEY) || "ru");
  localStorage.setItem(LANG_KEY, lang);
  document.documentElement.setAttribute("data-lang", lang);

  const t = (obj) => (obj && (obj[lang] ?? obj.ru)) || "";

  function setLang(next) {
    lang = next;
    localStorage.setItem(LANG_KEY, lang);
    document.documentElement.setAttribute("data-lang", lang);
    document.querySelectorAll(".lang-toggle button").forEach((b) =>
      b.classList.toggle("active", b.dataset.lang === lang)
    );
    // re-render dynamic project content
    if (document.getElementById("projects-grid")) renderProjects(currentFilter);
    if (document.getElementById("featured-grid")) renderFeatured();
  }

  /* ---------- header / footer injection ---------- */
  const PAGES = [
    { href: "index.html",    ru: "Главная",   en: "Home" },
    { href: "projects.html", ru: "Проекты",   en: "Projects" },
    { href: "about.html",    ru: "Обо мне",   en: "About" },
    { href: "contact.html",  ru: "Контакты",  en: "Contact" },
  ];
  const current = (location.pathname.split("/").pop() || "index.html") || "index.html";

  const ICON = {
    github:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.7.5.5 5.7.5 12c0 5.1 3.3 9.4 7.9 10.9.6.1.8-.2.8-.5v-1.7c-3.2.7-3.9-1.6-3.9-1.6-.5-1.3-1.3-1.7-1.3-1.7-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.7 1.3 3.4 1 .1-.8.4-1.3.7-1.6-2.6-.3-5.3-1.3-5.3-5.8 0-1.3.5-2.3 1.2-3.1-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.3 1.2a11.4 11.4 0 0 1 6 0C17.3 4.7 18.3 5 18.3 5c.6 1.6.2 2.8.1 3.1.8.8 1.2 1.8 1.2 3.1 0 4.5-2.7 5.5-5.3 5.8.4.4.8 1.1.8 2.2v3.3c0 .3.2.6.8.5 4.6-1.5 7.9-5.8 7.9-10.9C23.5 5.7 18.3.5 12 .5z"/></svg>',
    tg:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 3 2.5 10.5c-1 .4-1 1.6 0 1.9l4.9 1.5 1.9 5.9c.2.7 1.1.9 1.6.3l2.7-2.7 5 3.7c.6.4 1.4.1 1.6-.6L23.9 4.4C24.2 3.5 23 2.6 22 3zM9.6 14l8.3-5.2c.2-.1.4.2.2.4l-6.8 6.2c-.2.2-.4.5-.4.8l-.2 2.5-1.1-4.7z"/></svg>',
    mail:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    phone:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
    globe:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>',
    play:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>',
    drive:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="m7.7 3 8.6 0 4.3 7.5-4.3 7.5H7.7L3.4 10.5z" opacity=".4"/><path d="M8 3 2 13.5 5 19l6-10.5zm8 0H8l6 10.5h7.9zM5 19h12l-3-5H8z"/></svg>',
  };
  const LINKS = {
    github:"https://github.com/sergeychaliy2",
    tg:"https://t.me/russianew_s",
    mail:"mailto:sergeyviarovich@gmail.com",
    phone:"tel:+79062025578",
    tilda:"https://sergeyviarovich.tilda.ws",
    drive:"https://drive.google.com/drive/folders/1we5Rgr66OS8UHZUIFe4M9D8ugUueJ47v",
    press:"https://www.mediaoffice.abudhabi/en/education/rabdan-academy-integrates-virtual-reality-technologies-into-academic-programmes/"
  };

  function buildHeader() {
    const el = document.getElementById("site-header");
    if (!el) return;
    const links = PAGES.map(
      (p) =>
        `<a href="${p.href}" class="${p.href === current ? "active" : ""}"><span class="lang-ru">${p.ru}</span><span class="lang-en">${p.en}</span></a>`
    ).join("");
    el.className = "site-header";
    el.innerHTML = `
      <div class="wrap">
        <nav class="nav">
          <a class="brand" href="index.html"><span class="mark">SC</span>Sergey&nbsp;Chaliy</a>
          <div class="nav-links" id="nav-links">${links}</div>
          <div class="nav-tools">
            <div class="lang-toggle">
              <button data-lang="ru" class="${lang === "ru" ? "active" : ""}">RU</button>
              <button data-lang="en" class="${lang === "en" ? "active" : ""}">EN</button>
            </div>
            <a class="btn-cta" href="contact.html"><span class="lang-ru">Связаться</span><span class="lang-en">Get in touch</span></a>
            <button class="nav-burger" id="nav-burger" aria-label="Menu"><span></span><span></span><span></span></button>
          </div>
        </nav>
      </div>`;

    el.querySelectorAll(".lang-toggle button").forEach((b) =>
      b.addEventListener("click", () => setLang(b.dataset.lang))
    );
    const burger = document.getElementById("nav-burger");
    const navLinks = document.getElementById("nav-links");
    burger.addEventListener("click", () => navLinks.classList.toggle("open"));
    navLinks.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => navLinks.classList.remove("open"))
    );

    const onScroll = () => el.classList.toggle("scrolled", window.scrollY > 24);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  function buildFooter() {
    const el = document.getElementById("site-footer");
    if (!el) return;
    el.className = "site-footer";
    el.innerHTML = `
      <div class="wrap">
        <div class="footer-grid">
          <div class="footer-brand">
            <a class="brand" href="index.html"><span class="mark">SC</span>Sergey&nbsp;Chaliy</a>
            <p><span class="lang-ru">Senior Unity-разработчик — VR / AR / MR и кроссплатформенные приложения. Архитектура → реализация → CI/CD → релиз → поддержка.</span><span class="lang-en">Senior Unity developer — VR / AR / MR and cross-platform apps. Architecture → implementation → CI/CD → release → support.</span></p>
          </div>
          <div class="footer-cols">
            <div class="footer-col">
              <h4><span class="lang-ru">Навигация</span><span class="lang-en">Navigation</span></h4>
              ${PAGES.map((p) => `<a href="${p.href}"><span class="lang-ru">${p.ru}</span><span class="lang-en">${p.en}</span></a>`).join("")}
            </div>
            <div class="footer-col">
              <h4><span class="lang-ru">Ссылки</span><span class="lang-en">Links</span></h4>
              <a href="${LINKS.github}" target="_blank" rel="noopener">GitHub</a>
              <a href="${LINKS.drive}" target="_blank" rel="noopener">Google Drive</a>
              <a href="${LINKS.tilda}" target="_blank" rel="noopener">Tilda Portfolio</a>
              <a href="${LINKS.press}" target="_blank" rel="noopener"><span class="lang-ru">В прессе (Abu Dhabi)</span><span class="lang-en">Press (Abu Dhabi)</span></a>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <span>© <span id="yr"></span> Sergey Chaliy. <span class="lang-ru">Все права защищены.</span><span class="lang-en">All rights reserved.</span></span>
          <div class="socials">
            <a href="${LINKS.github}" target="_blank" rel="noopener" aria-label="GitHub">${ICON.github}</a>
            <a href="${LINKS.tg}" target="_blank" rel="noopener" aria-label="Telegram">${ICON.tg}</a>
            <a href="${LINKS.mail}" aria-label="Email">${ICON.mail}</a>
            <a href="${LINKS.drive}" target="_blank" rel="noopener" aria-label="Drive">${ICON.drive}</a>
          </div>
        </div>
      </div>`;
    const yr = document.getElementById("yr");
    if (yr) yr.textContent = String(new Date().getFullYear());
  }

  /* ---------- projects ---------- */
  let currentFilter = "all";

  function cardHTML(p, idx) {
    const cover = p.img[0];
    const ytBadge = p.yt
      ? `<span class="badge-yt">${ICON.play}<span style="width:14px;height:14px;display:none"></span>DEMO</span>`
      : "";
    const playOverlay = `<div class="play"><span>${ICON.play}</span></div>`;
    return `
      <article class="project-card" data-reveal data-delay="${(idx % 3) + 1}" data-idx="${p._i}">
        <div class="project-media">
          <img src="${cover}" alt="${t(p.title)}" loading="lazy">
          ${ytBadge}${playOverlay}
        </div>
        <div class="project-body">
          <span class="project-cat">${catName(p.cat)}</span>
          <h3>${t(p.title)}</h3>
          <p>${t(p.desc)}</p>
          <div class="tags">${p.tags.map((x) => `<span class="tag">${x}</span>`).join("")}</div>
        </div>
      </article>`;
  }

  function catName(id) {
    const c = CATEGORIES.find((c) => c.id === id);
    return c ? t(c) : "";
  }

  function renderProjects(filter) {
    currentFilter = filter;
    const grid = document.getElementById("projects-grid");
    if (!grid) return;
    const list = PROJECTS.filter((p) => filter === "all" || p.cat === filter);
    grid.innerHTML = list.length
      ? list.map((p, i) => cardHTML(p, i)).join("")
      : `<p style="color:var(--muted)">${t(UI.noResults)}</p>`;
    wireCards(grid);
    observeReveal(grid);
  }

  function renderFeatured() {
    const grid = document.getElementById("featured-grid");
    if (!grid) return;
    const list = PROJECTS.filter((p) => p.featured).slice(0, 6);
    grid.innerHTML = list.map((p, i) => cardHTML(p, i)).join("");
    wireCards(grid);
    observeReveal(grid);
  }

  function wireCards(scope) {
    scope.querySelectorAll(".project-card").forEach((card) => {
      card.addEventListener("click", () => openLightbox(+card.dataset.idx));
      attachTilt(card, 6);
    });
  }

  function buildFilters() {
    const bar = document.getElementById("filters");
    if (!bar) return;
    bar.innerHTML = CATEGORIES.map(
      (c) => `<button class="filter-btn ${c.id === "all" ? "active" : ""}" data-cat="${c.id}">${t(c)}</button>`
    ).join("");
    bar.querySelectorAll(".filter-btn").forEach((b) =>
      b.addEventListener("click", () => {
        bar.querySelectorAll(".filter-btn").forEach((x) => x.classList.remove("active"));
        b.classList.add("active");
        renderProjects(b.dataset.cat);
      })
    );
  }

  /* ---------- lightbox ---------- */
  function buildLightbox() {
    if (document.getElementById("lightbox")) return;
    const lb = document.createElement("div");
    lb.id = "lightbox";
    lb.className = "lightbox";
    lb.innerHTML = `
      <button class="lb-close" id="lb-close" aria-label="Close">×</button>
      <div class="lb-inner"><div class="lb-card glass">
        <div class="lb-media" id="lb-media"></div>
        <div class="lb-body">
          <span class="project-cat" id="lb-cat"></span>
          <h3 id="lb-title"></h3>
          <p id="lb-desc"></p>
          <div class="tags" id="lb-tags"></div>
          <div class="lb-thumbs" id="lb-thumbs"></div>
          <div style="margin-top:18px" id="lb-actions"></div>
        </div>
      </div></div>`;
    document.body.appendChild(lb);
    lb.addEventListener("click", (e) => { if (e.target === lb) closeLightbox(); });
    document.getElementById("lb-close").addEventListener("click", closeLightbox);
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeLightbox(); });
  }

  function openLightbox(i) {
    buildLightbox();
    const p = PROJECTS[i];
    if (!p) return;
    document.getElementById("lb-cat").textContent = catName(p.cat);
    document.getElementById("lb-title").textContent = t(p.title);
    document.getElementById("lb-desc").textContent = t(p.desc);
    document.getElementById("lb-tags").innerHTML = p.tags.map((x) => `<span class="tag">${x}</span>`).join("");

    const media = document.getElementById("lb-media");
    const showImg = (src) => { media.innerHTML = `<img src="${src}" alt="${t(p.title)}">`; };
    if (p.yt) media.innerHTML = `<iframe src="https://www.youtube.com/embed/${p.yt}?rel=0" title="${t(p.title)}" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe>`;
    else showImg(p.img[0]);

    const thumbs = document.getElementById("lb-thumbs");
    const localImgs = p.img.filter((s) => s.indexOf("http") !== 0);
    thumbs.innerHTML = localImgs.length > 1 || p.yt
      ? localImgs.map((s, k) => `<img src="${s}" class="${!p.yt && k === 0 ? "active" : ""}" data-src="${s}">`).join("")
      : "";
    thumbs.querySelectorAll("img").forEach((im) =>
      im.addEventListener("click", () => {
        showImg(im.dataset.src);
        thumbs.querySelectorAll("img").forEach((x) => x.classList.remove("active"));
        im.classList.add("active");
      })
    );

    const actions = document.getElementById("lb-actions");
    actions.innerHTML = p.yt
      ? `<a class="btn btn-primary" href="https://youtu.be/${p.yt}" target="_blank" rel="noopener">${ICON.play}${t(UI.watchDemo)}</a>`
      : "";

    document.getElementById("lightbox").classList.add("open");
    document.body.style.overflow = "hidden";
  }

  function closeLightbox() {
    const lb = document.getElementById("lightbox");
    if (!lb) return;
    lb.classList.remove("open");
    document.getElementById("lb-media").innerHTML = ""; // stop video
    document.body.style.overflow = "";
  }

  /* ---------- index PROJECTS to keep stable refs ---------- */
  PROJECTS.forEach((p, i) => (p._i = i));

  /* ---------- 3D tilt ---------- */
  function attachTilt(el, max) {
    if (matchMedia("(hover:none)").matches) return;
    let raf;
    el.addEventListener("mousemove", (e) => {
      const r = el.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - 0.5;
      const py = (e.clientY - r.top) / r.height - 0.5;
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        el.style.transform = `perspective(900px) rotateY(${px * max}deg) rotateX(${-py * max}deg) translateY(-6px)`;
      });
    });
    el.addEventListener("mouseleave", () => {
      cancelAnimationFrame(raf);
      el.style.transform = "";
    });
  }

  /* ---------- hero canvas (particle constellation) ---------- */
  function heroCanvas() {
    const cv = document.getElementById("hero-canvas");
    if (!cv || matchMedia("(prefers-reduced-motion:reduce)").matches) return;
    const ctx = cv.getContext("2d");
    let w, h, pts, dpr;
    const COUNT = window.innerWidth < 700 ? 34 : 72;

    function resize() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      w = cv.clientWidth; h = cv.clientHeight;
      cv.width = w * dpr; cv.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    function seed() {
      pts = Array.from({ length: COUNT }, () => ({
        x: Math.random() * w, y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.35, vy: (Math.random() - 0.5) * 0.35,
      }));
    }
    function tick() {
      ctx.clearRect(0, 0, w, h);
      for (const p of pts) {
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0 || p.x > w) p.vx *= -1;
        if (p.y < 0 || p.y > h) p.vy *= -1;
      }
      for (let i = 0; i < pts.length; i++) {
        for (let j = i + 1; j < pts.length; j++) {
          const dx = pts[i].x - pts[j].x, dy = pts[i].y - pts[j].y;
          const d = Math.hypot(dx, dy);
          if (d < 130) {
            ctx.strokeStyle = `rgba(120,160,255,${(1 - d / 130) * 0.32})`;
            ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(pts[i].x, pts[i].y); ctx.lineTo(pts[j].x, pts[j].y); ctx.stroke();
          }
        }
      }
      for (const p of pts) {
        ctx.fillStyle = "rgba(150,190,255,.8)";
        ctx.beginPath(); ctx.arc(p.x, p.y, 1.6, 0, Math.PI * 2); ctx.fill();
      }
      requestAnimationFrame(tick);
    }
    resize(); seed(); tick();
    window.addEventListener("resize", () => { resize(); seed(); });
  }

  /* ---------- reveal on scroll ---------- */
  let io;
  function observeReveal(scope) {
    if (!("IntersectionObserver" in window)) {
      (scope || document).querySelectorAll("[data-reveal]").forEach((e) => e.classList.add("in"));
      return;
    }
    if (!io) {
      io = new IntersectionObserver((entries) => {
        entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
      }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    }
    (scope || document).querySelectorAll("[data-reveal]:not(.in)").forEach((e) => io.observe(e));
  }

  /* ---------- counters ---------- */
  function counters() {
    const els = document.querySelectorAll("[data-count]");
    if (!els.length) return;
    const run = (el) => {
      const to = parseFloat(el.dataset.count);
      const dur = 1400; const start = performance.now();
      const pre = el.dataset.pre || ""; const suf = el.dataset.suf || "";
      const step = (now) => {
        const k = Math.min((now - start) / dur, 1);
        const e = 1 - Math.pow(1 - k, 3);
        el.textContent = pre + Math.round(to * e) + suf;
        if (k < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    const o = new IntersectionObserver((ents) => {
      ents.forEach((en) => { if (en.isIntersecting) { run(en.target); o.unobserve(en.target); } });
    }, { threshold: 0.5 });
    els.forEach((e) => o.observe(e));
  }

  /* ---------- init ---------- */
  function init() {
    buildHeader();
    buildFooter();
    buildFilters();
    renderFeatured();
    if (document.getElementById("projects-grid")) renderProjects("all");
    document.querySelectorAll(".hero-visual .tilt-stack").forEach((s) => attachTilt(s, 8));
    heroCanvas();
    counters();
    observeReveal(document);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
