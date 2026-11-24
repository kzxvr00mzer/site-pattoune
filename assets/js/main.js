/* Pattoune chez soi — animations et interactions (sans dépendance) */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.remove("no-js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* En-tête + barre de progression */
  var header = document.querySelector(".header");
  var bar = document.querySelector(".progress");
  var parallax = [].slice.call(document.querySelectorAll("[data-parallax]"));
  var ticking = false;
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("is-scrolled", y > 20);
    if (bar) {
      var h = doc.scrollHeight - window.innerHeight;
      bar.style.transform = "scaleX(" + (h > 0 ? y / h : 0) + ")";
    }
    if (!reduce) {
      parallax.forEach(function (el) {
        var speed = parseFloat(el.getAttribute("data-parallax")) || 0.2;
        var r = el.parentElement.getBoundingClientRect();
        el.style.transform = "translate3d(0," + (r.top * -speed).toFixed(1) + "px,0)";
      });
    }
    ticking = false;
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  onScroll();

  /* Menu mobile */
  var burger = document.querySelector(".burger");
  var nav = document.getElementById("nav");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
      document.body.style.overflow = open ? "" : "hidden";
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        burger.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
        document.body.style.overflow = "";
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) burger.click();
    });
  }

  /* Apparitions au scroll (avec décalage automatique dans un groupe) */
  document.querySelectorAll("[data-stagger]").forEach(function (group) {
    [].slice.call(group.children).forEach(function (child, i) {
      child.classList.add("reveal");
      child.style.setProperty("--d", (i * 0.1).toFixed(2) + "s");
    });
  });
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* Compteurs animés */
  var counters = document.querySelectorAll("[data-count]");
  function runCounter(el) {
    var end = parseFloat(el.getAttribute("data-count"));
    var dec = (el.getAttribute("data-count").split(".")[1] || "").length;
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduce) { el.textContent = end.toFixed(dec).replace(".", ",") + suffix; return; }
    var start = null;
    function step(t) {
      if (!start) start = t;
      var p = Math.min((t - start) / 1600, 1);
      var v = end * (1 - Math.pow(1 - p, 3));
      el.textContent = v.toFixed(dec).replace(".", ",") + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { runCounter(en.target); co.unobserve(en.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { co.observe(el); });
  } else {
    counters.forEach(runCounter);
  }

  /* Onglets accessibles (tarifs par distance) */
  document.querySelectorAll("[role='tablist']").forEach(function (list) {
    var tabs = [].slice.call(list.querySelectorAll("[role='tab']"));
    function select(tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
      });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(t); });
      t.addEventListener("keydown", function (e) {
        var n = null;
        if (e.key === "ArrowRight") n = tabs[(i + 1) % tabs.length];
        if (e.key === "ArrowLeft") n = tabs[(i - 1 + tabs.length) % tabs.length];
        if (n) { e.preventDefault(); select(n); n.focus(); }
      });
    });
  });

  /* Effet d'inclinaison au survol */
  var fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  if (fine && !reduce) {
    document.querySelectorAll("[data-tilt]").forEach(function (el) {
      el.addEventListener("mousemove", function (e) {
        var r = el.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = "perspective(900px) rotateY(" + (x * 8).toFixed(2) + "deg) rotateX(" + (-y * 8).toFixed(2) + "deg) translateY(-8px)";
      });
      el.addEventListener("mouseleave", function () { el.style.transform = ""; });
    });

    /* Boutons « magnétiques » */
    document.querySelectorAll(".btn").forEach(function (b) {
      b.addEventListener("mousemove", function (e) {
        var r = b.getBoundingClientRect();
        var x = e.clientX - r.left - r.width / 2;
        var y = e.clientY - r.top - r.height / 2;
        b.style.transform = "translate(" + (x * 0.15).toFixed(1) + "px," + (y * 0.25 - 3).toFixed(1) + "px)";
      });
      b.addEventListener("mouseleave", function () { b.style.transform = ""; });
    });

    /* Petites traces de pattes qui suivent la souris dans le héros */
    var hero = document.querySelector(".hero");
    var last = 0, flip = false;
    if (hero) {
      hero.addEventListener("mousemove", function (e) {
        var now = performance.now();
        if (now - last < 140) return;
        last = now; flip = !flip;
        var p = document.createElement("span");
        p.className = "paw-dot";
        p.innerHTML = '<svg viewBox="0 0 24 24" fill="currentColor"><use href="#paw"/></svg>';
        p.style.left = (e.clientX - 10 + (flip ? 8 : -8)) + "px";
        p.style.top = (e.clientY - 10) + "px";
        document.body.appendChild(p);
        setTimeout(function () { p.remove(); }, 1100);
      });
    }
  }

  /* Formulaire de demande : prépare un e-mail ou un SMS (site statique, sans serveur) */
  var form = document.getElementById("devis");
  if (form) {
    function body() {
      var f = new FormData(form), lines = [];
      f.forEach(function (v, k) {
        if (!v || k === "canal") return;
        if (/^\d{4}-\d{2}-\d{2}$/.test(v)) v = v.split("-").reverse().join("/");
        lines.push(k + " : " + v);
      });
      return lines.join("\n");
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var canal = (e.submitter && e.submitter.value) || "mail";
      var txt = "Bonjour Alicia,\n\nJe souhaite une garde pour mon animal :\n\n" + body() + "\n\nMerci !";
      if (canal === "sms") {
        location.href = "sms:+33626323167?&body=" + encodeURIComponent(txt);
      } else {
        location.href = "mailto:pattounechezsoi@gmail.com?subject=" + encodeURIComponent("Demande de garde - Pattoune chez soi") + "&body=" + encodeURIComponent(txt);
      }
    });
  }

  /* Calendrier : pas de date passée, fin après le début */
  var d1 = document.getElementById("f-debut"), d2 = document.getElementById("f-fin");
  if (d1 && d2) {
    var now = new Date(), iso = new Date(now.getTime() - now.getTimezoneOffset() * 60000).toISOString().slice(0, 10);
    d1.min = iso; d2.min = iso;
    [d1, d2].forEach(function (el) {
      el.addEventListener("click", function () { if (el.showPicker) { try { el.showPicker(); } catch (e) {} } });
    });
    d1.addEventListener("change", function () {
      d2.min = d1.value || iso;
      if (d2.value && d2.value < d1.value) d2.value = d1.value;
      if (d1.value && !d2.value && d2.showPicker) { try { d2.showPicker(); } catch (e) {} }
    });
  }

  /* Année du pied de page */
  var yr = document.getElementById("year");
  if (yr) yr.textContent = new Date().getFullYear();
})();

