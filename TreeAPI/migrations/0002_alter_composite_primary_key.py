from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('treeapi', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE treeapi_node "
            "DROP CONSTRAINT treeapi_node_pkey, "
            "ADD PRIMARY KEY (path, id);"
        )
    ]