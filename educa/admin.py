from django.contrib import admin

admin.autodiscover()
admin.site.index_template = "memcache_status/admin_index.html"
