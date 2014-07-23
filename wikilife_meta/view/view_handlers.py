# coding=utf-8

from wikilife_meta.rest.base_handler import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        self.render("api.html")


class NodeByIdHandler(BaseHandler):
    def get(self, node_id):
        children_page_index = int(self.get_argument("children_page", 0))
        node_id = int(node_id)
        meta_srv = self._services["meta"]
        node = meta_srv.get_node_full(node_id)

        children_page = meta_srv.get_node_children(node_id, children_page_index, 50)
        node["children"] = children_page
        node["children"]["pagePrev"] = "/nodes/%s?children_page=%s" %(node_id, children_page_index-1) if children_page_index>0 else None
        node["children"]["pageNext"] = "/nodes/%s?children_page=%s" %(node_id, children_page_index+1) if children_page_index<children_page["pageCount"]-1 else None

        self.success(response=node)

class NodeByOrigIdHandler(NodeByIdHandler):
    def get(self, node_orig_id):
        node_orig_id = int(node_orig_id)
        meta_srv = self._services["meta"]
        node = meta_srv.get_node_by_orig_id(node_orig_id)
        node_id = node["id"]
        NodeByIdHandler.get(self, node_id)

class MetricByIdHandler(BaseHandler):
    def get(self, metric_id):
        metric_id = int(metric_id)
        meta_srv = self._services["meta"]
        metric = meta_srv.get_metric_by_id(metric_id)
        self.success(response=metric)


class SearchHandler(BaseHandler):
    def get(self):
        node_name = self.get_argument("name", None)
        page_index = int(self.get_argument("page", 0))
        result = None

        if node_name != None:
            meta_srv = self._services["meta"]
            result = meta_srv.find_nodes(node_name, page_index)
            result["name"] = node_name
            result["pagePrev"] = "/search/?name=%s&page=%s" %(node_name, page_index-1) if page_index>0 else None
            result["pageNext"] = "/search/?name=%s&page=%s" %(node_name, page_index+1) if page_index<result["pageCount"]-1 else None

        self.success(response=result)
        


class DescendantsHandler(BaseHandler):
    def get(self, node_id):
        node_id = int(node_id)
        meta_srv = self._services["meta"]
        node = meta_srv.get_node_by_id(node_id)
        node["descendantsCount"] = meta_srv.get_descendants_count(node_id)
        self.success(response=node)
        

class ChildrenIDsHandler(BaseHandler):
    def get(self, node_id):
        children_page_index = int(self.get_argument("children_page", 0))
        node_id = int(node_id)
        meta_srv = self._services["meta"]
        node = meta_srv.get_node_by_id(node_id)

        children_page = meta_srv.get_node_children(node_id, children_page_index, 200)
        node["children"] = children_page
        node["children"]["pagePrev"] = "/childrenids/%s?children_page=%s" %(node_id, children_page_index-1) if children_page_index>0 else None
        node["children"]["pageNext"] = "/childrenids/%s?children_page=%s" %(node_id, children_page_index+1) if children_page_index<children_page["pageCount"]-1 else None
        
        self.success(response=node)