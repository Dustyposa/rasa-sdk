import logging
import warnings
from typing import Dict, Text, Any, List, Optional, Union
import datetime

logger = logging.getLogger(__name__)

EventType = Dict[Text, Any]


# noinspection PyPep8Naming
def UserUttered(
    text: Optional[Text],
    parse_data: Optional[Dict[Text, Any]] = None,
    timestamp: Optional[float] = None,
    input_channel: Optional[Text] = None,
) -> EventType:
    return {
        "event": "user",
        "timestamp": timestamp,
        "text": text,
        "parse_data": parse_data,
        "input_channel": input_channel,
    }


# noinspection PyPep8Naming
def BotUttered(
    text: Optional[Text] = None,
    data: Optional[Dict[Text, Any]] = None,
    metadata: Optional[Dict[Text, Any]] = None,
    timestamp: Optional[float] = None,
) -> EventType:
    return {
        "event": "bot",
        "timestamp": timestamp,
        "text": text,
        "data": data,
        "metadata": metadata,
    }


# noinspection PyPep8Naming
def SlotSet(
    key: Text, value: Any = None, timestamp: Optional[float] = None
) -> EventType:
    return {"event": "slot", "timestamp": timestamp, "name": key, "value": value}


# noinspection PyPep8Naming
def Restarted(timestamp: Optional[float] = None) -> EventType:
    return {"event": "restart", "timestamp": timestamp}


# noinspection PyPep8Naming
def SessionStarted(timestamp: Optional[float] = None) -> EventType:
    return {"event": "session_started", "timestamp": timestamp}


# noinspection PyPep8Naming
def UserUtteranceReverted(timestamp: Optional[float] = None) -> EventType:
    return {"event": "rewind", "timestamp": timestamp}


# noinspection PyPep8Naming
def AllSlotsReset(timestamp: Optional[float] = None) -> EventType:
    return {"event": "reset_slots", "timestamp": timestamp}


# noinspection PyPep8Naming
def ReminderScheduled(
    intent_name: Text,
    trigger_date_time: datetime.datetime,
    entities: Optional[Union[List[Dict[Text, Any]], Dict[Text, Text]]] = None,
    name: Optional[Text] = None,
    kill_on_user_message: bool = True,
    timestamp: Optional[float] = None,
) -> EventType:
    if intent_name.startswith("utter_"):
        warnings.warn(
            f"ReminderCancelled intent starts with 'utter_'"
            f"If {intent_name} is an intent, you can ignore this warning.",
            FutureWarning,
        )
    elif intent_name.startswith("action_"):
        warnings.warn(
            f"ReminderCancelled intent starts with 'action_'"
            f"If {intent_name} is an intent, you can ignore this warning.",
            FutureWarning,
        )
    return {
        "event": "reminder",
        "timestamp": timestamp,
        "intent": intent_name,
        "entities": entities,
        "date_time": trigger_date_time.isoformat(),
        "name": name,
        "kill_on_user_msg": kill_on_user_message,
    }


# noinspection PyPep8Naming
def ReminderCancelled(
    name: Optional[Text] = None,
    intent_name: Optional[Text] = None,
    entities: Optional[Union[List[Dict[Text, Any]], Dict[Text, Text]]] = None,
    timestamp: Optional[float] = None,
) -> EventType:
    if intent_name and intent_name.startswith("utter_"):
        warnings.warn(
            f"ReminderCancelled intent starts with 'utter_'"
            f"If {intent_name} is an intent, you can ignore this warning.",
            FutureWarning,
        )
    elif intent_name and intent_name.startswith("action_"):
        warnings.warn(
            f"ReminderCancelled intent starts with 'action_'"
            f"If {intent_name} is an intent, you can ignore this warning.",
            FutureWarning,
        )
    return {
        "event": "cancel_reminder",
        "timestamp": timestamp,
        "intent": intent_name,
        "entities": entities,
        "name": name,
    }


# noinspection PyPep8Naming
def ActionReverted(timestamp: Optional[float] = None) -> EventType:
    return {"event": "undo", "timestamp": timestamp}


# noinspection PyPep8Naming
def StoryExported(timestamp: Optional[float] = None) -> EventType:
    return {"event": "export", "timestamp": timestamp}


# noinspection PyPep8Naming
def FollowupAction(name: Text, timestamp: Optional[float] = None) -> EventType:
    return {"event": "followup", "timestamp": timestamp, "name": name}


# noinspection PyPep8Naming
def ConversationPaused(timestamp: Optional[float] = None) -> EventType:
    return {"event": "pause", "timestamp": timestamp}


# noinspection PyPep8Naming
def ConversationResumed(timestamp: Optional[float] = None) -> EventType:
    return {"event": "resume", "timestamp": timestamp}


# noinspection PyPep8Naming
def ActionExecuted(
    action_name,
    policy=None,
    confidence: Optional[float] = None,
    timestamp: Optional[float] = None,
) -> EventType:
    return {
        "event": "action",
        "name": action_name,
        "policy": policy,
        "confidence": confidence,
        "timestamp": timestamp,
    }


# noinspection PyPep8Naming
def AgentUttered(
    text: Optional[Text] = None, data=None, timestamp: Optional[float] = None
) -> EventType:
    return {"event": "agent", "text": text, "data": data, "timestamp": timestamp}


# noinspection PyPep8Naming
def Form(name: Optional[Text], timestamp: Optional[float] = None) -> EventType:
    return {"event": "form", "name": name, "timestamp": timestamp}


# noinspection PyPep8Naming
def FormValidation(validate, timestamp: Optional[float] = None) -> EventType:
    return {"event": "form_validation", "validate": validate, "timestamp": timestamp}


# noinspection PyPep8Naming
def ActionExecutionRejected(
    action_name: Text,
    policy: Optional[Text] = None,
    confidence: Optional[float] = None,
    timestamp: Optional[float] = None,
) -> EventType:
    return {
        "event": "action_execution_rejected",
        "name": action_name,
        "policy": policy,
        "confidence": confidence,
        "timestamp": timestamp,
    }
