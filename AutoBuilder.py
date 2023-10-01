import requests

url = 'https://public-api.wordpress.com/wp/v2/sites/162865469/posts/1906/autosaves?_envelope=1&_gutenberg_nonce=6d6105c301&_locale=user'

data_refom = {
	'body':
	'''
	{"body":
	{"author":150751209,
	"date":null,
	"date_gmt":null,
	"id":1906,
	"modified":"2022-06-02T16:25:23",
	"modified_gmt":"2022-06-02T08:25:23",
	"parent":0,
	"slug":"",
	"guid":{"rendered":"https:\/\/xoi.home.blog\/?p=1906","raw":"https:\/\/xoi.home.blog\/?p=1906"},
	"title":{"raw":"test","rendered":"test"},
	"content":{"raw":"<!-- wp:block {\"ref\":1862} \/-->",
	"rendered":"\n
	<div class=\"wp-container-3 wp-block-columns alignfull are-vertically-aligned-top\">\n
		<div class=\"wp-container-1 wp-block-column is-vertically-aligned-top has-foreground-color has-secondary-background-color has-text-color has-background\" style=\"flex-basis:66.66%;\">\n
			<figure class=\"wp-block-table\">
				<table>
					<tbody>
						<tr><td>\u79d1\uff1a\u79d1Family<br>\u5c5e\uff1a\u5c5eGenus<\/td><\/tr><tr><td>\u62c9\u4e01 \u4e2d\u6587\u6b63\u540d<br>\u540c\u7269\u5f02\u540d\uff1a<br>-\u62c9\u4e01 \u7ffb\u8bd1<\/td><\/tr>
						<tr><td>\u63cf\u8ff0\uff1a<br>\uff08\u6765\u6e90\u4e8e\u300a\u300b\uff09<\/td><\/tr>
						<tr><td>\u4e0e\u8fd1\u4f3c\u79cd\u533a\u5206\uff1a<br><a href=\"https:\/\/xoi.home.blog\/2021\/08\/24\/%e6%a2%ad%e5%9e%8b%e6%96%9c%e7%ae%a1%e8%9e%ba\/\">URL<\/a>\uff08\u62c9\u4e01\u5c5e\u540d\u5f00\u5934\u5927\u5199.\u62c9\u4e01\u79cd\u540d\uff09\uff1a\u65b9\u6cd5<\/td><\/tr>
						<tr><td>\u5176\u4ed6\u4fe1\u606f\uff1a \u526f\u6a21\u6807\u672c\u53f7\uff08\uff09<\/td><\/tr><\/tbody><\/table><\/figure>\n
						\n
						\n
						\n
		<div data-api-key=\"pk.eyJ1IjoiYXV0b21hdHRpYyIsImEiOiJjazVpZjA5aWswYTFvM21sOWtzNW1rNG9lIn0.Gu-sp4wRxnnQB-Qa8CpuZQ\" class=\"wp-block-jetpack-map is-style-default\" data-map-style=\"default\" data-map-details=\"true\" data-points=\"[]\" data-zoom=\"10.779496173169075\" data-map-center=\"{&quot;lng&quot;:109.60134588827498,&quot;lat&quot;:23.090887019814872}\" data-marker-color=\"red\" data-show-fullscreen-button=\"true\"><\/div>\n
		\n
		\n
		\n
		<p>\u5730\u56fe\uff1a\u53f3\u4e0a\u89d2\u8bbe\u7f6e\u952e\u4e2d\u7ba1\u7406\u79cd\u7c7b\u3001\u6807\u8bb0\u70b9\uff08\u6807\u8bb0\u70b9\u53ef\u4ee5\u5199\u5907\u6ce8\u3001\u6362\u989c\u8272\uff09<\/p>\n
		\n
		\n
		\n
		<p>\u6dfb\u52a0\u6807\u8bb0\u70b9\u65f6\u8f93\u5165\u5730\u533a\uff08\u82f1\u6587\uff09\u6dfb\u52a0<\/p>\n<\/div>\n
		\n
		\n
		\n
		<div class=\"wp-container-2 wp-block-column is-vertically-aligned-top has-tertiary-background-color has-background\" style=\"flex-basis:33.33%;\">\n
		\n
		\n
			<figure class=\"wp-block-table\">
				<table>
					<tbody>
						<tr><td>\u56fe\u7247\u8bf4\u660e\uff1a<\/td><\/tr><tr><td>\u4ea7\u5730\uff1a<\/td><\/tr>
						<tr><td>\u6a21\u5f0f\u6807\u672c\u4ea7\u5730\uff1a<\/td><\/tr>
						<tr><td>\u539f\u59cb\u6587\u732e\uff1a<a href=\"https:\/\/share.weiyun.com\/3WsDJc2z\">URL<\/a><\/td><\/tr>
						<tr><td>\u5907\u6ce8\uff1a<\/td><\/tr>
						<tr><td>\u5206\u7c7b\u53d8\u66f4\uff1a<br>Genus  &#8230;\uff08\u539f\u59cb\u6587\u732e\uff09\u2014\u2014Genus &#8230;\uff08\u6587\u732e\uff09<\/td><\/tr>
					<\/tbody>
				<\/table>
			<\/figure>\n
		<\/div>\n
	<\/div>\n"},
	"excerpt":{"raw":"","rendered":""},
	"preview_link":"https:\/\/xoi.home.blog\/?p=1906&preview=true"
},

"status":200,
"headers":{"Allow":"GET, POST"}}
	''',
	'headers':''
}


def RefData(name = None,Lt,Desc,Bok,):
	data = {
	
	}