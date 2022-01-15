from django.apps import AppConfig

class EmployeesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leavestracker.apps.employees'

    def ready(self):
        import leavestracker.apps.employees.signals


