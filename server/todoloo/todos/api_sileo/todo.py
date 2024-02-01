from sileo.sileo.resource import Resource
from sileo.sileo.fields import ResourceTypeConvert, ResourceModelManager
from sileo.sileo.registration import register
from todos.models import Todo
from todos.forms import TodoForm

class TodoResource(Resource):
    query_set = Todo.objects.all()
    fields = [
        'pk', 
        'title',
        'completed'
    ]
    allowed_methods = [
        'get_pk', 'filter', 'create', 'update', 'delete'
    ]
    update_filter_fields = ['pk']
    delete_filter_fields = ['pk']
    filter_fields = ['pk', 'title']
    form_class = TodoForm

    def delete_object(self, obj):

        obj.delete()
        return {'pk': obj.pk}


  
register(namespace='todos', name='todo', resource=TodoResource, version='v1')

