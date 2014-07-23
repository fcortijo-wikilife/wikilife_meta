# coding=utf-8

from tornado.web import Application
from wikilife_admin.view.view_handlers import NodeByIdHandler, MainHandler, \
    MetricByIdHandler, SearchHandler, DescendantsHandler, NodeByOrigIdHandler,\
    ChildrenIDsHandler
from wikilife_biz.utils.biz_service_builder import BizServiceBuilder
from wikilife_data.utils.dao_builder import DAOBuilder
from wikilife_data.utils.db_conn import DBConn


def _build_services(settings):
    logger = settings["LOGGER"]
    db_conn = DBConn(settings["DB_SETTINGS"], db_user=None, db_pass=None)
    dao_builder = DAOBuilder(logger, db_conn)
    biz_srv_builder = BizServiceBuilder(settings, logger, dao_builder)

    services = {}
    services["meta"] = biz_srv_builder.build_meta_service()
    
    return services

def setup_app(settings):
    routes = []
    settings["TORNADO"]['logger'] = settings["LOGGER"]
    services = _build_services(settings)

    """ VIEWS """
    routes.append(('/', MainHandler, {'services': services}))
    routes.append(('/nodes/(?P<node_id>\d+)?', NodeByIdHandler, {'services': services}))
    routes.append(('/nodes_orig/(?P<node_orig_id>\d+)?', NodeByOrigIdHandler, {'services': services}))
    routes.append(('/metrics/(?P<metric_id>\d+)?', MetricByIdHandler, {'services': services}))
    routes.append(('/search/', SearchHandler, {'services': services}))
    routes.append(('/descendants/(?P<node_id>\d+)?', DescendantsHandler, {'services': services}))
    routes.append(('/childrenids/(?P<node_id>\d+)?', ChildrenIDsHandler, {'services': services}))

    return Application(routes, **settings["TORNADO"])