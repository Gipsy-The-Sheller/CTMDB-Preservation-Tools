def OrgTheEntry(
	LtFam = None,ChFam = None,
	LtGen = None,ChGen = None,
	LtName = None,ChName = None,
	Desc = None,Book = None,
	Loc = None,TpLoc = None,
	Orig = None,OrigURL = None):
	# '<table><tbody><tr><td>产地：{}'.format(str(Loc))+
	# '</td></tr><tr><td>模式标本产地：{}'.format(str(TpLoc)+
	# '</td></tr><tr><td>原始文献：<a href="{}">'.format(str(OrigURL))+
	# str(Orig)+
	# '</a></td></tr><tr><td>备注：</td></tr><tr><td>分类变更：<br>Genus  ...（原'+
	# '始文献）——Genus ...（文献）</td></tr></tbody></table></figure>'+
	# '<!-- /wp:table --></div>'+
	# '<!-- /wp:column --></div>'+
	# '<!-- /wp:columns -->'
	prestr = '''<!-- wp:columns {"verticalAlignment":"top","align":"full"} -->
<div class="wp-block-columns alignfull are-vertically-aligned-top"><!-- wp:column {"verticalAlignment":"top","width":"66.66%","backgroundColor":"secondary","textColor":"foreground"} -->
<div class="wp-block-column is-vertically-aligned-top has-foreground-color has-secondary-background-color has-text-color has-background" style="flex-basis:66.66%"><!-- wp:table -->
<figure class="wp-block-table"><table><tbody><tr><td>'''+'科：{}Family<strong>{}</strong><br>属：{}<strong>{}</strong></td></tr><tr><td>{} {}'.format(
	 	str(ChFam),str(LtFam),str(ChGen),str(LtGen),str(LtName),str(ChName))+'''<br>同物异名：<br>-拉丁 翻译</td></tr><tr><td>描述：'''+'\n{}<br>（来源于{}）'.format(
	 	str(Desc),str(Book))+'''</td></tr><tr><td>与近似种区分：<br><a href="https://xoi.home.blog/2021/08/24/%e6%a2%ad%e5%9e%8b%e6%96%9c%e7%ae%a1%e8%9e%ba/">URL</a>（拉丁属名开头大写.拉丁种名）：方法</td></tr><tr><td>其他信息： 副模标本号（）</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:jetpack/map {"points":[],"zoom":10.779496173169075,"mapCenter":{"lng":109.60134588827498,"lat":23.090887019814872},"className":"is-style-default"} -->
<div class="wp-block-jetpack-map is-style-default" data-map-style="default" data-map-details="true" data-points="[]" data-zoom="10.779496173169075" data-map-center="{&quot;lng&quot;:109.60134588827498,&quot;lat&quot;:23.090887019814872}" data-marker-color="red" data-show-fullscreen-button="true"></div>
<!-- /wp:jetpack/map --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"top","width":"33.33%","backgroundColor":"tertiary"} -->
<div class="wp-block-column is-vertically-aligned-top has-tertiary-background-color has-background" style="flex-basis:33.33%"><!-- wp:jetpack/slideshow {"sizeSlug":"large"} /-->

<!-- wp:table -->
<figure class="wp-block-table"><table><tbody><tr><td>图片说明：</td></tr>'''+'<tr><td>产地：{}'.format(
	str(Loc))+'</td></tr><tr><td>模式标本产地：{}'.format(
	str(TpLoc))+	'</td></tr><tr><td>原始文献：<a href="{}">'.format(
		str(OrigURL))+str(Orig)+'''</a></td></tr><tr><td>备注：</td></tr><tr><td>分类变更：<br>Genus  ...（原始文献）——Genus ...（文献）</td></tr></tbody></table></figure>
<!-- /wp:table --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
	'''
	return prestr

