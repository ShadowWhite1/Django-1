from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='firstModelPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_var', models.CharField(max_length=100)),
                ('Description_var', models.TextField(null=True)),
                ('DateTime_var', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]