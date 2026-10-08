// Additions to the stock mdBook theme. Loaded through additional-js in book.toml.
// 1. Line numbers in every code block.
// 2. A thin reading-progress bar for the whole book, weighted by chapter length.
// 3. A link to the list of all books, when the book is served by the hub (under /<class>/).
(function () {
    'use strict';

    // ---- 1. line numbers ---------------------------------------------------
    function addLineNumbers() {
        document.querySelectorAll('main pre > code').forEach(function (code) {
            const pre = code.parentElement;
            if (pre.classList.contains('has-ln') || pre.classList.contains('mermaid')) {
                return;
            }
            const text = code.textContent.replace(/\n$/, '');
            const count = text.split('\n').length;
            const gutter = document.createElement('span');
            gutter.className = 'ln-gutter';
            gutter.setAttribute('aria-hidden', 'true');
            let numbers = '';
            for (let i = 1; i <= count; i++) {
                numbers += (i > 1 ? '\n' : '') + i;
            }
            gutter.textContent = numbers;
            const cs = getComputedStyle(code);
            gutter.style.paddingTop = cs.paddingTop;
            gutter.style.paddingBottom = cs.paddingBottom;
            gutter.style.fontSize = cs.fontSize;
            gutter.style.lineHeight = cs.lineHeight;
            pre.style.setProperty('--ln-width', String(count).length + 'ch');
            pre.classList.add('has-ln');
            pre.insertBefore(gutter, code);
        });
    }

    // ---- 2. reading progress -------------------------------------------------
    function chapterList() {
        const root = new URL(typeof path_to_root === 'string' && path_to_root ? path_to_root : './',
            document.location.href).href;
        const seen = new Set();
        const pages = [];
        document.querySelectorAll('mdbook-sidebar-scrollbox a[href], #mdbook-sidebar a[href], #sidebar a[href]')
            .forEach(function (a) {
                const url = a.href.split('#')[0].split('?')[0];
                if (!url.startsWith(root) || seen.has(url)) {
                    return;
                }
                seen.add(url);
                pages.push({ url: url, key: url.slice(root.length) });
            });
        return pages;
    }

    function setupProgress() {
        if (/\/print\.html$/.test(document.location.pathname)) {
            return;
        }
        const pages = chapterList();
        if (!pages.length) {
            return;
        }
        const weights = window.JEGYZET_WEIGHTS || {};
        let total = 0;
        pages.forEach(function (p) {
            p.weight = weights[p.key] > 0 ? weights[p.key] : (weights.__default || 1);
            total += p.weight;
        });
        let here = document.location.href.split('#')[0].split('?')[0];
        let index = pages.findIndex(function (p) { return p.url === here; });
        if (index < 0) {
            index = 0;                       // index.html is a copy of the first chapter
        }
        let before = 0;
        for (let i = 0; i < index; i++) {
            before += pages[i].weight;
        }

        const bar = document.createElement('div');
        bar.id = 'jz-progress';
        bar.setAttribute('role', 'progressbar');
        bar.setAttribute('aria-valuemin', '0');
        bar.setAttribute('aria-valuemax', '100');
        const fill = document.createElement('div');
        fill.className = 'jz-fill';
        const label = document.createElement('div');
        label.className = 'jz-label';
        bar.appendChild(fill);
        bar.appendChild(label);
        document.body.appendChild(bar);

        function update() {
            const el = document.scrollingElement || document.documentElement;
            const room = el.scrollHeight - el.clientHeight;
            const frac = room > 4 ? Math.min(1, Math.max(0, el.scrollTop / room)) : 1;
            const pct = 100 * (before + frac * pages[index].weight) / total;
            fill.style.width = pct.toFixed(2) + '%';
            const shown = Math.round(pct);
            bar.setAttribute('aria-valuenow', String(shown));
            label.textContent = shown + '% · ' + (index + 1) + ' / ' + pages.length;
        }

        let hideTimer = null;
        function open() {
            bar.classList.add('jz-open');
            if (hideTimer) {
                clearTimeout(hideTimer);
            }
            hideTimer = setTimeout(function () { bar.classList.remove('jz-open'); }, 1800);
        }
        // Open when the pointer is near the top edge. In fullscreen the browser may
        // cover the top pixels with its own toolbar, so a wider zone is used.
        document.addEventListener('mousemove', function (e) {
            if (e.clientY <= 44) {
                open();
            }
        }, { passive: true });
        document.addEventListener('mouseleave', open);
        let ticking = false;
        function onScroll() {
            if (!ticking) {
                ticking = true;
                requestAnimationFrame(function () { ticking = false; update(); });
            }
        }
        window.addEventListener('scroll', onScroll, { passive: true });
        window.addEventListener('resize', onScroll, { passive: true });
        window.addEventListener('load', update);
        update();
    }

    // ---- 3. back to the hub ------------------------------------------------------
    function addHomeLink() {
        if (!/^https?:$/.test(document.location.protocol)) {
            return;
        }
        const root = new URL(typeof path_to_root === 'string' && path_to_root ? path_to_root : './',
            document.location.href).pathname;
        const buttons = document.querySelector('.right-buttons');
        if (root === '/' || !buttons) {
            return;                          // served on its own (mdbook serve): no hub above it
        }
        const a = document.createElement('a');
        a.href = '/';
        a.title = 'Minden jegyzet';
        a.setAttribute('aria-label', 'Minden jegyzet');
        a.innerHTML = '<span class="fa-svg" id="jz-home-button"><svg xmlns="http://www.w3.org/2000/svg" ' +
            'viewBox="0 0 576 512"><path d="M575.8 255.5c0 18-15 32.1-32 32.1h-32l.7 160.2c0 2.7-.2 5.4-.5 ' +
            '8.1V472c0 22.1-17.9 40-40 40H456c-1.1 0-2.2 0-3.3-.1c-1.4 .1-2.8 .1-4.2 .1H416 392c-22.1 0-40-17.9-40-40V448 ' +
            '384c0-17.7-14.3-32-32-32H256c-17.7 0-32 14.3-32 32v64 24c0 22.1-17.9 40-40 40H160 128.1c-1.5 0-3-.1-4.5-.2' +
            'c-1.2 .1-2.4 .2-3.6 .2H104c-22.1 0-40-17.9-40-40V360c0-.9 0-1.9 .1-2.8V287.6H32c-18 0-32-14-32-32.1c0-9 3-17 ' +
            '10-24L266.4 8c7-7 15-8 22-8s15 2 21 7L564.8 231.5c8 7 12 15 11 24z"/></svg></span>';
        buttons.insertBefore(a, buttons.firstChild);
    }

    function init() {
        addLineNumbers();
        setupProgress();
        addHomeLink();
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
