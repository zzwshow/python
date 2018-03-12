from flask import session,g
from .models import CMSUser
from .views import bp
import config


#在返回cms主页前将用户信息绑定到g对象上供前端使用！
@bp.before_request
def before_request():
	if config.CMS_USER_ID in session:
		user_id = session.get(config.CMS_USER_ID)
		user = CMSUser.query.get(user_id)
		if user:
			g.cms_user = user