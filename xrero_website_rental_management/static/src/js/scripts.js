/***
*    Copyright (C) 2023-TODAY TechKhedut (<https://www.techkhedut.com>)
*    Part of TechKhedut. See LICENSE file for full copyright and licensing details.
****/
function dummy() {}
function initPropertyWebsite() {
    "use strict";
    $(".loader-wrap").fadeOut(300, function () {
        $("#main").animate({
            opacity: "1"
        }, 600);
    });
    var a = $(".bg");
    a.each(function (a) {
        if ($(this).attr("data-bg")) $(this).css("background-image", "url(" + $(this).data("bg") + ")");
    });
    if ($(".listing-slider").length > 0) {
        var lsw = new Swiper(".listing-slider .swiper-container", {
            preloadImages: false,
            slidesPerView: 4,
            spaceBetween: 15,
            loop: true,

            grabCursor: true,
            mousewheel: false,
            centeredSlides: true,
            pagination: {
                el: '.tc-pagination2',
                clickable: true,
                dynamicBullets: true,
            },
            navigation: {
                nextEl: '.listing-carousel-button-next2',
                prevEl: '.listing-carousel-button-prev2',
            },
            breakpoints: {
                1650: {
                    slidesPerView: 3,
                },
                1270: {
                    slidesPerView: 2,
                },
                850: {
                    slidesPerView: 1,
                },
            }
        });
    }
    if ($(".category-carousel").length > 0) {
        var j2 = new Swiper(".category-carousel .swiper-container", {
            preloadImages: false,
            freeMode: true,
            slidesPerView: 'auto',
            spaceBetween: 10,
            loop: false,
            grabCursor: true,
            mousewheel: true,
            observer: true,
            observeParents: true,
            scrollbar: {
                el: '.hs_init',
                draggable: true,
            },
            navigation: {
                nextEl: '.cc-next',
                prevEl: '.cc-prev',
            },
        });
    }
    if ($(".single-carousel").length > 0) {
        var j2 = new Swiper(".single-carousel .swiper-container", {
            preloadImages: false,
            freeMode: true,
            slidesPerView: 'auto',
            spaceBetween: 10,
            loop: false,
            grabCursor: true,
            mousewheel: false,
            observer: true,
            observeParents: true,
            navigation: {
                nextEl: '.sc-next',
                prevEl: '.sc-prev',
            },
        });
    }
    if ($(".single-slider").length > 0) {
        var j2 = new Swiper(".single-slider .swiper-container", {
            preloadImages: false,
            slidesPerView: 1,
            spaceBetween: 0,
            loop: true,
            autoHeight: true,
            grabCursor: true,
            mousewheel: false,
            pagination: {
                el: '.ss-slider-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.ss-slider-cont-next',
                prevEl: '.ss-slider-cont-prev',
            },
        });
    }
    if ($(".listing-carousel").length > 0) {
        var j3 = new Swiper(".listing-carousel .swiper-container", {
            preloadImages: true,
            loop: true,
            grabCursor: true,
            speed: 1400,
            init: false,
            slidesPerView: 'auto',
            spaceBetween: 0,
            effect: "slide",
            mousewheel: false,
            pagination: {
                el: '.listing-carousel_pagination-wrap',
                clickable: true,
            },
            navigation: {
                nextEl: '.listing-carousel-button-next',
                prevEl: '.listing-carousel-button-prev',
            },
        });
		j3.init();
    }
    if ($(".slider-widget").length > 0) {
        var j4 = new Swiper(".slider-widget .swiper-container", {
            preloadImages: false,
            loop: false,
            grabCursor: true,
            speed: 1400,

            slidesPerView: 1,
            spaceBetween: 10,
            effect: "slide",
            mousewheel: false,
            navigation: {
                nextEl: '.slider-widget-button-next',
                prevEl: '.slider-widget-button-prev',
            },
        });
    }
    if ($(".hero-slider").length > 0) {
        var hs = new Swiper(".hero-slider .swiper-container", {
            preloadImages: false,
            loop: true,
            speed: 1400,
            spaceBetween: 0,
            pagination: {
                el: '.listing-carousel_pagination-wrap',
                clickable: true,
            },

            navigation: {
                nextEl: '.slider-hero-button-next',
                prevEl: '.slider-hero-button-prev',
            },
        });

    }
    if ($(".slideshow-container").length > 0) {
        var ms1 = new Swiper(".slideshow-container .swiper-container", {
            preloadImages: false,
            loop: true,
            speed: 1400,
            spaceBetween: 0,
            effect: "fade",
            autoplay: {
                delay: 3000,
                disableOnInteraction: false
            },
        });
        kpsc();
        ms1.on("slideChangeTransitionStart", function () {
            eqwe();
        });
        ms1.on("slideChangeTransitionEnd", function () {
            kpsc();
        });
    }
    function kpsc() {
        $(".slide-progress").css({
            width: "100%",
            transition: "width 3000ms"
        });
    }
    function eqwe() {
        $(".slide-progress").css({
            width: 0,
            transition: "width 0s"
        });
    };
    if ($(".clients-carousel").length > 0) {
        var j2 = new Swiper(".clients-carousel .swiper-container", {
            preloadImages: false,
            freeMode: false,
            slidesPerView: 5,
            spaceBetween: 10,
            loop: true,
            grabCursor: true,
            mousewheel: false,
            navigation: {
                nextEl: '.cc-next',
                prevEl: '.cc-prev',
            },
            breakpoints: {
                1064: {
                    slidesPerView: 3,
                },
                768: {
                    slidesPerView: 2,
                },
                520: {
                    slidesPerView: 1,
                },
            }
        });
    }
    if ($(".testimonilas-carousel").length > 0) {
        var j2 = new Swiper(".testimonilas-carousel .swiper-container", {
            preloadImages: false,
            slidesPerView: 3,
            spaceBetween: 20,
            loop: true,
            grabCursor: true,
            mousewheel: false,
            centeredSlides: true,
            pagination: {
                el: '.tc-pagination',
                clickable: true,
                dynamicBullets: true,
            },
            navigation: {
                nextEl: '.listing-carousel-button-next',
                prevEl: '.listing-carousel-button-prev',
            },
            breakpoints: {
                1064: {
                    slidesPerView: 2,
                },
                640: {
                    slidesPerView: 1,
                },
            }
        });
    }
    if ($(".dashboard-header-stats").length > 0) {
        var j2 = new Swiper(".dashboard-header-stats .swiper-container", {
            preloadImages: false,
            freeMode: false,
            slidesPerView: 3,
            spaceBetween: 10,
            loop: false,
            grabCursor: true,
            mousewheel: false,

            navigation: {
                nextEl: '.dhs-next',
                prevEl: '.dhs-prev',
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                },
                640: {
                    slidesPerView: 1,
                },
            }
        });
    }
    //   Isotope------------------
    function initIsotope() {
        if ($(".gallery-items").length) {
            var ami = $(".gallery-items").isotope({
                singleMode: true,

                itemSelector: ".gallery-item, .gallery-item-second, .gallery-item-three",
                transformsEnabled: true,
                transitionDuration: "700ms",
                resizable: true
            });
            ami.imagesLoaded(function () {
                ami.isotope("layout");
            });
            $(".gallery-filters").on("click", "a.gallery-filter", function (a) {
                a.preventDefault();
                var brec = $(this).attr("data-filter");
                ami.isotope({
                    filter: brec
                });
                $(".gallery-filters a").removeClass("gallery-filter-active");
                $(this).addClass("gallery-filter-active");
            });
        }
        if ($(".restor-menu-widget").length) {
            var aresm = $(".restor-menu-widget").isotope({
                singleMode: true,
                itemSelector: ".restmenu-item",
                transformsEnabled: true,
                transitionDuration: "700ms",
                resizable: true
            });
            aresm.imagesLoaded(function () {
                aresm.isotope("layout");
            });
            $(".menu-filters").on("click", "a", function (a) {
                a.preventDefault();
                var brec = $(this).attr("data-filter");
                aresm.isotope({
                    filter: brec
                });
                $(".menu-filters a").removeClass("menu-filters-active");
                $(this).addClass("menu-filters-active");
            });
        }
    }
    initIsotope();
    $(".image-popup").lightGallery({
        selector: "this",
        cssEasing: "cubic-bezier(0.25, 0, 0.25, 1)",
        download: false,
        counter: false
    });
    var o = $(".lightgallery"),
        p = o.data("looped");
    o.lightGallery({
        selector: ".lightgallery a.popup-image",
        cssEasing: "cubic-bezier(0.25, 0, 0.25, 1)",
        download: false,
        loop: false,
        counter: false
    });
    function initHiddenGal() {
        $(".dynamic-gal").on('click', function () {
            var dynamicgal = eval($(this).attr("data-dynamicPath"));
            $(this).lightGallery({
                dynamic: true,
                dynamicEl: dynamicgal,
                download: false,
                loop: false,
                counter: false
            });

        });
    }
    initHiddenGal();
    $("<span class='footer-bg-pin'></span>").duplicate(4).prependTo(".footer-bg");
    function heroAnim() {
        function a(a) {
            var b = a.length,
                c, d;
            while (b) {
                d = Math.floor(Math.random() * b--);
                c = a[b];
                a[b] = a[d];
                a[d] = c;
            }
            return a;
        }

        var b = $(".footer-bg-pin");
        $(a(b).slice(0, $(".footer-bg").data("ran"))).each(function (a) {
            var bc = $(this);
            b.removeClass("footer-bg-pin-vis")
            bc.addClass("footer-bg-pin-vis");

        });
    }
    setInterval(function () {
        heroAnim();
    }, 2000);
    $(".lang-action li a").on('click', function (e) {
        e.preventDefault();
        var thdatlantext = $(this).data("lantext");
        $(".lang-action li a").removeClass("current-lan");
        $(this).addClass("current-lan");
        $(".show-lang span strong").text(thdatlantext);
    });
    $(".category-carousel-item").on("click", function (e) {
        e.preventDefault();
        $(this).toggleClass("checket-cat");
    });
    $(".show-more-snopt").on("click", function (e) {
        e.preventDefault();
        $(".show-more-snopt-tooltip").toggleClass("show-more-snopt-tooltip_vis");
    });
    //   appear------------------
    $(".stats").appear(function () {
        $(".num").countTo();
    });
    //   accordion ------------------
    $(".accordion a.toggle").on("click", function (a) {
        a.preventDefault();
        $(".accordion a.toggle").removeClass("act-accordion");
        $(this).addClass("act-accordion");
        if ($(this).next('div.accordion-inner').is(':visible')) {
            $(this).next('div.accordion-inner').slideUp();
        } else {
            $(".accordion a.toggle").next('div.accordion-inner').slideUp();
            $(this).next('div.accordion-inner').slideToggle();
        }
    });
    //   tabs------------------
    $(".tabs-menu a").on("click", function (a) {
        a.preventDefault();
        $(this).parent().addClass("current");
        $(this).parent().siblings().removeClass("current");
        var b = $(this).attr("href");
        $(this).parents(".tabs-act").find(".tab-content").not(b).css("display", "none");
        $(b).fadeIn();
    });
    $(".change_bg a").on("click", function () {
        var bgt = $(this).data("bgtab");
        $(".bg_tabs").css("background-image", "url(" + bgt + ")");
    });
    $(".list-single-facts .inline-facts-wrap").matchHeight({});
    $(".listing-item").matchHeight({});
    $(".article-masonry").matchHeight({});
    $(".grid-opt li span").on("click", function () {
        $(".listing-item").matchHeight({
            remove: true
        });
        setTimeout(function () {
            $(".listing-item").matchHeight();
        }, 50);
        $(".grid-opt li span").removeClass("act-grid-opt");
        $(this).addClass("act-grid-opt");
        if ($(this).hasClass("two-col-grid")) {
            $(".listing-item").removeClass("has_one_column");
            $(".listing-item").addClass("has_two_column");
        } else if ($(this).hasClass("one-col-grid")) {
            $(".listing-item").addClass("has_one_column");
        } else {
            $(".listing-item").removeClass("has_one_column").removeClass("has_two_column");
        }
    });
 // scroll animation ------------------
    $(".scroll-init  ul ").singlePageNav({
        filter: ":not(.external)",
        updateHash: false,
        offset: 160,
        threshold: 150,
        speed: 1200,
        currentClass: "act-scrlink"
    });
    $(".rate-item-bg").each(function () {
        $(this).find(".rate-item-line").css({
            width: $(this).attr("data-percent")
        });
    });
    $(window).on("scroll", function (a) {
        if ($(this).scrollTop() > 150) {
            $(".to-top").fadeIn(500);

            $(".clbtg").fadeIn(500);
        } else {
            $(".to-top").fadeOut(500);
            $(".clbtg").fadeOut(500);
        }
    });
    //   scroll to------------------
    $(".custom-scroll-link").on("click", function () {
        var a = 90 + $(".scroll-nav-wrapper").height();
        if (location.pathname.replace(/^\//, "") === this.pathname.replace(/^\//, "") || location.hostname === this.hostname) {
            var b = $(this.hash);
            b = b.length ? b : $("[name=" + this.hash.slice(1) + "]");
            if (b.length) {
                $("html,body").animate({
                    scrollTop: b.offset().top - a
                }, {
                    queue: false,
                    duration: 1200,
                    easing: "easeInOutExpo"
                });
                return false;
            }
        }
    });
    // modal ------------------
    var modal = {};
    modal.hide = function () {
        $('.modal , .reg-overlay').fadeOut(200);
        $("html, body").removeClass("hid-body");
        $(".modal_main").removeClass("vis_mr");
    };
    $('.modal-open').on("click", function (e) {
        e.preventDefault();
        $('.modal , .reg-overlay').fadeIn(200);
        $(".modal_main").addClass("vis_mr");
        $("html, body").addClass("hid-body");
    });
    $('.close-reg , .reg-overlay').on("click", function () {
        modal.hide();
    });
    $(".show_gcc").on("click", function (e) {
        e.preventDefault();
        $(this).parents(".geodir-category-footer").find(".geodir-category_contacts").addClass("visgdcc");
    });
    $(".close_gcc").on("click", function () {
        $(this).parent(".geodir-category_contacts").removeClass("visgdcc");
    });
    // Header ------------------
    $(".more-filter-option").on("click", function () {
        $(".hidden-listing-filter").slideToggle(500);
        $(this).find("span").toggleClass("mfilopact");
    });
    const headSearch = $(".header-search"),
        ssbut = $(".show-search-button"),
        wlwrp = $(".header-modal"),
        wllink = $(".show-header-modal"),
        mainheader = $(".main-header");

    function showSearch() {
        headSearch.addClass("vis-head-search").removeClass("vis-search");
        ssbut.find("span").text("Close");
        ssbut.find("i").addClass("vis-head-search-close");
        mainheader.addClass("vis-searchdec");
        hideWishlist();
    }
    function hideSearch() {
        headSearch.removeClass("vis-head-search").addClass("vis-search");
        ssbut.find("span").text("Search");
        ssbut.find("i").removeClass("vis-head-search-close");
        mainheader.removeClass("vis-searchdec");
    }
    ssbut.on("click", function () {
        if ($(".header-search").hasClass("vis-search")) showSearch();
        else hideSearch();
    });
    $(".header-search_close").on("click", function () {
        hideSearch();
    });
    function showWishlist() {
        wlwrp.fadeIn(1).addClass("vis-wishlist").removeClass("novis_wishlist")
        hideSearch();
        wllink.addClass("scwllink");
    }
    function hideWishlist() {
        wlwrp.fadeOut(1).removeClass("vis-wishlist").addClass("novis_wishlist");
        wllink.removeClass("scwllink");
    }
    wllink.on("click", function () {
        if (wlwrp.hasClass("novis_wishlist")) showWishlist();
        else hideWishlist();
    });
    $(".close-header-modal").on("click", function () {
        hideWishlist();
    });
    $(".act-hiddenpanel").on("click", function () {
        $(this).toggleClass("active-hidden-opt-btn").find("span").text($(this).find("span").text() === 'Close options' ? 'More options' : 'Close options');
        $(".hidden-listing-filter").slideToggle(400);
    });
    $(document).on('change', '.leave-rating input', function () {
        var $radio = $(this);
        $('.leave-rating .selected').removeClass('selected');
        $radio.closest('label').addClass('selected');
    });
    $(".show-hidden-map").on("click", function (e) {
        e.preventDefault();
        $(".show-hidden-map").find("span").text($(".show-hidden-map span").text() === 'Close' ? 'On The Map' : 'Close');
        $(".hidden-map-container").slideToggle(400);
    });
    $(".show-list-wrap-search").on("click", function (e) {
        $(".lws_mobile").slideToggle(400);
        $(this).toggleClass("slsw_vis");
    });
	$(".show-lpt").on("click", function (e) {
		e.preventDefault();
        $(".lost-password-tootip").addClass("lpt_vis");
    });
	$(".close-lpt").on("click", function () {
        $(".lost-password-tootip").removeClass("lpt_vis");
    });

    $(".submenu-link").on("click", function (ef) {
        ef.preventDefault();
        $(this).toggleClass("sl_tog");
        $(this).parent("li").find("ul").slideToggle(300);
    });
    $(".tfp-btn").on("click", function () {
        $(this).toggleClass("rot_tfp-btn");
        $(".tfp-det").toggleClass("vis_tfp-det ");
    });
    $(".dasboard-menu li").on({
        mouseenter: function () {

            $(this).find("a").css({
                "color": "#666",
                "background": "#fff"
            });

        },
        mouseleave: function () {
            $(this).find("a").css({
                "color": "#fff",
                "background": "none"
            });
        }
    });
    $(".fixed-listing-header").scrollToFixed({
        minWidth: 1064,
        marginTop: 80,
        removeOffsets: true,

        limit: function () {
            var a = $(".limit-box").offset().top - $(".fixed-listing-header").outerHeight();
            return a;
        }
    });
    $(".fixed-scroll-column-item").scrollToFixed({
        minWidth: 1064,
        marginTop: 200,
        removeOffsets: true,
        limit: function () {
            var a = $(".limit-box").offset().top - $(".fixed-scroll-column-item").outerHeight() - 46;
            return a;
        }
    });
    $(".fix-map").scrollToFixed({
        minWidth: 1064,
        zIndex: 0,
        marginTop: 80,
        removeOffsets: true,
        limit: function () {
            var a = $(".limit-box").offset().top - $(".fix-map").outerHeight(true);
            return a;
        }
    });
    $(".scroll-nav-wrapper").scrollToFixed({
        minWidth: 768,
        zIndex: 1112,
        marginTop: 80,
        removeOffsets: true,
        limit: function () {
            var a = $(".limit-box").offset().top - $(".scroll-nav-wrapper").outerHeight(true) - 50;
            return a;
        }
    });
    var v = $(".background-youtube-wrapper").data("vid");
    var f = $(".background-youtube-wrapper").data("mv");
    $(".background-youtube-wrapper").YTPlayer({
        fitToBackground: true,
        videoId: v,
        pauseOnScroll: true,
        mute: true,
        callback: function () {
            var a = $(".background-youtube-wrapper").data("ytPlayer").player;
        }
    });
    var w = $(".background-vimeo").data("vim"),
        bvc = $(".background-vimeo"),
        bvmc = $(".media-container"),
        bvfc = $(".background-vimeo iframe "),
        vch = $(".video-container");
    bvc.append('<iframe src="//player.vimeo.com/video/' + w + '?background=1"  frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen ></iframe>');
    $(".video-holder").height(bvmc.height());
    if ($(window).width() > 1024) {
        if ($(".video-holder").length > 0)
            if (bvmc.height() / 9 * 16 > bvmc.width()) {
                bvfc.height(bvmc.height()).width(bvmc.height() / 9 * 16);
                bvfc.css({
                    "margin-left": -1 * $("iframe").width() / 2 + "px",
                    top: "-75px",
                    "margin-top": "0px"
                });
            } else {
                bvfc.width($(window).width()).height($(window).width() / 16 * 9);
                bvfc.css({
                    "margin-left": -1 * $("iframe").width() / 2 + "px",
                    "margin-top": -1 * $("iframe").height() / 2 + "px",
                    top: "50%"
                });
            }
    } else if ($(window).width() < 760) {
        $(".video-holder").height(bvmc.height());
        bvfc.height(bvmc.height());
    } else {
        $(".video-holder").height(bvmc.height());
        bvfc.height(bvmc.height());
    }
    vch.css("width", $(window).width() + "px");
    vch.css("height", 720 / 1280 * $(window).width()) + "px";

    if (vch.height() < $(window).height()) {
        vch.css("height", $(window).height() + "px");
        vch.css("width", 1280 / 720 * $(window).height()) + "px";
    }
    $(".back-tofilters").scrollToFixed({
        minWidth: 1064,
        zIndex: 12,
        marginTop: 90,
        removeOffsets: true,

        limit: function () {
            var a = $(".limit-box").offset().top - $(".back-tofilters").outerHeight(true);
            return a;
        }
    });
    $(".help-bar").scrollToFixed({
        minWidth: 1064,
        zIndex: 12,
        marginTop: 100,
        removeOffsets: true,
        limit: function () {
            var a = $(".limit-box").offset().top - $(".help-bar").outerHeight(true) - 60;
            return a;
        }
    });
    if ($(".fixed-bar").outerHeight(true) < $(".post-container").outerHeight(true)) {
        $(".fixed-bar").addClass("fixbar-action");
        $(".fixbar-action").scrollToFixed({
            minWidth: 1064,
            zIndex: 12,
            marginTop: function () {
                var a = $(window).height() - $(".fixed-bar").outerHeight(true) - 100;
                if (a >= 0) return 20;
                return a;
            },
            removeOffsets: true,
            limit: function () {
                var a = $(".limit-box").offset().top - $(".fixed-bar").outerHeight() - 60;
                return a;
            }
        });
    } else $(".fixed-bar").removeClass("fixbar-action");
    const shf = $(".shsb_btn"),
        ahimcocn = $(".anim_clw"),
        mapover = $(".map-overlay , .close_sbfilters");

    function showhiddenfilters() {
        shf.removeClass("shsb_btn_act");
        ahimcocn.addClass("hidsb_act");
        mapover.fadeIn(200);
    }
    function hidehiddenfilters() {
        shf.addClass("shsb_btn_act");
        ahimcocn.removeClass("hidsb_act");
        mapover.fadeOut(200);
    }
    shf.on("click", function () {
        if ($(this).hasClass("shsb_btn_act")) showhiddenfilters();
        else hidehiddenfilters();
    });
    mapover.on("click", function () {
        hidehiddenfilters();
    });
    $(".url_btn").on("click", function (e) {
        e.preventDefault();
    });
    $('.chosen-select').niceSelect();
    $(".range-slider").ionRangeSlider({
        type: "double",
        keyboard: true
    });
    $(".rate-range").ionRangeSlider({
        type: "single",
        hide_min_max: true,
    });
    $(".price-range,.area-range").ionRangeSlider({
        type: "double",
    });
    function get_query(){
        var url = document.location.href;
        var qs = url.substring(url.indexOf('?') + 1).split('&');
        for(var i = 0, result = {}; i < qs.length; i++){
            qs[i] = qs[i].split('=');
            result[qs[i][0]] = decodeURIComponent(qs[i][1]);
        }
        return result;
    }
    var result = get_query();
    if(result['price-start'] !== undefined && result['price-end'] !== undefined){
        $(".price-range").data("ionRangeSlider").update({from:result['price-start'], to:result['price-end']})
    }
    if(result['area-start'] !== undefined && result['area-end'] !== undefined){
        $(".area-range").data("ionRangeSlider").update({from:result['area-start'], to:result['area-end']})
    }
    $('.toggle-filter-btn').on("click", function (e) {
        e.preventDefault();
        $(this).toggleClass("tsb_act");
    });
    $(".clear-singleinput").on("click", function (e) {
        $(this).parents(".clact").find("input").val('');
    });
    $('.init-dsmen').on("click", function () {
        $(".user-profile-menu-wrap").slideToggle(400);
    });
    function csselem() {
        $(".height-emulator").css({
            height: $(".fixed-footer").outerHeight(true)
        });
        $(".slideshow-container .swiper-slide").css({
            height: $(".slideshow-container").outerHeight(true)
        });
        $(".slider-container .slider-item").css({
            height: $(".slider-container").outerHeight(true)
        });
        $(".map-container.column-map").css({
            height: $(window).outerHeight(true) - 80 + "px"
        });
        $(".hidden-search-column-container").css({
            height: $(window).outerHeight(true) - 70 + "px"
        });
    }
    csselem();
    $(".nav-button-wrap").on("click", function () {
        $(".main-menu").toggleClass("vismobmenu");
        $(this).toggleClass("vismobmenu_btn");
    });
    function mobMenuInit() {
        const ww = $(window).width();
        if (ww < 1054) {
            $(".menusb").remove();
            $(".main-menu").removeClass("nav-holder");
            $(".main-menu nav").clone().addClass("menusb").appendTo(".main-menu");
            $(".menusb").mob_menu();
            $(".map-container.fw-map.big_map.hid-mob-map").css({
                height: $(window).outerHeight(true) - 110 + "px"
            });
        } else {
            $(".menusb").remove();
            $(".main-menu").addClass("nav-holder");
            $(".map-container.fw-map.big_map.hid-mob-map").css({
                height: 550 + "px"
            });
        }
    }
    mobMenuInit();
    const $window = $(window);
    $window.on("resize", function () {
        csselem();
        mobMenuInit();
        if ($(window).width() > 1064) {
            $(".lws_mobile , .dasboard-menu-wrap").addClass("vishidelem");
            $(".map-container.fw-map.big_map.hid-mob-map").css({
                "right": "0"
            });
            $(".map-container.column-map.hid-mob-map").css({
                "right": "0"
            });
        } else {
            $(".lws_mobile , .dasboard-menu-wrap").removeClass("vishidelem");
            $(".map-container.fw-map.big_map.hid-mob-map").css({
                "right": "-100%"
            });
            $(".map-container.column-map.hid-mob-map").css({
                "right": "-100%"
            });
        }
    });
    $(".box-cat").on({
        mouseenter: function () {
            var a = $(this).data("bgscr");
            $(".bg-ser").css("background-image", "url(" + a + ")");
        }
    });
    $(".header-user-name").on("click", function () {
        $(".header-user-menu ul").toggleClass("hu-menu-vis");
        $(this).toggleClass("hu-menu-visdec");
    });
    if ($(".counter-widget").length > 0) {
        var countCurrent = $(".counter-widget").attr("data-countDate");
        $(".countdown").downCount({
            date: countCurrent,
            offset: 0
        });
    }
    var bArray = [];
    var sArray = [2, 4, 6, 8];
    for (var i = 0; i < $('.bubbles').width(); i++) {
        bArray.push(i);
    }
    function randomValue(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }
    setInterval(function () {
        $('.individual-bubble').animate({
            'bottom': '100%',
            'opacity': '-=0.7'
        }, 4000, function () {
            $(this).remove()
        });
    }, 350);
    if ($(".col-list-wrap").hasClass("novis_to-top")) {
        $(".to-top").remove().clone().addClass("to-top_footer").appendTo(".main-footer")
    }
    $(".to-top , .to-top_footer").on("click", function (a) {
        a.preventDefault();
        $("html, body").animate({
            scrollTop: 0
        }, 800);
        return false;
    });
}
function initparallax() {
    var a = {
        Android: function () {
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function () {
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function () {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        Opera: function () {
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function () {
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function () {
            return a.Android() || a.BlackBerry() || a.iOS() || a.Opera() || a.Windows();
        }
    };
    trueMobile = a.any();
    if (null === trueMobile) {
        var b = new Scrollax();
        b.reload();
        b.init();
    }
    if (trueMobile) $(".bgvid , .background-vimeo , .background-youtube-wrapper ").remove();
}
$.fn.duplicate = function (a, b) {
    var c = [];
    for (var d = 0; d < a; d++) $.merge(c, this.clone(b).get());
    return this.pushStack(c);
};
function cardRaining() {
    var cr = $(".card-popup-raining");
    cr.each(function (cr) {
        var starcount = $(this).attr("data-starrating");
        $("<i class='fas fa-star'></i>").duplicate(starcount).prependTo(this);
    });
}
cardRaining();
function cardRaining2() {
    var cr2 = $(".card-popup-rainingvis"),
        sts = $(".price-level-item");
    cr2.each(function (cr) {
        var starcount2 = $(this).attr("data-starrating2");
        $("<i class='fas fa-star'></i>").duplicate(starcount2).prependTo(this);
    });
    sts.each(function (sts) {
        var pricecount = $(this).attr("data-pricerating");
        $("<strong>$</strong>").duplicate(pricecount).prependTo(this);
    });
    $("<div class='card-popup-rainingvis_bg'><div>").appendTo(".card-popup-rainingvis");
    $("<span class='card-popup-rainingvis_bg_item'></span>").duplicate(5).prependTo(".card-popup-rainingvis_bg");
}

$(".show-hidden-map").on("click", function (e) {
        e.preventDefault();
        $(".show-hidden-map").find("span").text($(".show-hidden-map span").text() === 'Close' ? 'On The Map' : 'Close');
        $(".hidden-map-container").slideToggle(400);
    });
    function showColumnhiddenmap() {
        if ($(window).width() < 1064) {
            $(".hid-mob-map").animate({
                right: 0
            }, 500, "easeInOutExpo").addClass("fixed-mobile");
        }
    }
    $(".map-item , .schm").on("click", function (e) {
        e.preventDefault();
        showColumnhiddenmap();
    });
    $('.map-close').on("click", function (e) {
        $(".hid-mob-map").animate({
            right: "-100%"
        }, 500, "easeInOutExpo").removeClass("fixed-mobile");
    });
cardRaining2();
$(document).ready(function () {
    initPropertyWebsite();
    initparallax();
});