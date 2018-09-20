# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.preview.permissions.voice_permission import VoicePermissionList


class Permissions(Version):

    def __init__(self, domain):
        """
        Initialize the Permissions version of Preview

        :returns: Permissions version of Preview
        :rtype: twilio.rest.preview.permissions.Permissions.Permissions
        """
        super(Permissions, self).__init__(domain)
        self.version = 'permissions'
        self._voice_permissions = None

    @property
    def voice_permissions(self):
        """
        :rtype: twilio.rest.preview.permissions.voice_permission.VoicePermissionList
        """
        if self._voice_permissions is None:
            self._voice_permissions = VoicePermissionList(self)
        return self._voice_permissions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Permissions>'