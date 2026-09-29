from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200, verbose_name='Rua / Avenida')),
                ('bairro', models.CharField(max_length=100)),
                ('referencia', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ponto de Referência')),
                ('descricao', models.TextField(verbose_name='Descrição do Problema')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='denuncias/', verbose_name='Foto do Buraco')),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Em Andamento', 'Em Andamento'), ('Resolvido', 'Resolvido')], default='Pendente', max_length=20)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data da Denúncia')),
            ],
        ),
    ]
