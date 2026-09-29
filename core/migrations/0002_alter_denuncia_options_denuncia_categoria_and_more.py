from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='denuncia',
            options={'ordering': ['-data_criacao'], 'verbose_name': 'Denúncia', 'verbose_name_plural': 'Denúncias'},
        ),
        migrations.AddField(
            model_name='denuncia',
            name='categoria',
            field=models.CharField(choices=[('Buraco', 'Buraco'), ('Alagamento', 'Alagamento'), ('Lixo e Entulho', 'Lixo e Entulho'), ('Outro', 'Outro')], default='Buraco', max_length=30, verbose_name='Tipo de problema'),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='email_contato',
            field=models.EmailField(blank=True, help_text='Se preenchido, você recebe um aviso quando o status desta denúncia mudar.', max_length=254, null=True, verbose_name='E-mail para contato (opcional)'),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
