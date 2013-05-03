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


from django.contrib import admin


from models import (Deb, Favorite, Message, Package, 
                    PackageInfo, Server, SourceFile, SourceInfo,
                    TaskQueue)


admin.site.register(Deb)
admin.site.register(Favorite)
admin.site.register(Message)
admin.site.register(Package)
admin.site.register(PackageInfo)
admin.site.register(Server)
admin.site.register(SourceFile)
admin.site.register(SourceInfo)
admin.site.register(TaskQueue)