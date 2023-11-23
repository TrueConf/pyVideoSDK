#Conference types
CONFTYPE_symmetric  = "symmetric"
CONFTYPE_asymmetric = "assymetric"                        
CONFTYPE_role       = "role"

CAUSE = {
    0: "Your call has been rejected",
    1: "Maximum number of conference participants is reached",
    2: "Participant is busy",
    3: "User is not available now",
    4: "Invalid conference",
    5: "User not found",
    6: "JOIN_OK",
    7: "Insufficient funds",
    8: "Access denied",
    9: "Rejected by logout",
    10: "The action cannot be completed",
    11: "Rejected by local resource limit",
    12: "Enter conference password",
    13: "Wrong password",
    14: "The user has rejected your call",
    15: "Rejected by bad rating",
    16: "The user does not answer",
    17: "Conference is not active yet",
    18: "Conference is over",
    19: "Conference not found",
    20: "Conference type is not supported"
}

'''
  All Events
'''
EV_ALL = "ALL"
EV_abReceivedAfterLogin = "abReceivedAfterLogin"
EV_allSlidesCachingStopped = "allSlidesCachingStopped"
EV_allSlidesRemoved = "allSlidesRemoved"
EV_appSndDevChanged = "appSndDevChanged"
EV_appStateChanged = "appStateChanged"
EV_appUpdateAvailable = "appUpdateAvailable"
EV_audioCapturerMute = "audioCapturerMute"
EV_audioDelayDetectorTestStateChanged = "audioDelayDetectorTestStateChanged"
EV_audioRendererMute = "audioRendererMute"
EV_authorizationNeeded = "authorizationNeeded"
EV_availableServersListLoaded = "availableServersListLoaded"
EV_backgroundImageChanged = "backgroundImageChanged"
EV_broadcastPictureStateChanged = "broadcastPictureStateChanged"
EV_broadcastSelfieChanged = "broadcastSelfieChanged"
EV_callHistoryCleared = "callHistoryCleared"
EV_cameraStateChangedByConferenceOwner = "cameraStateChangedByConferenceOwner"
EV_chatMessageSent = "chatMessageSent"
EV_cmdChatClear = "cmdChatClear"
EV_commandReceived = "commandReceived"
EV_commandSent = "commandSent"
EV_conferenceCreated = "conferenceCreated"
EV_conferenceDeleted = "conferenceDeleted"
EV_conferenceList = "conferenceList"
EV_contactBlocked = "contactBlocked"
EV_contactsAdded = "contactsAdded"
EV_contactsDeleted = "contactsDeleted"
EV_contactsRenamed = "contactsRenamed"
EV_contactUnblocked = "contactUnblocked"
EV_cropChanged = "cropChanged"
EV_currentSlideIndexChanged = "currentSlideIndexChanged"
EV_currentUserDisplayNameChanged = "currentUserDisplayNameChanged"
EV_currentUserProfileUrlChanged = "currentUserProfileUrlChanged"
EV_customLogoUsageChanged = "customLogoUsageChanged"
EV_dataDeleted = "dataDeleted"
EV_dataSaved = "dataSaved"
EV_detailsInfo = "detailsInfo"
EV_deviceModesDone = "deviceModesDone"
EV_deviceStatusReceived = "deviceStatusReceived"
EV_downloadProgress = "downloadProgress"
EV_dsStarted = "dsStarted"
EV_dsStopped = "dsStopped"
EV_enableAudioReceivingChanged = "enableAudioReceivingChanged"
EV_enableVideoReceivingChanged = "enableVideoReceivingChanged"
EV_extraVideoFlowNotify = "extraVideoFlowNotify"
EV_fileAccepted = "fileAccepted"
EV_fileConferenceSent = "fileConferenceSent"
EV_fileDownloadingProgress = "fileDownloadingProgress"
EV_fileRejected = "fileRejected"
EV_fileSent = "fileSent"
EV_fileStatus = "fileStatus"
EV_fileTransferAvailable = "fileTransferAvailable"
EV_fileTransferCleared = "fileTransferCleared"
EV_fileTransferFileDeleted = "fileTransferFileDeleted"
EV_fileTransferPinChanged = "fileTransferPinChanged"
EV_fileUploadingProgress = "fileUploadingProgress"
EV_groupChatMessageSent = "groupChatMessageSent"
EV_groupsAdded = "groupsAdded"
EV_groupsRemoved = "groupsRemoved"
EV_groupsRenamed = "groupsRenamed"
EV_hangUpPressed = "hangUpPressed"
EV_hardwareChanged = "hardwareChanged"
EV_hookOffPressed = "hookOffPressed"
EV_httpServerSettingChanged = "httpServerSettingChanged"
EV_httpServerStateChanged = "httpServerStateChanged"
EV_imageAddedToCachingQueue = "imageAddedToCachingQueue"
EV_imageRemovedFromCachingQueue = "imageRemovedFromCachingQueue"
EV_incomingChatMessage = "incomingChatMessage"
EV_incomingGroupChatMessage = "incomingGroupChatMessage"
EV_incomingPodiumInvitationRemoved = "incomingPodiumInvitationRemoved"
EV_incomingRequestCameraControlAccepted = "incomingRequestCameraControlAccepted"
EV_incomingRequestCameraControlRejected = "incomingRequestCameraControlRejected"
EV_incomingRequestToPodiumAnswered = "incomingRequestToPodiumAnswered"
EV_inviteReceived = "inviteReceived"
EV_inviteRequestSent = "inviteRequestSent"
EV_inviteSent = "inviteSent"
EV_joinToConferenceLinkReceived = "joinToConferenceLinkReceived"
EV_lastCallsViewed = "lastCallsViewed"
EV_licenseActivation = "licenseActivation"
EV_licenseStatusChanged = "licenseStatusChanged"
EV_login = "login"
EV_logoImageChanged = "logoImageChanged"
EV_logout = "logout"
EV_micStateChangedByConferenceOwner = "micStateChangedByConferenceOwner"
EV_monitorsInfoUpdated = "monitorsInfoUpdated"
EV_myEvent = "myEvent"
EV_mySlideShowStarted = "mySlideShowStarted"
EV_mySlideShowStopped = "mySlideShowStopped"
EV_mySlideShowTitleChanged = "mySlideShowTitleChanged"
EV_NDIDeviceCreated = "NDIDeviceCreated"
EV_NDIDeviceDeleted = "NDIDeviceDeleted"
EV_NDIStateChanged = "NDIStateChanged"
EV_newParticipantInConference = "newParticipantInConference"
EV_outgoingBitrateChanged = "outgoingBitrateChanged"
EV_outgoingRequestCameraControlAccepted = "outgoingRequestCameraControlAccepted"
EV_outgoingRequestCameraControlRejected = "outgoingRequestCameraControlRejected"
EV_outputSelfVideoRotateAngleChanged = "outputSelfVideoRotateAngleChanged"
EV_participantLeftConference = "participantLeftConference"
EV_peerAccepted = "peerAccepted"
EV_propertiesUpdated = "propertiesUpdated"
EV_ptzControlsChanged = "ptzControlsChanged"
EV_realtimeManagmentUrlAvailabilityChanged = "realtimeManagmentUrlAvailabilityChanged"
EV_receivedFileRequest = "receivedFileRequest"
EV_receiversInfoUpdated = "receiversInfoUpdated"
EV_recordRequest = "recordRequest"
EV_recordRequestReply = "recordRequestReply"
EV_rejectReceived = "rejectReceived"
EV_rejectSent = "rejectSent"
EV_remarkCountDown = "remarkCountDown"
EV_remotelyControlledCameraNotAvailableAnymore = "remotelyControlledCameraNotAvailableAnymore"
EV_requestCameraControlReceived = "requestCameraControlReceived"
EV_requestCameraControlSent = "requestCameraControlSent"
EV_requestInviteReceived = "requestInviteReceived"
EV_roleEventOccured = "roleEventOccured"
EV_serverConnected = "serverConnected"
EV_serverDisconnected = "serverDisconnected"
EV_settingsChanged = "settingsChanged"
EV_showCurrentUserWidget = "showCurrentUserWidget"
EV_showIncomingRequestWidget = "showIncomingRequestWidget"
EV_showInfoConnect = "showInfoConnect"
EV_showLogo = "showLogo"
EV_showTime = "showTime"
EV_showUpcomingMeetings = "showUpcomingMeetings"
EV_slideAdded = "slideAdded"
EV_slideCached = "slideCached"
EV_slideCachingStarted = "slideCachingStarted"
EV_slidePositionChanged = "slidePositionChanged"
EV_slideRemoved = "slideRemoved"
EV_slideShowAvailabilityChanged = "slideShowAvailabilityChanged"
EV_slideShowCleared = "slideShowCleared"
EV_slidesSorted = "slidesSorted"
EV_slideUploaded = "slideUploaded"
EV_stopCalling = "stopCalling"
EV_systemRatingUpdated = "systemRatingUpdated"
EV_tariffRestrictionsChanged = "tariffRestrictionsChanged"
EV_testAudioCapturerLevel = "testAudioCapturerLevel"
EV_testAudioCapturerStateChanged = "testAudioCapturerStateChanged"
EV_toneDial = "toneDial"
EV_updateAvatar = "updateAvatar"
EV_updateCameraInfo = "updateCameraInfo"
EV_updateFailed = "updateFailed"
EV_userRecordingMeStatusChanged = "userRecordingMeStatusChanged"
EV_usersAddedToGroups = "usersAddedToGroups"
EV_usersRemovedFromGroups = "usersRemovedFromGroups"
EV_usersStatusesChanged = "usersStatusesChanged"
EV_videoCapturerMute = "videoCapturerMute"
EV_videoMatrixChanged = "videoMatrixChanged"
EV_videoSlotMovedToMonitor = "videoSlotMovedToMonitor"
EV_videoSlotRemovedFromMonitor = "videoSlotRemovedFromMonitor"
EV_windowStateChanged = "windowStateChanged"

