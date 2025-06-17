from django.contrib import admin
from .models import Message, Room
from .forms import MessageAdminForm
from django.contrib.admin import SimpleListFilter
from django.template.response import TemplateResponse
from django.urls import path

class RecentMessagesFilter(SimpleListFilter):
    title='Messagens Recentes'
    parameter_name= 'recente'

    def lookups(self, request, model_admin):
        return [
            ('today', 'Today'),
            ('last_7_days', 'Last 7 Days')
        ]
    
    def queryset(self, request, queryset):
        from django.utils.timezone import now, timedelta
        
        if self.value() == 'today':
            return queryset.filter(timestamp__date=now().date())
        if self.value() == 'last_7_days':
            return queryset.filter(timestamp__gte=now() - timedelta(days=7))
    
def mark_messages_as_read(modeladmin, request, queryset):
    queryset.update(content="This message was marked as read.")

mark_messages_as_read.short_description = "Mark selected messages as read"
        
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
    search_fields=('name',)
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    actions=[mark_messages_as_read]
    form = MessageAdminForm
    list_display= ('id', 'room', 'user', 'content', 'timestamp')
    list_filter= ('timestamp', 'room', RecentMessagesFilter)
    search_fields= ('user', 'content')
    
def admin_dashboard(request):
    context = {
        'room_count': Room.objects.count(),
        'messages_count': Message.objects.count(),
    }
    
    return TemplateResponse(request, 'admin/dashboard.html', context)

class CustomAdminSite(admin.AdminSite):
    site_header = "Meu administrador personalizado"
    index_title = "Dashboard"
    
    def get_urls(self):
        urls = super().get_urls()
    
        custom_urls = [
            path('dashboard/', self.admin_view(admin_dashboard), name='dashboard')    
        ]
        return custom_urls + urls
    
custom_admin_site = CustomAdminSite(name='custom_admin')
custom_admin_site.register(Room)
custom_admin_site.register(Message)