#This is an API for the organized ENTRIES
#it has been formed into an function.

from wordpress_xmlrpc import Client,WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts,NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
#登录你的wordpress
wp=Client('https://shellsmap.com/xmlrpc.php','xuzhijie2024','gipsythesheller')
#function:创建新文章
#以后可加分类
def NewEntry(title,content):
	post=WordPressPost()
	post.title=title
	post.content=content
	#下面这一句必须加上，否则发布的文章只是草稿
	post.post_status ='pending'
	#设置文章分类以及标签
	post.terms_names={
	#'post_tag':['test','爬虫测试'],
	#'category':['网贷']
	}
	#发布文章
	wp.call(NewPost(post))
