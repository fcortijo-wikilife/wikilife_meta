# coding=utf-8

from os import path
import logging

#===================================
#   LOGGING
#===================================
LOGGER = logging.getLogger('wikilife admin')
handler = logging.FileHandler(path.join(path.dirname(__file__), "logs/wikilife_meta.log"))
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)

#===================================
#   TORNADO
#===================================
TORNADO = dict(
    db_name="",
    db_uri="",
    db_user="",
    db_pass="",
    login_url="/auth/login",
    static_path=path.join(path.dirname(__file__), "static"),
    template_path=path.join(path.dirname(__file__), "templates"),
    # md5(wikilife cookie secret)
    cookie_secret="2e1faa057cfe1c9a095ecaca8fc4d3f2",
    debug=False,
    debug_pdb=False,
    # The following are custom application settings
    _cookie_expiration=7,
    _min_search_length=3,
)

#===================================
#   BIZ 
#===================================

META_PAGE_SIZE = 50


#===================================
#   DB 
#===================================

DB_SETTINGS = {
    "db_meta_live": {},
    "db_meta_edit": {},
    "db_main_live": {"name": "wikilife_main_live"},
    "db_main_edit": {"name": "wikilife_main_edit"},
    "db_users": {"name": "wikilife_users"},
    "db_logs": {"name": "wikilife_logs"},
    "db_processors": {"name": "wikilife_processors"},
    "db_crawler": {"name": "wikilife_crawler"},
    "db_apps": {"name": "wikilife_apps"},
    "db_admin": {"name": "wikilife_admin"},
    "db_location": {"name": "geonames"}
}
