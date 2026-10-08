// Additions to the stock mdBook theme. Loaded through additional-js in book.toml.
// 1. Line numbers in every code block.
// 2. A thin reading-progress bar for the whole book, weighted by chapter length.
// 3. A link to the list of all books, when the book is served by the hub (under /<class>/).
// 4. Chapter changes without a page reload.
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
            if (count > 99) {                // two digits are reserved by notes.css
                pre.style.setProperty('--ln-width', String(count).length + 'ch');
            }
            pre.classList.add('has-ln');
            pre.insertBefore(gutter, code);
        });
    }

    // ---- 2. reading progress -------------------------------------------------
    let relocateProgress = function () {};   // set by setupProgress; called after a chapter swap

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
        const weights = window.NOTES_WEIGHTS || {};
        let total = 0;
        pages.forEach(function (p) {
            p.weight = weights[p.key] > 0 ? weights[p.key] : (weights.__default || 1);
            total += p.weight;
        });
        let index, before;
        function locate() {
            const here = document.location.href.split('#')[0].split('?')[0];
            index = pages.findIndex(function (p) { return p.url === here; });
            if (index < 0) {
                index = 0;                   // index.html is a copy of the first chapter
            }
            before = 0;
            for (let i = 0; i < index; i++) {
                before += pages[i].weight;
            }
        }
        locate();

        const bar = document.createElement('div');
        bar.id = 'notes-progress';
        bar.setAttribute('role', 'progressbar');
        bar.setAttribute('aria-valuemin', '0');
        bar.setAttribute('aria-valuemax', '100');
        const fill = document.createElement('div');
        fill.className = 'notes-fill';
        const label = document.createElement('div');
        label.className = 'notes-label';
        bar.appendChild(fill);
        bar.appendChild(label);

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
            bar.classList.add('notes-open');
            if (hideTimer) {
                clearTimeout(hideTimer);
            }
            hideTimer = setTimeout(function () { bar.classList.remove('notes-open'); }, 1800);
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
        // Start at this page's position; animate only later changes, not the jump from 0 on every page.
        update();
        relocateProgress = function () { locate(); update(); };
        document.body.appendChild(bar);
        requestAnimationFrame(function () {
            requestAnimationFrame(function () { bar.classList.add('notes-ready'); });
        });
    }

    // ---- 3. back to the hub ------------------------------------------------------
    function addHomeLink() {
        if (!/^https?:$/.test(document.location.protocol)) {
            return;
        }
        const root = new URL(typeof path_to_root === 'string' && path_to_root ? path_to_root : './',
            document.location.href);
        const buttons = document.querySelector('.right-buttons');
        if (root.pathname === '/' || !buttons) {
            return;                          // served on its own (mdbook serve): no hub above it
        }
        const a = document.createElement('a');
        a.href = new URL('../', root).href;  // the hub sits one level above the book, under any prefix
        a.title = 'All notes';
        a.setAttribute('aria-label', 'All notes');
        a.innerHTML = '<span class="fa-svg" id="notes-home-button"><svg xmlns="http://www.w3.org/2000/svg" ' +
            'viewBox="0 0 576 512"><path d="M575.8 255.5c0 18-15 32.1-32 32.1h-32l.7 160.2c0 2.7-.2 5.4-.5 ' +
            '8.1V472c0 22.1-17.9 40-40 40H456c-1.1 0-2.2 0-3.3-.1c-1.4 .1-2.8 .1-4.2 .1H416 392c-22.1 0-40-17.9-40-40V448 ' +
            '384c0-17.7-14.3-32-32-32H256c-17.7 0-32 14.3-32 32v64 24c0 22.1-17.9 40-40 40H160 128.1c-1.5 0-3-.1-4.5-.2' +
            'c-1.2 .1-2.4 .2-3.6 .2H104c-22.1 0-40-17.9-40-40V360c0-.9 0-1.9 .1-2.8V287.6H32c-18 0-32-14-32-32.1c0-9 3-17 ' +
            '10-24L266.4 8c7-7 15-8 22-8s15 2 21 7L564.8 231.5c8 7 12 15 11 24z"/></svg></span>';
        buttons.insertBefore(a, buttons.firstChild);
    }

    // ---- 4. chapter changes without a page reload -------------------------------
    // The Navigation API reports every navigation: links, mdBook's arrow keys, back and forward. For another
    // chapter of this book only the content is fetched and swapped in; the sidebar, menu bar and search keep
    // their state and the browser restores scroll and focus. Browsers without the API load pages normally.
    const pageCache = new Map();             // prefetched on hover, used once: a rebuilt book never shows old pages
    function fetchPage(url) {
        let page = pageCache.get(url);
        if (!page) {
            page = fetch(url).then(function (r) {
                if (!r.ok) {
                    throw new Error(url + ': ' + r.status);
                }
                return r.text();
            });
            page.catch(function () { pageCache.delete(url); });
            pageCache.set(url, page);
        }
        return page;
    }

    function markActiveChapter(root) {
        const scrollbox = document.querySelector('mdbook-sidebar-scrollbox');
        if (!scrollbox) {
            return;
        }
        scrollbox.querySelectorAll('.on-this-page').forEach(function (el) { el.remove(); });
        scrollbox.querySelectorAll('a.active').forEach(function (a) { a.classList.remove('active'); });
        let here = document.location.href.split('#')[0].split('?')[0];
        if (here.endsWith('/')) {
            here += 'index.html';
        }
        const links = Array.from(scrollbox.querySelectorAll('a[href]'));
        const strip = function (u) { return u.replace(/\.html$/, ''); };
        const link = links.find(function (a) { return strip(a.href) === strip(here); })
            || (here === root + 'index.html' ? links[0] : null);
        if (!link) {
            return;
        }
        link.classList.add('active');
        for (let li = link.closest('li.chapter-item'); li; li = li.parentElement.closest('li.chapter-item')) {
            li.classList.add('expanded');
        }
        // toc.js builds the "on this page" headings of the active chapter on DOMContentLoaded
        document.dispatchEvent(new Event('DOMContentLoaded'));
        // scrollIntoView would also move the page, which the browser has just restored
        const box = scrollbox.getBoundingClientRect();
        const at = link.getBoundingClientRect();
        if (at.top < box.top || at.bottom > box.bottom) {
            scrollbox.scrollTop += at.top - box.top - box.height / 2;
        }
    }

    // What book.js and the other scripts did to the content on page load.
    function prepareContent() {
        document.querySelectorAll('main code').forEach(function (code) {
            if (!code.parentElement.classList.contains('header')) {
                code.classList.add('hljs');
            }
        });
        if (window.playground_copyable) {
            document.querySelectorAll('main pre > code').forEach(function (code) {
                const pre = code.parentElement;
                let buttons = pre.querySelector('.buttons');
                if (!buttons) {
                    buttons = document.createElement('div');
                    buttons.className = 'buttons';
                    pre.insertBefore(buttons, pre.firstChild);
                }
                const clip = document.createElement('button');
                clip.className = 'clip-button';
                clip.title = 'Copy to clipboard';
                clip.setAttribute('aria-label', clip.title);
                clip.innerHTML = '<i class="tooltiptext"></i>';
                buttons.insertBefore(clip, buttons.firstChild);
            });
        }
        addLineNumbers();
        if (window.mermaid && document.querySelector('main .mermaid')) {
            window.mermaid.run({ querySelector: 'main .mermaid' });
        }
    }

    function setupNavigation() {
        if (!window.navigation || !/^https?:$/.test(document.location.protocol)) {
            return;
        }
        const root = new URL(typeof path_to_root === 'string' && path_to_root ? path_to_root : './',
            document.location.href).href;
        // mdBook resolves these against path_to_root, which stays the one of the first page loaded:
        // make them absolute while it is still right.
        const base = document.location.href;
        document.querySelectorAll('#mdbook-sidebar a[href]:not([href^="#"]), #mdbook-menu-bar a[href]')
            .forEach(function (a) { a.href = a.href; });
        if (window.path_to_searchindex_js) {
            window.path_to_searchindex_js = new URL(window.path_to_searchindex_js, base).href;
        }
        const results = document.getElementById('mdbook-searchresults');
        if (results) {
            new MutationObserver(function () {
                results.querySelectorAll('a[href]').forEach(function (a) {
                    a.href = new URL(a.getAttribute('href'), base).href;
                });
            }).observe(results, { childList: true });
        }

        function isChapter(url) {
            return url.href.startsWith(root) && /(\.html|\/)$/.test(url.pathname)
                && !/\/(print|toc)\.html$/.test(url.pathname);
        }
        // Start loading a chapter as soon as the pointer is over its link.
        document.addEventListener('pointerover', function (e) {
            const a = e.target.closest && e.target.closest('a[href]');
            if (a) {
                const url = new URL(a.href);
                if (isChapter(url) && !url.search && url.pathname !== document.location.pathname) {
                    fetchPage(url.origin + url.pathname);
                }
            }
        }, { passive: true });

        window.navigation.addEventListener('navigate', function (e) {
            const url = new URL(e.destination.url);
            if (!e.canIntercept || e.hashChange || e.downloadRequest !== null || e.formData
                || e.navigationType === 'reload' || !isChapter(url)) {
                return;
            }
            // pushState of the search box; links from search results (?highlight=) load normally to mark the words
            if (e.navigationType === 'traverse' ? url.pathname === document.location.pathname
                : e.destination.sameDocument || url.search) {
                return;
            }
            e.intercept({
                scroll: 'manual',
                handler: async function () {
                    let doc = null;
                    const key = url.origin + url.pathname;
                    try {
                        const text = await fetchPage(key);
                        pageCache.delete(key);
                        doc = new DOMParser().parseFromString(text, 'text/html');
                    } catch (err) {
                        console.warn(err);
                    }
                    if (e.signal.aborted) {
                        return;
                    }
                    const content = doc && doc.getElementById('mdbook-content');
                    const wide = doc && doc.querySelector('.nav-wide-wrapper');
                    if (!content || !wide) {
                        document.location.reload();      // the URL is already the new one
                        return;
                    }
                    // Firefox restores the scroll position of back/forward before the swap; scroll anchoring
                    // would then shift it when the old content goes
                    const html = document.documentElement;
                    html.style.overflowAnchor = 'none';
                    document.title = doc.title;
                    document.getElementById('mdbook-content').replaceWith(content);
                    document.querySelector('.nav-wide-wrapper').replaceWith(wide);
                    try {
                        sessionStorage.removeItem('sidebar-scroll-offset');   // toc.js reads it on the next full load
                    } catch (err) { /* storage blocked */ }
                    markActiveChapter(root);
                    prepareContent();
                    relocateProgress();
                    // on narrow screens the sidebar covers the page; a full load would have closed it
                    const toggle = document.getElementById('mdbook-sidebar-toggle-anchor');
                    if (toggle && toggle.checked && document.body.clientWidth < 1080) {
                        toggle.checked = false;
                        toggle.dispatchEvent(new Event('change'));
                    }
                    try {
                        e.scroll();                  // once the content has its final height
                    } finally {
                        html.style.overflowAnchor = '';
                    }
                },
            });
        });
    }

    function init() {
        addLineNumbers();
        setupProgress();
        addHomeLink();
        setupNavigation();
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init, { once: true });   // markActiveChapter fires it again
    } else {
        init();
    }
})();
