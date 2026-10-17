from spyne import Application, rpc, ServiceBase, Integer, Unicode, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from backend.databases import db


class TaskService(ServiceBase):
    @rpc(Integer, Unicode, Unicode, Boolean, _returns=Integer)
    def add_task(ctx, task_id, title, description, done):
        return db.add_task(title, description, done)    
    @rpc(_returns=Unicode)
    def get_tasks(ctx):
        return str(db.get_tasks())
    @rpc(Integer, _returns=Unicode)
    def get_task(ctx, task_id):
        return str(db.get_task(task_id))
    @rpc(Integer, Unicode, Unicode, Boolean, _returns=Boolean)
    def update_task(ctx, task_id, title, description, done):
        db.update_task(task_id, title, description, done)
        return True
    @rpc(Integer, _returns=Boolean)
    def delete_task(ctx, task_id):
        db.delete_task(task_id)
        return True

application = Application([TaskService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)