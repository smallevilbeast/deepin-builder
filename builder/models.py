#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 ~ 2013 Deepin, Inc.
#               2011 ~ 2013 Hou ShaoHui
# 
# Author:     Hou ShaoHui <houshao55@gmail.com>
# Maintainer: Hou ShaoHui <houshao55@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from django.db import models
from django.contrib.auth.models import User


class Package(models.Model):
    name = models.CharField(max_length=64L, blank=True, verbose_name="软件包名称")
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'dp_package'

class Deb(models.Model):
    package_name = models.ForeignKey(Package, verbose_name="名称")
    dirpath = models.CharField(max_length=4096L, blank=True, verbose_name="下载地址")
    last_time = models.DateTimeField(verbose_name="完成时间", blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.package_name)
    
    class Meta:
        db_table = 'dp_deb'
        
class Favorite(models.Model):
    user_id = models.ForeignKey(User, verbose_name="用户")
    package_name = models.ForeignKey(Package, verbose_name="软件包名称")
    addtime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    
    def __unicode__(self):
        return unicode(self.package_name)
    
    class Meta:
        db_table = 'dp_favorite'
        

class Message(models.Model):
    username = models.ForeignKey(User, verbose_name="用户")
    title = models.CharField(max_length=255L, blank=True, verbose_name="标题")
    content = models.TextField(blank=True, verbose_name="消息内容")
    posttime = models.DateTimeField(verbose_name="发布时间")
    
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        db_table = 'dp_message'


class PackageInfo(models.Model):
    package_name = models.ForeignKey(Package, verbose_name="软件包名称")
    dsc_path = models.CharField(max_length=1000L, blank=True, verbose_name="dsc文件路径")
    source_url = models.CharField(max_length=2000L, blank=True, verbose_name="源码地址")
     
    def __unicode__(self):
        return unicode(self.package_name)
   
    class Meta:
        db_table = 'dp_package_info'

class Server(models.Model):
    servername = models.CharField(max_length=255L, blank=True, verbose_name="服务器名称")
    address = models.CharField(max_length=16L, blank=True, verbose_name="服务器地址")
    
    def __unicode__(self):
        return self.servername
    
    class Meta:
        db_table = 'dp_server'

class SourceFile(models.Model):
    source_info = models.ForeignKey("SourceInfo", verbose_name="信息")
    filename = models.CharField(max_length=255L, db_column='Filename', blank=True, verbose_name="名称") 
    size = models.IntegerField(null=True, db_column='Size', blank=True, verbose_name="大小")
    md5 = models.CharField(max_length=255L, db_column='Md5', blank=True, verbose_name="MD5") 
    sha1 = models.CharField(max_length=255L, db_column='Sha1', blank=True, verbose_name="SHA")
    sha256 = models.CharField(max_length=255L, db_column='Sha256', blank=True, verbose_name="SHA256")
    
    def __unicode__(self):
        return unicode(self.source_info)
    
    class Meta:
        db_table = 'dp_source_file'