EVENT = {
    EV_ALL: {},
    EV_appStateChanged: {"event": "appStateChanged", "appState": None},
    EV_incomingChatMessage: {"event": "incomingChatMessage", "peerId": None, "message": None, "time": None, "method": "event"},
    EV_inviteReceived: {"event": "inviteReceived", "peerId": None, "peerDn": None, "type": None, "confId": None, "method": "event"},
    EV_rejectReceived: {"event": "rejectReceived", "cause": None, "peerId": None, "peerDn": None, "method": "event"},
    EV_myEvent: {"event": "myEvent", "data": None, "method": "event"},
    EV_abReceivedAfterLogin: {"event": "abReceivedAfterLogin", "abook": None, "method": "event"},
    EV_allSlidesCachingStopped: {"event": "allSlidesCachingStopped", "method": "event"},
    EV_allSlidesRemoved: {"event": "allSlidesRemoved", "removedFromServer": None, "method": "event"},
    EV_appSndDevChanged: {"event": "appSndDevChanged", "name": None, "description": None, "method": "event"},
    EV_audioCapturerMute: {"event": "audioCapturerMute", "mute": None, "method": "event"},
    EV_audioDelayDetectorTestStateChanged: {"event": "audioDelayDetectorTestStateChanged", "state": None, "delay": None, "method": "event"},
    EV_audioRendererMute: {"event": "audioRendererMute", "mute": None, "method": "event"},
    EV_authorizationNeeded: {"event": "authorizationNeeded", "cause": None, "method": "event"},
    EV_availableServersListLoaded: {"event": "availableServersListLoaded", "serverList": None, "method": "event"},
    EV_backgroundImageChanged: {"event": "backgroundImageChanged", "isCustomImage": None, "fileId": None, "method": "event"},
    EV_broadcastPictureStateChanged: {"event": "broadcastPictureStateChanged", "running": None, "fileName": None, "fileId": None, "method": "event"},
    EV_broadcastSelfieChanged: {"event": "broadcastSelfieChanged", "enabled": None, "fps": None, "method": "event"},
    EV_callHistoryCleared: {"event": "callHistoryCleared", "method": "event"},
    EV_cameraStateChangedByConferenceOwner: {"event": "cameraStateChangedByConferenceOwner", "mute": None, "confId": None, "method": "event"},
    EV_chatMessageSent: {"event": "chatMessageSent", "peerId": None, "message": None, "method": "event"},
    EV_cmdChatClear: {"event": "cmdChatClear", "id": None, "method": "event"},
    EV_commandReceived: {"event": "commandReceived", "peerId": None, "command": None, "method": "event"},
    EV_commandSent: {"event": "commandSent", "peerId": None, "command": None, "confId": None, "method": "event"},
    EV_conferenceCreated: {
        "event": "conferenceCreated",
        "confId": None,
        "confTitle": None,
        "confType": None,
        "conferenceOwner": None,
        "joinUrl": None,
        "realTimeConferenceManagmentUrl": None,
        "method": "event"
    },
    EV_conferenceDeleted: {"event": "conferenceDeleted", "confId": None, "method": "event"},
    EV_conferenceList: {"event": "conferenceList", "cnt": None, "conferences": None, "succeed": None, "method": "event"},
    EV_contactBlocked: {"event": "contactBlocked", "peerId": None, "peerDn": None, "method": "event"},
    EV_contactsAdded: {"event": "contactsAdded", "contacts": None, "method": "event"},
    EV_contactsDeleted: {"event": "contactsDeleted", "contacts": None, "method": "event"},
    EV_contactsRenamed: {"event": "contactsRenamed", "contacts": None, "method": "event"},
    EV_contactUnblocked: {"event": "contactUnblocked", "peerId": None, "peerDn": None, "method": "event"},
    EV_cropChanged: {"event": "cropChanged", "cropImageStatus": None, "method": "event"},
    EV_currentSlideIndexChanged: {"event": "currentSlideIndexChanged", "currentIdx": None, "method": "event"},
    EV_currentUserDisplayNameChanged: {"event": "currentUserDisplayNameChanged", "peerDn:": None, "method": "event"},
    EV_currentUserProfileUrlChanged: {"event": "currentUserProfileUrlChanged", "url": None, "method": "event"},
    EV_customLogoUsageChanged: {"event": "customLogoUsageChanged", "use": None, "method": "event"},
    EV_dataDeleted: {"event": "dataDeleted", "containerName": None, "method": "event"},
    EV_dataSaved: {"event": "dataSaved", "containerName": None, "data": None, "flag": None, "method": "event"},
    EV_detailsInfo: {
        "event": "detailsInfo",
        "peerId": None,
        "peerDn": None,
        "firstName": None,
        "lastName": None,
        "mobilePhone": None,
        "workPhone": None,
        "homePhone": None,
        "company": None,
        "isEditable": None,
        "method": "event"
    },
    EV_deviceModesDone: {
        "event": "deviceModesDone",
        "videoCapturerName": None,
        "videoCapturerDescription": None,
        "modeList": None,
        "pinList": None,
        "activePin": None,
        "activeMode": None,
        "supportPTZ": None,
        "method": "event"
    },
    EV_deviceStatusReceived: {
        "event": "deviceStatusReceived",
        "peerId": None,
        "mic": None,
        "confId": None,
        "video": None,
        "method": "event"
    },
    EV_dsStarted: {"event": "dsStarted", "captureId": None, "name": None, "method": "event"},
    EV_dsStopped: {"event": "dsStopped", "captureId": None, "method": "event"},
    EV_enableAudioReceivingChanged: {"event": "enableAudioReceivingChanged", "peerId": None, "enable": None, "method": "event"},
    EV_enableVideoReceivingChanged: {"event": "enableVideoReceivingChanged", "peerId": None, "enable": None, "method": "event"},
    EV_extraVideoFlowNotify: {
        "event": "extraVideoFlowNotify",
        "peerId": None,
        "confId": None,
        "extraVideo": None,
        "method": "event"
    },
    EV_fileAccepted: {"event": "fileAccepted", "id": None, "confId": None, "method": "event"},
    EV_fileConferenceSent: {
        "event": "fileConferenceSent",
        "name": None,
        "id": None,
        "fileId": None,
        "confId": None,
        "method": "event"
    },
    EV_fileDownloadingProgress: {
        "event": "fileDownloadingProgress",
        "totalSize": None,
        "processedSize": None,
        "speed": None,
        "id": None,
        "status": None,
        "fileId": None,
        "fileName": None,
        "peerId": None,
        "peerDisplayName": None,
        "confId": None,
        "timestamp": None,
        "method": "event"
    },
    EV_fileRejected: {"event": "fileRejected", "id": None, "confId": None, "method": "event"},
    EV_fileSent: {
        "event": "fileSent",
        "name": None,
        "id": None,
        "peerId": None,
        "peerDn": None,
        "fileId": None,
        "confId": None,
        "method": "event"
    },
    EV_fileStatus: {
        "event": "fileStatus",
        "id": None,
        "status": None,
        "directionType": None,
        "confId": None,
        "method": "event"
    },
    EV_fileTransferAvailable: {"event": "fileTransferAvailable", "available": None, "method": "event"},
    EV_fileTransferCleared: {"event": "fileTransferCleared", "method": "event"},
    EV_fileTransferFileDeleted: {"event": "fileTransferFileDeleted", "file": None, "method": "event"},
    EV_fileUploadingProgress: {
        "event": "fileUploadingProgress",
        "totalSize": None,
        "processedSize": None,
        "speed": None,
        "id": None,
        "status": None,
        "directionType": None,
        "fileName": None,
        "fileId": None,
        "peerId": None,
        "peerDisplayName": None,
        "confId": None,
        "timestamp": None,
        "method": "event"
    },
    EV_groupChatMessageSent: {"event": "groupChatMessageSent", "message": None, "method": "event"},
    EV_groupsAdded: {"event": "groupsAdded", "groups": None, "method": "event"},
    EV_groupsRemoved: {"event": "groupsRemoved", "groups": None, "method": "event"},
    EV_groupsRenamed: {"event": "groupsRenamed", "groups": None, "method": "event"},
    EV_hardwareChanged: {
        "event": "hardwareChanged",
        "audioCapturers": None,
        "currentAudioCapturerName": None,
        "currentAudioCapturerDescription": None,
        "currentAudioCapturerType": None,
        "audioRenderers": None,
        "currentAudioRendererName": None,
        "currentAudioRendererDescription": None,
        "currentAudioRendererType": None,
        "videoCapturers": None,
        "currentVideoCapturerName": None,
        "currentVideoCapturerDescription": None,
        "currentVideoCapturerType": None,
        "DSCaptureList": None,
        "method": "event"
    },
    EV_httpServerSettingChanged: {
        "event": "httpServerSettingChanged",
        "name": None,
        "value": None,
        "httpServerRestartNeededForApplying": None,
        "isPendingToBeApplied": None,
        "pendingValue": None,
        "method": "event"
    },
    EV_httpServerStateChanged: {"event": "httpServerStateChanged", "state": None, "method": "event"},
    EV_imageAddedToCachingQueue: {"event": "imageAddedToCachingQueue", "name": None, "fileId": None, "method": "event"},
    EV_imageRemovedFromCachingQueue: {"event": "imageRemovedFromCachingQueue", "name": None, "fileId": None, "method": "event"},
    EV_incomingGroupChatMessage: {
        "event": "incomingGroupChatMessage",
        "peerId": None,
        "peerDn": None,
        "message": None,
        "time": None,
        "confId": None,
        "method": "event"
    },
    EV_incomingPodiumInvitationRemoved: {"event": "incomingPodiumInvitationRemoved", "confId": None, "reason": None, "method": "event"},
    EV_incomingRequestCameraControlAccepted: {"event": "incomingRequestCameraControlAccepted", "callId": None, "method": "event"},
    EV_incomingRequestCameraControlRejected: {"event": "incomingRequestCameraControlRejected", "callId": None, "reason": None, "method": "event"},
    EV_incomingRequestToPodiumAnswered: {"event": "incomingRequestToPodiumAnswered", "peerId": None, "allow": None, "confId": None, "method": "event"},
    EV_inviteRequestSent: {"event": "inviteRequestSent", "peerId": None, "peerDn": None, "method": "event"},
    EV_inviteSent: {
        "event": "inviteSent",
        "peerId": None,
        "peerDn": None,
        "confType": None,
        "confId": None,
        "method": "event"
    },
    EV_joinToConferenceLinkReceived: {"event": "joinToConferenceLinkReceived", "confId": None, "link": None, "method": "event"},
    EV_lastCallsViewed: {"event": "lastCallsViewed", "lastView": None, "method": "event"},
    EV_licenseActivation: {
        "event": "licenseActivation",
        "status": None,
        "tariff": None,
        "start_date": None,
        "end_date": None,
        "method": "event"
    },
    EV_licenseStatusChanged: {"event": "licenseStatusChanged", "pro": None, "start_date": None, "end_date": None, "method": "event"},
    EV_login: {"event": "login", "result": None, "peerId": None, "peerDn": None, "method": "event"},
    EV_logoImageChanged: {"event": "logoImageChanged", "isCustomImage": None, "fileId": None, "mode": None, "method": "event"},
    EV_logout: {"event": "logout", "result": None, "cause": None, "method": "event"},
    EV_micStateChangedByConferenceOwner: {"event": "micStateChangedByConferenceOwner", "mute": None, "confId": None, "method": "event"},
    EV_monitorsInfoUpdated: {"event": "monitorsInfoUpdated", "monitors": None, "currentMonitor": None, "method": "event"},
    EV_mySlideShowStarted: {"event": "mySlideShowStarted", "title": None, "currentSlideIndex": None, "method": "event"},
    EV_mySlideShowStopped: {"event": "mySlideShowStopped", "method": "event"},
    EV_mySlideShowTitleChanged: {"event": "mySlideShowTitleChanged", "newTitle": None, "method": "event"},
    EV_NDIDeviceCreated: {"event": "NDIDeviceCreated", "deviceId": None, "displayName": None, "mixedType": None, "method": "event"},
    EV_NDIDeviceDeleted: {"event": "NDIDeviceDeleted", "deviceId": None, "displayName": None, "mixedType": None, "method": "event"},
    EV_NDIStateChanged: {"event": "NDIStateChanged", "enabled": None, "method": "event"},
    EV_newParticipantInConference: {
        "event": "newParticipantInConference",
        "peerId": None,
        "peerDn": None,
        "confId": None,
        "method": "event"
    },
    EV_outgoingBitrateChanged: {"event": "outgoingBitrateChanged", "bitrate": None, "method": "event"},
    EV_outgoingRequestCameraControlAccepted: {"event": "outgoingRequestCameraControlAccepted", "callId": None, "method": "event"},
    EV_outgoingRequestCameraControlRejected: {"event": "outgoingRequestCameraControlRejected", "callId": None, "reason": None, "method": "event"},
    EV_outputSelfVideoRotateAngleChanged: {"event": "outputSelfVideoRotateAngleChanged", "rotateAngle": None, "method": "event"},
    EV_participantLeftConference: {"event": "participantLeftConference", "peerId": None, "method": "event"},
    EV_peerAccepted: {"event": "peerAccepted", "peerId": None, "peerDn": None, "confId": None, "method": "event"},
    EV_propertiesUpdated: {"event": "propertiesUpdated", "properties": None, "method": "event"},
    EV_ptzControlsChanged: {"event": "ptzControlsChanged", "pan": None, "tilt": None, "zoom": None, "videoCapturerName": None, "videoCapturerDescription": None, "method": "event"},
    EV_realtimeManagmentUrlAvailabilityChanged: {"event": "realtimeManagmentUrlAvailabilityChanged", "available": None, "url": None, "confId": None, "method": "event"},
    EV_receivedFileRequest: {
        "event": "receivedFileRequest",
        "id": None,
        "peerId": None,
        "peerDn": None,
        "fileName": None,
        "confId": None,
        "method": "event"
    },
    EV_receiversInfoUpdated: {"event": "receiversInfoUpdated", "receivers": None, "confId": None, "method": "event"},
    EV_recordRequest: {"event": "recordRequest", "peerId": None, "peerDn": None, "confId": None, "method": "event"},
    EV_recordRequestReply: {"event": "recordRequestReply", "peerId": None, "recordAllowed": None, "confId": None, "method": "event"},
    EV_rejectSent: {"event": "rejectSent", "peerId": None, "recordAllowed": None, "confId": None, "cause": None, "method": "event"},
    EV_remarkCountDown: {"event": "remarkCountDown", "timeout": None, "confId": None, "method": "event"},
    EV_remotelyControlledCameraNotAvailableAnymore: {"event": "remotelyControlledCameraNotAvailableAnymore", "callId": None, "method": "event"},
    EV_requestCameraControlReceived: {"event": "requestCameraControlReceived", "callId": None, "method": "event"},
    EV_requestCameraControlSent: {"event": "requestCameraControlSent", "callId": None, "method": "event"},
    EV_requestInviteReceived: {"event": "requestInviteReceived", "peerId": None, "peerDn": None, "confId": None, "method": "event"},
    EV_roleEventOccured: {
        "event": "roleEventOccured",
        "peerId": None,
        "peerDn": None,
        "role": None,
        "type": None,
        "result": None,
        "broadcast": None,
        "confId": None,
        "method": "event"
    },
    EV_serverConnected: {"event": "serverConnected", "service": None, "server": None, "port": None, "domain": None, "method": "event"},
    EV_serverDisconnected: {"event": "serverDisconnected", "service": None, "server": None, "port": None, "method": "event"},
    EV_settingsChanged: {"event": "settingsChanged", "name": None, "value": None, "method": "event"},
    EV_showCurrentUserWidget: {"event": "showCurrentUserWidget", "show": None, "method": "event"},
    EV_showIncomingRequestWidget: {"event": "showIncomingRequestWidget", "method": "event"},
    EV_showInfoConnect: {"event": "showInfoConnect", "show": None, "method": "event"},
    EV_showLogo: {"event": "showLogo", "show": None, "method": "event"},
    EV_showTime: {"event": "showTime", "show": None, "method": "event"},
    EV_showUpcomingMeetings: {"event": "showUpcomingMeetings", "method": "event"},
    EV_slideAdded: {"event": "slideAdded", "name": None, "fileId": None, "idx": None, "method": "event"},
    EV_slideCached: {"event": "slideCached", "name": None, "fileId": None, "method": "event"},
    EV_slideCachingStarted: {"event": "slideCachingStarted", "name": None, "fileId": None, "method": "event"},
    EV_slidePositionChanged: {
        "event": "slidePositionChanged",
        "prevIdx": None,
        "newIdx": None,
        "name": None,
        "fileId": None,
        "method": "event"
    },
    EV_slideRemoved: {"event": "slideRemoved", "idx": None, "removedFromServer": None, "method": "event"},
    EV_slideShowAvailabilityChanged: {"event": "slideShowAvailabilityChanged", "available": None, "method": "event"},
    EV_slideShowCleared: {"event": "slideShowCleared", "method": "event"},
    EV_slidesSorted: {"event": "slidesSorted", "slides": None, "method": "event"},
    EV_slideUploaded: {"event": "slideUploaded", "idx": None, "url": None, "method": "event"},
    EV_stopCalling: {"event": "stopCalling", "peerId": None, "side": None,  "method": "event"},
    EV_systemRatingUpdated: {"event": "systemRatingUpdated", "videoQuality": None, "videoContentLevels": None, "method": "event"},
    EV_tariffRestrictionsChanged: {
        "event": "tariffRestrictionsChanged",
        "tariffName": None,
        "p2p": None,
        "createMulti": None,
        "symMaxNumber": None,
        "asymMaxNumber": None,
        "roleMaxNumber": None,
        "rlMaxNumber": None,
        "canUseSlideShow": None,
        "canUseDesktopSharing": None,
        "canChangeAddressBook": None,
        "canEditGroups": None,
        "canUseDialer": None,
        "method": "event"
    },
    EV_testAudioCapturerLevel: {"event": "testAudioCapturerLevel", "lvl": None, "method": "event"},
    EV_testAudioCapturerStateChanged: {"event": "testAudioCapturerStateChanged", "started": None, "method": "event"},
    EV_toneDial: {"event": "toneDial", "symbol": None, "confId": None, "callId": None, "method": "event"},
    EV_updateAvatar: {"event": "updateAvatar", "peerId": None, "method": "event"},
    EV_updateCameraInfo: {
        "event": "updateCameraInfo",
        "cameraWidth": None,
        "cameraHeight": None,
        "cameraFramerate": None,
        "sendWidth": None,
        "sendHeight": None,
        "format": None,
        "sendFormat": None,
        "sendFramerate": None,
        "stereo": None,
        "method": "event"
    },
    EV_userRecordingMeStatusChanged: {"event": "userRecordingMeStatusChanged", "peerId": None, "status": None, "confId": None, "method": "event"},
    EV_usersAddedToGroups: {"event": "usersAddedToGroups", "addedUsers": None, "method": "event"},
    EV_usersRemovedFromGroups: {"event": "usersRemovedFromGroups", "removedUsers": None, "method": "event"},
    EV_usersStatusesChanged: {"event": "usersStatusesChanged", "usersStatuses": None, "method": "event"},
    EV_videoCapturerMute: {"event": "videoCapturerMute", "mute": None, "method": "event"},
    EV_videoMatrixChanged: {
        "event": "videoMatrixChanged",
        "matrixType": None,
        "mainWindowWidth": None,
        "mainWindowHeight": None,
        "selfViewMode": None,
        "participants": None,
        "externVideoSlots": None,
        "hiddenVideoSlots": None,
        "method": "event"
    },
    EV_videoSlotMovedToMonitor: {
        "event": "videoSlotMovedToMonitor",
        "callId": None,
        "peerDn": None,
        "monitorDisplayName": None,
        "monitorIdx": None,
        "monitorIsPrimary": None,
        "method": "event"
    },
    EV_videoSlotRemovedFromMonitor: {"event": "videoSlotRemovedFromMonitor", "callId": None, "monitorDisplayName": None, "monitorIdx": None, "monitorIsPrimary": None, "method": "event"},
    EV_windowStateChanged: {"event": "windowStateChanged", "windowState": None, "stayOnTop": None, "method": "event"},
}

