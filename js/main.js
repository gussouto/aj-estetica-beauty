/* AJ Estética Beauty — scripts */
(function () {
  'use strict';

  var WA_NUMBER = '5534912345678'; // +55 34 91234-5678 (trocar pelo número real)
  var root = document.documentElement;


  /* ---------- transição suave ao trocar de página ---------- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
    if (a.target === '_blank' || a.hasAttribute('download')) return;
    var href = a.getAttribute('href');
    if (!href || href.charAt(0) === '#' || /^(mailto:|tel:|https?:|javascript:)/i.test(href)) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    e.preventDefault();
    document.body.classList.add('is-leaving');
    setTimeout(function () { window.location.href = a.href; }, 220);
  });
  window.addEventListener('pageshow', function () { document.body.classList.remove('is-leaving'); });

  /* ---------- tema claro / escuro ---------- */
  var themeBtn = document.querySelector('.theme-toggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem('aj-theme', next); } catch (e) {}
    });
  }

  /* ---------- menu mobile e submenu ---------- */
  var menuBtn = document.querySelector('.menu-toggle');
  var nav = document.getElementById('nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', open);
      menuBtn.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    });
  }
  var subToggle = document.querySelector('.sub-toggle');
  if (subToggle) {
    subToggle.addEventListener('click', function () {
      var li = subToggle.parentElement;
      var open = li.classList.toggle('open');
      subToggle.setAttribute('aria-expanded', open);
    });
    document.addEventListener('click', function (e) {
      if (!subToggle.parentElement.contains(e.target)) {
        subToggle.parentElement.classList.remove('open');
        subToggle.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        subToggle.parentElement.classList.remove('open');
        subToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---------- galeria antes e depois: pausar / retomar ---------- */
  var marquee = document.querySelector('.marquee');
  var pauseBtn = document.querySelector('[data-marquee-toggle]');
  if (marquee && pauseBtn) {
    pauseBtn.addEventListener('click', function () {
      var paused = marquee.classList.toggle('is-paused');
      pauseBtn.textContent = paused ? 'Retomar movimento' : 'Pausar movimento';
      pauseBtn.setAttribute('aria-pressed', paused);
    });
  }

  /* ---------- lightbox do estúdio ---------- */
  var box = document.getElementById('lightbox');
  if (box) {
    var boxImg = box.querySelector('img');
    document.querySelectorAll('.studio__item').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var img = btn.querySelector('img');
        if (!img) return; // sem foto ainda: nada para ampliar
        boxImg.src = img.currentSrc || img.src;
        boxImg.alt = img.alt;
        box.showModal();
      });
    });
    box.addEventListener('click', function (e) { if (e.target === box) box.close(); });
    box.querySelector('button').addEventListener('click', function () { box.close(); });
  }

  /* ---------- formulário de contato → WhatsApp ---------- */
  var form = document.getElementById('contact-form');
  if (form) {
    var msg = document.getElementById('form-msg');
    var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

    function setError(input, text) {
      var err = input.parentElement.querySelector('.err');
      input.setAttribute('aria-invalid', text ? 'true' : 'false');
      if (err) err.textContent = text || '';
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var nome = form.elements.nome, email = form.elements.email;
      var ok = true;

      if (!nome.value.trim()) { setError(nome, 'Informe seu nome.'); ok = false; } else setError(nome, '');
      if (!email.value.trim()) { setError(email, 'Informe seu e-mail.'); ok = false; }
      else if (!emailRe.test(email.value.trim())) { setError(email, 'Esse e-mail parece incompleto. Exemplo: nome@email.com'); ok = false; }
      else setError(email, '');

      if (!ok) {
        form.querySelector('[aria-invalid="true"]').focus();
        return;
      }

      var linhas = [
        'Olá, Dra. Ana Júlia! Vim pelo site e gostaria de agendar uma avaliação.',
        '',
        'Nome: ' + nome.value.trim(),
        'E-mail: ' + email.value.trim()
      ];
      if (form.elements.telefone.value.trim()) linhas.push('Telefone: ' + form.elements.telefone.value.trim());
      if (form.elements.tratamento.value) linhas.push('Tratamento de interesse: ' + form.elements.tratamento.value);
      if (form.elements.mensagem.value.trim()) linhas.push('', form.elements.mensagem.value.trim());

      var url = 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(linhas.join('\n'));
      msg.textContent = 'Pronto! Abrimos o WhatsApp com os seus dados já preenchidos. É só tocar em enviar.';
      msg.classList.add('show');
      window.open(url, '_blank', 'noopener');
      form.reset();
    });
  }
})();
