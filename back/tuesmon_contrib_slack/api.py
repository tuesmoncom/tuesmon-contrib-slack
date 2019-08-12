# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tuesmon.base import filters
from tuesmon.base import response
from tuesmon.base.api import ModelCrudViewSet
from tuesmon.base.decorators import detail_route

from . import models
from . import serializers
from . import permissions
from . import tasks


class SlackHookViewSet(ModelCrudViewSet):
    model = models.SlackHook
    serializer_class = serializers.SlackHookSerializer
    permission_classes = (permissions.SlackHookPermission,)
    filter_backends = (filters.IsProjectAdminFilterBackend,)
    filter_fields = ("project",)

    @detail_route(methods=["POST"])
    def test(self, request, pk=None):
        slackhook = self.get_object()
        self.check_permissions(request, 'test', slackhook)

        tasks.test_slackhook(slackhook.url, slackhook.channel)

        return response.NoContent()