'''
  All Methods
'''
M_accept = "accept"
M_acceptFile = "acceptFile"
M_acceptInvitationToPodium = "acceptInvitationToPodium"
M_acceptPeer = "acceptPeer"
M_acceptRequestCameraControl = "acceptRequestCameraControl"
M_acceptRequestToPodium = "acceptRequestToPodium"
M_activateLicense = "activateLicense"
M_addSlide = "addSlide"
M_addToAbook = "addToAbook"
M_addToGroup = "addToGroup"
M_allowRecord = "allowRecord"
M_auth = "auth"
M_block = "block"
M_call = "call"
M_cancelUpdate = "cancelUpdate"
M_changeCurrentMonitor = "changeCurrentMonitor"
M_changeVideoMatrix = "changeVideoMatrix"
M_changeVideoMatrixType = "changeVideoMatrixType"
M_changeWindowState = "changeWindowState"
M_chatClear = "chatClear"
M_checkFileTransferPIN = "checkFileTransferPIN"
M_clearCallHistory = "clearCallHistory"
M_clearFileTransfer = "clearFileTransfer"
M_clearTokens = "clearTokens"
M_connectToServer = "connectToServer"
M_connectToService = "connectToService"
M_createConference = "createConference"
M_createGroup = "createGroup"
M_createNDIDevice = "createNDIDevice"
M_deleteData = "deleteData"
M_deleteFileTransferFile = "deleteFileTransferFile"
M_deleteNDIDevice = "deleteNDIDevice"
M_denyRecord = "denyRecord"
M_enableAudioReceiving = "enableAudioReceiving"
M_enableVideoReceiving = "enableVideoReceiving"
M_expandCallToMulti = "expandCallToMulti"
M_fireMyEvent = "fireMyEvent"
M_getAbook = "getAbook"
M_getAllUserContainersNames = "getAllUserContainersNames"
M_getAppSndDev = "getAppSndDev"
M_getAppState = "getAppState"
M_getAudioDelayDetectorInfo = "getAudioDelayDetectorInfo"
M_getAudioMute = "getAudioMute"
M_getAudioReceivingLevel = "getAudioReceivingLevel"
M_getAuthInfo = "getAuthInfo"
M_getAvailableServersList = "getAvailableServersList"
M_getBackground = "getBackground"
M_getBanList = "getBanList"
M_getBroadcastPicture = "getBroadcastPicture"
M_getBroadcastSelfie = "getBroadcastSelfie"
M_getCallHistory = "getCallHistory"
M_getChatLastMessages = "getChatLastMessages"
M_getConferenceParticipants = "getConferenceParticipants"
M_getConferences = "getConferences"
M_getConnected = "getConnected"
M_getContactDetails = "getContactDetails"
M_getCreatedNDIDevices = "getCreatedNDIDevices"
M_getCrop = "getCrop"
M_getCurrentUserProfileUrl = "getCurrentUserProfileUrl"
M_getDisplayNameById = "getDisplayNameById"
M_getFileInfo = "getFileInfo"
M_getFileList = "getFileList"
M_getFileRequests = "getFileRequests"
M_getFileTransferAvailability = "getFileTransferAvailability"
M_getFileTransferInfo = "getFileTransferInfo"
M_getFileTransferPIN = "getFileTransferPIN"
M_getFileUploads = "getFileUploads"
M_getGroups = "getGroups"
M_getHardware = "getHardware"
M_getHardwareKey = "getHardwareKey"
M_getHttpServerSettings = "getHttpServerSettings"
M_getHttpServerState = "getHttpServerState"
M_getIncomingCameraControlRequests = "getIncomingCameraControlRequests"
M_getInfoWidgetsState = "getInfoWidgetsState"
M_getLastCallsViewTime = "getLastCallsViewTime"
M_getLastSelectedConference = "getLastSelectedConference"
M_getLastUsedServersList = "getLastUsedServersList"
M_getLicenseServerStatus = "getLicenseServerStatus"
M_getLicenseType = "getLicenseType"
M_getListOfChats = "getListOfChats"
M_getLogin = "getLogin"
M_getLogo = "getLogo"
M_getMaxConfTitleLength = "getMaxConfTitleLength"
M_getMicMute = "getMicMute"
M_getModes = "getModes"
M_getMonitorsInfo = "getMonitorsInfo"
M_getNDIState = "getNDIState"
M_getOutgoingBitrate = "getOutgoingBitrate"
M_getOutgoingCameraControlRequests = "getOutgoingCameraControlRequests"
M_getOutputSelfVideoRotateAngle = "getOutputSelfVideoRotateAngle"
M_getProperties = "getProperties"
M_getPtzControls = "getPtzControls"
M_getRemotelyControlledCameras = "getRemotelyControlledCameras"
M_getRenderInfo = "getRenderInfo"
M_getScheduler = "getScheduler"
M_getServerDomain = "getServerDomain"
M_getSettings = "getSettings"
M_getShowFileTransferTools = "getShowFileTransferTools"
M_getSlideShowCache = "getSlideShowCache"
M_getSlideShowInfo = "getSlideShowInfo"
M_getSystemInfo = "getSystemInfo"
M_getTariffRestrictions = "getTariffRestrictions"
M_getTokenForHttpServer = "getTokenForHttpServer"
M_getTrueConfRoomProKey = "getTrueConfRoomProKey"
M_getUpdateInfo = "getUpdateInfo"
M_getVideoMatrix = "getVideoMatrix"
M_getVideoMute = "getVideoMute"
M_gotoPodium = "gotoPodium"
M_hangUp = "hangUp"
M_hideVideoSlot = "hideVideoSlot"
M_inviteToConference = "inviteToConference"
M_inviteToPodium = "inviteToPodium"
M_kickFromPodium = "kickFromPodium"
M_kickPeer = "kickPeer"
M_leavePodium = "leavePodium"
M_loadData = "loadData"
M_login = "login"
M_logout = "logout"
M_moveVideoSlotToMonitor = "moveVideoSlotToMonitor"
M_productRegistrationOffline = "productRegistrationOffline"
M_ptzDown = "ptzDown"
M_ptzLeft = "ptzLeft"
M_ptzRight = "ptzRight"
M_ptzStop = "ptzStop"
M_ptzUp = "ptzUp"
M_ptzZoomDec = "ptzZoomDec"
M_ptzZoomInc = "ptzZoomInc"
M_rebootSystem = "rebootSystem"
M_reject = "reject"
M_rejectFile = "rejectFile"
M_rejectInvitationToPodium = "rejectInvitationToPodium"
M_rejectPeer = "rejectPeer"
M_rejectRequestCameraControl = "rejectRequestCameraControl"
M_rejectRequestToPodium = "rejectRequestToPodium"
M_remotelyControlledCameraPtzDown = "remotelyControlledCameraPtzDown"
M_remotelyControlledCameraPtzLeft = "remotelyControlledCameraPtzLeft"
M_remotelyControlledCameraPtzRight = "remotelyControlledCameraPtzRight"
M_remotelyControlledCameraPtzUp = "remotelyControlledCameraPtzUp"
M_remotelyControlledCameraPtzZoomDec = "remotelyControlledCameraPtzZoomDec"
M_remotelyControlledCameraPtzZoomInc = "remotelyControlledCameraPtzZoomInc"
M_removeAllSlides = "removeAllSlides"
M_removeFromAbook = "removeFromAbook"
M_removeFromGroup = "removeFromGroup"
M_removeFromServersList = "removeFromServersList"
M_removeGroup = "removeGroup"
M_removeImageFromCachingQueue = "removeImageFromCachingQueue"
M_removeSlide = "removeSlide"
M_removeVideoSlotFromMonitor = "removeVideoSlotFromMonitor"
M_renameGroup = "renameGroup"
M_renameInAbook = "renameInAbook"
M_requestParticipantCameraControl = "requestParticipantCameraControl"
M_resetFileTransferPIN = "resetFileTransferPIN"
M_restoreWindow = "restoreWindow"
M_saveData = "saveData"
M_sendCommand = "sendCommand"
M_sendConferenceFile = "sendConferenceFile"
M_sendFile = "sendFile"
M_sendGroupMessage = "sendGroupMessage"
M_sendMessage = "sendMessage"
M_setAppSndDev = "setAppSndDev"
M_setAudioCapturer = "setAudioCapturer"
M_setAudioMute = "setAudioMute"
M_setAudioReceivingLevel = "setAudioReceivingLevel"
M_setAudioRenderer = "setAudioRenderer"
M_setAuthParams = "setAuthParams"
M_setBackground = "setBackground"
M_setBroadcastSelfie = "setBroadcastSelfie"
M_setCrop = "setCrop"
M_setDefaultBackground = "setDefaultBackground"
M_setDefaultLogo = "setDefaultLogo"
M_setHttpServerSettings = "setHttpServerSettings"
M_setLastCallsViewed = "setLastCallsViewed"
M_setLogo = "setLogo"
M_setMicMute = "setMicMute"
M_setModeratorRole = "setModeratorRole"
M_setModes = "setModes"
M_setNDIState = "setNDIState"
M_setOutputSelfVideoRotateAngle = "setOutputSelfVideoRotateAngle"
M_setPanPos = "setPanPos"
M_setPtzDefaults = "setPtzDefaults"
M_setSettings = "setSettings"
M_setShowFileTransferTools = "setShowFileTransferTools"
M_setSlidePosition = "setSlidePosition"
M_setTiltPos = "setTiltPos"
M_setUsedApiVersion = "setUsedApiVersion"
M_setVideoCapturer = "setVideoCapturer"
M_setVideoMute = "setVideoMute"
M_setZoomPos = "setZoomPos"
M_showFirstSlide = "showFirstSlide"
M_showLastSlide = "showLastSlide"
M_showNextSlide = "showNextSlide"
M_showPrevSlide = "showPrevSlide"
M_showSlide = "showSlide"
M_showVideoSlot = "showVideoSlot"
M_shutdown = "shutdown"
M_shutdownSystem = "shutdownSystem"
M_sortSlides = "sortSlides"
M_startAudioDelayDetectorTest = "startAudioDelayDetectorTest"
M_startBroadcastPicture = "startBroadcastPicture"
M_startCapture = "startCapture"
M_startHttpServer = "startHttpServer"
M_startRemark = "startRemark"
M_startSlideShow = "startSlideShow"
M_startUpdate = "startUpdate"
M_stopAudioDelayDetectorTest = "stopAudioDelayDetectorTest"
M_stopBroadcastPicture = "stopBroadcastPicture"
M_stopCachingAllImages = "stopCachingAllImages"
M_stopCapture = "stopCapture"
M_stopHttpServer = "stopHttpServer"
M_stopSlideShow = "stopSlideShow"
M_swapVideoSlots = "swapVideoSlots"
M_switchVideoFlow = "switchVideoFlow"
M_testAudioCapturerStart = "testAudioCapturerStart"
M_testAudioCapturerStop = "testAudioCapturerStop"
M_testAudioRenderer = "testAudioRenderer"
M_toneDial = "toneDial"
M_turnRemoteCamera = "turnRemoteCamera"
M_turnRemoteMic = "turnRemoteMic"
M_turnRemoteSpeaker = "turnRemoteSpeaker"
M_unblock = "unblock"
# version 4.2
M_searchContact = "searchContact"