def OrgTheEntry2(LtFam = None,ChFam = None,
	LtGen = None,ChGen = None,
	LtName = None,ChName = None,
	Desc = None,Book = None,
	Loc = None,TpLoc = None,
	Orig = None,OrigURL = None):
	prestr = '''
<!-- wp:columns {"verticalAlignment":"top","align":"full"} -->
<div class="wp-block-columns alignfull are-vertically-aligned-top"><!-- wp:column {"verticalAlignment":"top","width":"66.66%","backgroundColor":"secondary","textColor":"foreground"} -->
<div class="wp-block-column is-vertically-aligned-top has-foreground-color has-secondary-background-color has-text-color has-background" style="flex-basis:66.66%"><!-- wp:table -->
<figure class="wp-block-table"><table><tbody><tr><td>科：{}Family <strong>{}</strong><br>属：{}<strong>{}</strong></td></tr><tr><td><strong>{} {}</strong><br>同物异名：</td></tr><tr><td>描述：
{}<br>（来源于{}）</td></tr><tr><td>与近似种区分：</td></tr><tr><td>其他信息：/td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:jetpack/map {"points":[{"placeTitle":"Taiwan","title":"Taiwan","caption":"Taiwan","id":"country.8935","coordinates":{"longitude":120.930229378541,"latitude":23.7779779950014}},{"placeTitle":"高雄市","title":"高雄市","caption":"高雄市, Kaohsiung, Taiwan","id":"place.3074279","coordinates":{"longitude":120.312037,"latitude":22.620335}}],"zoom":7.512134273062739,"mapCenter":{"lng":120.6211331892705,"lat":23.199156497500702},"className":"is-style-default"} -->
<div class="wp-block-jetpack-map is-style-default" data-map-style="default" data-map-details="true" data-points="[{&quot;placeTitle&quot;:&quot;Taiwan&quot;,&quot;title&quot;:&quot;Taiwan&quot;,&quot;caption&quot;:&quot;Taiwan&quot;,&quot;id&quot;:&quot;country.8935&quot;,&quot;coordinates&quot;:{&quot;longitude&quot;:120.930229378541,&quot;latitude&quot;:23.7779779950014}},{&quot;placeTitle&quot;:&quot;高雄市&quot;,&quot;title&quot;:&quot;高雄市&quot;,&quot;caption&quot;:&quot;高雄市, Kaohsiung, Taiwan&quot;,&quot;id&quot;:&quot;place.3074279&quot;,&quot;coordinates&quot;:{&quot;longitude&quot;:120.312037,&quot;latitude&quot;:22.620335}}]" data-zoom="7.512134273062739" data-map-center="{&quot;lng&quot;:120.6211331892705,&quot;lat&quot;:23.199156497500702}" data-marker-color="red" data-show-fullscreen-button="true"><ul><li><a href="https://www.google.com/maps/search/?api=1&amp;query=23.7779779950014,120.930229378541">Taiwan</a></li><li><a href="https://www.google.com/maps/search/?api=1&amp;query=22.620335,120.312037">高雄市</a></li></ul></div>
<!-- /wp:jetpack/map --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"top","width":"33.33%","backgroundColor":"tertiary"} -->
<div class="wp-block-column is-vertically-aligned-top has-tertiary-background-color has-background" style="flex-basis:33.33%"><!-- wp:jetpack/slideshow {"ids":[4420,4422,4425],"sizeSlug":"large"} -->
<div class="wp-block-jetpack-slideshow aligncenter" data-effect="slide"><div class="wp-block-jetpack-slideshow_container swiper-container"><ul class="wp-block-jetpack-slideshow_swiper-wrapper swiper-wrapper"><li class="wp-block-jetpack-slideshow_slide swiper-slide"><figure><img alt="" class="wp-block-jetpack-slideshow_image wp-image-4420" data-id="4420" src="https://xoihome.files.wordpress.com/2023/02/satsuma-succincta-tw.png?w=750"/><figcaption class="wp-block-jetpack-slideshow_caption gallery-caption">来源：台湾蜗牛图鉴</figcaption></figure></li><li class="wp-block-jetpack-slideshow_slide swiper-slide"><figure><img alt="" class="wp-block-jetpack-slideshow_image wp-image-4422" data-id="4422" src="https://xoihome.files.wordpress.com/2023/02/satsuma-succincta-alv.jpg"/><figcaption class="wp-block-jetpack-slideshow_caption gallery-caption">生活照，图片来源于台湾蜗牛图鉴</figcaption></figure></li><li class="wp-block-jetpack-slideshow_slide swiper-slide"><figure><img alt="" class="wp-block-jetpack-slideshow_image wp-image-4425" data-id="4425" src="https://xoihome.files.wordpress.com/2023/02/satsuma-succincta-orig.png?w=750"/><figcaption class="wp-block-jetpack-slideshow_caption gallery-caption">图片来源于发表文献</figcaption></figure></li></ul><a class="wp-block-jetpack-slideshow_button-prev swiper-button-prev swiper-button-white" role="button"></a><a class="wp-block-jetpack-slideshow_button-next swiper-button-next swiper-button-white" role="button"></a><a aria-label="Pause Slideshow" class="wp-block-jetpack-slideshow_button-pause" role="button"></a><div class="wp-block-jetpack-slideshow_pagination swiper-pagination swiper-pagination-white"></div></div></div>
<!-- /wp:jetpack/slideshow -->

<!-- wp:block {"ref":2805} /-->

<!-- wp:table -->
<figure class="wp-block-table"><table><tbody><tr><td>产地：{}</td></tr><tr><td>模式标本产地：{}</td></tr><tr><td>原始文献：<a href="https://www.biodiversitylibrary.org/page/28627804">dams, H. (1866). Descriptions of fifteen new species of land and freshwater shells from Formosa, collected by Robert Swinhoe, Esq., Consul at Taiwan in that island. Proceedings of the Zoological Society of London. (1866) 34: 316-319 , pl. 33.</a></td></tr><tr><td>备注：小菱蜗牛、红菱蜗牛、圆菱蜗牛可能只是同一族群的渐变群（cline）。学名「succincta」在拉丁文中有「束带、紧束」之意，用以形容壳的形态。（台湾蜗牛图鉴）</td></tr></tbody></table></figure>
<!-- /wp:table --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->'''.format(str(ChFam),str(LtFam),str(ChGen),str(LtGen),str(LtName),str(ChName),str(Desc),str(Book),str(Loc),str(TpLoc),str(Orig),str(OrigURL))
	return prestr