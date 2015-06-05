from django.contrib import admin

from .models import Scan
from .models import Scan_results

admin.site.register(Scan)
admin.site.register(Scan_results)