METHOD_RESPONSE = {
    M_getHardware: {
      "method": "getHardware",
      "audioCapturers": None,
      "currentAudioCapturerName": None,
      "currentAudioCapturerDescription": None,
      #"currentAudioCapturerType": None, # version 4.1 or later
      "audioRenderers": None,
      "currentAudioRendererName": None,
      "currentAudioRendererDescription": None,
      #"currentAudioRendererType": None, # version 4.1 or later
      "videoCapturers": None,
      "currentVideoCapturerName": None,
      "currentVideoCapturerDescription": None,
      "currentVideoCapturerType": None,
      "DSCaptureList": None,
      "result": None
    },
    M_acceptFile: {"method": "acceptFile", "result": None},
    M_acceptInvitationToPodium: {"method" : "acceptInvintationToPodium", "result": None},
    M_acceptRequestCameraControl: {"method": "acceptRequestCameraControl", "result": None},
    M_acceptRequestToPodium: {"method": "acceptRequestToPodium", "result": None},
    M_activateLicense: {"method": "activateLicense", "status": None, "result": None},
    M_addSlide: {"method": "addSlide", "result": None},
    M_addToAbook: {"method": "addToAbook", "peerId": None, "result": None},
    M_addToGroup: {"method": "addToGroup", "result": None},
    M_allowRecord: {"method": "allowRecord", "result": None},
    M_block: {"method": "block", "peerId": None, "result": None},
    M_changeCurrentMonitor: {"method": "changeCurrentMonitor", "result": None},
    M_changeVideoMatrixType: {"method": "changeVideoMatrixType", "result": None},
    M_changeWindowState: {"method": "changeWindowState", "result": None},
    M_chatClear: {"method": "chatClear", "result": None},
    M_clearCallHistory: {"method": "clearCallHistory", "result": None},
    M_clearFileTransfer: {"method": "clearFileTransfer", "result": None},
    M_clearTokens: {"method": "clearTokens", "result": None},
    M_connectToServer: {"method": "connectToServer", "result": None},
    M_connectToService: {"method": "connectToService", "result": None},
    M_createConference: {"method": "createConference", "result": None},
    M_createGroup: {"method": "createGroup", "result": None},
    M_createNDIDevice: {"method" : "createNDIDevice", "result": None},
    M_deleteData: {"method" : "deleteData", "result": None},
    M_deleteFileTransferFile: {"method": "deleteFileTransferFile", "result": None},
    M_deleteNDIDevice: {"method": "deleteNDIDevice", "result": None},
    M_denyRecord: {"method": "denyRecord", "result": None},
    M_enableAudioReceiving: {"method": "enableAudioReceiving", "result": None},
    M_enableVideoReceiving: {"method": "enableVideoReceiving", "result": None},
    M_expandCallToMulti: {"method": "expandCallToMulti", "result": None},
    M_fireMyEvent: {"method": "fireMyEvent", "result": None},
    M_getAbook: {"method": "getAbook", "abook": None, "result": None},
    M_getAllUserContainersNames: {"method": "getAllUserContainersNames", "containersNames": None, "result": None},
    M_getAppSndDev: {"method" : "getAppSndDev", "name" : None, "description" : None, "result" : False},
    M_getAppState: {"method": "getAppState", "embeddedHttpPort": None, "appState": None, "result": None},
    M_getAudioDelayDetectorInfo: {"method": "getAudioDelayDetectorInfo", "state": None, "result": None},
    M_getAudioMute: {"method": "getAudioMute", "mute": None, "result": None},
    M_getAudioReceivingLevel: {"method": "getAudioReceivingLevel", "level": None, "result": None},
    M_getAuthInfo: {"method": "getAuthInfo", "adminAuth": None, "userAuth": None, "result": None},
    M_getAvailableServersList: {"method": "getAvailableServersList", "result": None},
    M_getBackground: {"method": "getBackground", "isCustomImage": None, "fileId": None, "result": None},
    M_getBanList: {"method": "getBanList", "banList": None, "result": None},
    M_getBroadcastPicture: {"method": "getBroadcastPicture", "fileName": None, "fileId": None, "result": None},
    M_getBroadcastSelfie: {"method": "getBroadcastSelfie", "enabled": None, "fps": None, "result": None},
    M_getCallHistory: {"method": "getCallHistory", "calls" : None, "lastView": None, "result": None},
    M_getChatLastMessages: {"method": "getChatLastMessages", "messages": None, "result": None},
    M_getConferenceParticipants: {"method": "getConferenceParticipants", "confId": None, "participants": None, "result": None},
    M_getConferences: {"method": "getConferences", "confId": None, "result": None},
    M_getConnected: {"method": "getConnected", "state": None, "serverInfo": None, "result": None},
    M_getContactDetails: {"method": "getContactDetails", "result": None},
    M_getCreatedNDIDevices: {"method": "getCreatedNDIDevices", "createdNDIDevices": None, "result": None},
    M_getCrop: {"method": "getCrop", "enabled": None, "result": None},
    M_getCurrentUserProfileUrl: {"method": "getCurrentUserProfileUrl", "url": None, "result": None},
    M_getDisplayNameById: {"method": "getDisplayNameById", "peerDn": None, "peerId": None, "result": None},
    M_getFileInfo: {
        "method": "getFileInfo",
        "id": None,
        "status": None,
        "directionType": None,
        "fileName": None,
        "fileId": None,
        "peerId": None,
        "peerDisplayName": None,
        "timestamp": None,
        "confId": None,
        "totalSize": None,
        "processedSize": None,
        "speed": None,
        "peersCount": None,
        "result": None,
    },
    M_getFileList: {"method": "getFileList", "fileList": None, "result": None},
    M_getFileRequests: {"method": "getFileRequests", "files": None, "result": None},
    M_getFileTransferAvailability: {"method": "getFileTransferAvailability", "available": None, "result": None},
    M_getFileTransferInfo: {"method": "getFileTransferInfo", "files": None, "result": None},
    M_getFileUploads: {"method": "getFileUploads", "files": None, "result": None},
    M_getGroups: {"method": "getGroups", "groups": None, "result": None},
    M_getHardwareKey: {"method": "getHardwareKey", "key": None, "result": None},
    M_getHttpServerSettings: {"method": "getHttpServerSettings", "settings": None, "result": None},
    M_getHttpServerState: {"method": "getHttpServerState", "state": None, "result": None},
    M_getIncomingCameraControlRequests: {"method": "getIncomingCameraControlRequests", "callIdList": None, "result": None},
    M_getInfoWidgetsState: {
        "method": "getInfoWidgetsState",
        "logoDisplaying": None,
        "timeDisplaying": None,
        "connectInfoDisplaying": None,
        "currentUserInfoWidgetDisplaying": None,
        "incomingRequestWidgetDisplaying": None,
        "upcomingMeetingsComponentDisplaying" : None,
        "result": None,
    },
    M_getLastCallsViewTime: {"method": "getLastCallsViewTime", "time": None, "result": None},
    M_getLastSelectedConference: {"method": "getLastSelectedConference", "confType": None, "result": None},
    M_getLastUsedServersList: {"method": "getLastUsedServersList", "lastUsedServersList": None, "result": None},
    M_getLicenseServerStatus: {"method": "getLicenseServerStatus", "status": None, "result": None},
    M_getLicenseType: {
        "method": "getLicenseType",
        "product_id": None,
        "value" : None,
        "start_date": None,
        "end_date": None,
        "result": None
    },
    M_getListOfChats: {"method": "getListOfChats", "list": None, "result": None},
    M_getLogin: {"method": "getLogin", "isLoggedIn": None, "peerId": None, "peerDn": None, "result": None},
    M_getLogo: {"method": "getLogo", "isCustomImage": None, "result": None},
    M_getMaxConfTitleLength: {"method": "getMaxConfTitleLength", "length": None, "result": None},
    M_getMicMute: {"method": "getMicMute", "mute": None, "result": None},
    M_getModes: {
        "method": "getModes",
        "activeMode": None,
        "activePin": None,
        "modeList": None,
        "pinList": None,
        "supportPTZ": None,
        "videoCapturerName": None,
        "videoCapturerDescription": None,
        "result": None,
    },
    M_getMonitorsInfo: {"method": "getMonitorsInfo", "monitors": None, "currentMonitor": None, "result": None},
    M_getNDIState: {"method": "getNDIState", "enabled": None, "result": None},
    M_getOutgoingBitrate: {"method": "getOutgoingBitrate", "bitrate": None, "result": None},
    M_getOutgoingCameraControlRequests: {"method": "getOutgoingCameraControlRequests", "callIdList": None, "result": None},
    M_getOutputSelfVideoRotateAngle: {"method": "getOutputSelfVideoRotateAngle", "outputSelfVideoRotateAngle": None, "result": None},
    M_getProperties: {"method": "getProperties", "properties": None, "result": None},
    M_getPtzControls: {
        "method": "getPtzControls",
        "pan": None,
        "tilt": None,
        "zoom": None,
        "videoCapturerName": None,
        "videoCapturerDescription": None,
        "result": None
    },
    M_getRemotelyControlledCameras: {"method": "getRemotelyControlledCameras", "callIdList": None, "result": None},
    M_getRenderInfo: {
        "method": "getRenderInfo",
        "render": None,
        "version": None,
        "vendor": None,
        "result": None
    },
    M_getScheduler: {"method": "getScheduler", "cnt": None, "conferences": None, "result": None},
    M_getServerDomain: {"method": "getServerDomain", "domain": None, "result": None},
    M_getSettings: {"method": "getSettings", "settings": None, "result": None},
    M_getSlideShowCache: {
        "method": "getSlideShowCache",
        "imagesQueueForCaching": None,
        "cachedSlides": None,
        "isImagesCachingRunning": None,
        "currentlyCachingImage": None,
        "result": None
    },
    M_getSlideShowInfo: {
        "method": "getSlideShowInfo",
        "available": None,
        "started": None,
        "slides": None,
        "currentSlideIdx": None,
        "result": None
    },
    M_getSystemInfo: {
        "method": "getSystemInfo",
        "authInfo": None,
        "fileInfo": None,
        "productInfo": None,
        "permissionsInfo": None,
        "bitrateLimits": None,
        "systemRating": None,
        "cameraInfo": None,
        "result": None
    },
    M_getTariffRestrictions: {
        "method": "getTariffRestrictions",
        "tariffName": None,
        "p2p": None,
        "createMulti": None,
        "symMaxNumber": None,
        "asymMaxNumber": None,
        "roleMaxNumber": None,
        "rlMaxNumber": None,
        "canUseSlideShow": None,
        "canUseDesktopSharing": None,
        "canChangeAddressBook": None,
        "canEditGroups": None,
        "canUseDialer": None,
        "result": None
    },
    M_getTokenForHttpServer: {"method": "getTokenForHttpServer", "token": None, "result": None},
    M_getTrueConfRoomProKey: {"method": "getTrueConfRoomProKey", "trueconfRoomKey": None, "result": None},
    M_getVideoMatrix: {
        "method": "getVideoMatrix",
        "matrixType": None,
        "mainWindowWidth": None,
        "mainWindowHeight": None,
        "selfViewMode": None,
        "participants": None,
        "externVideoSlots": None,
        "hiddenVideoSlots": None,
        "result": None
    },
    M_getVideoMute: {"method": "getVideoMute", "mute": None, "result": None},
    M_gotoPodium: {"method": "gotoPodium", "result": None},
    M_hangUp: {"method": "hangUp", "result": None},
    M_hideVideoSlot: {"method": "hideVideoSlot", "result": None},
    M_inviteToConference: {"method": "inviteToConference", "result": None},
    M_inviteToPodium: {"method": "inviteToPodium", "result": None},
    M_kickFromPodium: {"method": "kickFromPodium", "result": None},
    M_kickPeer: {"method": "kickPeer", "result": None},
    M_leavePodium: {"method": "leavePodium", "result": None},
    M_loadData: {"method": "loadData", "data": None, "containerName": None, "result": None},
    M_login: {"method": "login", "isLoggedIn": None, "peerId": None, "peerDn": None, "result": None},
    M_logout: {"method": "logout", "result": None},
    M_moveVideoSlotToMonitor: {"method": "moveVideoSlotToMonitor", "result": None},
    M_productRegistrationOffline: {"method": "productRegistrationOffline", "result": None},
    M_ptzDown: {"method": "ptzDown", "result": None},
    M_ptzLeft: {"method": "ptzLeft", "result": None},
    M_ptzRight: {"method": "ptzRight", "result": None},
    M_ptzStop: {"method": "ptzStop", "result": None},
    M_ptzUp: {"method": "ptzUp", "result": None},
    M_ptzZoomDec: {"method": "ptzZoomDec", "result": None},
    M_ptzZoomInc: {"method": "ptzZoomInc", "result": None},
    M_rebootSystem: {"method": "rebootSystem", "result": None},
    M_reject: {"method": "reject", "result": None},
    M_rejectFile: {"method": "rejectFile", "result": None},
    M_rejectInvitationToPodium: {"method": "rejectInvitationToPodium", "result": None},
    M_rejectPeer: {"method": "rejectPeer", "result": None},
    M_rejectRequestCameraControl: {"method": "rejectRequestCameraControl", "result": None},
    M_rejectRequestToPodium: {"method": "rejectRequestToPodium", "result": None},
    M_remotelyControlledCameraPtzLeft: {"method": "remotelyControlledCameraPtzLeft", "result": None},
    M_remotelyControlledCameraPtzRight: {"method": "remotelyControlledCameraPtzRight", "result": None},
    M_remotelyControlledCameraPtzUp: {"method": "remotelyControlledCameraPtzUp", "result": None},
    M_remotelyControlledCameraPtzZoomDec: {"method": "remotelyControlledCameraPtzZoomDec", "result": None},
    M_remotelyControlledCameraPtzZoomInc: {"method": "remotelyControlledCameraPtzZoomInc", "result": None},
    M_removeAllSlides: {"method": "removeAllSlides", "result": None},
    M_removeFromAbook: {"method": "removeFromAbook", "peerId": None, "result": None},
    M_removeFromGroup: {"method": "removeFromGroup", "result": None},
    M_removeFromServersList: {"method": "removeFromServersList", "result": None},
    M_removeGroup: {"method": "removeGroup", "result": None},
    M_removeImageFromCachingQueue: {"method": "removeImageFromCachingQueue", "result": None},
    M_removeSlide: {"method": "removeSlide", "result": None},
    M_removeVideoSlotFromMonitor: {"method": "removeVideoSlotFromMonitor", "result": None},
    M_renameGroup: {"method": "renameGroup", "result": None},
    M_renameInAbook: {"method": "renameInAbook", "peerId": None, "result": None},
    M_requestParticipantCameraControl: {"method": "requestParticipantCameraControl", "result": None},
    M_restoreWindow: {"method": "restoreWindow", "result": None},
    M_saveData: {"method": "saveData", "result": None},
    M_sendCommand: {"method": "sendCommand", "result": None},
    M_sendConferenceFile: {"method": "sendConferenceFile", "result": None},
    M_sendFile: {"method": "sendFile", "result": None},
    M_sendGroupMessage: {"method": "sendGroupMessage", "result": None},
    M_sendMessage: {"method": "sendMessage", "result": None},
    M_setAppSndDev: {"method": "setAppSndDev", "result": None},
    M_setAudioCapturer: {"method": "setAudioCapturer", "result": None},
    M_setAudioMute: {"method": "setAudioMute", "result": None},
    M_setAudioReceivingLevel: {"method": "setAudioReceivingLevel", "result": None},
    M_setAudioRenderer: {"method": "setAudioRenderer", "result": None},
    M_setAuthParams: {"method": "setAuthParams", "result": None},
    M_setBackground: {"method": "setBackground", "result": None},
    M_setBroadcastSelfie: {"method": "setBroadcastSelfie", "result": None},
    M_setCrop: {"method": "setCrop", "result": None},
    M_setDefaultBackground: {"method": "setDefaultBackground", "result": None},
    M_setDefaultLogo: {"method": "setDefaultLogo", "result": None},
    M_setHttpServerSettings: {"method": "setHttpServerSettings", "result": None},
    M_setLastCallsViewed: {"method": "setLastCallsViewed", "result": None},
    M_setLogo: {"method": "setLogo", "result": None},
    M_setMicMute: {"method": "setMicMute", "result": None},
    M_setModeratorRole: {"method": "setModeratorRole", "result": None},
    M_setModes: {"method": "setModes", "result": None},
    M_setNDIState: {"method": "setNDIState", "result": None},
    M_setOutputSelfVideoRotateAngle: {"method": "setOutputSelfVideoRotateAngle", "result": None},
    M_setPanPos: {"method": "setPanPos", "result": None},
    M_setPtzDefaults: {"method": "setPtzDefaults", "result": None},
    M_setSettings: {"method": "setSettings", "result": None},
    M_setSlidePosition: {"method": "setSlidePosition", "result": None},
    M_setTiltPos: {"method": "setTiltPos", "result": None},
    M_setUsedApiVersion: {"method": "setUsedApiVersion", "result": None},
    M_setVideoCapturer: {"method": "setVideoCapturer", "result": None},
    M_setVideoMute: {"method": "setVideoMute", "result": None},
    M_setZoomPos: {"method": "setZoomPos", "result": None},
    M_showFirstSlide: {"method": "showFirstSlide", "result": None},
    M_showLastSlide: {"method": "showLastSlide", "result": None},
    M_showNextSlide: {"method": "showNextSlide", "result": None},
    M_showPrevSlide: {"method": "showPrevSlide", "result": None},
    M_showSlide: {"method": "showSlide", "result": None},
    M_showVideoSlot: {"method": "showVideoSlot", "result": None},
    M_shutdown: {"method": "shutdown", "result": None},
    M_shutdownSystem: {"method": "shutdownSystem", "result": None},
    M_sortSlides: {"method": "sortSlides", "result": None},
    M_startAudioDelayDetectorTest: {"method": "startAudioDelayDetectorTest", "result": None},
    M_startBroadcastPicture: {"method": "startBroadcastPicture", "result": None},
    M_startCapture: {"method": "startCapture", "result": None},
    M_startHttpServer: {"method": "startHttpServer", "result": None},
    M_startRemark: {"method": "startRemark", "result": None},
    M_startSlideShow: {"method": "startSlideShow", "result": None},
    M_stopAudioDelayDetectorTest: {"method": "stopAudioDelayDetectorTest", "result": None},
    M_stopBroadcastPicture: {"method": "stopBroadcastPicture", "result": None},
    M_stopCachingAllImages: {"method": "stopCachingAllImages", "result": None},
    M_stopCapture: {"method": "stopCapture", "result": None},
    M_stopHttpServer: {"method": "stopHttpServer", "result": None},
    M_stopSlideShow: {"method": "stopSlideShow", "result": None},
    M_swapVideoSlots: {"method": "swapVideoSlots", "result": None},
    M_switchVideoFlow: {"method": "switchVideoFlow", "result": None},
    M_testAudioCapturerStart: {"method": "testAudioCapturerStart", "result": None},
    M_testAudioCapturerStop: {"method": "testAudioCapturerStop", "result": None},
    M_testAudioRenderer: {"method": "testAudioRenderer", "result": None},
    M_toneDial: {"method": "toneDial", "result": None},
    M_turnRemoteCamera: {"method": "turnRemoteCamera", "result": None},
    M_turnRemoteMic: {"method": "turnRemoteMic", "result": None},
    M_turnRemoteSpeaker: {"method": "turnRemoteSpeaker", "result": None},
    M_unblock: {"method": "unblock", "peerId": None, "result": None},
    # version 4.2
    M_searchContact: {
        "method": "searchContact",
        "searchingResult": None,
        "foundContacts": None,
        "result": None
}

}