/* Menu : surligne la section visible (page unique) */
(function () {
  var links = [].slice.call(document.querySelectorAll('.nav a[href^="#"]:not(.btn)'));
  if (!links.length || !("IntersectionObserver" in window)) return;
  var map = {};
  links.forEach(function (a) { var s = document.querySelector(a.getAttribute("href")); if (s) map[s.id] = a; });
  var spy = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      links.forEach(function (a) { a.removeAttribute("aria-current"); });
      if (map[en.target.id]) map[en.target.id].setAttribute("aria-current", "true");
    });
  }, { rootMargin: "-45% 0px -50% 0px" });
  document.querySelectorAll("main > section[id]").forEach(function (s) { spy.observe(s); });
})();

/* Galerie des Pattounes gardées : apparition, « voir plus » et visionneuse */
(function () {
  var list = document.getElementById("gallery");
  if (!list) return;
  var items = [].slice.call(list.querySelectorAll(".g-item"));
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var io = ("IntersectionObserver" in window && !reduce) ? new IntersectionObserver(function (en) {
    en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -30px 0px", threshold: 0.1 }) : null;
  function watch(el) { if (io) io.observe(el); else el.classList.add("is-in"); }
  items.forEach(function (el) { if (!el.hidden) watch(el); });

  var more = document.getElementById("gallery-more");
  if (more) more.addEventListener("click", function () {
    var open = more.getAttribute("aria-expanded") === "true";
    if (!open) {
      items.forEach(function (el) { if (el.hidden) { el.hidden = false; watch(el); } });
      more.setAttribute("aria-expanded", "true");
      more.textContent = "Afficher moins de photos";
    } else {
      items.forEach(function (el, i) { if (i >= 18) { el.hidden = true; el.classList.remove("is-in"); } });
      more.setAttribute("aria-expanded", "false");
      more.textContent = "Voir toutes les photos";
      list.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    }
  });

  var dlg = document.getElementById("lightbox");
  if (!dlg || typeof dlg.showModal !== "function") return;
  var img = dlg.querySelector(".lb-img"), cap = dlg.querySelector(".lb-count");
  var btns = [].slice.call(list.querySelectorAll(".g-btn")), cur = 0, opener = null;
  function visible() { return btns.filter(function (b) { return !b.parentElement.hidden; }); }
  function show(i) {
    var v = visible(); cur = (i + v.length) % v.length;
    var src = v[cur].querySelector("img");
    img.style.animation = "none"; void img.offsetWidth; img.style.animation = "";
    img.src = src.currentSrc || src.src; img.alt = src.alt;
    cap.textContent = (cur + 1) + " / " + v.length;
  }
  list.addEventListener("click", function (e) {
    var b = e.target.closest(".g-btn"); if (!b) return;
    opener = b; show(visible().indexOf(b)); dlg.showModal(); document.body.style.overflow = "hidden";
  });
  dlg.querySelector(".lb-prev").addEventListener("click", function () { show(cur - 1); });
  dlg.querySelector(".lb-next").addEventListener("click", function () { show(cur + 1); });
  dlg.querySelector(".lb-close").addEventListener("click", function () { dlg.close(); });
  dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  dlg.addEventListener("close", function () { document.body.style.overflow = ""; if (opener) opener.focus(); });
  dlg.addEventListener("keydown", function (e) {
    if (e.key === "ArrowRight") { e.preventDefault(); show(cur + 1); }
    if (e.key === "ArrowLeft") { e.preventDefault(); show(cur - 1); }
  });
  var x0 = null;
  dlg.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  dlg.addEventListener("touchend", function (e) {
    if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
    if (Math.abs(dx) > 40) show(cur + (dx < 0 ? 1 : -1));
  });
})();
