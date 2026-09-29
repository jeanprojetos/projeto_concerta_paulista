from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import Denuncia


@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('rua', 'bairro', 'categoria', 'status', 'data_criacao')
    list_editable = ('status',)
    list_filter = ('status', 'categoria', 'bairro')
    search_fields = ('rua', 'bairro', 'descricao')
    date_hierarchy = 'data_criacao'
    ordering = ('-data_criacao',)

    def save_model(self, request, obj, form, change):
        status_mudou = change and 'status' in form.changed_data
        super().save_model(request, obj, form, change)

        if status_mudou and obj.email_contato:
            try:
                send_mail(
                    subject=f"Atualização da sua denúncia em {obj.rua}",
                    message=(
                        f"Olá,\n\n"
                        f"A denúncia registrada em {obj.rua}, {obj.bairro} "
                        f"mudou de status para: {obj.status}.\n\n"
                        f"Obrigado por ajudar a melhorar as ruas de Paulista.\n"
                        f"Concerta Paulista"
                    ),
                    from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', None),
                    recipient_list=[obj.email_contato],
                    fail_silently=True,
                )
            except Exception:
                # Nunca deixamos um problema de e-mail impedir a atualização do status.
                pass
