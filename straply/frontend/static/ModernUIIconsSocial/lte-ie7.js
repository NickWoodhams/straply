/* Load this script using conditional IE comments if you need to support IE 7 and IE 6. */

window.onload = function() {
	function addIcon(el, entity) {
		var html = el.innerHTML;
		el.innerHTML = '<span style="font-family: \'Modern-UI-Icons---Social\'">' + entity + '</span>' + html;
	}
	var icons = {
			'icon-social-aim' : '&#xe000;',
			'icon-social-aim-variant' : '&#xe001;',
			'icon-social-amazon-appstore' : '&#xe002;',
			'icon-social-amazon' : '&#xe003;',
			'icon-social-android' : '&#xe004;',
			'icon-social-apple' : '&#xe005;',
			'icon-social-apple-mobileme' : '&#xe006;',
			'icon-social-apple-appstore' : '&#xe007;',
			'icon-social-appnet' : '&#xe008;',
			'icon-social-artcom' : '&#xe009;',
			'icon-social-arto' : '&#xe00a;',
			'icon-social-aws' : '&#xe00b;',
			'icon-social-baidu' : '&#xe00c;',
			'icon-social-basecamp' : '&#xe00d;',
			'icon-social-bebo' : '&#xe00e;',
			'icon-social-behance' : '&#xe00f;',
			'icon-social-blogger' : '&#xe010;',
			'icon-social-cloudapp' : '&#xe011;',
			'icon-social-coding4fun' : '&#xe013;',
			'icon-social-deviantart' : '&#xe014;',
			'icon-social-digg' : '&#xe015;',
			'icon-social-digg-variant' : '&#xe016;',
			'icon-social-disqus' : '&#xe017;',
			'icon-social-dribbble' : '&#xe018;',
			'icon-social-dropbox-download' : '&#xe019;',
			'icon-social-dropbox' : '&#xe01a;',
			'icon-social-dropbox-upload' : '&#xe01b;',
			'icon-social-drupal' : '&#xe01c;',
			'icon-social-dnd' : '&#xe01d;',
			'icon-social-engadget' : '&#xe01e;',
			'icon-social-etsy' : '&#xe01f;',
			'icon-social-evernote' : '&#xe020;',
			'icon-social-facebook-heartbreak' : '&#xe021;',
			'icon-social-facebook-heart' : '&#xe022;',
			'icon-social-facebook' : '&#xe023;',
			'icon-social-facebook-variant' : '&#xe024;',
			'icon-social-foursquare' : '&#xe025;',
			'icon-social-gdgt' : '&#xe027;',
			'icon-social-github-octocat-solid' : '&#xe028;',
			'icon-social-github' : '&#xe029;',
			'icon-social-google' : '&#xe02a;',
			'icon-social-google-plus' : '&#xe02b;',
			'icon-social-grooveshark' : '&#xe02c;',
			'icon-social-indiegogo' : '&#xe02d;',
			'icon-social-jira' : '&#xe02e;',
			'icon-social-kickstarter' : '&#xe02f;',
			'icon-social-lastfm' : '&#xe030;',
			'icon-social-linkedin' : '&#xe031;',
			'icon-social-linkedin-variant' : '&#xe032;',
			'icon-social-microsoft' : '&#xe033;',
			'icon-social-mono' : '&#xe034;',
			'icon-social-openid' : '&#xe035;',
			'icon-social-picasa' : '&#xe036;',
			'icon-social-pinterest' : '&#xe037;',
			'icon-social-playstation' : '&#xe038;',
			'icon-social-rdio' : '&#xe039;',
			'icon-social-reddit' : '&#xe03a;',
			'icon-social-sharethis' : '&#xe03b;',
			'icon-social-share-open' : '&#xe03c;',
			'icon-social-share' : '&#xe03e;',
			'icon-social-skype' : '&#xe03f;',
			'icon-social-slashdot' : '&#xe040;',
			'icon-social-soundcloud' : '&#xe041;',
			'icon-social-spotify' : '&#xe042;',
			'icon-social-stackoverflow' : '&#xe043;',
			'icon-social-theverge' : '&#xe044;',
			'icon-social-twitter' : '&#xe045;',
			'icon-social-twitter-retweet' : '&#xe026;',
			'icon-social-tumblr' : '&#xe046;',
			'icon-social-uservoice' : '&#xe047;',
			'icon-social-vimeo' : '&#xe048;',
			'icon-social-wikipedia' : '&#xe049;',
			'icon-social-windows' : '&#xe04a;',
			'icon-social-wordpress' : '&#xe04b;',
			'icon-social-wordpress-variant' : '&#xe012;',
			'icon-social-xbox' : '&#xe04c;',
			'icon-social-yahoo' : '&#xe04d;',
			'icon-social-ycombinator' : '&#xe04e;',
			'icon-social-yelp' : '&#xe04f;',
			'icon-social-youtube' : '&#xe050;',
			'icon-social-youtube-play' : '&#xe03d;',
			'icon-social-zappos' : '&#xe051;'
		},
		els = document.getElementsByTagName('*'),
		i, attr, html, c, el;
	for (i = 0; ; i += 1) {
		el = els[i];
		if(!el) {
			break;
		}
		attr = el.getAttribute('data-icon');
		if (attr) {
			addIcon(el, attr);
		}
		c = el.className;
		c = c.match(/icon-social-[^\s'"]+/);
		if (c && icons[c[0]]) {
			addIcon(el, icons[c[0]]);
		}
	}
};