class SourceInfo(models.Model):
    apport = models.TextField(db_column='Apport', blank=True, verbose_name="Apport") 
    architecture = models.TextField(db_column='Architecture', blank=True, verbose_name="架构") 
    autobuild = models.TextField(db_column='Autobuild', blank=True, verbose_name="自动构建") 
    binary = models.TextField(db_column='Binary', blank=True, verbose_name="二进制名称") 
    build_conflicts = models.TextField(db_column='Build-Conflicts', blank=True, verbose_name="Bulid Conflict") 
    build_conflicts_indep = models.TextField(db_column='Build-Conflicts-Indep', blank=True, verbose_name="Conflict Indep")
    build_depends = models.TextField(db_column='Build-Depends', blank=True, verbose_name="依赖")
    build_depends_indep = models.TextField(db_column='Build-Depends-Indep', blank=True, verbose_name="依赖Indep")
    checksums_sha1 = models.TextField(db_column='Checksums-Sha1', blank=True, verbose_name="SHA1") 
    checksums_sha256 = models.TextField(db_column='Checksums-Sha256', blank=True, verbose_name="SHA256")
    debian_vcs_browser = models.TextField(db_column='Debian-Vcs-Browser', blank=True, verbose_name="Debian-Vcs-Browser") 
    debian_vcs_bzr = models.TextField(db_column='Debian-Vcs-Bzr', blank=True, verbose_name="Debian-Vcs-Bzr")
    debian_vcs_git = models.TextField(db_column='Debian-Vcs-Git', blank=True, verbose_name="Debian-Vcs-Git")
    debian_vcs_svn = models.TextField(db_column='Debian-Vcs-Svn', blank=True, verbose_name="Debian-Vcs-Svn")
    directory = models.TextField(db_column='Directory', blank=True, verbose_name="Directory")
    dm_upload_allowed = models.TextField(db_column='Dm-Upload-Allowed', blank=True, verbose_name="Dm-Upload-Allowed") 
    files = models.TextField(db_column='Files', blank=True, verbose_name="Files")
    format = models.TextField(db_column='Format', blank=True, verbose_name="Format") 
    homepage = models.TextField(db_column='Homepage', blank=True, verbose_name="主页")
    maintainer = models.TextField(db_column='Maintainer', blank=True, verbose_name="维护者")
    orig_maintainer = models.TextField(db_column='Orig-Maintainer', blank=True, verbose_name="Orig-Maintainer")
    orig_vcs_browser = models.TextField(db_column='Orig-Vcs-Browser', blank=True, verbose_name="Orig-Vcs-Browser")
    orig_vcs_svn = models.TextField(db_column='Orig-Vcs-Svn', blank=True, verbose_name="Orig-Vcs-Svn")
    origin = models.TextField(db_column='Origin', blank=True, verbose_name="Origin")
    original_maintainer = models.TextField(db_column='Original-Maintainer', blank=True, verbose_name="Original-Maintainer")
    original_vcs_browser = models.TextField(db_column='Original-Vcs-Browser', blank=True, verbose_name="Original-Vcs-Browser")
    original_vcs_bzr = models.TextField(db_column='Original-Vcs-Bzr', blank=True, verbose_name="Original-Vcs-Bzr")
    original_vcs_git = models.TextField(db_column='Original-Vcs-Git', blank=True, verbose_name="Original-Vcs-Git")
    package = models.TextField(db_column='Package', blank=True, verbose_name="Package")
    package_list = models.TextField(db_column='Package-List', blank=True, verbose_name="Package-List")
    priority = models.TextField(db_column='Priority', blank=True)
    python_version = models.TextField(db_column='Python-Version', blank=True)
    python3_version = models.TextField(db_column='Python3-Version', blank=True)
    ruby_versions = models.TextField(db_column='Ruby-Versions', blank=True)
    section = models.TextField(db_column='Section', blank=True)
    standards_version = models.TextField(db_column='Standards-Version', blank=True)
    testsuite = models.TextField(db_column='Testsuite', blank=True)
    uploaders = models.TextField(db_column='Uploaders', blank=True)
    upstream_vcs_bzr = models.TextField(db_column='Upstream-Vcs-Bzr', blank=True)
    vcs_arch = models.TextField(db_column='Vcs-Arch', blank=True)
    vcs_browser = models.TextField(db_column='Vcs-Browser', blank=True)
    vcs_bzr = models.TextField(db_column='Vcs-Bzr', blank=True)
    vcs_cvs = models.TextField(db_column='Vcs-Cvs', blank=True)
    vcs_darcs = models.TextField(db_column='Vcs-Darcs', blank=True)
    vcs_git = models.TextField(db_column='Vcs-Git', blank=True)
    vcs_hg = models.TextField(db_column='Vcs-Hg', blank=True)
    vcs_mtn = models.TextField(db_column='Vcs-Mtn', blank=True)
    vcs_svn = models.TextField(db_column='Vcs-Svn', blank=True)
    vcs_upstream_bzr = models.TextField(db_column='Vcs-Upstream-Bzr', blank=True)
    version = models.TextField(db_column='Version', blank=True)
    
    def __unicode__(self):
        return self.package
    
    class Meta:
        db_table = 'dp_source_info'

class TaskQueue(models.Model):
    package_name = models.ForeignKey(Package, verbose_name="软件包名称")
    dp_server_id = models.ForeignKey(Server, verbose_name="服务器")
    uid = models.ForeignKey(User, verbose_name="用户")
    status = models.CharField(max_length=255L, blank=True, verbose_name="状态")
    used_time = models.CharField(max_length=50L, blank=True, verbose_name="编译时间")
    
    def __unicode__(self):
        return unicode(self.package_name)
    
    class Meta:
        db_table = 'dp_task_queue'
