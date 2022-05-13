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

EV_appStateChanged = "appStateChanged"
EV_incomingChatMessage = "incomingChatMessage"
EV_inviteReceived = "inviteReceived"
EV_rejectReceived = "rejectReceived"

EVENT = {
    "ALL": {},
    EV_appStateChanged: {"event": "appStateChanged", "appState": None},
    EV_incomingChatMessage: {"event": "incomingChatMessage", "peerId": None, "peerDn": None, "message": None, "time": None, "method": "event"},
    EV_inviteReceived: {"event": "inviteReceived", "peerId": None, "peerDn": None, "type": None, "confId": None, "method": "event"},
    EV_rejectReceived: {"event": "rejectReceived", "cause": None, "peerId": None, "peerDn": None, "method": "event"}

}

M_getAppState = "getAppState"

METHOD = {
    "getAppState": {"method": "getAppState", "appState": None},
}