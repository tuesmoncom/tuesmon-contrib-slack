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

from django.apps import AppConfig
from django.conf.urls import include, url


def connect_tuesmon_contrib_slack_signals():
    from django.db.models import signals
    from tuesmon.projects.history.models import HistoryEntry
    from . import signal_handlers as handlers
    signals.post_save.connect(handlers.on_new_history_entry, sender=HistoryEntry, dispatch_uid="tuesmon_contrib_slack")


def disconnect_tuesmon_contrib_slack_signals():
    from django.db.models import signals
    signals.post_save.disconnect(dispatch_uid="tuesmon_contrib_slack")


class TuesmonContribSlackAppConfig(AppConfig):
    name = "tuesmon_contrib_slack"
    verbose_name = "Tuesmon contrib slack App Config"

    def ready(self):
        from tuesmon.base import routers
        from tuesmon.urls import urlpatterns
        from .api import SlackHookViewSet

        router = routers.DefaultRouter(trailing_slash=False)
        router.register(r"slack", SlackHookViewSet, base_name="slack")
        urlpatterns.append(url(r'^api/v1/', include(router.urls)))

        connect_tuesmon_contrib_slack_signals()
