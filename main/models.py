# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cityshp(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    admincode = models.CharField(db_column='ADMINCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kind = models.CharField(db_column='KIND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    citycode = models.CharField(db_column='CITYCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    provincena = models.CharField(db_column='PROVINCENA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    the_geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cityshp'


class DistinctPoisSuzhou(models.Model):
    poiid = models.CharField(primary_key=True, max_length=64)
    title = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    category_name = models.CharField(max_length=128, blank=True, null=True)
    poi_street_address = models.CharField(max_length=128, blank=True, null=True)
    checkin_user_num = models.IntegerField(blank=True, null=True)
    checkin_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    dig_time_start = models.BigIntegerField(blank=True, null=True)
    dig_time_end = models.BigIntegerField(blank=True, null=True)
    digmark = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distinct_pois_suzhou'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TravelPoiUserinfoSuzhou(models.Model):
    id = models.BigIntegerField(primary_key=True)
    screen_name = models.CharField(max_length=128, blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    domain = models.CharField(max_length=128, blank=True, null=True)
    weihao = models.CharField(max_length=128, blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    statuses_count = models.IntegerField(blank=True, null=True)
    favourites_count = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=128, blank=True, null=True)
    created_at_int = models.BigIntegerField(blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    verified_type = models.IntegerField(blank=True, null=True)
    verified_reason = models.CharField(max_length=512, blank=True, null=True)
    bi_followers_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel_poi_userinfo_suzhou'


class TravelPoiUsersWeibodataSuzhou(models.Model):
    created_at = models.CharField(max_length=128, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    text = models.CharField(max_length=512, blank=True, null=True)
    source = models.CharField(max_length=128, blank=True, null=True)
    geo = models.CharField(max_length=256, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    reposts_count = models.IntegerField(blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)
    attitudes_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel_poi_users_weibodata_suzhou'


class TravelPoiWeibosSuzhou(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.CharField(max_length=512, blank=True, null=True)
    source = models.CharField(max_length=128, blank=True, null=True)
    geo = models.CharField(max_length=256, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    reposts_count = models.IntegerField(blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)
    attitudes_count = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=128, blank=True, null=True)
    created_at_int = models.BigIntegerField(blank=True, null=True)
    original_pic = models.CharField(max_length=128, blank=True, null=True)
    annotation_count = models.IntegerField(blank=True, null=True)
    annotation_client_mblogid = models.CharField(max_length=128, blank=True, null=True)
    annotation_place_poiid = models.CharField(max_length=128)
    annotation_place_title = models.CharField(max_length=128, blank=True, null=True)
    annotation_place_lon = models.FloatField(blank=True, null=True)
    annotation_place_lat = models.FloatField(blank=True, null=True)
    annotation_place_type = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel_poi_weibos_suzhou'
